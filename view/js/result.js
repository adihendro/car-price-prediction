const find = document.getElementById("button-back");
find.addEventListener("click", postBack);

async function postBack() {
    // const username = form.username.value;
    // const fullname = form.fullname.value;
    // const email = form.email.value;
    // const password = form.password.value;
    // const data = {
    //     "username": username,
    //     "fullname": fullname,
    //     "email": email,
    //     "password": password,
    //     "role": ["ROLE_CLIENT"]
    // };
    window.location.href = '/'
}

function currencyFormat(value) {
    if (isNaN(value)) {
      value = 0
    } else {
        value = parseInt(value)
    }
    return value.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ".");
}

let modal = document.getElementById("modal")
let profit = document.getElementById("result1")
let hargaJual = document.getElementById("result2")

modal.innerHTML = currencyFormat(modal.innerHTML)
profit.innerHTML = currencyFormat(profit.innerHTML)
hargaJual.innerHTML = currencyFormat(hargaJual.innerHTML)