<script setup>

import {ref} from "vue";

let dan = ref("2");
let disp = ref("__")
</script>

<template>
  <table>
    <tr>
      <td>출력단수:</td>
      <td>
        <input type="text" v-model:="dan" />
      </td>
    </tr>
    <tr>
      <td>
        <input type="button" value="출력하기"/>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <div>{{disp}}</div>
      </td>
    </tr>
  </table>
</template>

<style scoped>
input[type='text']{
  width: 30px;
}
table, td{
  border: 1px solid #ccc;
}
div {
  height: 200px;
}
</style>