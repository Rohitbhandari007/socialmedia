import React from 'react'
import ale from './image/ale.jpg';
import joshi from './image/joshi.jpg';
import mero from './image/mero.jpg';



function PostItem() {
    return (
        <div className='grid grid-cols-1 gap-0 place-items-center'>
            <div class="mt-5 rounded overflow-hidden border h-auto w-full lg:w-1/3 md:w-1/3 bg-white mx-3 md:mx-0 lg:mx-0">
                <div class="w-full flex justify-between p-2">
                    <div class="flex">
                        <div class="rounded-full h-8 w-8 bg-gray-500 flex items-center justify-center overflow-hidden">
                            <img src={joshi} alt="profilepic" />
                        </div>
                        <span class="pt-1 ml-2 font-bold text-sm">joshi</span>
                    </div>
                    <span class="cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                            <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </span>
                </div>
                <img class="w-full h-1/5 object-contain" src={joshi} />
                <div class="px-3 pb-2">
                    <div class="pt-2">
                        <i class="far fa-heart cursor-pointer">+</i>
                        <span class="text-sm text-gray-400 font-medium">69 likes</span>
                    </div>
                    <div class="pt-1">
                        <div class="mb-2 text-sm">
                            Lord of the Rings is my favorite film-series. One day I'll make my way to New Zealand to visit the Hobbiton set!
                        </div>
                    </div>
                    <div class="text-sm mb-2 text-gray-400 cursor-pointer font-medium">View all 14 comments</div>
                    <div class="mb-2">

                    </div>
                </div>
            </div>
            <div class="mt-5 rounded overflow-hidden border w-full h-auto lg:w-1/3 md:w-1/3 bg-white mx-3 md:mx-0 lg:mx-0">
                <div class="w-full flex justify-between p-3">
                    <div class="flex">
                        <div class="rounded-full h-8 w-8 bg-gray-500 flex items-center justify-center overflow-hidden">
                            <img src={ale} alt="profilepic" />
                        </div>
                        <span class="pt-1 ml-2 font-bold text-sm">aale</span>
                    </div>
                    <span class="px-2 hover:bg-gray-300 cursor-pointer rounded"><i class="fas fa-ellipsis-h pt-2 text-lg"></i></span>
                </div>
                <img class="w-full h-1/5 object-contain" src={ale} />
                <div class="px-3 pb-2">
                    <div class="pt-2">
                        <i class="far fa-heart cursor-pointer">+</i>
                        <span class="text-sm text-gray-400 font-medium">12 Dislikes</span>
                    </div>
                    <div class="pt-1">
                        <div class="mb-2 text-sm">
                            Lord of the Rings is not my favorite film-series. One day I'll not make my way to New Zealand to visit the Hobbiton set!
                        </div>
                    </div>
                    <div class="text-sm mb-2 text-gray-400 cursor-pointer font-medium">View all 14 comments</div>
                    <div class="mb-2">

                    </div>
                </div>
            </div>
            <div class="mt-5 rounded overflow-hidden border h-auto w-full lg:w-1/3 md:w-1/3 bg-white mx-3 md:mx-0 lg:mx-0">
                <div class="w-full flex justify-between p-3">
                    <div class="flex">
                        <div class="rounded-full h-8 w-8 bg-gray-500 flex items-center justify-center overflow-hidden">
                            <img src={mero} alt="profilepic" />
                        </div>
                        <span class="pt-1 ml-2 font-bold text-sm">bhandari</span>
                    </div>
                    <span class="px-2 hover:bg-gray-300 cursor-pointer rounded"><i class="fas fa-ellipsis-h pt-2 text-lg"></i></span>
                </div>
                <img class="w-full h-1/5 object-contain" src={mero} />
                <div class="px-3 pb-2">
                    <div class="pt-2">
                        <i class="far fa-heart cursor-pointer">+</i>
                        <span class="text-sm text-gray-400 font-medium">0 likes</span>
                    </div>
                    <div class="pt-1">
                        <div class="mb-2 text-sm">
                            Lord of the Rings was my favorite film-series. One day I'll make my way to North Korea to visit the Hobbiton set!
                        </div>
                    </div>
                    <div class="text-sm mb-2 text-gray-400 cursor-pointer font-medium">View all 14 comments</div>
                    <div class="mb-2">

                    </div>
                </div>
            </div>
        </div>





    )
}

export default PostItem