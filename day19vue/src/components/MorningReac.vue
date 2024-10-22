<script setup>
import {reactive, ref} from 'vue'

const data = reactive({msg: 'Good Morning'})

let myclick = () => {
  data.msg = "Good Evening"
}

</script>

<template>
  <span>{{data.msg}}</span>
  <input type="button" value="CLICK" @click="myclick" />
</template>

<style scoped>

</style>
