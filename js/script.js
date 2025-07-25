let productos = [];

fetch("./js/productos.json")
    .then(response => response.json())
    .then(data => {
        productos = data;
        mostrarProductos(); 
    })
    

const contenedor = document.getElementById("productos");
const navLinks = document.querySelectorAll(".nav-links a");
const numerito = document.querySelector("#numerito");
let productosEnCarrito = JSON.parse(localStorage.getItem("productos-en-carrito")) || [];

function mostrarProductos(categoria = "todos") {
    contenedor.innerHTML = "";

    const productosFiltrados = categoria === "todos" 
        ? productos 
        : productos.filter(producto => producto.categoria.id === categoria);

    productosFiltrados.forEach(producto => {
        const div = document.createElement("div");
        div.classList.add("producto");
        div.innerHTML = `
            <img src="${producto.imagen}" alt="${producto.nombre}">
            <h2>${producto.titulo}</h2>
            <p>$${producto.precio}.00</p>
            <button class="producto-agregar carrito" id="${producto.id}"><i class="bi bi-cart-fill"> Compra ya</i></button>
            
        
        `;

        // <button class="producto-agregar corazon" id="${producto.id}"><i class="bi bi-heart"></i></button>
        contenedor.appendChild(div);
    });

    actualizarBotonesAgregar();
}

navLinks.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        const categoriaSeleccionada = e.target.innerText.toLowerCase();
        mostrarProductos(categoriaSeleccionada);
    });
});

function actualizarBotonesAgregar() {
    const botonesAgregar = document.querySelectorAll(".producto-agregar");

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", agregarAlCarrito);
    });
}

function agregarAlCarrito(e) {
    const idBoton = e.currentTarget.id;
    const productoAgregado = productos.find(producto => producto.id === idBoton);

    if (productosEnCarrito.some(producto => producto.id === idBoton)) {
        const index = productosEnCarrito.findIndex(producto => producto.id === idBoton);
        productosEnCarrito[index].cantidad++;
    } else {
        productoAgregado.cantidad = 1;
        productosEnCarrito.push(productoAgregado);
    }

    localStorage.setItem("productos-en-carrito", JSON.stringify(productosEnCarrito));
    actualizarNumerito();
    
}

function actualizarNumerito() {
    let nuevoNumerito = productosEnCarrito.reduce((acc, producto) => acc + producto.cantidad, 0);
    numerito.innerText = nuevoNumerito;
}


document.addEventListener("DOMContentLoaded", function () {

    const numerito = document.querySelector("#numerito");
    let productosEnCarrito = JSON.parse(localStorage.getItem("productos-en-carrito")) || [];

    let nuevoNumerito = productosEnCarrito.reduce((acc, producto) => acc + producto.cantidad, 0);
    numerito.innerText = nuevoNumerito;

    const chatInput = document.getElementById("chatbot-input");
    const sendButton = document.getElementById("send-chatbot");
    const messagesContainer = document.getElementById("chatbot-messages");

    const chatContainer = document.getElementById("chatbot-container");
    const closeChatbot = document.getElementById("close-chatbot");
    const chatBtn = document.getElementById("chatbot-btn");

    // Verificar el estado del chatbot desde localStorage
    if (localStorage.getItem("chatbotOpen") === "false") {
        chatContainer.style.display = "none";
    } else {
        chatContainer.style.display = "block";
    }

    function sendMessage() {
        const message = chatInput.value.trim();
        if (message === "") return;

        messagesContainer.innerHTML += `<div class="user-message">Tú: ${message}</div>`;

        fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            messagesContainer.innerHTML += `<div class="bot-message">Chatbot: ${data.response}</div>`;
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        })
        .catch(error => console.error("Error:", error));

        chatInput.value = "";
    }

    sendButton.addEventListener("click", sendMessage);
    chatInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    // Cerrar el chatbot
    closeChatbot.addEventListener("click", () => {
        chatContainer.style.display = "none";
        localStorage.setItem("chatbotOpen", "false"); // Guardar el estado de cerrado
    });

    // Mostrar el chatbot
    chatBtn.addEventListener("click", () => {
        chatContainer.style.display = "block";
        localStorage.setItem("chatbotOpen", "true"); // Guardar el estado de abierto
    });
});

