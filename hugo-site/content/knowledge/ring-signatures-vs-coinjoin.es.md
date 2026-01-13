---
title: "Las firmas del anillo de Monero contra CoinJoin como en Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A medida que las herramientas de privacidad de Bitcoin han ido ganando en atención y uso, se han visto sometidas a un mayor escrutinio normativo. Este escrutinio ha llevado a un [reciente anuncio](https://twitter.com/wasabiwallet/status/1503091503207432193) por parte de una herramienta de privacidad de Bitcoin, Wasabi Wallet, de que empezarán a censurar y rechazar las entradas a las mezclas que consideren ilícitas o que vayan en contra de sus ToS, y pagarán a una empresa de análisis de cadenas para "investigar" a los participantes en las mezclas que lleguen.

El uso de transacciones CoinJoin para ofuscar el origen de los fondos en Bitcoin ha sido el núcleo de la privacidad de Bitcoin durante muchos años, y los problemas y riesgos inherentes a su uso son algunos de los problemas principales que las firmas en anillo de Monero corrigen y evitan.

En esta entrada del blog nos adentraremos brevemente en una comparación entre CoinJoin y las firmas en anillo, así como en las razones por las que el enfoque adoptado en Monero conduce a una mayor resistencia a la censura, mayor privacidad y menos molestias para los usuarios.

## ¿Qué es una transacción CoinJoin?

Como todas las transacciones son completamente transparentes en Bitcoin - revelando el remitente, el destinatario y las cantidades - los usuarios deben tomar medidas adicionales para preservar su privacidad frente a los remitentes anteriores y los futuros destinatarios de sus fondos o arriesgarse a la censura, la vigilancia o el robo de fondos a través de la violencia física.

La mejor solución actual para la privacidad en Bitcoin es una herramienta llamada ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/)donde 2 o más usuarios trabajan juntos (normalmente a través de un coordinador centralizado) para crear una transacción especial que dificulta a los observadores externos la conexión de las entradas con las salidas. Cada participante se comunica para construir conjuntamente la transacción sin ceder la custodia de sus fondos, y recibe al final un resultado cuya historia previa no está clara (u ofuscada) para los observadores externos.

Esto rompe la historia de los UTXOs específicos, permitiendo a los usuarios de Bitcoin ganar un poco de secreto a la hora de realizar la transacción. Sin embargo, CoinJoin (tal y como se implementa en Wasabi Wallet y Samourai Wallet, las dos herramientas CoinJoin más utilizadas para Bitcoin) tiene algunos inconvenientes importantes:

  * Como las transacciones de CoinJoin son completamente opt-in y requieren una participación activa, cualquier participante muestra necesariamente que busca una mayor privacidad que la de los usuarios "normales" de Bitcoin, lo que potencialmente les señala y causa problemas para gastar fondos en muchos intercambios o entidades reguladas. Cada usuario no puede negar que ha participado en una transacción CoinJoin.
  * Para encontrar a otros con los que CoinJoin, la mayoría de los enfoques de CoinJoin (incluyendo Wasabi Wallet) utilizan un coordinador centralizado que conecta a los participantes y les ayuda a comunicarse y construir una transacción CoinJoin adecuada. Este coordinador centralizado nunca tiene la custodia de los fondos de los usuarios, pero sí obtiene una amplia visión de las transacciones que coordina, puede censurar las entradas (como en el caso de Wasabi Wallet) y puede ser presionado para que recoja o comparta información sobre los participantes de CoinJoin.
  * Los usuarios con grandes cantidades de fondos para CoinJoin a menudo tienen que esperar horas (¡o incluso días!) para encontrar suficientes participantes con los que CoinJoin, lo que provoca grandes retrasos desde que un usuario recibe los fondos hasta que puede gastarlos en privado.
  * La privacidad proporcionada por una transacción CoinJoin se degrada con el tiempo a medida que otros participantes gastan los fondos o vinculan sus salidas a su identidad a través de intercambios KYC, comerciantes que exigen identificación, etc. Esto significa que lo ideal es que los usuarios mantengan sus fondos constantemente en transacciones CoinJoin para mantener su conjunto de anonimato ("multitud en la que esconderse") lo más fresco posible.
  * En la mayoría de los enfoques de CoinJoin, los participantes deben utilizar un UTXO de tamaño fijo (es decir, 0,1 BTC) para dificultar la conexión de las entradas y salidas de las transacciones CoinJoin. Esto lleva a unas tarifas más altas (se necesitan más transacciones separadas por cada entrada grande), más "cambio tóxico" (fondos que no se pueden gastar sin graves riesgos para la privacidad), y puede impedir que los usuarios más pequeños puedan mezclar en absoluto si no tienen el saldo mínimo requerido.

