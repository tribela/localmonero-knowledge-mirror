---
title: "Lo que todo usuario de Monero necesita saber cuando se trata de redes"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
No debería sorprender a nadie que Monero, y de hecho todas las criptomonedas, se ejecuten en Internet. Y, sin embargo, aunque esta afirmación parece básica y obvia, muchos no consideran las implicaciones de lo que esto significa con respecto a su privacidad. En otras palabras, hay algunas cosas contra las que Monero puede y no puede protegerse, simplemente por la naturaleza de su ejecución en Internet. Algunas de estas consideraciones son meros inconvenientes, mientras que otras son mucho más graves en un escenario donde se requiere absoluta privacidad. Tomemos el tiempo para familiarizarnos con cómo los usuarios de Monero interactúan entre sí en la red y lo que esto significa para su privacidad.

Empezando por el lado trivial de las cosas, si un usuario no tiene acceso a Internet, no puede descargar nuevos bloques, propagar transacciones en nombre de otros o enviar transacciones propias. Algo interesante a tener en cuenta es que un usuario con un nodo completo, sin acceso a Internet, puede construir una transacción fuera de línea que se puede enviar más tarde. Esto se debe a que una firma de anillo solo necesita salidas de la cadena de bloques para esconderse. Un breve recordatorio sobre [cómo funcionan las firmas de anillo](/knowledge/ring-signatures), oculta la salida real que envía un usuario entre una colección de salidas no afiliadas elegidas en el pasado. Si el usuario tiene acceso a estas salidas en forma de una cadena de bloques completamente descargada (nodo completo), entonces puede crear la firma del anillo a partir de las salidas anteriores y, una vez que se reanude la conectividad a Internet, propagar la transacción a la red.

Un usuario que está utilizando un nodo remoto no puede hacer esto, ya que cuando construyen su firma de anillo, se comunican con el nodo completo remoto para obtener resultados para incluir en la firma de anillo. Sin Internet significa que no pueden acceder a este nodo, por lo que no tienen capacidades de construcción de transacciones fuera de línea.

Antes de continuar con algunas de las consideraciones de privacidad, hagamos una breve introducción a cómo funciona Internet en su conjunto. Todo Internet no es más que computadoras conectadas a otras computadoras. Eso es. ¿El blog que te gusta leer? Solo algunos archivos alojados en la computadora de otra persona. ¿En este sitio web estás leyendo este artículo (LocalMonero)? Archivos y código alojados en una computadora en algún lugar. Incluso los grandes sitios locos funcionan de esta manera. Tome YouTube por ejemplo. Solo archivos de video alojados en los gigantescos sistemas informáticos de Google, y usted se conecta a ellos para descargar el video a su propia computadora y poder verlo.

Estas computadoras se pueden distinguir entre sí porque a todas y cada una de las computadoras conectadas a Internet se les asigna un número de identificación único llamado dirección IP. Por lo general, son cuatro conjuntos de números separados por puntos, por ejemplo: 172.66.35.7. Es importante tener esto en cuenta cuando consideramos cómo se mueve la información de Monero por Internet. Monero es una red peer-to-peer (P2P), lo que significa que las computadoras se conectan directamente entre sí en lugar de usar un intermediario. Entonces, cuando el nodo completo de un usuario está descargando un bloque recién descubierto, no lo está descargando de un servidor central, sino de sus pares. La desventaja de esto es que, dado que los usuarios se conectan entre sí directamente, conocen las direcciones IP de los demás.

¿Y bien? ¿Cual es el problema? Es solo un número, ¿verdad? No exactamente. Las propias direcciones IP contienen información sobre el usuario, como el país de origen y el proveedor de red, pero, lo que es peor, los proveedores de servicios de Internet (ISP) conocen la dirección IP de cada persona que utiliza sus servicios. Esto significa que estos ISP y aquellos con los que trabajan pueden observar el tráfico de Internet de un usuario y, utilizando algunas tácticas inteligentes, descubrir que están usando Monero. Ahora, antes de asustarse, observe la redacción allí. Todo lo que estos fisgones pueden hacer es ver que una persona se está conectando a otros nodos de la red Monero. Debido a la tecnología de privacidad de Monero, no se filtra nada más sobre el individuo. No si están ejecutando un nodo o no, o si / cuando envían transacciones, y si se envía una transacción, no se conoce ninguna de su información. Todo lo que estos ISP pueden ver es que uno de sus usuarios se está conectando a la red Monero.

