"use client";
import { motion } from "framer-motion";
import Image from "next/image";
import React from "react";
import { PhotoIcon,UserCircleIcon } from "@heroicons/react/24/solid";


// src/app/dashboard/page.tsx
// import { auth } from "@/auth"

// export default async function Dashboard() {
//   const session = await auth()

//   return (
//     <div>
//       <h1>Welcome, {session?.user?.email}</h1>
//     </div>
//   )
// }
const PostTask = () =>{
    /**
   * Source: https://www.joshwcomeau.com/react/the-perils-of-rehydration/
   * Reason: To fix rehydration error
   */
    const [hasMounted,setHasMounted]=React.useState(false);
    React.useEffect(()=>{
        setHasMounted(true);
    },[]);
    if (!setHasMounted){
        return null;
        }

    return (
        <>
        {/* <!-- ===== Contact Start ===== --> */}
        <section id="support" className="px-4 md:px-6 2xl:px-0">
          <div className="relative mx-auto max-w-c-1390 px-7.5 pt-10 lg:px-15 lg:pt-10 xl:px-10 xl:pt-10">
            <div className="absolute left-0 top-0 -z-1 h-2/3 w-full rounded-lg bg-gradient-to-t from-transparent to-[#dee7ff47] dark:bg-gradient-to-t dark:to-[#252A42]"></div>
            <div className="absolute bottom-[-255px] left-0 -z-1 h-full w-full">
              <Image
                src="./images/shape/shape-dotted-light.svg"
                alt="Dotted"
                className="dark:hidden"
                fill
              />
              <Image
                src="./images/shape/shape-dotted-dark.svg"
                alt="Dotted"
                className="hidden dark:block"
                fill
              />
            </div>
  
            <div className="flex flex-col-reverse flex-wrap gap-8 md:flex-row md:flex-nowrap md:justify-center xl:gap-20">
              <motion.div
                variants={{
                  hidden: {
                    opacity: 0,
                    y: -20,
                  },
  
                  visible: {
                    opacity: 1,
                    y: 0,
                  },
                }}
                initial="hidden"
                whileInView="visible"
                transition={{ duration: 1, delay: 0.1 }}
                viewport={{ once: true }}
                className="animate_top w-full rounded-lg bg-white p-7.5 shadow-solid-8 dark:border dark:border-strokedark dark:bg-black md:w-5/5 lg:w-4/4 xl:p-15"
              >
                <h2 className="mb-15 text-center text-3xl font-semibold text-black dark:text-white xl:text-sectiontitle2">
                  Create Task
                </h2>
               

                <form className="-1/2 sm:w-auto md:w-full lg:w-32 xl:w-3/4 pb-3 px-2 mx-auto">
                <div className="mb-5">
                <label htmlFor="sector" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Sector </label>
                <select id="sector" className="bg-gray-50 h-14 border border-gray-300 text-gray-900 text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>Gachie</option>
                    <option>Adungosi</option>
                    <option>Town</option>
                    <option>Ruaka</option>
                </select>
                </div>

                <div className="mb-5">
                <label htmlFor="issue" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Issue Type </label>
                <select id="issue" className="bg-gray-50 h-14 border border-gray-300 text-gray-900 text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>New Install</option>
                    <option>Support</option>
                    <option>Rellocation</option>
                    
                </select>
                </div>
                <div className="mb-5">
                <label htmlFor="prioity" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Priority</label>
                <select id="priority" className="bg-gray-50 h-14 border border-gray-300 text-gray-900 text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>HIgh</option>
                    <option>LOw</option>
                    <option>Rellocation</option>
                    
                </select>
                </div>
                <div className="mb-7.5">
                    <label htmlFor="summary" className="block mb-5 text-lg font-medium text-gray-900 dark:text-white">Summary</label>
                    <input type="text" id="text" className="h-14 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="New install mugacha" required />
                </div>
                
                <div className="mb-7.5">
                <label htmlFor="message" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Description</label>
                <textarea id="message" rows="4" className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Leave a comment..."></textarea>

                </div>
                <div className="mb-5">
                <label htmlFor="countries" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Support Type</label>
                <select id="countries" className="bg-gray-50 h-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>Slow Speed</option>
                    <option>RElocation</option>
                    <option>Payments</option>                    
                </select>
                </div>
                <div className="mb-5">
                <label htmlFor="countries" className="block mb-2 text-lg font-medium text-gray-900 dark:text-white">Source Of Task </label>
                <select id="countries" className="bg-gray-50 h-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>Customer</option>
                    <option>Technician</option>
                    <option>Payments</option>                    
                </select>
                </div>
                <div className="mb-7.5">
                    <label htmlFor="summary" className="block mb-5 text-lg font-medium text-gray-900 dark:text-white">Customer Account Number</label>
                    <input type="text" id="text" className="h-14 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="New install mugacha" required />
                </div>
                <div className="mb-5">
                    <div className="col-span-full">
                            <label htmlFor="cover-photo" className="block text-lg font-medium text-gray-900">
                                Attachments
                            </label>
                            <div className="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                                <div className="text-center">
                                <PhotoIcon aria-hidden="true" className="mx-auto size-12 text-gray-300" />
                                <div className="mt-4 flex text-sm/6 text-gray-600">
                                    <label
                                    htmlFor="file-upload"
                                    className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 focus-within:outline-hidden hover:text-indigo-500"
                                    >
                                    <span>Upload a file</span>
                                    <input id="file-upload" name="file-upload" type="file" className="sr-only" />
                                    </label>
                                    <p className="pl-1">or drag and drop</p>
                                </div>
                                <p className="text-xs/5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
                                </div>
                            </div>
                            </div>
                </div>
                <div className="flex flex-wrap gap-4 xl:justify-center ">                 

                <button
                aria-label="Create"
                className="inline-flex items-center gap-2.5 rounded-full bg-black px-6 py-3 font-medium text-white duration-300 ease-in-out hover:bg-blackho dark:bg-btndark"
                >
                Create
                <svg
                    className="fill-white"
                    width="14"
                    height="14"
                    viewBox="0 0 14 14"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                    d="M10.4767 6.16664L6.00668 1.69664L7.18501 0.518311L13.6667 6.99998L7.18501 13.4816L6.00668 12.3033L10.4767 7.83331H0.333344V6.16664H10.4767Z"
                    fill=""
                    />
                </svg>
                </button>
                </div>

                </form>



              </motion.div>

            {/* <motion.div
              variants={{
                hidden: {
                  opacity: 0,
                  y: -20,
                },

                visible: {
                  opacity: 1,
                  y: 0,
                },
              }}
              initial="hidden"
              whileInView="visible"
              transition={{ duration: 2, delay: 0.1 }}
              viewport={{ once: true }}
              className="animate_top w-full md:w-2/5 md:p-7.5 lg:w-[26%] xl:pt-15"
            >
              <h2 className="mb-12.5 text-3xl font-semibold text-black dark:text-white xl:text-sectiontitle2">
                Find us
              </h2>

              <div className="5 mb-7">
                <h3 className="mb-4 text-metatitle3 font-medium text-black dark:text-white">
                  Our Loaction
                </h3>
                <p>290 Maryam Springs 260, Courbevoie, Paris, France</p>
              </div>
              <div className="5 mb-7">
                <h3 className="mb-4 text-metatitle3 font-medium text-black dark:text-white">
                  Email Address
                </h3>
                <p>
                  <a href="#">yourmail@domainname.com</a>
                </p>
              </div>
              <div>
                <h4 className="mb-4 text-metatitle3 font-medium text-black dark:text-white">
                  Phone Number
                </h4>
                <p>
                  <a href="#">+009 42334 6343 843</a>
                </p>
              </div>
            </motion.div> */}
          </div>
        </div>
      </section>
      {/* <!-- ===== Contact End ===== --> */}
    </>

    );
};
export default PostTask;