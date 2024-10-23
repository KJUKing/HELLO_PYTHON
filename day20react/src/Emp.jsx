import {useEffect, useState} from 'react'


function Emp() {
    const [e_id, setE_id] = useState("")
    const [e_name, setE_name] = useState("")
    const [e_gen, setE_gen] = useState("")
    const [e_addr, setE_addr] = useState("")

    const [list, setList] = useState(
        [
            {e_id: '1', e_name: '1', e_gen: '1', e_addr: '1'},
            {e_id: '2', e_name: '2', e_gen: '2', e_addr: '2'}
        ]
    )

    let fn_one = (e) => {
        let e_id = e.target.innerHTML;
        fetch('http://127.0.0.1/emp_one.ajax', {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({e_id: e_id})
        })
            .then(response => response.json())
            .then(json => {
                console.log(json);
            })
    }

    let fn_list = () => {
        fetch('http://127.0.0.1/emp_list.ajax', {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({menu: "짬뽕"})
        })
            .then(response => response.json())
            .then(json => {
                let list = json;
                setList(list);
                console.log(json.list);
            })
    }

    useEffect(() => {
        console.log("useEffect:onMount");
        fn_list();
    }, []);

    return (
        <>
            <table>
                <tbody>
                <tr>
                    <td>사번</td>
                    <td>이름</td>
                    <td>성별</td>
                    <td>주소</td>
                </tr>

                {list.map((vo, index) => (
                    <tr key={index}>
                        <td><a onClick={fn_one}>{vo.e_id}</a></td>
                        <td>{vo.e_name}</td>
                        <td>{vo.e_gen}</td>
                        <td>{vo.e_addr}</td>
                    </tr>
                ))}


                </tbody>
            </table>


            <table>
                <tbody>
                <tr>
                    <td>사번</td>
                    <td>
                        <input type="text" value={e_id} onChange={(e) => setE_id(e.target.value)}/>
                    </td>
                </tr>
                <tr>
                    <td>이름</td>
                    <td>
                        <input type="text" value={e_name} onChange={(e) => setE_name(e.target.value)}/>
                    </td>
                </tr>
                <tr>
                    <td>성별</td>
                    <td>
                        <input type="text" value={e_gen} onChange={(e) => setE_gen(e.target.value)}/>
                    </td>
                </tr>
                <tr>
                    <td>주소</td>
                    <td>
                        <input type="text" value={e_addr} onChange={(e) => setE_addr(e.target.value)}/>
                    </td>
                </tr>
                <tr>
                    <td colSpan="2">
                        <input type="button" value="추가"/>
                        <input type="button" value="수정"/>
                        <input type="button" value="삭제"/>
                    </td>
                </tr>
                </tbody>
            </table>
        </>
    )
}

export default Emp
