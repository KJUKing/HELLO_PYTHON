<script setup>
import { ref } from 'vue'

let l1 = ref("__")
let l2 = ref("__")
let l3 = ref("__")
let l4 = ref("__")
let l5 = ref("__")
let l6 = ref("__")

let myclick = () => {
	let arr =  [
	    1,2,3,4,5,   6,7,8,9,10,
	    11,12,13,14,15,   16,17,18,19,20,
	    21,22,23,24,25,   26,27,28,29,30,
	    31,32,33,34,35,   36,37,38,39,40,
	    41,42,43,44,45
	];

	for(let i=0;i<1000;i++){
		let rnd = parseInt(Math.random()*45);
		let a = arr[0];
		let b = arr[rnd];
		arr[0]=b;
		arr[rnd]=a;
	}

  l1.value = arr[0]
  l2.value = arr[1]
  l3.value = arr[2]
  l4.value = arr[3]
  l5.value = arr[4]
  l6.value = arr[5]

}

</script>

<template>
  <table>
    <tr>
      <td>{{l1}}</td>
      <td>{{l2}}</td>
      <td>{{l3}}</td>
      <td>{{l4}}</td>
      <td>{{l5}}</td>
      <td>{{l6}}</td>
    </tr>
    <tr>
      <td colspan="6">
        <input type="button" value="로또생성하기" @click="myclick">
      </td>
    </tr>
  </table>


</template>

<style scoped>
table,td {
  border : 1px solid #ccc;
}
</style>
