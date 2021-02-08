document.getElementById("btn-login").addEventListener("click", (e) => {
    let form = document.querySelector("#form-login")
    let data = new FormData(form)
    let url = e.target.dataset.url
    fetch(url, {
        method: "POST",
        body: data
    }).then(data => data.json()).then(response => {
        if (response.status == 200) {
            window.location.href = response.success
        } else {
            document.getElementById("id_username").value = ""
            document.getElementById("id_password").value = ""
            messages(2000,"Error!","error",response.message)
        }
    })
})
