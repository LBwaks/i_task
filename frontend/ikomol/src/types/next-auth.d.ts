import NextAuth,{DefaultSession,DefaultUser,JWT} from "next-auth";
import {User as AdapterUser } from "next-auth/adapters"
//extend the default user type

declare module "next-auth"{
    interface User extends DefaultUser{
        accessToken?:string
        refreshToken?: string
        emailVerified?: string | null  // Adding emailVerified field, which is required
    }
    //extend the fault session type tp include accestoken
    interface Session extends DefaultSession{
        user: {id:string;email:string;name:string;};
        accessToken?: string;
    }
    //extend the jwt type to inclue accessToken refreshToken

    interface JWT extends JWT {
        user: {id:string;email:string;name:string;};
        accessToken?:string;
        refreshToken?: string;

    }
}