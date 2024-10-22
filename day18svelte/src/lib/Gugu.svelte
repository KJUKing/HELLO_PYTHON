<script>
  let dan = "2"
  let disp = ""

  let myclick = () => {
      let idan = parseInt(dan)
      disp = ""
      for (let i = 1; i <= 9; i++) {
          disp += dan+"*"+i+"="+(idan*i)+"<br/>"
      }
  }

</script>

<style>
    #it{
        width: 30px;
    }
    table,td{
        border:1px solid;
    }
    div{
        height: 200px;
    }
</style>

<table >
    <tr>
        <td>출력단수</td>
        <td><input type="text" id="it" bind:value="{dan}" ></td>
    </tr>
    <tr>
        <td colspan="2">
            <input type="button" value="구구단출력" on:click={myclick} />
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <div>{@html disp}</div>
        </td>
    </tr>

</table>