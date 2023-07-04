const imagenes = document.querySelectorAll('.image-block img');

imagenes.forEach((imagen) => {
    imagen.addEventListener('mouseover', () => {
        imagen.classList.add('resaltado');
    });

    imagen.addEventListener('mouseout', () => {
        imagen.classList.remove('resaltado');
    });
});


// Obtener el elemento del carrito
var cartElement = document.getElementById("cart-icon");

// Variable para llevar el conteo de los elementos en el carrito
var cartCount = 0;

// Función para agregar un elemento al carrito
function addToCart() {
  cartCount++;
  cartElement.textContent = "Carrito (" + cartCount + ")";
}

// Asociar la función addToCart a algún evento, por ejemplo, al hacer clic en un botón "Agregar al carrito"
var addToCartButton = document.getElementById("add-to-cart-button");
addToCartButton.addEventListener("click", addToCart);
