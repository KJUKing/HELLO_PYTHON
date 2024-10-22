<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Morning from "./components/Morning.vue";
import MorningReac from "./components/MorningReac.vue";
import Lotto from "./components/Lotto.vue";
import Gugu from "./components/Gugu.vue";
import Phone from "./components/Phone.vue";
import Life from "./components/Life.vue";
import {onBeforeUpdate, onMounted, onUpdated} from "vue";
import Strike from "./components/Strike.vue";
import Emp from "./components/Emp.vue";

onMounted(() => {
  console.log("[App]onMounted")
})
onBeforeUpdate(() => {
  console.log("[App]onBeforeUpdate")
})
onUpdated(() => {
  console.log("[App]onUpdated")
})

</script>

<template>
  <Emp/>
</template>

<style scoped>

</style>
