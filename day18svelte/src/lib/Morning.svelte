<script>
  let msg = "Good Morning"

  const evening = () => {
    msg = "Good Evening"
  }

</script>

<span>{msg}</span>
<input type="button" value="CLICK" on:click={evening}>