## ¿Cómo se resuelven estos problemas con las firmas anulares?

Como [hemos profundizado en lo que son las firmas de anillo en el pasado](/knowledge/ring-signatures)no entraré en grandes detalles sobre los aspectos técnicos de su funcionamiento en esta entrada del blog. En su lugar, vamos a ver cómo los enfoques adoptados en Monero resuelven los problemas con CoinJoin discutidos anteriormente.

> CoinJoin es opt-in y requiere la participación

CoinJoin es opt-in y requiere la participación

Las firmas en anillo de Monero son una característica central del protocolo de privacidad, y _cada_ transacción en la red las utiliza. Esto significa que las transacciones de ningún usuario destacan por buscar una mayor privacidad que los usuarios "normales" de Monero, y todos los usuarios obtienen una negación plausible de que han gastado fondos en cualquier transacción. Como un usuario que gasta fondos no coordina ni participa con las entradas señuelo en una transacción, aquellos usuarios que poseen entradas que resultan ser seleccionadas como señuelo pueden decir honestamente que no estaban participando en esa transacción, reforzando su privacidad.

> Uso de un coordinador centralizado

Uso de un coordinador centralizado

Como las firmas en anillo de Monero son totalmente no coordinadas y requieren sólo el verdadero gastador de fondos para crear la transacción, no hay necesidad de un coordinador centralizado en Monero. Esto asegura que _nadie_ puede negarte el acceso a la privacidad en Monero, y no hay ninguna entidad centralizada que pueda ser presionada, ni ataques Sybil fáciles a la liquidez, etc. Mientras tu transacción pague las tasas adecuadas, obtienes un acceso sin censura a la privacidad, la seguridad y el anonimato en Monero.

> CoinJoin requiere liquidez

CoinJoin requiere liquidez

La "liquidez" disponible para cualquier persona que gaste Monero para utilizarlo como señuelo es siempre el conjunto total de salidas en la cadena, por lo que nunca hay escasez de señuelos para esconderse con Monero. Alguien que quiera gastar Monero puede hacerlo ~20min después de recibir los fondos, y no necesita realizar ningún paso adicional para obtener una fuerte privacidad en Monero.

> La privacidad de CoinJoin se degrada con el tiempo

La privacidad de CoinJoin se degrada con el tiempo

Como los resultados de Monero nunca son conocidos por la red, la privacidad proporcionada por las firmas en anillo es mucho menos susceptible de degradarse con el tiempo. Un usuario no necesita cambiar constantemente los resultados en Monero, y fuera de circunstancias extremadamente raras, no pierde la privacidad con el paso del tiempo.

Sin embargo, si un usuario quiere "refrescar" los señuelos utilizados con una salida, puede simplemente enviar los fondos a sí mismo y ser capaz de gastarlos ~20min más tarde como de costumbre.

> CoinJoin suele requerir entradas de tamaño fijo

CoinJoin suele requerir entradas de tamaño fijo

Como las cantidades se ocultan en cada transacción utilizando ["Transacciones Confidenciales"](/knowledge/monero-ringct) (una parte de "RingCT"), los señuelos utilizados en cualquier transacción pueden ser de cualquier tamaño. No hay razón para preocuparse por la heurística basada en la cantidad en Monero, por lo que las transacciones son mucho más simples de construir y pueden aprovechar los señuelos de cualquier punto en el tiempo y de cualquier cantidad en el blockchain de Monero.

## ¿Cómo puedo saber más?

Si tienes curiosidad y quieres entender mejor las firmas de anillos o las transacciones de CoinJoin, consulta los siguientes enlaces para empezar:

  * [Cómo las firmas en anillo ocultan las salidas de Monero](/knowledge/ring-signatures)
  * [Firma del anillo - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Visión general de CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies/)

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