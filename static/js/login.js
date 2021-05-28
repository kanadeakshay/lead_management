heading = document.querySelector('.right h1');
// console.log(heading);

if(heading.textContent == "") {
    heading.classList.toggle('none');
}

flex = document.querySelector('.flex')
// console.log(flex);

left = document.querySelector('.left');
right = document.querySelector('.right');
// console.log(left);


function func(x) {
    if(x.matches) {
        left.classList.add('none');
        right.style.width = "80%";
    }
    else {
        left.classList.remove('none');
        right.style.width = "60%";
    }
}

var x = window.matchMedia("(max-width : 700px)")
func(x)
x.addListener(func)