const productosEnCarrito = JSON.parse(localStorage.getItem("productos-en-carrito")) || [];

const contenedorCarritoVacio = document.querySelector("#carrito-vacio");
const contenedorCarritoProductos = document.querySelector("#carrito-productos");
const contenedorCarritoAcciones = document.querySelector("#carrito-acciones");
const contenedorCarritoComprado = document.querySelector("#carrito-comprado");
const numerito = document.querySelector("#numerito");

function cargarCarrito() {
    if (productosEnCarrito.length > 0) {
        contenedorCarritoVacio.classList.add("disabled");
        contenedorCarritoProductos.classList.remove("disabled");
        contenedorCarritoAcciones.classList.remove("disabled");
        contenedorCarritoComprado.classList.add("disabled");

        contenedorCarritoProductos.innerHTML = "";

        productosEnCarrito.forEach(producto => {
            const div = document.createElement("div");
            div.classList.add("carrito-producto");
            div.innerHTML = `
                <img class="carrito-producto-imagen" src="${producto.imagen}" alt="${producto.titulo}">
                <div class="carrito-titulo">
                    <small>Titulo</small>
                    <h3>${producto.titulo}</h3>
                </div>
                <div class="carrito-producto-precio">
                    <small>Precio</small>
                    <p>$${producto.precio}</p>
                </div>
                <button class="carrito-producto-eliminar" data-id="${producto.id}">
                    <i class="bi bi-trash-fill"></i>
                </button>
            `;
            contenedorCarritoProductos.append(div);
        });

        actualizarBotonesEliminar();
    } else {
        contenedorCarritoVacio.classList.remove("disabled");
        contenedorCarritoProductos.classList.add("disabled");
        contenedorCarritoAcciones.classList.add("disabled");
        contenedorCarritoComprado.classList.add("disabled");
    }
    actualizarNumerito();
}

function actualizarBotonesEliminar() {
    const botonesEliminar = document.querySelectorAll(".carrito-producto-eliminar");

    botonesEliminar.forEach(boton => {
        boton.addEventListener("click", eliminarDelCarrito);
    });
}

function eliminarDelCarrito(e) {
    const idBoton = e.currentTarget.dataset.id;
    const index = productosEnCarrito.findIndex(producto => producto.id === idBoton);

    if (index !== -1) {
        if (productosEnCarrito[index].cantidad > 1) {
            productosEnCarrito[index].cantidad--; // Reducir cantidad si hay más de uno
        } else {
            productosEnCarrito.splice(index, 1); // Eliminar si solo queda uno
        }

        localStorage.setItem("productos-en-carrito", JSON.stringify(productosEnCarrito));
        cargarCarrito(); // Recargar la interfaz
    }
}

function actualizarNumerito() {
    let nuevoNumerito = productosEnCarrito.reduce((acc, producto) => acc + producto.cantidad, 0);
    numerito.innerText = nuevoNumerito;
}

cargarCarrito();
