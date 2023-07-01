const imagenes = document.querySelectorAll('.image-block img');

imagenes.forEach((imagen) => {
    imagen.addEventListener('mouseover', () => {
        imagen.classList.add('resaltado');
    });

    imagen.addEventListener('mouseout', () => {
        imagen.classList.remove('resaltado');
    });
});