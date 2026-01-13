---
title: "Por qué Monero tiene una emisión de cola"
slug: "monero-tail-emission"
date: "2020-07-30"
image: "/images/emission.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Cuando la mayoría de las personas piensan en lo que distingue a Monero, piensan en la tecnología de privacidad de Monero. De hecho, la mayoría consideraría la privacidad y la fungibilidad que desbloquea, como el rasgo definitorio de Monero, y el arma principal que trae al ring en comparación con otras monedas. Lo que la mayoría de la gente podría no saber es que Monero contiene otras diferencias de protocolo de Bitcoin y sus derivados que algunos podrían argumentar que son tan importantes como las tecnologías de privacidad de Monero. En este artículo, veremos uno de estos: la emisión de cola.

Primero, definamos qué significa este término. Una emisión de cola es un subsidio incesante de recompensas en bloque, incluso después de que se acuñe el "último" Monero. En otras palabras, la recompensa de bloque de Monero nunca caerá a cero, sino que caerá hasta alcanzar 0.6 XMR por bloque, y luego permanecerá allí para siempre. A los mineros siempre se les pagará por minar Monero, y nunca tendrán que depender únicamente de un mercado de tarifas.

Pero retrocedamos un momento y veamos la minería en un nivel muy alto. Los mineros de Monero tienen incentivos para asegurar una red mediante la extracción de hashes. El incentivo es la oportunidad de hacer Monero si encuentran un nuevo bloque. Este Monero se otorga de dos maneras. En primer lugar, el minero recibe las tarifas pagadas de cada usuario que pagó por la inclusión de sus transacciones en el bloque. Estas son las tarifas de transacción que paga cuando envía una transacción. En segundo lugar, el minero recibe una cantidad predeterminada de Monero del propio protocolo. En la mayoría de los casos, esta "recompensa en bloque" es sustancialmente más alta que las tarifas de transacción del usuario, y es donde los mineros ganan más dinero. Esta recompensa en bloque sirve para mantener a los mineros financieramente invertidos en la seguridad de la cadena, pero también para poner en circulación nuevas monedas.

En la mayoría de los protocolos de criptomonedas, esta recompensa de bloque está configurada para disminuir con el tiempo. La mayoría de los derivados de Bitcoin tienen lo que se llama mitades, puntos predeterminados en el tiempo donde el bloque recompensa las mitades (como de 20 BTC a 10 BTC). Estas reducciones ocurren cada pocos años, y cada vez que sucede, la seguridad en la red disminuye. ¿Por qué? Bueno, alentamos al lector a leer nuestro [artículo sobre Minería y RandomX](/knowledge/monero-mining-randomx), y al hacerlo aprenderán que la minería es una carrera. Las recompensas de bloque solo se otorgan a aquellos que encuentran un bloque, y hay muchas entidades en competencia para hacerlo. Cuando las recompensas son más altas, más personas están interesadas en jugar este juego, mientras que cuando las recompensas son bajas, menos personas, incluso aquellas con el equipo para hacerlo, estarán dispuestas a usar su tiempo y recursos en la oportunidad de ganar un miserable premio.

Ya comenzamos a rascar la superficie del motivo de la emisión de cola de Monero. Monero también tiene una recompensa de bloque decreciente, aunque a diferencia de Bitcoin no hay reducciones. En cambio, cada recompensa de bloque es una pequeña cantidad menor que la anterior, por lo que la reducción es mucho más suave. Pero la pregunta para todas las criptomonedas es: "¿Qué sucede cuando la recompensa en bloque llega a cero?" Esta es una situación extraña en la que ambos sabemos y no sabemos la respuesta. La parte que sabemos es que no habrá más subsidio de recompensa en bloque, lo que significa que los mineros tendrán que ser incentivados solo por las tarifas de transacción del usuario. Lo que no sabemos es si estas cantidades serán suficientes para mantener a los mineros asegurando la cadena.

