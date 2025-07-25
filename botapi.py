from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para evitar problemas con peticiones desde el frontend

rules = {
    "hola": "¡Hola! ¿Te puedo ayudar en algo? Estamos aquí para ayudarte con nuestros productos y servicios.",
    "adios": "Hasta luego, ¡que tengas un excelente día! No dudes en volver si necesitas algo más.",
    "gracias": "De nada, ¡cualquier cosa no dudes en preguntar! Estamos para servirte.",
    "tienen envios?": "¡Sí! Realizamos envíos a nivel nacional. El costo de envío depende de la ubicación, pero generalmente varía entre $5 y $10 USD.",
    "cual es el costo de envio?": "El costo de envío depende del destino. Para un envío estándar dentro del país, el costo es de $8 USD. Para más detalles, por favor proporciona tu ubicación.",
    "como hago un pedido?": "Para hacer un pedido, simplemente selecciona el producto que deseas, agrégalo a tu carrito y sigue los pasos de pago. Si tienes dudas, ¡aquí estamos para ayudarte!",
    "cuanto tarda el envio?": "El tiempo de entrega varía según la ubicación, pero generalmente los envíos llegan entre 3 y 5 días hábiles.",
    "aceptan devoluciones?": "Sí, aceptamos devoluciones dentro de los 30 días posteriores a la compra, siempre y cuando el producto esté en su estado original.",
    "que ropa tienen para mujeres?": "En Eternal Boutique tenemos una variedad de ropa femenina, desde vestidos elegantes, blusas, hasta chaquetas y más. ¿Qué tipo de prenda buscas?",
    "tienen chaquetas?": "¡Sí! Tenemos varias chaquetas elegantes y de temporada. Por ejemplo, tenemos chaquetas casuales y de oficina a partir de $1299.",
    "que tipo de chaquetas tienen?": "Disponemos de chaquetas de diversos estilos, como chaquetas formales, de lana, y de cuero, perfectas para cualquier ocasión.",
    "tienen ropa formal?": "Sí, contamos con una gran selección de ropa formal para mujer, ideal para ocasiones especiales o para la oficina.",
    "que vestidos tienen?": "Tenemos vestidos elegantes para todo tipo de evento, desde bodas hasta cenas formales. ¿Te gustaría ver alguno?",
    "tienen ropa de oficina?": "Sí, ofrecemos una excelente selección de ropa para oficina, incluyendo blusas, pantalones de vestir y vestidos sofisticados.",
    "tienen ropa de noche?": "Sí, tenemos ropa ideal para eventos nocturnos, como vestidos de noche, blusas con detalles elegantes y más.",
    "tienen ropa de invierno?": "Sí, contamos con ropa de invierno como abrigos, suéteres y chaquetas, todo en tendencias de temporada.",
    "tienen ropa de verano?": "¡Claro! Tenemos ropa ligera para el verano, como blusas de manga corta, vestidos frescos y pantalones cortos.",
    "que tops tienen?": "Tenemos una gran variedad de tops, incluyendo blusas casuales, blusas de oficina y camisetas elegantes. ¿Qué estilo prefieres?",
    "tienen suéteres?": "Sí, contamos con una selección de suéteres en varios colores y estilos, ideales para el clima frío.",
    "tienen ropa con estampados?": "¡Sí! Disponemos de prendas con estampados modernos y únicos, desde flores hasta cuadros y rayas.",
    "tienen ropa casual?": "Sí, tenemos ropa casual cómoda y de estilo para el día a día, incluyendo jeans, camisetas y blusas de algodón.",
    "tienen ropa para eventos especiales?": "Sí, tenemos ropa para eventos especiales, como vestidos formales, conjuntos elegantes y accesorios para complementar tu look.",
    "tienen ropa deportiva?": "No, en este momento no contamos con ropa deportiva, pero sí tenemos algunas opciones para un look más casual.",
    "tienen ropa para bodas?": "Sí, ofrecemos una variedad de vestidos elegantes y conjuntos sofisticados para bodas y eventos especiales.",
    "que tipo de pantalones tienen?": "Disponemos de pantalones de mezclilla, pantalones de vestir y pantalones de lana, perfectos para cualquier ocasión.",
    "cuanto cuestan las chaquetas?": "Las chaquetas en nuestra tienda tienen precios que comienzan desde $1299, dependiendo del estilo y material.",
    "tienen ropa con descuento?": "Sí, tenemos promociones especiales y descuentos en algunas de nuestras prendas. ¡No olvides revisar nuestra sección de ofertas!",
    "como hago un pedido?": "Para hacer un pedido, simplemente selecciona los productos que te gustan, agrégales al carrito y sigue los pasos para el pago. Si tienes dudas, ¡estamos aquí para ayudarte!",
    "cual es el costo de envio?": "El costo de envío depende del destino, pero en general, es de aproximadamente $8 USD para envíos nacionales.",
    "cuanto tarda el envio?": "El tiempo de entrega varía según tu ubicación, pero generalmente entre 3 y 5 días hábiles.",
    "aceptan devoluciones?": "Sí, aceptamos devoluciones dentro de los 30 días posteriores a la compra, siempre y cuando los productos estén en su estado original.",
    "tienen blusas de manga larga?": "Sí, tenemos varias blusas de manga larga en diferentes estilos y materiales, perfectas para el clima más frío.",
    "tienen vestidos de fiesta?": "Sí, ofrecemos una hermosa selección de vestidos de fiesta, desde diseños sencillos hasta más sofisticados.",
    "tienen faldas?": "Sí, tenemos faldas de varios estilos, desde faldas cortas hasta faldas largas, perfectas para el día o para eventos formales.",
    "tienen ropa de noche para mujeres?": "¡Sí! Tenemos opciones de ropa de noche, incluyendo vestidos elegantes y conjuntos con detalles especiales.",
    "que tipo de accesorios tienen?": "En nuestra boutique, también ofrecemos una gama de accesorios, como bolsos, joyería, bufandas y más para complementar tu look.",
    "tienen pantalones de mezclilla?": "Sí, tenemos pantalones de mezclilla en diferentes cortes y estilos, desde rectos hasta ajustados.",
    "tienen vestidos cortos?": "Sí, tenemos una variedad de vestidos cortos ideales para ocasiones casuales o eventos formales.",
    "tienen ropa de gala?": "Sí, contamos con vestidos de gala y conjuntos para ocasiones formales, perfectos para eventos importantes.",
    "tienen ropa para el trabajo?": "Sí, tenemos ropa cómoda y profesional para el trabajo, incluyendo trajes, blusas elegantes y faldas formales.",
    "tienen ropa de verano para oficina?": "Sí, tenemos ropa ligera para la oficina en verano, como blusas de manga corta y pantalones frescos.",
    "que tipos de chaquetas tienen para mujeres?": "Tenemos chaquetas de lana, chaquetas de cuero, blazers, y más, todas ideales para completar tu look.",
    "que colores tienen en blusas?": "Contamos con blusas en una amplia variedad de colores, desde neutros como blanco, negro y beige, hasta tonos más vibrantes.",
    "tienen ropa con encajes?": "Sí, tenemos prendas con detalles de encaje, como blusas, vestidos y tops, perfectas para un look romántico.",
    "que estilos de vestidos tienen?": "Tenemos vestidos de diferentes estilos, desde los más sencillos hasta los más elaborados, incluyendo vestidos ajustados y sueltos.",
    "cuanto cuestan los vestidos?": "Los precios de nuestros vestidos varían, pero generalmente comienzan en $1499 dependiendo del diseño y material.",
    "tienen ropa para primavera?": "¡Sí! Tenemos ropa fresca para primavera, como vestidos ligeros, tops de manga corta y pantalones de lino.",
    "tienen ropa para el otoño?": "Sí, tenemos ropa perfecta para el otoño, incluyendo suéteres, chaquetas y vestidos de manga larga.",
    "tienen conjuntos de dos piezas?": "Sí, ofrecemos conjuntos de dos piezas, perfectos para combinar con accesorios y crear un look armonioso.",
    "tienen ropa con botones?": "Sí, tenemos prendas con botones, como blusas, chaquetas y vestidos, ideales para un estilo clásico.",
    "tienen ropa de algodon?": "Sí, contamos con una variedad de prendas de algodón, como camisetas, blusas y vestidos, perfectas para el día a día.",
    "tienen ropa para el invierno?": "Sí, ofrecemos abrigos, bufandas, guantes y más para mantenerte cálida durante el invierno.",
    "tienen pantalones cortos?": "Sí, tenemos pantalones cortos y bermudas para el clima cálido, disponibles en varios estilos.",
    "tienen ropa con tela de seda?": "Sí, ofrecemos blusas y vestidos de seda, ideales para un look elegante y sofisticado.",
    "tienen ropa para fiestas?": "Sí, tenemos ropa de fiesta, incluyendo vestidos y conjuntos para una noche especial.",
    "que tipo de suéteres tienen?": "Tenemos suéteres de lana, de algodón, con cuello alto y más, ideales para el frío.",
    "tienen ropa con terciopelo?": "Sí, tenemos prendas de terciopelo, como vestidos y blusas, perfectas para eventos formales.",
    "tienen ropa para bodas?": "Sí, contamos con vestidos y conjuntos especiales para bodas y otros eventos importantes.",
    "tienen ropa para cenas elegantes?": "Sí, tenemos ropa elegante para cenas, como vestidos formales, blusas con detalles y más.",
    "tienen ropa para la oficina?": "Sí, tenemos ropa profesional para la oficina, incluyendo pantalones, blusas y chaquetas.",
    "tienen ropa de algodón orgánico?": "Sí, contamos con algunas prendas hechas de algodón orgánico, perfectas para quienes buscan materiales más sostenibles.",
    "tienen ropa de lana?": "Sí, tenemos ropa de lana, ideal para el invierno, como suéteres, bufandas y abrigos.",
    "tienen ropa con lentejuelas?": "Sí, ofrecemos blusas y vestidos con lentejuelas, ideales para ocasiones especiales y eventos nocturnos.",
    "tienen vestidos largos?": "Sí, tenemos una gran variedad de vestidos largos, perfectos para eventos formales o de gala.",
    "tienen ropa para el día a día?": "Sí, tenemos ropa cómoda y casual para el día a día, como jeans, blusas y vestidos sencillos.",
    "tienen ropa de noche para invierno?": "Sí, tenemos opciones de ropa de noche para invierno, como vestidos de manga larga y abrigos elegantes.",
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip().lower()
    response = rules.get(user_input, "No entiendo la pregunta. ¿Podrías reformularla?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
