---
title: "Monero Mining: lo que hace que RandomX sea tan especial"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
El 30 de noviembre de 2019, Monero tuvo su bifurcación semianual, con el cambio más esperado como un cambio del antiguo algoritmo PoW, cryptonight, al completamente nuevo, desarrollado internamente, RandomX. La comunidad de Monero cree que RandomX es un gran paso hacia la minería igualitaria, pero profundicemos para ver si ese es el caso.

## Propósito

Para juzgar si RandomX es una mejora, primero debemos entender cuál es el propósito de la minería. La minería asegura una cadena de bloques de los gastos dobles a través del Consenso de Nakamoto. Las complejidades exactas de cómo lo hace están más allá del alcance de este artículo, pero se pueden aprender de muchas fuentes diferentes en Internet. Lo importante es que la seguridad proviene de los hash generados por las computadoras (mineros), en competencia unos con otros para encontrar la solución matemática necesaria para crear otro bloque. A medida que hacen esto, agregan nuevas transacciones a la cadena de bloques. A cambio de su trabajo (hashes) son compensados con monedas recién acuñadas.   
  
Hay varios problemas que pueden ocurrir con esta configuración, y requieren incentivos adecuados para funcionar correctamente, pero nos centraremos en un problema particular que pueda surgir. Si se supone que la minería es una competencia, ¿qué sucede cuando un minero obtiene una ventaja?

## Fondo

Para contextualizar, hablemos un poco sobre el hardware de minería. Los mineros utilizan computadoras para hacer el trabajo, pero todos sabemos que no todas las computadoras se fabrican de la misma manera. Algunas computadoras son lo suficientemente potentes como para ejecutar redes de inteligencia artificial o juegos intensos, mientras que otras tienen dificultades incluso con tareas simples. Estas diferencias en la potencia informática también afectan la tasa de hash, o la velocidad a la que buscan soluciones de bloque.   
  
Pero incluso estas diferencias entre computadoras palidecen en comparación con las tasas de hash del hardware especializado, también conocido como circuitos integrados de aplicaciones específicas (ASIC), que superan a las computadoras normales en varios órdenes de magnitud. Tomémonos un tiempo para explorar qué hace que los ASIC sean tan poderosos. Imaginemos que todas las computadoras se encuentran en algún lugar de un espectro que va desde poder hacer muchas cosas, pero nada bien, hasta hacer solo una cosa, pero hacerlo muy bien. Las CPU y los ASIC se encuentran en extremos opuestos de este espectro.  
  
Las CPU que se encuentran en todas las computadoras estándar se encuentran en el primer extremo. Pueden hacer muchas cosas, como navegar por la web, jugar o renderizar vídeos, pero ninguna de ellas es particularmente buena. Pero esta flexibilidad tiene el costo de la eficiencia.  
  
Los ASIC están en el otro extremo, donde solo pueden hacer una cosa, pero a un ritmo increíble. Sólo pueden realizar una función matemática, pero como pueden ignorar todo lo demás, las ganancias de rendimiento son astronómicas. Sin embargo, esta eficiencia tiene el costo de la flexibilidad, por lo que si la función cambia aunque sea ligeramente (un ejemplo es x + y = z cambia a 2x + y = z), entonces el ASIC dejará de funcionar por completo.   
  
No todo el mundo posee un ASIC, pero sí todo el mundo posee computadoras. Esto puede conducir a una ventaja injusta.

## Una analogía divertida

Si esto sigue siendo confuso, quizás la siguiente analogía ayude. ¡Imagínese una lotería donde se otorgan mil dólares cada hora, y esta lotería le permite imprimir sus propios boletos! Empiezas a imprimir tantos tickets como puedas en tu impresora doméstica, que puede imprimir un ticket por segundo. Después de restar los costos de electricidad y tinta, verá que aún puede obtener ganancias, incluso si solo gana la lotería una vez cada pocas semanas.  
  
Con el tiempo, expande su operación hasta tener una sala completa dedicada a las impresoras. 20 en total. Todo está bien ... hasta un fatídico día.  
  
