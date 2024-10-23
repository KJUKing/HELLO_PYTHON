import {useEffect, useState} from 'react'

function Life() {
  const [msg, setMsg] = useState("Good Morning")

    const myclick = () => {
        setMsg("Good Evening");
    }
    useEffect(() => {
        console.log("useEffect:onMount");
        return () => {
            console.log("userEffect:onMount**")
        }
    }, []);
  return (
    <>
        <div>{msg}</div>
        <input type="button" onClick={myclick}/>
    </>
  )
}

export default Life
