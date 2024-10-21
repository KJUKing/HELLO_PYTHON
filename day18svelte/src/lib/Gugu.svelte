 <script>
    let dan = "2"
    let disp = ""

    const myClick = () => {

        var idan = parseInt(dan);
        for (var i = 1; i <= 9; i++) {
            disp += dan+" * "+i+" = "+(idan*i)+"<br/>" ;
        }
    }
</script>
<style>
    #it{
        width: 30px;
    }
    table,td{
        border: 1px;
    }
    div{
        height: 200px;
    }
</style>

<table>
    <tr>
        <td>출력단수</td>
        <td><input type="text" id="it" bind:value={dan}></td>
    </tr>
    <tr>
        <td colspan="2">
            <input type="text"value="구구단출력" on:click={myClick}>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div>{@html disp}</div>
<!--           @html html화로 선언한다-->
        </td>
    </tr>


</table>
