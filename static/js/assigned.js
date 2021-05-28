table = document.querySelectorAll('tbody .status')
console.log(table);

for (let i=0;i<table.length;i++) {
    if(table[i].textContent == "OPEN") {
        table[i].style.color = "blue";
    }
    else if(table[i].textContent == "REJECTED") {
        table[i].style.color = "red";
    }
    else if(table[i].textContent == "VALIDATED") {
        table[i].style.color = "green";
    }
    else {
        table.style.color = "black";
    }
}