
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

  // Array para almacenar los artículos seleccionados
  var carrito = [];

  // Función para agregar un artículo al carrito
  function agregarAlCarrito(articulo) {
    carrito.push(articulo);
    console.log("Artículo agregado al carrito:", articulo);
  }

  // Evento click del botón "Agregar al carrito"
  var botonesAgregar = document.querySelectorAll(".articulo button");
  botonesAgregar.forEach(function (boton) {
    boton.addEventListener("click", function (event) {
      var articulo = event.target.parentElement;
      agregarAlCarrito(articulo);
    });
  });
