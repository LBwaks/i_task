import React from "react";
import PostTask from "../../../../components/task/postTask";
import { Metadata } from "next";
import { div } from "motion/react-client";

export const metadata :Metadata ={
    title:"Create Task -Itask",
    description:"This is a page for creating tasks"
}
const CreateTask =()=>{
    return (
        <div className="pb-20 pt-40">
            <PostTask/>
        </div>
    );
};
export default CreateTask