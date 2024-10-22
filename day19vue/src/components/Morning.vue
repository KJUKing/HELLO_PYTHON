<script setup>
import { ref } from 'vue'

const msg = ref("Good Morning")


let myclick = () => {
  msg.value = "Good Evening"
}

</script>

<template>
  <span>{{msg}}</span>

  <input type="button" value="CLICK" @click="myclick" />

</template>

<style scoped>

</style>
