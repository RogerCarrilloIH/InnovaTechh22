function removerImagen() {
    var inputImagen = document.getElementById("inputImagen");
    var seccionImagen = document.getElementById("seccionImagen");
    var inputNombreImagen = document.getElementById("inputNombreImagen");
    
    seccionImagen.classList.add('d-none');
    inputImagen.classList.remove('d-none');
    inputNombreImagen.value = "1";
}