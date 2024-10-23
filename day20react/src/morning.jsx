import { useState } from 'react'

function Morning() {
  const [msg, setMsg] = useState("Good Morning")

    const myclick = () =>{
        setMsg("Good Evening");
    }

  return (
    <>
        <div>{msg}</div>
        <input type="button" value="CLICK" onClick={myclick}/>
    </>
  )
}

export default Morning
