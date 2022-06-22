import React from 'react'
import cat from './image/cat.jpg';
import ale from './image/ale.jpg';
import joshi from './image/joshi.jpg';
import niskon from './image/nikson.jpg';
import mero from './image/mero.jpg';
import sh from './image/sh.jpg';


function Stories() {
    return (
        <div class="max-w-full mx-12 p-8 border-b-2 border-[#ded9d9]">
            <ul class="flex space-x-6 font-serif ">

                <li class="flex flex-col items-center space-y-1 relative">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={sh} alt="cute kitty" />
                        </a>
                    </div>

                    <a href="#">
                        mam
                    </a>
                </li>
                <li class="flex flex-col items-center space-y-1 ">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={ale} alt="cute kitty" />
                        </a>
                    </div>
                    <a href="#">
                        aale
                    </a>
                </li>
                <li class="flex flex-col items-center space-y-1 ">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={joshi} alt="cute kitty" />
                        </a>
                    </div>
                    <a href="#">
                        joshi
                    </a>
                </li>
                <li class="flex flex-col items-center space-y-1 ">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={mero} alt="cute kitty" />
                        </a>
                    </div>
                    <a href="#">
                        bhandari
                    </a>
                </li>
                <li class="flex flex-col items-center space-y-1 ">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={cat} alt="cute kitty" />
                        </a>
                    </div>
                    <a href="#">
                        acharya
                    </a>
                </li>
                <li class="flex flex-col items-center space-y-1 ">
                    <div class="bg-[#a974ff] p-1 rounded-full">
                        <a class=" bg-white block rounded-full p-1 hover:-rotate-6 transform transition" href="#">
                            <img class="h-16 w-16 rounded-full" src={niskon} alt="cute kitty" />
                        </a>
                    </div>
                    <a href="#">
                        chikson
                    </a>
                </li>



            </ul>

        </div>
    );
}

export default Stories