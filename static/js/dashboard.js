items = document.querySelectorAll('.item');
console.log(items);

for(let i =0;i<items.length;i++) {
    console.log(items[i]);
    plus = items[i].querySelector('.plus a');
    console.log(plus);
    plus.addEventListener('click', function() {
        first = items[i].querySelector('.first');
        first.nextElementSibling.classList.toggle('none');
    })
}