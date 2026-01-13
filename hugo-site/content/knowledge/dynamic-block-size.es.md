---
title: "Cómo Monero resolvió el problema del tamaño del bloque que afecta a Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Nota:** Se recomienda encarecidamente que el lector haya leído nuestros artículos ["Por qué Monero tiene una emisión de cola"](/knowledge/monero-tail-emission) y [“Monero Mining: What Makes RandomX tan especial”](/knowledge/monero-mining-randomx). Este artículo se basa en los conceptos presentados allí._

Cada vez que las personas discuten los problemas con blockchain, una de las primeras palabras que aparecerá será "escalado". No es un secreto que las cadenas de bloques no escalan bien, pero la mayoría de la gente no sabe por qué.

La verdad es que el escalado es en realidad un término general que cubre dos categorías diferentes: soporte de protocolo y soporte tecnológico en un momento determinado. En este artículo, centraremos nuestra atención en uno: el soporte del protocolo es básicamente una medida de cuántas transacciones puede manejar el protocolo en un momento dado.

Bitcoin tiene un límite de tamaño de bloque, lo que significa que una vez que se incluyen suficientes transacciones en un bloque, cualquier transacción adicional tendrá que esperar en fila para el siguiente bloque. Una analogía útil sería pensar en un tren. Un tren se detiene en la estación y los que están en la fila entran en fila. Una vez que el tren está lleno, cualquiera que se quede afuera tendrá que esperar al siguiente.

Bitcoin usa tarifas para determinar quién ingresa al bloque o no. Volviendo a la analogía del tren, podemos imaginar que un pasajero potencial, que está a punto de quedarse atrás, ofrece al maquinista cinco dólares para que le deje un asiento. Otros pasajeros hacen lo mismo y, finalmente, hay una guerra de ofertas para ver quién se queda con qué asientos. Depende del conductor decidir si quiere respetar la política de "primero en llegar, primero en ser atendido", pero le conviene maximizar sus ingresos aceptando a los mejores postores a bordo.

En esta analogía, los mineros son los conductores de trenes. Pueden incluir cualquier transacción que quieran en el bloque, pero generalmente elegirán las que tengan las tarifas pagadas más altas.

Alternativamente, si los bloques no están muy llenos, la gente no tiene incentivos para pagar tarifas elevadas porque hay muchos asientos libres de sobra.

En el apogeo del auge de las criptomonedas de 2017, Bitcoin se vio inundado de transacciones y las tarifas se dispararon para aquellos que querían ser incluidos en el siguiente bloque, o en cualquier bloque del futuro cercano. Aquellos que no estaban dispuestos a pagar tarifas elevadas vieron cómo sus transacciones se retrasaban durante horas, días o incluso salían de la cola por completo.

Esta fue una visión desgarradora de cómo le iría a Bitcoin si ocurriera la tan mencionada "adopción masiva". Si Bitcoin fuera utilizado por las masas, las cosas serían incluso peores que en 2017, y Bitcoin sería inaccesible para cualquiera excepto para los ricos, simplemente porque el rendimiento es pequeño debido a un tamaño de bloque fijo, lo que provocaría que el mercado de tarifas se hiciera cargo. .

Monero previó esto y quiso hacer algo diferente. Entonces los desarrolladores de Monero implementaron un tamaño de bloque dinámico.

Básicamente, Monero también tiene un límite de tamaño de bloque, pero es un límite suave. Cuando la fila de transacciones en espera se vuelve demasiado larga, los mineros pueden aumentar el tamaño de los bloques. Con nuestra analogía del tren, puedes imaginar agregar más vagones de tren para acomodar a los pasajeros adicionales. Una vez que la cola está vacía, los bloques vuelven a su tamaño original en el futuro. 

Si esto parece una buena idea, parece razonable preguntarse por qué Monero es la única criptomoneda que lo ha implementado. ¿Por qué no agregarlo a Bitcoin para poner fin a los problemas de rendimiento?

