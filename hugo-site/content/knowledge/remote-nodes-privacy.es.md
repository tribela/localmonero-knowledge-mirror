---
title: "Cómo afectan los nodos remotos a la privacidad de Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Una de las mayores ventajas que tiene Monero sobre otras criptomonedas es su privacidad en la cadena, pero ¿te has preguntado alguna vez cómo se mantiene la privacidad de Monero cuando utilizas un nodo remoto? ¿Qué tal si utilizas un servidor de "cartera ligera" como MyMonero?

En este artículo nos adentraremos en algunos de los detalles de cómo Monero proporciona una excepcional privacidad en la cadena incluso cuando se utiliza un nodo remoto, así como lo que hay que tener en cuenta cuando se utilizan nodos remotos.

## ¿Qué función cumplen los nodos en Monero?

## ¿Qué función cumplen los nodos en Monero?

Para aquellos que no estén familiarizados con el funcionamiento de Monero, los nodos (o servidores) de la red Monero pueden ser gestionados por cualquier persona y permiten al propietario del nodo -¡o a otros que decidan compartirlo! - sincronizar una copia de la cadena de bloques y proporcionar esa copia a otros en la red. Estos nodos también verifican todas las transacciones que se producen en la red, así como todos los bloques que se publican y se aseguran de que todos ellos siguen las reglas establecidas por consenso.

La otra función que cumplen los nodos en Monero es la de proporcionar todos los datos que necesita tu monedero favorito para comprobar adecuadamente las transacciones que te pertenecen y realizar nuevas transacciones. Estos datos son proporcionados por los nodos de dos maneras:

  * Los datos de cada bloque de la cadena de bloques son solicitados por el monedero, escaneados en busca de transacciones que le pertenezcan, y luego descartados una vez comprobados por el monedero. 
    * Este paso pronto se mejorará drásticamente, gracias a [las etiquetas de vista](/knowledge/view-tags-reduce-monero-sync-time).
  * Cuando se envían transacciones, el nodo que se utiliza proporciona una lista de posibles señuelos (o entradas falsas) para usar cuando se construye la transacción, asegurando que se tiene una buena multitud para esconderse cada vez que se gasta Monero. 
    * Estos señuelos son una parte de [las firmas de anillo](/knowledge/ring-signatures)una pieza importante del enfoque de Monero para la privacidad en la cadena.

  * Este paso pronto se mejorará drásticamente, gracias a [las etiquetas de vista](/knowledge/view-tags-reduce-monero-sync-time).

  * Estos señuelos son una parte de [las firmas de anillo](/knowledge/ring-signatures)una pieza importante del enfoque de Monero para la privacidad en la cadena.

## ¿Cuál es la forma más privada y segura de utilizar Monero?

## ¿Cuál es la forma más privada y segura de utilizar Monero?

Lo mejor que se puede hacer, incluso con la fuerte privacidad en la cadena proporcionada por Monero cuando se utilizan nodos remotos, es ejecutar su propio nodo de Monero para asegurarse de que tiene una copia prístina del blockchain de Monero a mano y que su dirección IP está bien protegida. El otro beneficio al ejecutar tu propio nodo es que puedes contribuir a la red, permitiendo que otros nodos se sincronicen desde tu nodo o incluso permitiendo que otros usuarios se conecten a tu nodo con sus carteras.

