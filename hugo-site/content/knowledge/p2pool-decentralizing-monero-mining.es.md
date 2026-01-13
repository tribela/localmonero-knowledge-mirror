---
title: "P2Pool y su papel en la descentralización de la minería de Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Uno de los objetivos principales del proyecto Monero es permitir una red justa, descentralizada y segura a través de enfoques nuevos e innovadores para la minería proof-of-work (PoW), la principal forma de asegurar las redes de criptomonedas hoy en día.

Mientras que un algoritmo de minería único [como RandomX](/knowledge/monero-mining-randomx) es extremadamente importante para este objetivo, ya que ayuda a garantizar que cualquier persona con un ordenador pueda contribuir de manera justa a la seguridad de la red, RandomX no resuelve los problemas que pueden ocurrir debido a la minería de pool. La minería de pool es, con mucho, la forma más común de minar criptomonedas hoy en día, incluyendo Monero, pero afortunadamente la aparición de la minería p2pool está cambiando rápidamente eso.

## ¿Qué es la minería de pool?

La minería en grupo es una forma de que los mineros compartan la tarea de intentar resolver un bloque en la red y luego compartan las recompensas de manera uniforme para todos los bloques que el grupo encuentre. Aunque esto ayuda enormemente a igualar la frecuencia con la que se paga a los mineros frente a la minería de Monero en solitario, no está exento de graves problemas de centralización.

Cuando cada minero contribuye al pool, cede el control del trabajo que realiza y de los bloques que encuentra al propio pool, confiando en que el pool repartirá de forma honesta y justa las recompensas entre todos los mineros en función de la cantidad de trabajo que haya realizado cada uno. Si todo va bien, el operador del pool recoge el trabajo de todos los mineros, lo envía a la red y reparte las recompensas a partes iguales.

## ¿Cuál es el problema de la minería de pool?

Desgraciadamente, esto se basa totalmente en la confianza y permite al operador del pool hacer cosas nefastas con el trabajo realizado por los mineros. El operador del pool podría utilizar el trabajo realizado para atacar la red, intentar duplicar los fondos (si el pool es lo suficientemente grande), o simplemente utilizar el trabajo realizado por los mineros para pagarse a sí mismo y nunca recompensar a los mineros adecuadamente por su trabajo.

El mayor riesgo para la red es que un pool (o varios pools trabajando juntos) tenga más del 51% del hashrate de la red bajo su control, ya que podría utilizarlo para hacer trampas y gastar los fondos dos veces (un ataque de doble gasto) o intentar cambiar las reglas de la red.

## ¿Qué es p2pool?

p2pool es un concepto que se creó originalmente para el minado de Bitcoin en 2011, pero nunca vio una amplia adopción y permanece prácticamente inutilizado en Bitcoin. Afortunadamente, uno de los desarrolladores clave detrás de RandomX, SChernykh, pasó sus vacaciones buscando soluciones a algunos de los problemas con la implementación de Bitcoin de p2pool y reescribiendo todo el software desde cero.

p2pool en Monero permite una forma completamente libre de confianza para que los mineros trabajen juntos para resolver los bloques y asegurar la red de Monero mediante el uso de software de nodo especial para p2pool con el fin de compartir el trabajo.

Esto se hace utilizando una nueva cadena de bloques (una "cadena lateral") que mantiene un registro del trabajo que cada minero realiza, su dirección de cartera, y la cantidad de Monero que ha ganado, y luego paga la recompensa de una manera descentralizada y sin confianza. Como esta cadena lateral tiene muchos menos mineros, es mucho más fácil encontrar y enviar bloques en ella que en la red principal de Monero, lo que hace más fácil para los mineros obtener pagos consistentes frente a la minería de Monero solo.

## ¿Cómo resuelve p2pool los problemas de la minería de pool?

