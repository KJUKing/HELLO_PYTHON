<script>
let disp = ""

let myclick = (e) =>{
    let str_new =  e.target.value
    let str_old = disp

    disp = str_old + str_new
}
let mycall = () =>{
    alert("calling\n"+disp)
}


</script>
<style>
    input[type='text']{
        width: 100px;
        text-align: right;
    }
    td{
        text-align: center;
    }
    table,td {
        border:1px solid;
    }

</style>
<table>
    <tr>
        <td colspan="3">
            <input type="text" value="{disp}" />
        </td>
    </tr>
    <tr>
        <td><input type="button" value="1" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="2" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="3" on:click={(event)=>{myclick(event)}} /></td>
    </tr>
    <tr>
        <td><input type="button" value="4" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="5" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="6" on:click={(event)=>{myclick(event)}} /></td>
    </tr>
    <tr>
        <td><input type="button" value="7" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="8" on:click={(event)=>{myclick(event)}} /></td>
        <td><input type="button" value="9" on:click={(event)=>{myclick(event)}} /></td>
    </tr>
    <tr>
        <td><input type="button" value="0" on:click={(event)=>{myclick(event)}} /></td>
        <td colspan="2">
            <input type="button" value="☏" on:click={mycall} />
        </td>
    </tr>

</table>
