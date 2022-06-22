import React from 'react'
import ale from './image/ale.jpg';
import joshi from './image/joshi.jpg';



function PostItem() {
    return (

        <div class="mt-5 rounded overflow-hidden border w-full lg:w-4/6 md:w-4/6 bg-white mx-3 md:mx-0 lg:mx-0">
            <div class="w-full flex justify-between p-3">
                <div class="flex">
                    <div class="rounded-full h-8 w-8 bg-gray-500 flex items-center justify-center overflow-hidden">
                        <img src={ale} alt="profilepic" />
                    </div>
                    <span class="pt-1 ml-2 font-bold text-sm">braydoncoyer</span>
                </div>
                <span class="px-2 hover:bg-gray-300 cursor-pointer rounded"><i class="fas fa-ellipsis-h pt-2 text-lg"></i></span>
            </div>
            <img class="w-full h-auto object-contain" src={joshi} />
            <div class="px-3 pb-2">
                <div class="pt-2">
                    <i class="far fa-heart cursor-pointer">+</i>
                    <span class="text-sm text-gray-400 font-medium">12 likes</span>
                </div>
                <div class="pt-1">
                    <div class="mb-2 text-sm">
                        Lord of the Rings is my favorite film-series. One day I'll make my way to New Zealand to visit the Hobbiton set!
                    </div>
                </div>
                <div class="text-sm mb-2 text-gray-400 cursor-pointer font-medium">View all 14 comments</div>
                <div class="mb-2">
                    <div class="mb-2 text-sm">
                        <span class="font-medium mr-2">razzle_dazzle</span> Dude! How cool! I went to New Zealand last summer and had a blast taking the tour! So much to see! Make sure you bring a good camera when you go!
                    </div>
                </div>
            </div>
        </div>




    )
}

export default PostItem