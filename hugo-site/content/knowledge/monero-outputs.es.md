---
title: "Explicación de las salidas de Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, al igual que otras criptomonedas, utiliza los resultados como medio para contabilizar los fondos. Muchos usuarios expertos en criptografía probablemente hayan escuchado este término antes, pero no todos entienden lo que significan y cómo funcionan. Como se explora en nuestro [artículo sobre firmas de anillo](/knowledge/ring-signatures), las salidas son la unidad real intercambiada en la cadena de bloques entre las partes que realizan la transacción. Similar a un billete de un dólar, pero la cantidad no está en una denominación fija.

Si le pagan $ 16 por un trabajo, es posible que reciba un billete de un dólar, un billete de cinco dólares y un billete de diez dólares. Tienes $ 16, pero también tienes tres billetes diferentes en tu billetera. Si quisiera pagarle a alguien 6 dólares, podría usar el billete de 5 y el billete de 1, pero si quisiera pagarle a alguien $ 8, solo podría usar los $ 10 y recibir $ 2 en cambio. Por último, si quisiera pagarle a alguien $ 14, tendría que usar las tres facturas y recibiría $ 2 de vuelta en cambio, pero por un momento, cuando entrega las tres facturas, no tiene dinero en su billetera hasta que obtenga la cambiar de nuevo.

Monero funciona de manera similar. Suponga que tiene una tienda y realiza tres ventas en tres artículos diferentes. Es posible que reciba 1.5 XMR, 2.25 XMR y 5.25 XMR para un total de 9 XMR, pero también tiene tres salidas diferentes en su billetera de las denominaciones indicadas anteriormente. Al igual que con los dólares, es posible que desee pagarle a alguien 3 XMR. Puede usar solo la salida 5.25 XMR y recibir 2.25 XMR nuevamente en cambio, o puede combinar las salidas 1.5 y 2.25 XMR y obtener 0.75 XMR nuevamente en cambio.

Pero, tan pronto como envía la transacción, las salidas que usa se colocan en un estado "bloqueado", lo que significa que son inaccesibles hasta que reciba el cambio. El protocolo desbloquea los fondos (es decir, le devuelve el cambio) después de 10 confirmaciones, o alrededor de 20 minutos. Al igual que una vez que entrega los billetes de un dólar de su billetera, no puede usar el dinero nuevamente hasta que reciba el cambio de vuelta del cajero, su Monero es inaccesible hasta que reciba el cambio.

Regresemos al ejemplo de enviar 3 XMR a alguien, y usas la salida 5.25 XMR. Ahora, mientras espera que su 1.75 XMR vuelva a cambiar, no puede usarlo. Este 1.75 XMR es inaccesible para ti. Pero aún puede usar las salidas 1.5 XMR y 2.25 XMR, ya que no se gastaron. Volviendo al ejemplo del dólar, si le pagaste a alguien $ 8, como en el ejemplo anterior, no podrías usar los $ 2 que esperas como cambio hasta que te lo den, pero en este ejemplo, todavía tienes un Billete de $ 10 que no se usa en su billetera. Esto aún se puede usar para comprar lo que desee mientras espera el cambio. Lo mismo con Monero.

Este suele ser un punto de confusión para los nuevos usuarios de Monero. A menudo, un usuario puede tener solo una salida en su billetera, recibida de un intercambio o un amigo. Digamos que esta salida es 20 XMR. No tienen otras salidas en su billetera. Ahora quieren hacer una donación a dos de sus organizaciones benéficas favoritas. Envían 5 XMR a la primera organización benéfica y luego están confundidos porque, aunque deberían tener 15 XMR restantes, no pueden enviar inmediatamente la siguiente donación a la segunda organización benéfica. Como habrás adivinado, esto se debe a que el 15 XMR está bloqueado. No se puede gastar hasta que se devuelva como cambio (10 confirmaciones o alrededor de 20 minutos). Una vez que se desbloqueen sus fondos, podrán enviar su segunda donación.

Solo para reiterar el punto, no habrían tenido este problema si hubieran tenido múltiples salidas en su lugar, como dos salidas 10 XMR o similares. Podrían enviar ambas donaciones una tras otra, porque la primera donación usaría una de las 10 salidas de XMR (y esperaría 10 confirmaciones para recibir 5 XMR nuevamente en cambio), y la segunda donación usaría las otras 10 XMR salida.

Algunas carteras de criptomonedas tienen una función llamada 'gestión de salida', que simplemente muestra al usuario qué salidas tiene actualmente (además de su suma total), y también les permite elegir cuáles quieren usar cuando gastan su criptomoneda.

A partir de ahora, la GUI de Monero realiza la selección de salida para los usuarios automáticamente, ya que los usuarios que seleccionan sus propias salidas a menudo generan confusión o, en algunos casos, dañan la privacidad. Sin embargo, hay carteras en construcción, como el nuevo proyecto de carteras Feather, que contendrá estas funciones de gestión de salida.

Hemos estado hablando mucho sobre la parte de envío, pero sucede algo fascinante en el extremo receptor. Volviendo a nuestro ejemplo de enviar 3 XMR a alguien, y usando sus salidas 1.5 XMR y 2.25 XMR en la transacción (mientras espera 0.75 XMR en cambio), el receptor NO recibe dos salidas de 1.5 XMR y 2.25 XMR. En su lugar, reciben una salida ONE 3 XMR.

En segundo plano, el protocolo combina todas las salidas utilizadas para el gasto y le da al receptor una salida de la cantidad pagada y envía una salida de cambio al remitente. Por lo tanto, el remitente también recibirá una salida como cambio, independientemente de si utilizó dos, tres o diez salidas para enviar la transacción.

Esperamos que esto haya aclarado algo de confusión sobre los resultados y cómo funciona la contabilidad interna del protocolo, así como el problema de confusión que enfrentan los usuarios comunes al encontrar fondos bloqueados. En otro artículo, exploraremos la administración de sus salidas para minimizar la posibilidad de tener que esperar fondos desbloqueados antes de enviar transacciones futuras.

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