const number = (x) =>{
    let ans = document.getElementById("ans");
    ans.value += x // ans.value = ans.value + x

}
const empty = () =>{
   document.getElementById("ans").value = ""
}
const lClear = () =>{
    
    let ans = document.getElementById("ans");
    let newData ="";

    for (let i = 0 ; i<(ans.value.length - 1) ; i++) {
        newData += ans.value[i]
    }
    ans.value = newData;
}

const answer = () =>{
    let ans = document.getElementById("ans");
    ans.value = eval(ans.value)
}