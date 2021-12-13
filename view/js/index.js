const find = document.getElementById("button-find");
const form = document.querySelector("form");

find.addEventListener("click", postFind);
async function postFind() {
    const harga = form.harga.value;
    const data = {
        "harga": harga
    };
    console.log(data)
    window.location = '/result.html'
}