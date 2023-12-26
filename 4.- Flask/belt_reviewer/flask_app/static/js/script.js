var login_form = document.querySelector('#login-form');
login_form.onsubmit = function (event) {
    //Previene el comportamiento por default de mi formulario
    event.preventDefault();

    //Obtener los datos del formulario
    var formulario = new FormData(login_form);
    /*
    formulario = {
        "email": "elena@codingdojo.com",
        "password": "password1212"
    }
    */
    fetch('/login',  { method:'POST', body:formulario })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.message != 'correcto') {
                alert(data.message);
            } else {
                //Todo está bien, redireccionamos
                window.location.href = "/dashboard";
            }
        })
}