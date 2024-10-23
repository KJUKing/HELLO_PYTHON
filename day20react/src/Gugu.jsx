import { useState } from 'react'

function Gugu() {
  const [dan, setDan] = useState("2")
    const [result, setResult] = useState("");

    const myclick = () =>{

        let idan = parseInt(dan);
        let resultStr = "";

        for (let i = 1; i <= 9; i++) {
            resultStr += `${idan} * ${i} = ${idan*i}<br/>`;
        }
        setResult(resultStr)
    }

  return (
    <>
        <table>
            <tbody>
            <tr>
                <td>출력단수</td>
                <td><input type="text" id="it" value={dan} onChange={(e) => setDan(e.target.value)}/> </td>
            </tr>
            <tr>
                <td colSpan="2">
                    <input type="button" value="구구단 출력" onClick={myclick}/>
                </td>
            </tr>
            <tr>
                <td colSpan={2}>
                    <div dangerouslySetInnerHTML={{ __html: result }} /> {/* 결과 출력 */}
                </td>
            </tr>
            </tbody>
        </table>
    </>
  )
}

export default Gugu
