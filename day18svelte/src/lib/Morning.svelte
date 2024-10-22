<script>
  let msg = "Good Morning"
  const myclick = () =>{
    msg = "Good Evening"
  }
</script>

<span>{msg}</span>
<input type="button" value="CLICK" on:click={myclick} />
