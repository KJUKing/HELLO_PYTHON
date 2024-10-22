<script>
    import {onMount} from "svelte";

    let mylist = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1'},
        {'e_id':'2','e_name':'2','gen':'2','addr':'2'}
    ]
    let vo = {'e_id':'','e_name':'','gen':'','addr':''}

    function fn_list(){
        fetch('http://127.0.0.1/emp_list.ajax',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify({menu: "짬뽕"})
        })
        .then(response => response.json())
        .then(json => {
            console.log(json.list);
            mylist = json.list;
        })
    }
    let fn_one = (e_id)=>{
        fetch('http://127.0.0.1/emp_one.ajax',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify({e_id: e_id})
        })
        .then(response => response.json())
        .then(json => {
            vo = json.vo
        })
    }
    let fn_add = () => {
        let param = vo
        fetch('http://127.0.0.1/emp_add.ajax',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify(param)
        })
        .then(response => response.json())
        .then(json => {
		    let cnt = json.cnt;
            if(cnt==1){
                alert("정상적으로 추가되었습니다.")
                fn_list()
                vo.e_id = ""
                vo.e_name = ""
                vo.gen = ""
                vo.addr = ""
            }else{
                alert("추가도중 문제가 생겼습니다.");
            }
        })
    }

    let fn_mod = () => {
        let param = vo
        fetch('http://127.0.0.1/emp_mod.ajax',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify(param)
        })
        .then(response => response.json())
        .then(json => {
		    let cnt = json.cnt;
            if(cnt==1){
                alert("정상적으로 수정되었습니다.")
                fn_list()
                vo.e_id = ""
                vo.e_name = ""
                vo.gen = ""
                vo.addr = ""
            }else{
                alert("수정도중 문제가 생겼습니다.");
            }
        })
    }

    let fn_del = () => {
        let param = vo
        fetch('http://127.0.0.1/emp_del.ajax',{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify(param)
        })
        .then(response => response.json())
        .then(json => {
		    let cnt = json.cnt;
            if(cnt==1){
                alert("정상적으로 삭제되었습니다.")
                fn_list()
                vo.e_id = ""
                vo.e_name = ""
                vo.gen = ""
                vo.addr = ""
            }else{
                alert("삭제도중 문제가 생겼습니다.");
            }
        })
    }

    onMount(async() => {
        fn_list()
    })

</script>
<style>
    table,td{
        border: 1px solid #ddd;
    }
</style>

<a on:click={fn_list}>ajax</a>

<table>
    <tr>
        <td>사번</td>
        <td>이름</td>
        <td>성별</td>
        <td>주소</td>
    </tr>
    {#each mylist as vo}
    <tr>
        <td><a on:click={fn_one(vo.e_id)}>{vo.e_id}</a></td>
        <td>{vo.e_name}</td>
        <td>{vo.gen}</td>
        <td>{vo.addr}</td>
    </tr>
    {/each}
</table>

<table>
    <tr>
        <td>사번</td>
        <td>
            <input type="text" bind:value="{vo.e_id}" />
        </td>
    </tr>
    <tr>
        <td>이름</td>
        <td>
            <input type="text" bind:value="{vo.e_name}" />
        </td>
    </tr>
    <tr>
        <td>성별</td>
        <td>
            <input type="text" bind:value="{vo.gen}" />
        </td>
    </tr>
    <tr>
        <td>주소</td>
        <td>
            <input type="text" bind:value="{vo.addr}" />
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <input type="button" value="추가" on:click={fn_add} />
            <input type="button" value="수정" on:click={fn_mod} />
            <input type="button" value="삭제" on:click={fn_del} />
        </td>
    </tr>
</table>
