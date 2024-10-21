<script setup>
import {reactive, ref} from 'vue'

const msg = reactive({msg : "Good Morning"});

let myclick = () => {
  msg.value = "Good Evening"
}
</script>

<template>
    <span>{{data.msg}}</span>

  <input type="button" value="CLICK" @click="myclick"/>
</template>

<style scoped>

</style>