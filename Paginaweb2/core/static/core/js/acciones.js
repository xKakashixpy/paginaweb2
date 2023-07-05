
// Acciones para destacar tarjetas cuando paso el cursor
$(document).ready(function() {
  $(".highlight-image").mouseover(function() {
    $(this).addClass("highlighted");
  });

  $(".highlight-image").mouseout(function() {
    $(this).removeClass("highlighted");
  });
});

