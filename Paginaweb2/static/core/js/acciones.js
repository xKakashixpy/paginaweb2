
// Acciones para destacar tarjetas cuando paso el cursor
$(document).ready(function() {
  $(".highlight-image").mouseover(function() {
    $(this).addClass("highlighted");
  });

  $(".highlight-image").mouseout(function() {
    $(this).removeClass("highlighted");
  });
});

// acciones relacioandas al carrito de compras 

// Obtener todos los botones de agregar al carrito
const agregarCarritoButtons = document.querySelectorAll('.agregar-carrito');

// Agregar evento de clic a cada botón
agregarCarritoButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Obtener el ID del producto desde el atributo de datos
    const productoId = button.dataset.producto;

    // Realizar una solicitud AJAX o enviar el ID del producto al servidor para agregarlo al carrito
    // Puedes usar fetch() u otra biblioteca de AJAX como Axios

    // Ejemplo utilizando fetch():
    fetch('/agregar-al-carrito/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}', // Obtener el token de seguridad de Django
      },
      body: JSON.stringify({ productoId }),
    })
    .then(response => {
      // Manejar la respuesta del servidor
      if (response.ok) {
        // Producto agregado correctamente al carrito
        console.log('Producto agregado al carrito');
      } else {
        // Error al agregar el producto al carrito
        console.error('Error al agregar el producto al carrito');
      }
    })
    .catch(error => {
      console.error('Error en la solicitud AJAX:', error);
    });
  });
});