Ahora, para algunas personas, en algunos lugares, esta información por sí sola puede ser suficiente para dañar la reputación o la libertad. O quizás la idea de que alguien invada su privacidad y lo que hace en Internet, por cualquier motivo, no le resulte aceptable. Se anima a estas personas a que solo se conecten a la red Monero mediante VPN, Tor o I2P, todos los cuales son servicios que ocultan la dirección IP de un usuario a los demás y también ocultan lo que un usuario está haciendo a su ISP. Las diferencias entre estos servicios están más allá del alcance de este artículo, pero hay muchos artículos de alta calidad escritos sobre el tema, por lo que se anima a los usuarios preocupados a que estudien.

Para el resto de nosotros, podemos pensar que que otros sepan que estamos conectados a la red Monero no es tan importante. Después de todo, el contenido real de nuestras transacciones, o si estamos enviando alguno, está oculto al público, entonces, ¿cuál es el daño? Si bien esto puede ser cierto, se alienta a los usuarios a considerar el hecho de que el principal atractivo de las criptomonedas es su propio banco. Cuando tiene su clave privada, y si algo le sucede, nadie puede ayudarlo a recuperar sus fondos perdidos.

Ser su propio banco significa considerar, no solo su seguridad digital, sino también su seguridad física. Es muy posible que el conocimiento de un individuo que se conecta a la red Monero pueda atraer atención no deseada, no necesariamente de actores a gran escala como los estados nacionales, sino de actores más pequeños con intereses egoístas, como los piratas informáticos que buscan hacer dinero fácil. De hecho, hay innumerables historias en todo el espacio criptográfico de tales escenarios que realmente tienen lugar.

Este artículo no pretende provocar miedo ni asustar, sino animar a los usuarios a investigar un poco sobre qué métodos de protección de la navegación web son adecuados para ellos. La buena noticia es que estas habilidades también se transferirán al uso general de Internet, no solo al uso de Monero, y como tal, en nuestro mundo cada vez más conectado a Internet, un usuario inteligente no puede equivocarse al acumular los conocimientos y habilidades adecuados para mantenerse seguro. y ser verdaderamente su propio banco.

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies/)

  * [Las firmas del anillo de Monero contra CoinJoin como en Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Por qué (y cómo) deberías tener tus propias llaves](/knowledge/hold-your-keys/)

  * [Contribuyendo a Monero](/knowledge/contributing-to-monero/)

  * [Cómo afectan los nodos remotos a la privacidad de Monero](/knowledge/remote-nodes-privacy/)

  * [Cómo Monero utiliza las horquillas para actualizar la red](/knowledge/network-upgrades/)

  * [Ver etiquetas: Cómo un byte reducirá los tiempos de sincronización de la cartera de Monero en más de un 40%](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool y su papel en la descentralización de la minería de Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Lo que hará por Monero](/knowledge/seraphis-for-monero/)

  * [¿Es la conversión de Bitcoin a Monero tan privada como la compra directa de Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [Por qué Monero utiliza una configuración sin confianza a diferencia de Zcash](/knowledge/monero-trustless-setup/)

  * [Por qué Monero es una mejor reserva de valor que Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Cómo Monero puede superar los efectos de red de Bitcoin](/knowledge/network-effect/)

  * [Por qué Monero tiene la comunidad de pensamiento más crítica](/knowledge/critical-thinking/)

  * [Estafas a tener en cuenta al usar Monero](/knowledge/monero-scams/)

  * [Cómo funcionarán los intercambios atómicos en Monero](/knowledge/monero-atomic-swaps/)

  * [Cómo RingCT oculta los importes de las transacciones de Monero](/knowledge/monero-ringct/)

  * [Cómo las direcciones de Monero Stealth protegen su identidad](/knowledge/monero-stealth-addresses/)

  * [Cómo las subdirecciones de Monero previenen la vinculación de identidades](/knowledge/monero-subaddresses/)

  * [Explicación de las salidas de Monero](/knowledge/monero-outputs/)

  * [Mejores prácticas de Monero para principiantes](/knowledge/monero-best-practices/)

  * [Cómo las firmas de anillo oscurecen los resultados de Monero](/knowledge/ring-signatures/)

  * [Cómo Monero resolvió el problema del tamaño del bloque que afecta a Bitcoin](/knowledge/dynamic-block-size/)

  * [Cómo CLSAG mejorará la eficiencia de Monero](/knowledge/what-is-clsag/)

  * [Por qué Monero tiene una emisión de cola](/knowledge/monero-tail-emission/)

  * [La historia de monero](/knowledge/monero-history/)

  * [Wired Magazine está equivocado sobre Monero, aquí está el por qué](/knowledge/wired-article-debunked/)

  * [Los 15 principales mitos y preocupaciones de Monero desacreditados](/knowledge/monero-myths-debunked/)

  * [Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado](/knowledge/monero-dandelion/)

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx/)

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better/)