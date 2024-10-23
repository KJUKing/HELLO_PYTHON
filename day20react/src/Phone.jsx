import {useState} from 'react'
import './Phone.css'

function Phone() {
    const [disp, setDisp] = useState("")

    let myclick = (e) => {
        let str_new = e.target.value
        let str_old = disp

        let resultStr = "";
        resultStr = str_old + str_new;
        setDisp(resultStr)
    }
    let mycall = () => {
        alert("calling\n" + disp)
    }

    return (
        <>
            <table>
                <tbody>
                <tr>
                    <td colSpan="3">
                        <input type="text" value={disp} onChange={(e) => setDisp(e.target.value)}/>
                    </td>
                </tr>
                <tr>
                    <td><input type="button" value="1" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="2" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="3" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                </tr>
                <tr>
                    <td><input type="button" value="4" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="5" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="6" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                </tr>
                <tr>
                    <td><input type="button" value="7" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="8" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td><input type="button" value="9" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                </tr>
                <tr>
                    <td><input type="button" value="0" onClick={(event) => {
                        myclick(event)
                    }}/></td>
                    <td colSpan="2">
                        <input type="button" value="☏" onClick={mycall}/>
                    </td>
                </tr>
                </tbody>
            </table>

        </>
    )

}


export default Phone
