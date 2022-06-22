import React from 'react'

function Nav() {
   return (
      <div className=''>
         <aside class="h-screen fixed w-64 border-r-2 border-[#ded9d9]" aria-label="Sidebar">
            <div className='bg-[#fff]'>
               <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                  <svg
                     class="h-6 w-6 text-indigo-500 mt-2"
                     xmlns="http://www.w3.org/2000/svg"
                     fill="none"
                     viewBox="0 0 24 24"
                     stroke="currentColor"
                  >
                     <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17 8l4 4m0 0l-4 4m4-4H3"
                     />
                  </svg>
                  <span class="ml-3 mt-2">Samajik Sanjal</span>
               </a>
            </div>

            <div class="overflow-y-auto py-20 px-3 bg-gray-50 rounded dark:bg-white">
               <ul class="space-y-10 space-x-12">
                  <li>
                     <span class="ml-3">Menu</span>

                  </li>
                  <li>
                     <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                        <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-black" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                        <span class=" ml-3 blackspace-nowrap">Home</span>

                     </a>
                  </li>
                  <li>
                     <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                        <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-black" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"></path><path d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"></path></svg>
                        <span class=" ml-3 blackspace-nowrap">Messages
                           <span class="inline-flex justify-center items-center p-3 ml-3 w-3 h-3 text-sm font-medium text-blue-600 bg-blue-200 rounded-full dark:bg-blue-900 dark:text-blue-200">60</span>
                        </span>

                     </a>
                  </li>
                  <li>
                     <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                        <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-black" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
                        <span class=" ml-3 blackspace-nowrap">Profile</span>
                     </a>
                  </li>
                  <li>
                     <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                        <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-black" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd"></path></svg>
                        <span class=" ml-3 blackspace-nowrap">Saved Post</span>
                     </a>
                  </li>
                  <li>
                     <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-black hover:bg-gray-100 dark:hover:bg-[#a974ff]">
                        <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-black" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z" clip-rule="evenodd"></path></svg>
                        <span class=" ml-3 blackspace-nowrap">Settings</span>
                     </a>
                  </li>
               </ul>
            </div>
         </aside>
      </div>

   )
}

export default Nav