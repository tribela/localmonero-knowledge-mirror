---
title: "Cómo las direcciones de Monero Stealth protegen su identidad"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ha implementado un enfoque de privacidad de tres pilares. Estas tecnologías son [firmas en anillo](/knowledge/ring-signatures), que ocultan la salida real (remitente), RingCT que oculta las cantidades y direcciones furtivas, que oculta al receptor. Hoy, discutiremos la última de estas tecnologías mencionadas: direcciones furtivas.

Hay muchas razones por las que una persona puede querer ocultar a quién envía. Nunca debemos permitir que nadie intente convencernos de que todos los ejemplos de esto son comportamientos desagradables. Cosas como enviar a un partido político impopular, donar a organizaciones benéficas o apoyar a aquellas que la cultura considera 'canceladas' son ejemplos de dónde uno podría querer ocultar sus comportamientos de gasto por temor a repercusiones, pero son de naturaleza perfectamente legítima.

En una cadena de bloques transparente, las direcciones a las que uno envía sus transacciones son visibles para todos. Es importante tener en cuenta que si los propios mineros no están de acuerdo con el destino del dinero, pueden optar por no extraerlo en un bloque, censurando efectivamente esta transacción en una plataforma aparentemente resistente a la censura. La única forma de hacer que esta censura, ciertamente poco probable, no sea posible es si los mineros no pueden distinguir entre transacciones porque todos los metadatos en la cadena están ocultos por varios medios. Algo por lo que se conoce a Monero.

Monero resuelve este problema de direcciones transparentes implementando direcciones furtivas, una tecnología que en realidad fue creada inicialmente para Bitcoin en 2011 por el usuario del foro Bitcoin Talk ByteCoin (se desconoce la relación con Bytecoin, que luego integraría direcciones furtivas). Sin embargo, la forma actual de direcciones furtivas tiene varias mejoras con respecto a la idea inicial. Pero primero, para ver cómo funcionan, hablemos de claves.

Es difícil estar en el espacio de las criptomonedas y no escuchar acerca de las claves. Frases como "haga una copia de seguridad de su clave privada" son comunes, pero cuando un ciudadano medio escucha las palabras "clave pública" y "clave privada", se asusta y piensa que será demasiado técnico y confuso de entender. Pero no se preocupe. Lo tomaremos con calma y usaremos muchos ejemplos.

Los dos tipos de claves que se utilizan en las criptomonedas son, como se acaba de mencionar, públicas y privadas. Estas dos claves generalmente vienen en un par, lo que significa que una clave pública y una privada en particular están vinculadas entre sí. De hecho, por lo general, la clave pública se deriva de la privada, lo que significa que si conoce la clave privada, su billetera puede hacer algunas matemáticas ingeniosas y generar la clave pública correcta en todo momento.

Ahora, como implican los nombres, la clave pública puede ser pública sin consecuencias. Por lo general, es parte de la dirección que comparte para recibir dinero en su billetera de criptomonedas. También siguiendo su homónimo, la clave privada es una que no debe compartirse. Es lo que le permite firmar y gastar una transacción, por lo que si es robada o compartida, entonces el cobarde tercero puede gastar su dinero, generalmente para ellos mismos.

Una analogía fácil con esto sería un candado y la llave necesaria para desbloquearlo. El candado abierto se puede compartir libremente y, de hecho, se puede bloquear cualquier cosa con este candado, pero solo la persona con la llave puede abrir cualquier cosa en la que esté cerrado el candado. El candado se puede copiar y compartir, la llave no debe ser.

Estas claves generalmente se extraen del usuario, por lo que nunca las ve realmente. En Monero, no aparecen como una cadena alfanumérica aterradora en absoluto. En Monero, el usuario común conoce la clave privada como su semilla. La semilla (que debe escribir si no lo ha hecho), en realidad es solo una clave privada legible por humanos. 

¿Ves? Después de todo, no da tanto miedo. De vuelta a las direcciones furtivas.

Como se mencionó anteriormente, las direcciones ocultas no se hicieron originalmente para Monero, sino para Bitcoin. Sin embargo, como con la mayoría de las ideas incipientes, esta primera iteración tuvo problemas. El siguiente intento llegó cuando CryptoNote fue creado por Nicholas van Saberhagan para Bytecoin, el precursor de Monero ([vea nuestra historia de Monero y Bytecoin aquí](/knowledge/monero-history)), y aunque fue una mejora definitiva con respecto al original, incluso tuvo algunos defectos sutiles.