Hay grandes noticias. Alguien ha inventado un nuevo tipo de impresora. Solo puede imprimir boletos de lotería. No puede imprimir imágenes ni documentos de oficina, ni imprimir a doble cara. Solo boletos de lotería. Pero puede imprimirlos a una velocidad de 1000 boletos por segundo. Miras en tu pequeña sala de impresoras. 20 impresoras ¿Necesita 980 impresoras más solo para mantenerse al día con UNA de estas impresoras monstruosas, y si alguien tiene dos ...?  
  
Lamentablemente sales del juego de lotería ya que ya no puedes justificar los costos de electricidad y tinta.  
  
¡Pero espera! ¡Un par de semanas hay más noticias! El diseño del boleto ha cambiado. Ahora los números, que solían estar en la parte superior, ahora están en la parte inferior. Las nuevas impresoras monstruosas son tan inflexibles que no pueden hacerlo. Solo podían hacer el diseño anterior. No pasa mucho tiempo antes de que vuelva a imprimir felizmente. Al menos hasta que alguien haga una nueva impresora monstruosa para el nuevo diseño.

## RandomX

¿Dónde encaja RandomX en todo esto? Busca igualar la ventaja de los ASIC haciendo que los ASIC sean muy difíciles de hacer. Para ello, requiere que los mineros creen y ejecuten código aleatorio en lugar de hashing basado en un algoritmo.  
  
Puede ser confuso cómo esto realmente ayuda a algo, así que volvamos a la analogía de nuestra impresora. ¿Recuerdas lo que sucedió cuando el diseño cambió? Las viejas impresoras monstruosas se vuelven obsoletas todas las noches, y las nuevas tuvieron que desarrollarse teniendo en cuenta el nuevo diseño. ¿Qué pasaría si cada nuevo boleto de premio de lotería tuviera que adherirse a un nuevo estándar de diseño para cada nuevo premio mayor?   
  
Crear una nueva impresora monstruo se volvería increíblemente difícil. Ya no puedes planificar el diseño de un boleto. Dado que el diseño es aleatorio, los fabricantes de impresoras monstruosas tendrían que agregar capacidades de color, formas de imprimir diferentes letras y bordes y formas y más. En resumen, la máquina que terminaron inventando sería una impresora estándar y normal. Al igual que todos los demás.  
  
Simplemente implementando esta aleatoriedad en el diseño del ticket, redujimos sustancialmente la gran ventaja obtenida del hardware especializado. RandomX hace lo mismo, pero con la minería.  
  
De esta manera, se minimizan las ventajas obtenidas por unas pocas personas ricas seleccionadas, ya que si invierten en crear "ASIC" para minar RandomX, en realidad simplemente inventarán CPU más fuertes y mejores, lo que beneficia al mundo en general.  
  
Esto significa que el pequeño con sus 20 impresoras de boletos está de vuelta en el juego. Puede que aún tenga más dificultades ya que estas personas adineradas aún pueden comprar más impresoras que él, pero al menos ahora no es superado por órdenes de magnitud simplemente de una máquina. Es competitivo a su pequeña manera.  
  
Sabiendo que incluso el pequeño puede ser competitivo en la minería de Monero, alentamos a todos a darle un giro, ya sea en la billetera GUI de Monero, que tiene soporte para la minería en solitario, o descargando software mantenido por la comunidad. Es fácil, competitivo y abierto a todos.

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

  * [Cómo las firmas de anillo oscurecen los resultados de Monero](/knowledge/ring-signatures)/

  * [Cómo Monero resolvió el problema del tamaño del bloque que afecta a Bitcoin](/knowledge/dynamic-block-size)/

  * [Cómo CLSAG mejorará la eficiencia de Monero](/knowledge/what-is-clsag)/

  * [Por qué Monero tiene una emisión de cola](/knowledge/monero-tail-emission)/

  * [La historia de monero](/knowledge/monero-history)/

  * [Wired Magazine está equivocado sobre Monero, aquí está el por qué](/knowledge/wired-article-debunked)/

  * [Los 15 principales mitos y preocupaciones de Monero desacreditados](/knowledge/monero-myths-debunked)/

  * [Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado](/knowledge/monero-dandelion)/

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better)/