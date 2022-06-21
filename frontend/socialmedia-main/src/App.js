import React from 'react'
import axios from 'axios'

const App = () => {
  axios.get('http://127.0.0.1:8000/').then(
    res =>{
      console.log(res)
    }
  )
  return (
    <div>App</div>
  )
}

export default App