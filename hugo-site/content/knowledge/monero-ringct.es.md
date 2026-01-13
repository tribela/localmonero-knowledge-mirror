---
title: "Cómo RingCT oculta los importes de las transacciones de Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
La privacidad de Monero no depende de un mecanismo singular que, si se rompe, revelaría la totalidad de las transacciones, sino de tres tecnologías diferentes que funcionan en conjunto para brindar privacidad holística al tiempo que compensan las debilidades de las otras partes. Este enfoque de tres puntas consta de firmas de anillo, RingCT y direcciones ocultas. Estas tres tecnologías ocultan la salida real (emisor), la cantidad y el receptor, respectivamente. Hoy hablaremos de RingCT.

RingCT es posiblemente el más técnico de los tres y puede ser difícil de entender, por lo que no cubriremos cómo funciona exactamente, sino más bien mostraremos cómo es posible no saber una cantidad y aún así confirmar cosas al respecto. . Y no se preocupe, usaremos muchos ejemplos como siempre.

Primero, exploremos por qué es importante verificar algo sobre las cantidades. ¿Por qué no podemos simplemente mantenerlos en secreto? La respuesta es que hay formas inteligentes en que las personas pueden crear dinero de la nada si se les da la oportunidad. ¿Cómo podría funcionar algo como esto? Veamos un ejemplo.

Si quieres comprarle un artículo a tu amigo y él quiere diez dólares por él, entonces comienzas con diez dólares y él comienza con cero. Después de que le des los diez dólares, él tiene diez dólares y tú tienes cero. Empezaste con diez y ahora él tiene diez. No se creó ni destruyó dinero en esta transacción.

Con las criptomonedas, una persona inteligente puede dar diez dólares por el artículo y, en lugar de recibir cero dólares en cambio, puede recibir dos dólares de vuelta. En lugar de 0 y 10 que conducen a 10 y 0 (o 10 = 10), ahora es 0 y 10 conduce a 10 y 2 (o 10 = 12). Two Monero fue creado de la nada. Puede imaginar que si el individuo se hiciera esto a sí mismo varias veces, podría amasar una fortuna gigantesca en poco tiempo.

Con Bitcoin y otros, esto sería fácil de ver. Observa las entradas que entran en una transacción y las salidas que salen y se asegura de que lo que se envía es igual a lo que se recibe. Si estas cantidades están encriptadas y no son visibles, el usuario no tiene forma de verificar que lo que se envía y lo que se recibe es lo mismo.

En un intento por aumentar la privacidad de Bitcoin, Gregory Maxwell creó Confidential Transactions (CT), una nueva tecnología que permitiría cantidades encriptadas, mientras demostraba que nada fue creado o destruido en el proceso. Como ocurre con la mayoría de las tecnologías de privacidad, no se convirtió en Bitcoin, pero Monero estaba interesado en adoptarlo. Hubo solo un problema. La tecnología ya implementada de firmas en anillo era incompatible con la idea propuesta. Entonces, uno de los investigadores de MRL en ese momento, Shen Noether, modificó CT en RingCT, una versión de CT que era compatible con firmas de anillo.

Una vez más, la forma en que esto funciona es bastante técnica y sería difícil de explicar en un artículo introductorio. Para el entusiasta de la criptografía que simplemente debe saber, hay muchos artículos detallados escritos en Internet sobre el funcionamiento interno de la TC. Para el resto de nosotros, este artículo mostrará cómo es posible ocultar las cantidades, pero aún así probar que no se creó ni se destruyó nada.

Supongamos que Alice quería enviarle dinero a Bob. Alice enviará 10 XMR a Bob, quien recibirá 10 XMR. 10 = 10 por lo que no hay nada malo aquí. Pero Alice no quiere que nadie sepa cuánto está enviando. Entonces ella y Bob crean un secreto compartido. Básicamente un número que solo ellos dos conocen. Supongamos que el número es 22. Ahora, Alice multiplica 10 (lo que realmente está enviando) por 22 para obtener 220. Este es el número que comparte con la red.

Los propios mineros no conocen el número secreto. Si lo hicieran, podrían dividir el número que se muestra por el número secreto y obtener la cantidad real enviada. Pero como no lo hacen, no pueden. Sin embargo, ven que Bob recibirá 220. 220 enviados. 220 recibidos. 220 = 220. De esta manera, la red puede verificar que ningún Monero fue creado o destruido, todo sin saber la cantidad real que Alice envió a Bob.

Dado que Bob conoce el número secreto compartido, cuando recibe el dinero, solo divide por 22 para obtener la cantidad real que envió Alice, 10. Alice y Bob saben cuánto se envió y cuánto se recibió, todo mientras todos los demás reciben un número falso.

Una vez más, esta no es la forma real en que funciona CT, pero da una idea de cómo podría ser posible algo como esto. La forma real involucra cosas como compromisos de Pedersen, dos cantidades enviadas (una cantidad encriptada al receptor y una cantidad de compromiso a la red), y ... sí, ya es fácil ver cómo uno podría perderse en todo eso.

Sin embargo, una cosa a tener en cuenta es que, si bien RingCT oculta la cantidad negociada entre dos partes en una transacción, no oculta otros dos conjuntos de números.

La primera son las transacciones de coinbase. Si este término no le resulta familiar, básicamente significa la recompensa que obtienen los mineros por encontrar el siguiente bloque. Este número no está oculto. Cualquiera puede ver cuánto ha otorgado el protocolo a un minero por su servicio. De esta manera, la cantidad actual de Monero existente se puede conocer sumando todas las transacciones de la base de monedas. Su suma será igual a la actual Monero en circulación.

El segundo número no oculto es la tarifa que se paga a los mineros cuando un usuario envía una transacción. Las tarifas deben estar claras para que los mineros puedan saber a quién priorizar. Sin embargo, esta es una forma en que los usuarios pueden dañar su privacidad, como si alguien usara una tarifa de minero única cada vez que envía una transacción (como 0.12345), entonces sus transacciones se pueden vincular.

Aparte de estos casos, RingCT ha estado ocultando montos de Monero desde 2017, y nuestra privacidad colectiva es aún más fuerte por ello.

Otras lecturas