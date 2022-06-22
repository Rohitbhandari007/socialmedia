import React from 'react'
import Stories from './stories'
import Posts from './Posts'

function Feeds() {
    return (
        <div className='w-2/3 mx-64'>

            <Stories />
            <Posts />

        </div>
    )
}

export default Feeds