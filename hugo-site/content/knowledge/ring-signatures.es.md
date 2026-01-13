---
title: "Cómo las firmas de anillo oscurecen los resultados de Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero es conocido en todo el mundo de las criptomonedas como el rey de las monedas de privacidad. Si bien todos saben que Monero ofrece una buena privacidad, no muchos comprenden cómo funciona la privacidad.

Muchas otras monedas de privacidad publican infografías de gráficos comparativos, que enumeran los nombres de la tecnología de privacidad de cada moneda y, en la mayoría, etiquetan la tecnología de Monero como RingCT, pero esto es solo parcialmente cierto. Monero en realidad tiene un enfoque de privacidad de tres puntas. Una tecnología para ocultar al receptor de una transacción, otra para ocultar la cantidad enviada y otra para ocultar la salida utilizada, son direcciones ocultas, RingCT y firmas de anillo, respectivamente.

Este enfoque triple significa que si una de las tecnologías se rompe, las otras no necesariamente comparten el mismo destino. Las firmas de anillo son el eslabón más débil del esquema de privacidad; la palabra débil aquí significa el más susceptible a ataques heurísticos. Tomemos un tiempo para explorarlos, ¿de acuerdo?

Como se mencionó anteriormente, el objetivo de las firmas de anillo es ocultar una salida utilizada en una transacción. Si la terminología de 'entrada / salida' de la criptomoneda le resulta confusa, no se preocupe. En realidad, no es tan complicado. Cuando escuche "salida", piense en un cheque. Una de esas cosas, que ya no son tan comunes, con las que la gente paga. Como un cheque, se puede denotar en cualquier cantidad ($ 10, $ 32,50, etc.) y se intercambia entre las partes que realizan la transacción. Para las criptomonedas, las salidas cumplen estas funciones.

Cuando alguien le paga 10 Monero, recibe una salida de 10 XMR. Esta salida tiene un valor (10), y es lo que se saca de la billetera del remitente, de la misma manera cuando pagas por un servicio, una factura sale de tu billetera física y se entrega a la persona a la que le estás comprando.

La forma en que se oculta la salida es mediante la construcción de un anillo (de ahí el nombre) de salidas señuelo. Pero estos señuelos no son salidas "falsas". Son salidas pasadas reales de la cadena de bloques que no tienen nada que ver con la transacción actual, pero para un observador externo, cada una de estas salidas podría parecer igualmente probable que la real. El tamaño del conjunto de salidas señuelo, más el real, se llama tamaño de anillo, y actualmente el de Monero es once. Entonces hay diez salidas señuelo y una real.

¿Por qué no aumentamos este número a 100 o incluso a 1000? Cuanto más mejor, ¿verdad? Bueno, desde una perspectiva de privacidad, sí, pero hay otras cosas a considerar. Volvamos a un ejemplo físico para ver a qué me refiero. Si quisiera esconder uno de sus billetes de un dólar entre diez señuelos, necesitaría llevar alrededor de once dólares en su billetera por cada dólar que quisiera gastar. Un dólar real y diez falsos. Esto ya se vuelve bastante engorroso si desea gastar incluso unos pocos dólares. Ahora imagina que aumentamos la cantidad de señuelos a 1000. Por cada dólar que quisieras gastar, necesitarías llevar alrededor de 1001 dólares. ¡Necesitaría llevar un maletín solo para comprar una barra de chocolate! Es importante tener en cuenta que las firmas de anillo no funcionan de esta manera, por ejemplo, los señuelos en sí no son parte de la firma, solo referencias a ellos, pero esperamos que esta analogía pueda ser de alguna ayuda para representar los conceptos básicos.

Los señuelos de la cadena de bloques funcionan de manera similar. Cada señuelo agregado aumenta el tiempo y el costo de verificación de la transacción. Cada nodo tiene que descargar la firma de anillo completa para cada transacción, y cada firma de anillo contiene la salida real, así como los señuelos. No solo eso, sino que tiene que verificar la matemática de que al menos una de estas salidas es real, y el tiempo de verificación matemática también aumenta con cada señuelo. Esto significa que tenemos que encontrar un término medio feliz, donde el tamaño del anillo sea lo suficientemente grande como para oscurecer adecuadamente la salida real, incluso contra muchos ataques heurísticos, pero lo suficientemente pequeño como para no hacer que la cadena de bloques aumente a un ritmo masivo. No es suficiente elegir un número arbitrario o simplemente aumentar el tamaño del anillo cuando hacemos la firma más pequeña (como con CLSAG). La comunidad de Monero quiere evidencia matemática concreta sobre qué tamaño de anillo ofrece las mejores compensaciones. Un número demasiado pequeño y la privacidad no será lo suficientemente fuerte contra los ataques heurísticos. Demasiado grande, y es posible que obtengamos solo un beneficio marginal en el lado de la privacidad, y suframos innecesariamente con respecto a la escala.

Una última cosa que mencionar. Alguna literatura de Monero simplifica y dice que las firmas de anillo ocultan al remitente, pero esto no es del todo cierto, y la diferencia no es solo pedante. La diferencia entre el remitente (un humano) y una salida (una factura) es grande cuando se trata de preservar la privacidad. Si bien una salida puede tener vínculos con un remitente, una salida en sí misma no es igual a un remitente. Por lo tanto, incluso si se rompiera una firma de anillo, no necesariamente se vincula con la identidad de una persona, y tanto la cantidad como el destinatario siguen ocultos, lo que minimiza el daño causado a la privacidad de todas las partes.

Eso no quiere decir que una firma de anillo rota sea insignificante. Cualquier metadato filtrado es malo y tiene el potencial de revelar más información de la que pensamos, especialmente cuando se usa junto con otros metadatos. Por lo tanto, hacemos todo lo posible para asegurarnos de que el tamaño de anillo elegido tenga el rigor académico detrás de la decisión, se minimice la fuga de otros metadatos y las experiencias del usuario adopten las mejores acciones posibles por defecto.

Pero si la probabilidad de una firma rota todavía le preocupa, bueno, hay noticias increíbles en el horizonte. La próxima generación de protocolos de privacidad en los que se está trabajando, como Triptych, Arcturus y Lelantus, tienen capacidades realmente interesantes. En estos protocolos, el tamaño escala logarítmicamente, no linealmente, a medida que aumenta el tamaño del anillo. Esto significa que podemos colocar 100 señuelos, pero el espacio utilizado está más cerca del tamaño de anillo 10 en la tecnología antigua. Esa es una gran diferencia y mejorará significativamente la privacidad en general.

En el juego del gato y el ratón que es la privacidad, Monero innova continuamente para mantenerse a la vanguardia y garantizar la mejor privacidad práctica para todos.

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

  * [Cómo las direcciones de Monero Stealth protegen su identidad](/knowledge/monero-stealth-addresses)/

  * [Cómo las subdirecciones de Monero previenen la vinculación de identidades](/knowledge/monero-subaddresses)/

  * [Explicación de las salidas de Monero](/knowledge/monero-outputs)/

  * [Mejores prácticas de Monero para principiantes](/knowledge/monero-best-practices)/

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