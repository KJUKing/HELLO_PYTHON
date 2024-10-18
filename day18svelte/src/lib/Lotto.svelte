<script>
  let l1 = "__"
  let l2 = "__"
  let l3 = "__"
  let l4 = "__"
  let l5 = "__"
  let l6 = "__"


  const myClick = () =>{


  const arr =[1,2,3,4,5   ,6,7,8,9,10,
            11,12,13,14,15,   16,17,18,19,20,
            21,22,23,24,25,   26,27,28,29,30,
            31,32,33,34,35,   36,37,38,39,40,
            41,42,43,44,45
        ];

      for (var i = 0; i < 1000; i++) {
            var rnd = parseInt(""+Math.random() *45);
            let a = arr[0];
            let b = arr[rnd];
            arr[0]=b
            arr[rnd]=a;
      }
      var lottoArr = [arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]]

      l1 = "" + lottoArr[0];
      l2 = "" + lottoArr[1];
      l3 = "" + lottoArr[2];
      l4 = "" + lottoArr[3];
      l5 = "" + lottoArr[4];
      l6 = "" + lottoArr[5];

  }

</script>
<table border="1px">
    <tr>
        <td>{l1}</td>
        <td>{l2}</td>
        <td>{l3}</td>
        <td>{l4}</td>
        <td>{l5}</td>
        <td>{l6}</td>
    </tr>
    <tr>
        <td colspan="6">
            <input type="button" value="로또생성하기" on:click={myClick} />
        </td>
    </tr>
</table>