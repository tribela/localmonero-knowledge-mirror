---
title: "Ver etiquetas: Cómo un byte reducirá los tiempos de sincronización de la cartera de Monero en más de un 40%"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Una de las quejas más comunes en torno al uso diario de Monero es el tiempo que puede llevar sincronizar una cartera antes de poder enviar Monero. Afortunadamente, los desarrolladores e investigadores de la comunidad de Monero han encontrado una forma brillante de reducir el tiempo que se tarda en sincronizar la cartera en más de un 40%, sin que se añada ninguna sobrecarga de la cadena de bloques, ni tarifas, etc.

Introduzca las "etiquetas de visualización", un añadido de un byte a los datos de cada transacción - ¡que llegará a Monero en la próxima actualización de la red!

## ¿Por qué la sincronización del monedero de Monero es más lenta que la de Bitcoin?

## ¿Por qué la sincronización del monedero de Monero es más lenta que la de Bitcoin?

Una de las primeras preguntas que tenemos que responder para entender mejor la necesidad de una solución como las etiquetas de vista es por qué la sincronización de la cartera de Monero es más lenta que la de criptomonedas como Bitcoin.

En Bitcoin, como todas las transacciones no son privadas y revelan las monedas que se gastan, las cantidades y las direcciones implicadas en la cadena, los monederos de Bitcoin pueden simplemente buscar cualquier salida de transacción no gastada (UTXOs) o direcciones usadas para un monedero dado, escaneando rápidamente la cadena de bloques para encontrar sólo los UTXOs que pertenecen a esas direcciones para averiguar qué monedas pertenecen a su monedero y pueden ser gastadas.

En Monero, sin embargo, todas las transacciones preservan la privacidad del usuario al ocultar el remitente, el receptor y las cantidades involucradas en cada transacción. Esta privacidad, aunque es vital para proteger a los usuarios de la red, también introduce una sincronización más lenta del monedero. En Monero, tu monedero tiene que comparar cada salida de transacción (TXO) que existe en la red con las claves privadas de tu monedero.

Esta comparación implica una gran cantidad de matemáticas complejas y criptografía para validar que una salida es realmente suya, ya que todas las cantidades, direcciones y salidas (o monedas) gastadas están ocultas en la cadena en Monero.

## ¿Qué son las etiquetas de vista?

## ¿Qué son las etiquetas de vista?

Como forma de ayudar a reducir el tiempo de sincronización de los monederos de Monero, [un investigador llamado UkoeHB ideó un novedoso enfoque](https://github.com/monero-project/research-lab/issues/73) \- añadir una "etiqueta" de 1 byte a cada transacción utilizando un secreto compartido que sólo conocen el emisor y el receptor de esa transacción.

Este secreto compartido lo genera el remitente a partir de la dirección que le proporciona el destinatario, y no requiere ninguna colaboración activa por parte del remitente y el destinatario. El primer byte (o carácter) de este secreto compartido se añade a los datos de la transacción cuando se publica en la red Monero.

Cuando uno de los participantes en esa transacción quiere sincronizar su cartera con el blockchain de Monero después, en lugar de necesitar realizar toda la compleja matemática y criptografía para todos y cada uno de los TXO en la red, la cartera puede ahora sólo comprobar ese campo de 1 byte en cada transacción y sólo entonces realizar la verificación que consume tiempo en las transacciones que tienen esa etiqueta - ¡1/256 TXOs en la red, para ser precisos!

Esta etiqueta no revela ninguna información sobre la transacción a los espectadores externos, sólo añade 1 byte (una cantidad insignificante) al tamaño de las transacciones, y sin embargo nos permite reducir los tiempos de sincronización en más de un 40% al reducir las complejas verificaciones necesarias.

## Ver etiquetas: un ejemplo simplificado

## Ver etiquetas: un ejemplo simplificado

Imagina que tienes 4.096 cajas en una habitación, de las cuales sólo 5 te pertenecen. Todas las cajas son completamente indistinguibles desde el exterior, y la única forma de saber si una caja es para ti es abrirla y resolver un problema matemático escrito en su interior que requiere mucho tiempo para asegurarse de que es tuya.

Ahora, imagina que decides que la persona que te envía esas 5 cajas genere un código especial utilizando tu dirección, y luego ponga sólo el primer carácter de ese código generado en el exterior de cada caja que te envían. Todos los demás hacen lo mismo con sus cajas (para asegurarse de que todas las cajas sigan siendo indistinguibles), pero ahora usted puede simplemente mirar el código de un carácter en el exterior de la caja, y sólo abrir aquellas cajas que tengan ese carácter.

Mientras que otras cajas coincidirán con tu código, incluso algunas que no son de tu propiedad, el número de cajas que necesitas abrir y resolver un problema matemático es ahora sólo 16 (¡1/256 cajas!) en lugar de las 4.096.

Ahora abres esas 16 cajas, resuelves los problemas matemáticos y te quedas con las 5 cajas que realmente te pertenecen de ese grupo.

## ¿Cuándo estarán disponibles las etiquetas de visualización en Monero?

## ¿Cuándo estarán disponibles las etiquetas de visualización en Monero?

Las etiquetas de visualización son una de las características que actualmente se planea incluir en la [próxima actualización de la red](https://github.com/monero-project/meta/issues/630)y deberían ser lanzadas en algún momento de esta primavera. La comunidad [recaudó 23,3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (en el momento de escribir este artículo) para incentivar el desarrollo y la implementación de las etiquetas de vista, y como resultado la gran mayoría del trabajo para incluir las etiquetas de vista en la base de código de Monero ya ha sido completado por j-berman en colaboración con revisores e investigadores.

Una vez que las etiquetas de vista sean aplicadas por la red, todas las transacciones enviadas después de la actualización de la red se beneficiarán del tiempo de sincronización de la cartera drásticamente mejorado. No necesitarás hacer nada especial para empezar a usar las etiquetas de vista, tu monedero favorito para Monero simplemente empezará a usarlas después de la actualización de la red automáticamente.

## ¿Cómo puedo saber más?

## ¿Cómo puedo saber más?

Si esto ha despertado su curiosidad sobre las etiquetas de vista, eche un vistazo a continuación a algunos enlaces adicionales que profundizan en el tema:

  * [Reduzca los tiempos de escaneo con la "etiqueta de vista" de 1 byte por salida](https://github.com/monero-project/research-lab/issues/73)
  * [Añadir etiquetas de vista a las salidas para reducir el tiempo de escaneo de la cartera](https://github.com/monero-project/monero/pull/8061)

Otras lecturas

  * [Cómo Monero permite de forma única las economías circulares](/knowledge/monero-circular-economies)/

  * [Las firmas del anillo de Monero contra CoinJoin como en Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por qué (y cómo) deberías tener tus propias llaves](/knowledge/hold-your-keys)/

  * [Contribuyendo a Monero](/knowledge/contributing-to-monero)/

  * [Cómo afectan los nodos remotos a la privacidad de Monero](/knowledge/remote-nodes-privacy)/

  * [Cómo Monero utiliza las horquillas para actualizar la red](/knowledge/network-upgrades)/

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