<script>
import {onMount} from "svelte";

let mine = ""
let disp = ""
let com = "546"

let myclick = ()=> {
    let s = getS(mine,com);
    let b = getB(mine,com);

    let line = mine + "\t" + s+"S"+b+"B\n"
    disp = disp + line
    mine = ""
    if(s==3){
        alert("축하합니다.")
    }
}
function getS(mine,com){
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
function getB(mine,com){
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
function ran3(){
	var arr = [1,2,3,4,5,6,7,8,9];

	for(var i=0;i<1000;i++){
		var rnd = parseInt(Math.random()*9);
		var a = arr[0];
		var b = arr[rnd];
		arr[0]=b;
		arr[rnd]=a;
	}


	return arr[0]+""+arr[1]+""+arr[2];
}
onMount(async() => {
    com = ran3()
    console.log("com",com)
})

</script>
<style>
input[type='text']{
    width: 30px;
}
table,td{
    border:1px solid;
}

</style>

<table>
    <tr>
        <td>스트라이크</td>
        <td>
            <input type="text" bind:value="{mine}" />
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <input type="button" value="게임하기" on:click={myclick}/>
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <textarea rows="20" cols="20" >{disp}</textarea>
        </td>
    </tr>
</table>