En p2pool no hay un pool centralizado, ni un operador de pool centralizado, ni una sola persona que retenga los fondos y distribuya los pagos. Todo el trabajo realizado colectivamente por aquellos que minan a través de p2pool es comprobado por la blockchain de p2pool y otros operadores de nodos para asegurar que es legítimo, y todos los mineros son pagados de acuerdo con el trabajo que han realizado inmediatamente cuando se encuentra un bloque directamente de las recompensas en ese bloque encontrado.

Cuando los mineros eligen utilizar p2pool en lugar de un pool centralizado, eliminan todo el poder y la confianza de los operadores del pool y se aseguran de que su trabajo contribuye al bien de la red y a sus propias recompensas, reducen el riesgo de ataques a la red, el mal uso de su trabajo o el robo de las recompensas que se les deben.

El uso de p2pool también ayuda inmensamente a reducir el riesgo que los estados-nación o los reguladores podrían suponer para la salud de la red, ya que no hay operadores de pools centralizados a los que presionar, ni concentración geográfica de pools en la que apoyarse, ni ningún otro punto de presión fácil de usar contra Monero.

## ¿Cuáles son los inconvenientes?

Afortunadamente p2pool en Monero ha sido bien diseñado y construido, ¡y funciona extremadamente bien! Sin embargo, la principal desventaja de la minería p2pool es que cada minero que quiera usar p2pool tiene que ejecutar su propio nodo de Monero, lo que hace que el proceso de empezar sea un poco más complicado. Sin embargo, este nodo se utiliza para calcular toda la información necesaria para la construcción y comprobación de los bloques, y garantiza que el minero tenga un control total de su trabajo. El nodo también puede funcionar como un nodo remoto para la propia cartera del minero, contribuye a la red, y mucho más.

La otra diferencia clave con respecto a la minería centralizada es que los pequeños mineros que utilizan p2pool tendrán un poco más de "varianza"que un gran pool centralizado - pero es's _extremadamente_ importante tener en cuenta que esto no conducirá a ganar menos Monero con el tiempo! p2pool será tan rentable para los mineros pequeños con el tiempo como los pools centralizados. Parte de esta variación también se ve compensada por el hecho de que p2pool tiene de forma nativa 0% de tasas, ¡ya que no hay un operador de pool centralizado al que pagar por sus servicios!

## ¿Cómo puedo empezar?

Afortunadamente, debido al excelente diseño de la implementación de p2pool de Monero'y a la gran cantidad de personas de la comunidad que han dedicado su tiempo a ayudar a simplificar el proceso de minería a través de p2pool, empezar es cada vez más sencillo. Hay varias maneras de empezar a minar con p2pool, pero como los detalles técnicos están más allá del alcance de este artículo, siéntete libre de saltar a un enlace de abajo dependiendo de tu sistema operativo:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## ¿Cómo puedo saber más?

Si esto ha despertado su curiosidad sobre la minería de p2pool, eche un vistazo a continuación para obtener algunos enlaces y explicaciones adicionales sobre p2pool, cómo funciona y qué significa para Monero:

  * [El Github oficial para p2pool](https://github.com/SChernykh/p2pool)
  * [Los documentos oficiales sobre el uso de p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool ahora está en vivo](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, un explorador de bloques de "" tipo para p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Sobre su desarrollo de P2Pool un grupo de minería XMR descentralizado](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies/)

  * [Las firmas del anillo de Monero contra CoinJoin como en Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Por qué (y cómo) deberías tener tus propias llaves](/knowledge/hold-your-keys/)

  * [Contribuyendo a Monero](/knowledge/contributing-to-monero/)

  * [Cómo afectan los nodos remotos a la privacidad de Monero](/knowledge/remote-nodes-privacy/)

  * [Cómo Monero utiliza las horquillas para actualizar la red](/knowledge/network-upgrades/)

  * [Ver etiquetas: Cómo un byte reducirá los tiempos de sincronización de la cartera de Monero en más de un 40%](/knowledge/view-tags-reduce-monero-sync-time/)

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