Como se mencionó anteriormente, en la actualidad, la recompensa en bloque supera las tarifas de transacción en una cantidad sustancial, por lo que la esperanza es que, a medida que más usuarios usen la cadena, las tarifas aumentarán y, con el aumento de las tarifas, los mineros considerarán que vale la pena su tiempo para continuar minando. Sin embargo, hay otro lado de este escenario, el lado de los usuarios. Si las tarifas aumentan, se volverá mucho más costoso realizar transacciones con criptomonedas para todos, lo que podría bloquearlo para aquellos que no tienen suficientes recursos monetarios. Pero, por otro lado, si las tarifas se mantienen bajas y la recompensa en bloque llega a cero, muy pocos mineros asegurarán la red, dejándola vulnerable al 51% de ataques y transacciones revertidas.

Nadie tiene buenas respuestas para este escenario, y ninguna moneda importante aún ha entrado en esta fase de la vida de su criptomoneda, por lo que tampoco tenemos experiencia en el mundo real. Todo es especulación. Una apuesta. Bitcoin apuesta a que las tarifas serán suficientes para mantener a los mineros, incluso si eso significa excluir a los empobrecidos. Monero hace una apuesta diferente. Monero apuesta que las tarifas por sí solas no serían suficientes para la seguridad de la cadena, por lo que incluye una emisión de cola como parte del protocolo.

Le recordamos al lector que la recompensa del bloque no será inferior a 0.6 XMR por bloque, nunca. ¿Será esto suficiente para incentivar a los mineros? No lo sabemos, pero ciertamente es mejor que 0, que es lo que casi todas las demás monedas han incorporado a su protocolo.

La principal crítica en contra de este enfoque es que esto significa que la oferta de Monero es teóricamente infinita, causando inflación con el tiempo, mientras que las monedas que limitan la recompensa del bloque tienen una oferta limitada, su escasez aumenta el valor con el tiempo. Consideramos que este argumento es insuficiente por varias razones.

En primer lugar, ¿de qué sirve una moneda escasa y de alto valor que se ataca, censura y subvierte fácilmente debido a la baja seguridad? En todo caso, la baja seguridad disminuiría el valor, más que compensar lo que aumentaría la escasez. En segundo lugar, aunque la oferta de Monero es teóricamente infinita, la inflación es lineal y tiende a cero como porcentaje anual, a diferencia del fiat que es exponencial.

La inflación de Monero se conoce de manera precisa con anticipación, y se puede proyectar con precisión, a diferencia del fiat que puede aumentar más o menos en un año determinado según los caprichos de los poderes fácticos. Esto aún conserva el espíritu cypherpunk de eliminar la posibilidad de corrupción humana a través de la tecnología aplicada por el protocolo. Con el beneficio adicional de la tranquilidad de saber que la seguridad de la cadena de bloques de Monero a través de la minería existirá mientras el mundo la necesite.

El último punto que queremos tocar es el de la justicia. El dinero se usa de varias maneras, como una reserva de valor, como un medio de intercambio y como una unidad de cuenta. En un sistema donde el suministro es finito, la inflación se detendrá, lo que significa que aquellos que lo usan como una reserva de valor usan el sistema de forma gratuita. Se benefician de la seguridad continua proporcionada por los mineros sin pagar nada por ello, ya que sin inflación, su dinero no pierde valor lentamente con el tiempo. Por el contrario, cualquier persona que use la moneda como medio de intercambio es penalizado (a través de tarifas de transacción potencialmente altas). Esto alentará a las personas a mantener pero no gastar, y sesga la equidad del sistema para favorecer a los titulares. Al tener una emisión de cola, esto iguala la ecuación. Ahora los titulares también pagan un pequeño impuesto, a través de la inflación, por la seguridad del sistema. La emisión de la cola lo hace más justo para todos. 

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

  * [La historia de monero](/knowledge/monero-history)/

  * [Wired Magazine está equivocado sobre Monero, aquí está el por qué](/knowledge/wired-article-debunked)/

  * [Los 15 principales mitos y preocupaciones de Monero desacreditados](/knowledge/monero-myths-debunked)/

  * [Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado](/knowledge/monero-dandelion)/

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx)/

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better)/

Otras lecturas