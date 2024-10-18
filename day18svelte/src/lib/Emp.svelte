<script>
  let mylist = [
      {'e_id' : '1','e_name' : '1','e_gen' : '1','e_addr' : '1'},
      {'e_id' : '2','e_name' : '2','e_gen' : '2','e_addr' : '2'}
  ]

</script>
<style>
    table,td{
        border: 1px solid #ddd;
    }
</style>
<table>
    <tr>
        <td>사번</td>
        <td>이름</td>
        <td>성별</td>
        <td>주소</td>
    </tr>
    <tr>
        {#each mylist as item}
        <td>{item.e_id}</td>
        <td>{item.e_name}</td>
        <td>{item.e_gen}</td>
        <td>{item.e_addr}</td>
            {/each}
    </tr>
    <tr>
        <td colspan="4">
            선택된 데이터가 없습니다.
        </td>
    </tr>
</table>