Eventualmente, surgió una última iteración de un desarrollador para otra criptomoneda de privacidad ahora desaparecida, que solucionó los problemas pendientes de privacidad y seguridad con la idea. Esto finalmente se abrió camino en Monero, y es lo que se usa hoy.

Aunque estos problemas de privacidad y seguridad se resolvieron, las direcciones sigilosas en sí mismas agregaron un tipo diferente de peculiaridad a las tecnologías blockchain, una que no existía antes. La necesidad de escanear. Dado que las direcciones de recepción no se muestran públicamente en la cadena de bloques, el receptor nunca sabe si una determinada transacción es suya, por lo que debe escanear todas las transacciones entrantes con su clave privada para ver si es suya.

Con las monedas transparentes, todo lo que tienen que hacer es verificar si una transacción se está enviando a su dirección. Una pregunta fácil de sí o no. Pero con las direcciones ocultas, cada transacción podría ser una que se le envíe, por lo que debe intentar desbloquear cada una con su clave privada para ver si se abre.

Este es un paso adicional que Bitcoin y sus derivados no tienen, y hace la configuración inicial de la billetera, además de sincronizar una billetera cuando no la ha abierto por un tiempo, mucho más que Bitcoin. Sin embargo, la compensación es necesaria para desbloquear las garantías de privacidad que tiene. Cabe señalar que, a diferencia del punto más débil de la trifecta de privacidad, las firmas de anillo, las direcciones furtivas no son susceptibles a la heurística. Se basa en una criptografía de curva elíptica probada y verdadera, en la que se basa todo Internet, por lo que romperla significaría el fin de la seguridad informática en general, no solo de Monero.

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies)/

  * [Las firmas del anillo de Monero contra CoinJoin como en Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por qué (y cómo) deberías tener tus propias llaves](/knowledge/hold-your-keys)/

  * [Contribuyendo a Monero](/knowledge/contributing-to-monero)/

  * [Cómo afectan los nodos remotos a la privacidad de Monero](/knowledge/remote-nodes-privacy)/

  * [Cómo Monero utiliza las horquillas para actualizar la red](/knowledge/network-upgrades)/

  * [Ver etiquetas: Cómo un byte reducirá los tiempos de sincronización de la cartera de Monero en más de un 40%](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool y su papel en la descentralización de la minería de Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Lo que hará por Monero](/knowledge/seraphis-for-monero)/

  * [¿Es la conversión de Bitcoin a Monero tan privada como la compra directa de Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [Por qué Monero utiliza una configuración sin confianza a diferencia de Zcash](/knowledge/monero-trustless-setup)/

  * [Por qué Monero es una mejor reserva de valor que Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Cómo Monero puede superar los efectos de red de Bitcoin](/knowledge/network-effect)/

  * [Por qué Monero tiene la comunidad de pensamiento más crítica](/knowledge/critical-thinking)/

  * [Estafas a tener en cuenta al usar Monero](/knowledge/monero-scams)/

  * [Cómo funcionarán los intercambios atómicos en Monero](/knowledge/monero-atomic-swaps)/

  * [Lo que todo usuario de Monero necesita saber cuando se trata de redes](/knowledge/monero-networking)/

  * [Cómo RingCT oculta los importes de las transacciones de Monero](/knowledge/monero-ringct)/

  * [Cómo las subdirecciones de Monero previenen la vinculación de identidades](/knowledge/monero-subaddresses)/

  * [Explicación de las salidas de Monero](/knowledge/monero-outputs)/

  * [Mejores prácticas de Monero para principiantes](/knowledge/monero-best-practices)/

  * [Cómo las firmas de anillo oscurecen los resultados de Monero](/knowledge/ring-signatures)/

  * [Cómo Monero resolvió el problema del tamaño del bloque que afecta a Bitcoin](/knowledge/dynamic-block-size)/

  * [Cómo CLSAG mejorará la eficiencia de Monero](/knowledge/what-is-clsag)/

  * [Por qué Monero tiene una emisión de cola](/knowledge/monero-tail-emission)/

  * [La historia de monero](/knowledge/monero-history)/

  * [Wired Magazine está equivocado sobre Monero, aquí está el por qué](/knowledge/wired-article-debunked)/

  * [Los 15 principales mitos y preocupaciones de Monero desacreditados](/knowledge/monero-myths-debunked)/

  * [Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado](/knowledge/monero-dandelion)/

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx)/

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better)/

Otras lecturas