Desafortunadamente, esto no es posible. Hay varias razones y haremos todo lo posible para explicarlas.

Siempre es mejor para un minero tener bloques grandes. Con bloques grandes, pueden realizar más transacciones y ganar más dinero con las tarifas, así como con las recompensas del bloque. Esto tiene el potencial de provocar ataques de spam, en los que alguien envía muchas transacciones pequeñas, con tarifas pequeñas, para inflar la cadena. Los mineros simplemente aumentarían el tamaño del bloque y los incluirían a todos porque el dinero es dinero, sin importar cuán pequeño sea. Esto conduciría a bloques consistentemente grandes con pocos beneficios económicos. Bitcoin resuelve esto restringiendo artificialmente el tamaño del bloque, generando así un mercado de tarifas. Los atacantes de spam tendrían que pagar más honorarios que los demás usuarios, y ya no es barato. Pero esto significa que los bloques se llenan dejando algunas transacciones en espera como se mencionó anteriormente.

Entonces, ¿cómo puede Monero tener tamaños de bloques dinámicos pero evitar ataques de spam? La respuesta es simple, pero inteligente. Se introduce una penalización en la recompensa del bloque cuando un bloque es más grande de lo normal. Si un minero quiere aumentar el tamaño del bloque, la recompensa que obtendrá al encontrar ese bloque será menor de la que recibiría de otro modo. Por lo tanto, solo aumentarán el tamaño del bloque cuando las tarifas de transacción pagadas por los usuarios superen la parte perdida de la recompensa del bloque. Por ejemplo, si el minero perdiera 0,5 XMR al aumentar el tamaño del bloque, y la suma de las tarifas de transacción pagadas fuera 0,4 XMR, entonces habría una pérdida neta de 0,1 XMR si aumentara el tamaño, por lo que No lo hagas. Por el contrario, si las tarifas totales de transacción sumaron 0,7 XMR, entonces habría una ganancia neta de 0,2 XMR, aunque pierdan los 0,5 XMR de la penalización de recompensa del bloque, por lo que el minero aumentará el tamaño.

Estos bloques dinámicos permiten que la red crezca orgánicamente, sin restringir artificialmente el tamaño del bloque para crear un mercado de tarifas forzadas, y al mismo tiempo evitar ataques de spam. Hay varios ángulos más desde los que podemos ver esta idea y más razones por las que no sería posible agregarla a Bitcoin, pero por ahora, esperamos que el lector comprenda cómo Monero evita varios de los problemas de Bitcoin y sus derivados y cómo planea escalar su rendimiento en el futuro.

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

  * [Lo que todo usuario de Monero necesita saber cuando se trata de redes](/knowledge/monero-networking/)

  * [Cómo RingCT oculta los importes de las transacciones de Monero](/knowledge/monero-ringct/)

  * [Cómo las direcciones de Monero Stealth protegen su identidad](/knowledge/monero-stealth-addresses/)

  * [Cómo las subdirecciones de Monero previenen la vinculación de identidades](/knowledge/monero-subaddresses/)

  * [Explicación de las salidas de Monero](/knowledge/monero-outputs/)

  * [Mejores prácticas de Monero para principiantes](/knowledge/monero-best-practices/)

  * [Cómo las firmas de anillo oscurecen los resultados de Monero](/knowledge/ring-signatures/)

  * [Cómo CLSAG mejorará la eficiencia de Monero](/knowledge/what-is-clsag/)

  * [Por qué Monero tiene una emisión de cola](/knowledge/monero-tail-emission/)

  * [La historia de monero](/knowledge/monero-history/)

  * [Wired Magazine está equivocado sobre Monero, aquí está el por qué](/knowledge/wired-article-debunked/)

  * [Los 15 principales mitos y preocupaciones de Monero desacreditados](/knowledge/monero-myths-debunked/)

  * [Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado](/knowledge/monero-dandelion/)

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx/)

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better/)