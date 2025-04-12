import NextAuth from "next-auth"
import Google from "next-auth/providers/google"
import { ZodError } from "zod"
import { signInSchema } from "./lib/zod"
import Credentials from "next-auth/providers/credentials"
import axios from "axios"
//import { saltAndHashPassword } from "@/utils/password"
import { processEnv } from "@next/env"
import type { User } from "next-auth"
import { Session, JWT } from 'next-auth'
import { AdapterUser } from 'next-auth/adapters'
import {DefaultSession,} from "next-auth"
import DefaultUser from "next-auth"
 
export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [//Google
    Credentials({
        credentials:{
            username:{},
            password:{},
        },
        authorize:async (credentials)=>{
            try {

                const { username, password } = await signInSchema.parseAsync(credentials) 
                // logic to salt and hash password
                //const pwHash = saltAndHashPassword(password)

                const response = await axios.post(process.env.NEXTAUTH_BACKEND_URL + "auth/login",credentials,{ 
                    headers :{"Content-Type":"application/json"}
                })
                const user =response.data.user as User 
                return {
                    user,
                    accessToken:response.data.access,
                    refreshToken:response.data.refresh
                }


            } catch (error:any){
                if (error instanceof ZodError){
                    // Return `null` to indicate that the credentials are invalid
                    return null
                }
                const message =  error.response?.data?.detail || error.message ||"Login Failed"
                throw new Error (message)
            }

        },
    }),
    Google({
        clientId:process.env.GOOGLE_CLIENT_ID,
        clientSecret:process.env.GOGGLE_CLIENT_SECRECT,
        authorization:"https://accounts.google.com/o/oauth2/v2/auth",
        token:"https://oauth2.googleapis.com/token",
        userinfo:"https://www.googleapis.com/oauth2/v3/userinfo",
        profile(profile){
            return {
                id:profile.sub,
                name:profile.name,
                email:profile.email
            }
        },
    }),

  ],
  session :{
    strategy:"jwt",
    maxAge: 45*60
  },
  callbacks :{
    async  jwt ({token,user,trigger}) {
        ///handle first time login
        if (user&&trigger ==="signIn"){
            token.user=user
            token.accessToken=user.accessToken
            token.refreshToken=user.refreshToken
        }
        // refresh the token if it expires
        if (trigger ==="update" && token.refreshToken){
            try{
                //make a refersh token request to  backend
                const res = await axios.post(process.env.NEXTAUTH_BACKEND_URL + "dj-rest-auth/token/refresh/",{refresh:token.refreshToken})
                //update the access token and refersh token
                token.accessToken= res.data.access,
                token.refreshToken = res.data.refresh
            }catch(err){
                console.error(" FAiled to refresh token",err)
            }
        }
        return token
        
    },
    async session({ session, token }) {
        //session.user = token.user;
        //session.accessToken = token.accessToken;
        return session;
      },
    
  },

  pages:{
    signIn:"/login",
  },
  secret:process.env.AUTH_SECRET, //Secret for signing the jwt token
  
})

declare module "next-auth"{
    // interface User extends DefaultUser{
    //     accessToken?:string
    //     refreshToken?: string
    //     emailVerified?: string | null  // Adding emailVerified field, which is required
    // }
    //extend the fault session type tp include accestoken
    interface Session extends DefaultSession{
        user: {id:string;email:string;name:string;};
        accessToken?: string;
    }
    //extend the jwt type to inclue accessToken refreshToken

    interface JWT{
        user: {id:string;email:string;name:string;};
        accessToken?:string;
        refreshToken?: string;

    }
}

