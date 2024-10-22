<script setup>
import {onMounted, ref} from 'vue'

const mine = ref("")
const com = ref("123")
const disp = ref("")

let myclick = ()=> {
  let s = getS(mine.value,com.value);
  let b = getB(mine.value,com.value);
  let line = mine.value + "\t" + s+"S"+b+"B\n"

  disp.value += line
  mine.value = ""
  if(s==3){
      alert("축하합니다.")
  }
}

let getS = (mine,com) => {
	var m1 = mine.substring(0,1);
	var m2 = mine.substring(1,2);
	var m3 = mine.substring(2,3);

	var c1 = com.substring(0,1);
	var c2 = com.substring(1,2);
	var c3 = com.substring(2,3);

	var ret = 0;
	if(m1 == c1) ret++;
	if(m2 == c2) ret++;
	if(m3 == c3) ret++;

	return ret;
}

let getB = (mine,com) => {
	var m1 = mine.substring(0,1);
	var m2 = mine.substring(1,2);
	var m3 = mine.substring(2,3);

	var c1 = com.substring(0,1);
	var c2 = com.substring(1,2);
	var c3 = com.substring(2,3);

	var ret = 0;
	if(m1 == c2 || m1 == c3) ret++;
	if(m2 == c1 || m2 == c3) ret++;
	if(m3 == c1 || m3 == c2) ret++;

	return ret;
}
let ran3 = () => {
	var arr = [1,2,3,4,5,6,7,8,9];

	for(let i=0;i<1000;i++){
		let rnd = parseInt(Math.random()*9);
		let a = arr[0];
		let b = arr[rnd];
		arr[0]=b;
		arr[rnd]=a;
	}
	return arr[0]+""+arr[1]+""+arr[2];
}

onMounted(() => {
    com.value = ran3()
    console.log("com",com.value)
})

</script>

<template>
  <table>
    <tr>
      <td>야구게임</td>
      <td><input type="text" v-model:="mine"></td>
    </tr>
    <tr>
      <td colspan="2">
        <input type="button" value="스크라이크"  @click="myclick" >
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <textarea rows="14" v-model:="disp"></textarea>
      </td>
    </tr>
  </table>

</template>

<style scoped>
input[type='text']{
  width: 30px;
}
table,td{
  border : 1px solid #ccc;
}
</style>
