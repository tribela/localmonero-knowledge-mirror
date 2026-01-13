---
title: "Cómo Dandelion ++ mantiene los orígenes de las transacciones de Monero en privado"
slug: "monero-dandelion"
date: "2020-04-28"
image: "/images/dandelion.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Privacidad como prioridad

Como criptomoneda, Monero puede parecer muy aburrido a simple vista. No tiene un gran reclamo a la fama, como ser una "computadora mundial" o "revolucionar la industria xyz". Solo está tratando de ser un dinero privado, digital y fungible, y cada actualización y nueva tecnología solo promueve este fin.   
  
Aquellos que consideran que este objetivo es demasiado estrecho o poco interesante generalmente no entienden lo difícil que es lograr una privacidad significativa, especialmente en un libro abierto permanente como una cadena de bloques. Cualquier vía de fuga de metadatos es un potencial para la erosión de la privacidad.   
  
Monero toma precauciones para ofuscar datos en la cadena, como el remitente, el receptor y los importes, a través de direcciones ocultas, firmas de anillo y compromisos de Pedersen, respectivamente. Esto minimiza las posibilidades de que un observador casual deduzca información crítica después de que las transacciones ya se han enviado y ahora son solo una parte del historial registrado. Sin embargo, hay algunos ataques que se pueden realizar en el momento en que se produce una transacción que no se puede realizar más adelante.

## Ataque para revelar la dirección IP

Estos ataques giran en torno a identificar de qué dirección IP proviene una transacción. Si se deduce esta información, podría revelar que un individuo envió una transacción de Monero. No puede mostrar a quién y cuánto, pero hay algunos casos en los que el conocimiento de alguien que usa Monero es suficiente para causar daño.   
  
La buena noticia es que si esta información no se obtiene en el momento en que se realiza la transacción, entonces no se puede aprender en una fecha posterior, ya que las direcciones IP no se almacenan en la cadena de bloques. También es reconfortante saber que tal ataque es poco probable que se vea en la naturaleza, ya que, para lograrlo, el atacante necesitaría una gran mayoría de nodos en la red. Sin embargo, si una persona fuera capaz de comandar esta gran mayoría, podría identificar la "dirección" de la que provino la transacción.   
  
Esto puede ser confuso, por lo que explicaremos algunos antecedentes aquí. Cada nodo se conecta a otros nodos en la red, para que puedan mantener su blockchain actualizada, así como compartir lo que saben con los demás. Estas conexiones les permiten aprender sobre nuevas transacciones, propagarlas y enviar las suyas. Dado que un nodo solo puede informar a sus pares sobre las transacciones que conocen, es lógico que el primer nodo que propaga una transacción sea el nodo que realmente envía a Monero.   
  
Si un atacante posee una gran mayoría de nodos en la red, cada nodo escuchará acerca de una transacción de uno de sus pares y, en función del momento en que cada nodo recibe esta información, puede deducir posibles candidatos para el inicio de la transacción.   
  
Si esto sigue siendo confuso, ofrecemos este ejemplo. Supongamos que ambos tenemos un amigo mutuo que se esconde de nuestra visión. Este amigo llama en voz alta. Primero escucho su llamada, y la escucho más fuerte que tú. A partir de esta información, podemos saber que probablemente estoy más cerca de nuestro amigo que tú. El hecho de que escuches el sonido más tarde (incluso por solo una fracción de segundo) y el sonido sea más tenue significa que debemos comenzar nuestra búsqueda en mi área, no en la tuya.   
  
Si un atacante puede adivinar con éxito cuál de sus pares envió la transacción, ya que tiene la dirección IP que está conectada a su nodo y se la reenvió, puede estar seguro de la dirección IP que la envió. Esta es una información poderosa, ya que las direcciones IP contienen información sobre el país y el proveedor de servicios de Internet (ISP) del usuario, y el propio ISP sabe qué usuario está vinculado a qué dirección IP exacta, desanonizando efectivamente al usuario de Monero.

## La mitigación (s)

Una posible mitigación para este ataque es el uso de una red superpuesta como Tor o I2P. Esto hace que incluso si un atacante puede deducir una dirección IP de origen, probablemente no sea la que realizó la transacción, sino el nodo de salida (I2P) o de salida (Tor) de la red superpuesta. Sin embargo, esta no es una solución integral, ya que las redes superpuestas, las VPN y el software similar están prohibidos en muchos países, y es poco realista esperar que todos usen, sincronicen y se propaguen en estas redes. Debe haber una solución que no requiera el uso de software y redes externas; uno que está disponible para la persona común.   
  
Esta solución es Dandelion ++ (DPP), que es un protocolo actualizado a la propuesta original de Dandelion para Bitcoin. En este protocolo, hay dos fases, la fase madre y la fase esponjosa; se supone que ambos juntos representan la forma de un diente de león.   
  
En la fase madre, cada pocos minutos, el nodo de envío elige aleatoriamente dos pares de todos los nodos a los que está conectado. Cuando el nodo de envío envía una transacción, ya sea en nombre de sí mismo o simplemente reenviando la transacción desde otro nodo en la fase troncal, elige aleatoriamente uno de estos dos pares seleccionados y le envía la transacción.   
  
La fase fluff es cuando un nodo recibe una transacción y la transmite a cada conexión saliente, en lugar de solo a una elegida al azar, esto permite la propagación de la transacción verdadera. Cada pocos minutos, un nodo se define a sí mismo como uno que se propagará a través de un tallo o una pelusa al azar, por lo que una fase de tallo puede ser bastante larga si cada nodo de conexión se ha definido como un nodo de tallo, pero una vez que la transacción llega a la fase de pelusa, se queda ahi.   
  
Esto significa que un atacante ya no podrá simplemente escuchar la dirección de una transacción, porque antes de que se propagara a todos, se sometió a la fase troncal, y el nodo de origen de la fase fluff no es el nodo del que se originó la transacción , y se desconoce cuántos saltos a lo largo del tallo sufrió la transacción.   
  
Por supuesto, la combinación de las soluciones anteriores (DPP más una red superpuesta) dará garantías aún más fuertes de privacidad y protección contra el rastreo de IP. También se debe tener en cuenta que DPP no se defiende contra otra forma de ataque de rastreo de red que se puede hacer con ISP, pero esto está más allá del alcance de este artículo.   
  
Dandelion ++ está configurado para lanzarse en vivo en la red Monero, y ser utilizado por defecto en el cliente de referencia, en la versión 0.16. Este pequeño cambio mitigará aún más los posibles ataques en la red de Monero y ejemplifica por qué Monero lidera el paquete en tecnologías prácticas y aplicadas de privacidad.

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

  * [Por qué Monero es de código abierto y descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: lo que hace que RandomX sea tan especial](/knowledge/monero-mining-randomx)/

  * [Por qué Monero es mejor que Dash, Zcash, Zcoin (incluso con Lelantus), Grin y Bitcoin Mixers como Wasabi (Actualizado en mayo de 2020)](/knowledge/why-monero-is-better)/