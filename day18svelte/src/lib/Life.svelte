

<script>
    import { onMount, onDestroy, beforeUpdate, afterUpdate} from 'svelte'
    let msg = "Life Cycle"


    onMount(async() => {
        console.log('[Life] onMount')
    })

    onDestroy(async() => {
        console.log('[Life] onDestroy')
    })

    beforeUpdate(async() => {
      console.log('[Life] beforeUpdate')
    })

    afterUpdate(async() => {
        console.log('[Life] afterUpdate')
    })

</script>

<span>{msg}</span>

