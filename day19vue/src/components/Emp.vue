
<script setup>
import {onMounted, ref} from 'vue'
import axios from "axios";

const mylist = ref([
  {"e_id":"1","e_name":"1","e_gen":"1","e_addr":"1"},
  {"e_id":"2","e_name":"2","e_gen":"2","e_addr":"2"}
])

const vo = ref({e_id:"_",e_name:"_",e_gen:"_",e_addr:"_"})

let fn_list = () => {
	axios.post('http://127.0.0.1/emp_list.ajax').then((resp)=>{
	    console.log(resp.data.list);
      mylist.value = resp.data.list;
	})
}

let fn_one = (e_id) => {
  const param ={
    e_id : e_id
  }

  axios.post('http://127.0.0.1/emp_one.ajax', param).then((resp)=>{
	    console.log(resp.data.vo);
      vo.value = resp.data.vo;
	})
}

let fn_add = () => {
  axios.post('http://127.0.0.1/emp_add.ajax', vo.value).then((resp) => {
    console.log(resp.data.cnt);
    let cnt = resp.data.cnt;
    if (cnt == 1) {
      alert("정상 추가");
      fn_list();
      vo.value.e_id = "";
      vo.value.e_name = "";
      vo.value.e_gen = "";
      vo.value.e_addr = "";
    } else {
      alert("추가 도중 문제발생")
    }
  })
}

let fn_mod = () => {
  axios.post('http://127.0.0.1/emp_mod.ajax', vo.value.e_id).then((resp) => {
    console.log(resp.data.cnt);
    let cnt = resp.data.cnt;
    if (cnt == 1) {
      alert("정상 수정");
      fn_list();
      vo.value.e_id = "";
      vo.value.e_name = "";
      vo.value.e_gen = "";
      vo.value.e_addr = "";
    } else {
      alert("수정 도중 문제발생")
    }
  })
}

let fn_del = () => {
  var flag = confirm("한번 지워진 데이터는 복구 불가합니다. \n 그래도 지우십니까?");
  if (!flag) return;
  axios.post('http://127.0.0.1/emp_del.ajax', vo.value).then((resp) => {
    console.log(resp.data.cnt);
    let cnt = resp.data.cnt;
    if (cnt == 1) {
      alert("정상 삭제");
      fn_list();
      vo.value.e_id = "";
      vo.value.e_name = "";
      vo.value.e_gen = "";
      vo.value.e_addr = "";
    } else {
      alert("삭제 도중 문제발생")
    }
  })
}

onMounted(() => {
  fn_list()
})

</script>

<template>
  <table>
    <tr>
      <td>사번</td>
      <td>이름</td>
      <td>성별</td>
      <td>주소</td>
    </tr>

    <tr v-for="(vo, index) in mylist" :key="index" >
      <td><a @click="fn_one(vo.e_id)">{{vo.e_id}}</a></td>
      <td>{{vo.e_name}}</td>
      <td>{{vo.e_gen}}</td>
      <td>{{vo.e_addr}}</td>
    </tr>

  </table>
  <table>
    <tr>
      <td>사번</td>
      <td><input type="text" v-model:="vo.e_id" /></td>
    </tr>
    <tr>
      <td>이름</td>
      <td><input type="text" v-model:="vo.e_name" /></td>
    </tr>
    <tr>
      <td>성별</td>
      <td><input type="text" v-model:="vo.e_gen" /></td>
    </tr>
    <tr>
      <td>주소</td>
      <td><input type="text" v-model:="vo.e_addr" /></td>
    </tr>
    <tr>
      <td colspan="2">
        <button @click="fn_add">추가</button>
        <button @click="fn_mod" >수정</button>
        <button @click="fn_del">삭제</button>
      </td>
    </tr>
  </table>

</template>

<style scoped>
table,td{
  border : 1px solid #ccc;
}
input[type=text]{
  width: 80px;
}
</style>