Dicho esto, Monero sigue proporcionando una excelente privacidad cuando se utiliza un nodo remoto. Si estás interesado en ejecutar tu propio nodo de Monero, aquí tienes una guía fácil de seguir para hacerlo:

  * [Ejecutar un nodo Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## ¿Qué puede saber de mí un nodo remoto?

## ¿Qué puede saber de mí un nodo remoto?

Cuando se utiliza un nodo remoto, hay algunas piezas clave de información que se exponen a un nodo remoto y un par de formas clave en que ese nodo puede atacarte, impedirte realizar transacciones, y más.

Lo primero que un nodo remoto puede saber de ti es tu dirección IP pública. Aunque es de esperar que esto se oculte a través de una VPN o Tor, el nodo remoto podría asociar su dirección IP pública con la transacción, ayudándole a reducir el lugar desde el que está realizando la transacción. El nodo remoto también puede saber el último bloque que tu cartera ha sincronizado y utilizarlo para intentar hacer conjeturas sobre ti, como por ejemplo cuándo usas normalmente Monero y cuándo gastaste por última vez Monero. Esto es especialmente cierto si siempre vienes desde la misma dirección IP (como tu casa). La última cosa clave que un nodo remoto puede aprender sobre ti es la información básica sobre las transacciones que envías a través de él. Aunque estos pueden ser los datos más obvios que el operador del nodo remoto obtiene sobre ti, es importante entender que esto podría ser utilizado para ayudar a rastrear al remitente de la transacción al combinar esa información con otros datos fuera de la cadena. Esto puede ser especialmente peligroso si el nodo remoto está dirigido por una entidad maliciosa, una empresa de análisis de la cadena de bloques o un Estado-nación opresor.

Un nodo remoto también puede intentar causarte problemas ocultándote bloques, haciendo creer a tu cartera que se ha sincronizado cuando no es así. Esto puede hacerte pensar que los fondos se han perdido o impedirte gastar fondos hasta que te conectes a otro nodo. La última cosa clave que un nodo remoto podría hacer es alimentar tu cartera con una lista manipulada de señuelos. Esto podría hacer que tu monedero fallara completamente en la creación de transacciones (haciendo que no puedas gastar fondos), o podría permitir que el nodo remoto intentara proporcionar señuelos que sabe que están gastados para reducir el anonimato que recibes en cada transacción.

## ¿Qué garantías de privacidad siguen existiendo cuando se utiliza un nodo remoto?

## ¿Qué garantías de privacidad siguen existiendo cuando se utiliza un nodo remoto?

Aunque este artículo puede haberle asustado un poco, es importante darse cuenta de que la privacidad proporcionada por Monero es excelente incluso cuando se utiliza un nodo remoto, y supera con creces a cualquier otra criptomoneda cuando se utiliza de esta manera. Sigues ganando la fuerte privacidad en la cadena proporcionada por Monero, ya que el nodo remoto nunca sabe la verdadera entrada (qué monedas estás gastando), la cantidad de Monero gastada en la transacción, o la dirección del destinatario de la transacción. Los observadores externos tampoco pueden ver la verdadera entrada, la cantidad o las direcciones involucradas (¡no importa el tipo de nodo que elijas usar!), asegurando que fuera del nodo remoto incluso tu dirección IP, la información de sincronización de la cartera y las transacciones tienen fuertes garantías de privacidad.

El nodo remoto tampoco tiene acceso a las transacciones anteriores que has enviado o recibido o a la cantidad de Monero que hay actualmente en tu cartera, y pierde toda la visibilidad de tus transacciones en el momento en que empiezas a usar otro nodo. Nunca se proporcionan claves privadas (ni de gasto ni de visualización) al nodo remoto, por lo que tu cartera sigue siendo privada, segura y utilizable. Independientemente del nodo remoto, nunca corres el riesgo de perder Monero o de que te lo roben, ya que el nodo no puede editar la dirección del destinatario, nunca tiene acceso a las claves privadas de tu cartera, y no puede confiscar tu Monero de ninguna manera.

## ¿Qué tal las "carteras ligeras" como MyMonero?

## ¿Qué tal las "carteras ligeras" como MyMonero?

Aunque el tema está un poco fuera del alcance de este artículo, quería abordar un tipo único de monedero en Monero: los monederos ligeros. El nombre de monedero ligero viene del hecho de que tu monedero (en tu teléfono u ordenador) no tiene que realizar ninguna de las sincronizaciones de la cadena de bloques, haciendo la experiencia más rápida y fluida.

Sin embargo, los monederos como este vienen con una severa contrapartida de privacidad por ahora - tu monedero envía la clave de vista privada al servidor remoto que utilizas (como el predeterminado en MyMonero), dando al servidor remoto visibilidad completa de cualquier fondo recibido desde la creación de tu monedero (y hasta que dejes de usar ese monedero o semilla). Esto reduce drásticamente la privacidad que recibes del operador del nodo, y debe ser abordado con precaución.

Afortunadamente, la comunidad de Monero está trabajando en la mejora del software que puedes utilizar para alojar tu propio servidor ligero de monederos (LWS), lo que te permitirá tener una rápida sincronización sin tener que confiar a un tercero tus claves privadas de vista - ¡ya que ejecutarás el software donde tu monedero envía las claves privadas de vista!

Para más información sobre el servidor de carteras ligero personalizado, consulte el siguiente repositorio de Github:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## ¿Cómo puedo saber más?

## ¿Cómo puedo saber más?

Si eres curioso y te gustaría entender mejor los nodos en Monero y buscar el uso de un nodo remoto o ejecutar el tuyo propio, mira los enlaces de abajo para los grandes lugares para empezar:

  * [Monero World, una lista de nodos remotos gestionados por la comunidad que se pueden utilizar](https://moneroworld.com/#nodes)
  * [Nodos Monero gestionados por Seth For Privacy, el autor de este artículo](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, una lista de nodos remotos con estado de comprobación frecuente](https://monero.fail/)
  * [Cómo conectarse a un nodo remoto dentro de la cartera GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Nodo Remoto](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies)/

  * [Las firmas del anillo de Monero contra CoinJoin como en Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por qué (y cómo) deberías tener tus propias llaves](/knowledge/hold-your-keys)/

  * [Contribuyendo a Monero](/knowledge/contributing-to-monero)/

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

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx)/

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better)/

Otras lecturas