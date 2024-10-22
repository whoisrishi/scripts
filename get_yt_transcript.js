//run in console

data = document.getElementsByClassName("segment-text")
let formatted_data = ""

for(let i = 0; i < data.length; i++){
formatted_data += " " + data[i].innerText;
}

console.log(formatted_data)
