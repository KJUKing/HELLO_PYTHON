<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Morning from "./lib/Morning.svelte";
  import Lotto from "./lib/Lotto.svelte";
  import Gugu from "./lib/Gugu.svelte";
  import Phone from "./lib/Phone.svelte";
  import Life from "./lib/Life.svelte";

   import {onMount, onDestroy, beforeUpdate, afterUpdate, tick} from 'svelte'
  import Strike from "./lib/Strike.svelte";
  import Emp from "./lib/Emp.svelte";

    let msg = "Life Cycle"

    onMount(async () => {
        console.log('[Life] onMount')
    })

    onDestroy(async () => {
        console.log('[Life] onDestroy')
    })

    beforeUpdate(async () => {
        console.log('[Life] beforeUpdate')
    })

    afterUpdate(async () => {
        console.log('[Life] afterUpdate')
    })
</script>

<main>


  <div class="card">
<!--    <Morning />-->
    <Emp />
  </div>

</main>

<style>

</style>
