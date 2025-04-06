import Link from "next/link";
import next from "next";
import Image from "next/image";
import Signin from "../../../../components/auth/Signin";
import { Metadata } from "next";

export const metadata:Metadata ={
    title:"Login Page- Itask",
    description:"THis is a login page for Itask"
}
const SignInPage=() => {
    return (
        <>
           <Signin />
        </>
    );
};

export default SignInPage
