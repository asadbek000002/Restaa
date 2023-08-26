let list = document.querySelectorAll('.list .item');
// let arr = [];
list.forEach(item => {
    item.addEventListener('click', function(event){
        if(event.target.classList.contains('add')){

            var itemNew = item.cloneNode(true);
            let checkIsset  = false;

            let listCart = document.querySelectorAll('.cart .item');
            listCart.forEach(cart =>{
                cart.classList.add('totall')
                // console.log(cart)
                if(cart.getAttribute('data-key') == itemNew.getAttribute('data-key')){
                    checkIsset = true;
                    cart.classList.add('danger');
                    setTimeout(function(){
                        cart.classList.remove('danger');
                    },1000)
                }
            })
            if(checkIsset == false){
                document.querySelector('.listCart').appendChild(itemNew);
            }

        }
    })
})
function Remove($key){
    let listCart = document.querySelectorAll('.cart .item');
    listCart.forEach(item => {
        if(item.getAttribute('data-key') == $key){
            item.remove();
            return;
        }
    })
}


let title = document.querySelector('.center-title')
let menuss = document.querySelector('.previuse-ul')
let center = document.querySelectorAll('.list');


menuss.addEventListener('click', (e) => {
    if (e.target.tagName == 'LI'){
        // console.log(e.target.textContent);
        title.textContent = e.target.textContent
        // console.log(center)
        center.forEach((item) => {
            item.style.display="none";
            // console.log(item.className.includes(e.target.textContent))
            // console.log(item.className, e.target.textContent )
         if(item.className.includes(e.target.textContent)){
                item.style.display="grid";
        console.log(e.target.textContent);

        console.log(center)

            }
        })
    }

})


let cartList = document.querySelector('.listCart')

// console.log(cartList.childElement)


const le =  setInterval(() => {
    console.log(cartList.childNodes)
}, 1000);

