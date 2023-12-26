/* PROMESA */
function muestraPerrito() {
    fetch("https://dog.ceo/api/breeds/image/random")
        .then(response => response.json())
        .then(data => {
            /*
            data = {
                "message": "url/imagen.png",
                "status": "success"
            }
            */
           console.log(data);
           
           var img_perrito = `<img src="${data['message']}" alt="perrito">`;
           var otra_imagen = '<img src="'+data['message']+'" alt="perrito">'; //Si no tenemos las comillas `
           document.querySelector('.imagen-perrito').innerHTML = img_perrito;
        })
}