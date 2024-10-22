<script setup>
import { ref } from 'vue'

const num = ref("")

let myclick = (e) =>{
  let str_new = e.target.value
  num.value = num.value + str_new
}
let mycall = () => {
  alert("calling\n"+num.value)
}

</script>

<template>
  <table>
    <tr>
      <td colspan="3">
        <input type="text" v-model="num" />
      </td>
    </tr>
    <tr>
      <td><input type="button" value="1" @click="myclick($event)"></td>
      <td><input type="button" value="2" @click="myclick($event)"/></td>
      <td><input type="button" value="3" @click="myclick($event)"/></td>
    </tr>
    <tr>
      <td><input type="button" value="4" @click="myclick($event)"/></td>
      <td><input type="button" value="5" @click="myclick($event)"/></td>
      <td><input type="button" value="6" @click="myclick($event)"/></td>
    </tr>
    <tr>
      <td><input type="button" value="7" @click="myclick($event)"/></td>
      <td><input type="button" value="8" @click="myclick($event)"/></td>
      <td><input type="button" value="9" @click="myclick($event)"/></td>
    </tr>
    <tr>
      <td><input type="button" value="0" @click="myclick($event)"/></td>
      <td colspan="2">
        <input type="button" value="☎" v-on:click="mycall"/>
      </td>
    </tr>

  </table>

</template>

<style scoped>
table,td{
  border : 1px solid #ccc;
  text-align: center;
}
input[type='text']{
  width: 90px;
  text-align: right;
}
</style>
