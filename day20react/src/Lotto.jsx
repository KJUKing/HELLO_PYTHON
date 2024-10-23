import { useState } from 'react'

function Lotto() {
  const [l1, setL1] = useState("__")
  const [l2, setL2] = useState("__")
  const [l3, setL3] = useState("__")
  const [l4, setL4] = useState("__")
  const [l5, setL5] = useState("__")
  const [l6, setL6] = useState("__")

    const myclick = () =>{
        var arr =  [
            1,2,3,4,5,   6,7,8,9,10,
            11,12,13,14,15,   16,17,18,19,20,
            21,22,23,24,25,   26,27,28,29,30,
            31,32,33,34,35,   36,37,38,39,40,
            41,42,43,44,45
        ];

        for(var i=0;i<1000;i++){
            var rnd = parseInt( Math.random()*45+"");
            var a = arr[0];
            var b = arr[rnd];
            arr[0]=b;
            arr[rnd]=a;
        }

        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 6; j++) {
                if (arr[i] < arr[j]) {
                    let a = arr[i]
                    let b = arr[j];
                    arr[i] = b;
                    arr[j] = a;
                }
            }
        }

        setL1(arr[0]);
        setL2(arr[1]);
        setL3(arr[2]);
        setL4(arr[3]);
        setL5(arr[4]);
        setL6(arr[5]);
    }

  return (
    <>
        <table>
            <tbody>
            <tr>
                <td>{l1}</td>
                <td>{l2}</td>
                <td>{l3}</td>
                <td>{l4}</td>
                <td>{l5}</td>
                <td>{l6}</td>
            </tr>
            <tr>
                <td colSpan={6}>
                    <input type="button" value="로또 생성하기" onClick={myclick}/>
                </td>
            </tr>
            </tbody>
        </table>
    </>
  )
}

export default Lotto
