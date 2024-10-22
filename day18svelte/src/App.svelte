<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Morning from './lib/Morning.svelte'
  import Lotto from "./lib/Lotto.svelte";
  import Gugu from "./lib/Gugu.svelte";
  import Phone from "./lib/Phone.svelte";
  import Life from "./lib/Life.svelte";
  import {afterUpdate, beforeUpdate, onDestroy, onMount} from "svelte";
  import Strike from "./lib/Strike.svelte";
  import Emp from "./lib/Emp.svelte";
  onMount(async() => {
    console.log('[App] onMount')
  })

  onDestroy(async() => {
    console.log('[App] onDestroy')
  })

  beforeUpdate(async() => {
    console.log('[App] beforeUpdate')
  })

  afterUpdate(async() => {
    console.log('[App] afterUpdate')
  })
</script>
<main>

  <div class="card">
    <Emp />
  </div>

</main>

<style>

</style>
