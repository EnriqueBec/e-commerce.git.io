document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const totalPago = document.querySelector("#total-pago");
    const productosEnCarrito = JSON.parse(localStorage.getItem("productos-en-carrito")) || [];
  
    const total = productosEnCarrito.reduce((acc, producto) => {
      return acc + producto.precio * producto.cantidad;
    }, 0);
  
    totalPago.innerText = `$${total.toFixed(2)}`;
  
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // Evita el envío normal del formulario
  
      // Aquí puedes limpiar el carrito si quieres
      localStorage.removeItem("productos-en-carrito");
  
      // Redireccionar a la página de confirmación
      window.location.href = "compraterminada.html";
    });
  });
  