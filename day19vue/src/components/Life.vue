<script setup>
import {onBeforeUpdate, onMounted, onUpdated, ref} from 'vue'

const msg = ref("Life Cycle")

onMounted(() => {
  console.log("[Life]onMounted")
})
onBeforeUpdate(() => {
  console.log("[Life]onBeforeUpdate")
})
onUpdated(() => {
  console.log("[Life]onUpdated")
})

</script>

<template>
  <span>{{msg}}</span>

</template>

<style scoped>

</style>
