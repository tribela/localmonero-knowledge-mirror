---
title: "Seraphis: Lo que hará por Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: una actualización de diseño modular para las transacciones de Monero

Este post describe [Seraphis](https://github.com/UkoeHB/Seraphis)un conjunto de estructuras y abstracciones de protocolos de transacciones desarrollado por un colaborador de investigación seudónimo [`koe`](https://github.com/UkoeHB) para el ecosistema Monero, y con el análisis de seguridad en curso por el colaborador seudónimo [`coinstudent2048`](https://github.com/coinstudent2048).  
Hacemos algunas simplificaciones y omitimos ciertos detalles técnicos en aras de la claridad; por esta razón, y porque el diseño de Seraphis todavía está en progreso, los lectores interesados deben consultar la documentación de Seraphis para obtener la información más actualizada.

## Transacciones en Monero

Protocolos como Bitcoin y Monero y otros se basan en el llamado "modelo de salida" de funcionamiento, donde una _salida_ es una representación de valor que puede ser transferida.  
Las transacciones consumen una o más salidas controladas por un emisor, y generan nuevas salidas dirigidas a los receptores (o de vuelta al emisor como cambio); la transacción debe equilibrarse en el sentido de que las salidas consumidas deben contener un valor total exactamente igual al valor en las nuevas salidas (más una tasa impuesta por la red).  
En muchos protocolos como Bitcoin, el valor contenido en una salida se escribe en claro, al igual que el destinatario.  
Además, mirando el blockchain, es trivial ver si y cuando una salida ha sido gastada (es decir, si ha sido consumida en una transacción posterior, y qué transacción la gastó).

En cambio, protocolos como Monero introducen un diseño diferente:

  * Los valores de salida están ocultos y no son visibles en la cadena de bloques
  * Las direcciones de los destinatarios se ocultan mediante el uso de un protocolo de direccionamiento único
  * El hecho de que una salida se haya gastado o no queda oculto por el uso de firmas ambiguas

El resultado es que, en ausencia de información externa, es difícil determinar si una salida determinada se ha gastado, cuál es su valor y quién es su destinatario.

El actual protocolo de transacciones de Monero se llama _RingCT_ y utiliza varios bloques de construcción criptográficos para lograr estos objetivos de diseño.

  * _Los compromisos_ ocultan las cantidades de forma matemáticamente útil
  * _Las pruebas de rango_ evitan el desbordamiento que podría inflar la oferta
  * _Las firmas anulares enlazables_ proporcionan ambigüedad al firmante y evitan los intentos de doble gasto
  * _Las compensaciones de compromisos_ afirman que las transacciones se equilibran

Estos bloques de construcción están cuidadosamente entrelazados para construir el protocolo RingCT.

Una propiedad útil del protocolo RingCT es que algunos bloques de construcción pueden ser cambiados o actualizados de una manera que mantiene el diseño general y las propiedades intactas, pero que puede proporcionar eficiencia o mejoras de seguridad. De hecho, este tipo de actualizaciones han ocurrido (o están previstas) varias veces en la historia de Monero. Las pruebas de rango en el protocolo original RingCT eran voluminosas y lentas; más tarde se actualizaron a una construcción llamada [Bulletproofs](https://eprint.iacr.org/2017/1066) que hizo las transacciones más pequeñas y más rápidas con un mejor análisis de seguridad, y está previsto que se actualice a una construcción más nueva llamada [Bulletproofs+](https://eprint.iacr.org/2020/735) para obtener beneficios de eficiencia aún mayores.

Un proceso similar se llevó a cabo con el bloque de construcción de firma de anillo enlazable. En el protocolo original, se utilizó una construcción llamada [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) . Posteriormente se actualizó a una construcción más nueva llamada [CLSAG](https://eprint.iacr.org/2019/654) que es más rápida, da lugar a transacciones más pequeñas y tiene un mejor análisis de seguridad. Una construcción de firma de anillo enlazable aún más nueva basada en [Triptych](https://eprint.iacr.org/2020/018) fue propuesta, pero no fue seleccionada para el despliegue debido a sus impactos en las operaciones de multifirma.

## Seraphis

Seraphis lleva esta idea un paso más allá.  
En lugar de actualizar los bloques de construcción individuales del protocolo de transacciones RingCT existente, introduce un protocolo diferente que puede aprovechar los diferentes bloques de construcción y ofrecer una funcionalidad mejorada.

## Bloques de construcción

Seraphis utiliza un conjunto diferente de componentes básicos criptográficos para lograr sus objetivos de diseño.

  * _Los compromisos_ aún ocultan cantidades
  * _Las pruebas de rango_ aún evitan el desbordamiento y la inflación de la oferta
  * _Pruebas de membresía_ proporcionar ambigüedad del firmante
  * _Compensaciones de compromisos_ seguir afirmando el saldo
  * _Autorizar pruebas_ evitar intentos de doble gasto

Observe el cambio aquí: las firmas de anillo enlazables se reemplazan con una combinación de pruebas de membresía y pruebas de autorización. En términos generales, las pruebas de membresía muestran que una salida consumida es parte de un conjunto más grande, similar a lo que sucede en RingCT. ¡Pero a diferencia de RingCT, las pruebas de membresía no involucran la etiqueta de enlace en absoluto! Las pruebas de autorización muestran que la etiqueta de enlace es válida y se utilizan para firmar la transacción final.

Debido a que RingCT integra la etiqueta de enlace en la firma ambigua, las operaciones de firma (y firma múltiple) son más intensivas desde el punto de vista informático y se vuelve más desafiante crear otras funciones relacionadas con la etiqueta. Pero en Seraphis, la construcción de pruebas de membresía se puede delegar de manera segura desde dispositivos altamente confiables (que pueden tener una potencia informática limitada, como una billetera de hardware) a un dispositivo menos confiable, y las operaciones de firma (y firma múltiple) son mucho más fáciles usando la prueba de autorización mucho más simple .

Afortunadamente, algunos de los componentes básicos necesarios para Seraphis ya existen en otros lugares y no es necesario diseñarlos desde cero. Tanto las construcciones Bulletproofs como Bulletproofs+ se pueden utilizar como pruebas de alcance. Las modificaciones a los sistemas de prueba tipo Schnorr se pueden utilizar para autorizar pruebas. Y un [sistema de prueba eficiente](https://eprint.iacr.org/2015/643) que ya se usó como base para Triptych, [Lelantus](https://eprint.iacr.org/2019/373)y [Spark](https://eprint.iacr.org/2021/1173)* se puede modificar para las pruebas de membresía.

* Cypher Stack recibe financiación para el desarrollo de Spark.

## Dirigiéndose a

Lamentablemente, las direcciones de Monero que se utilizan actualmente no son compatibles con Seraphis. Los usuarios tendrían que generar nuevas direcciones a partir de las claves de sus monederos para poder recibir Monero si se implementara Seraphis. Sin embargo, este coste del ecosistema viene acompañado de una serie de beneficios.

Aparte de los beneficios estructurales comentados anteriormente, el diseño de Seraphis se presta a muchas posibilidades de construcción de direcciones diferentes, cada una de las cuales conlleva ventajas. Mientras que la construcción final de la dirección que se utilizará en Seraphis está [aún en proceso de decisión](https://github.com/monero-project/research-lab/issues/92) (un esquema que está recibiendo mucha atención se llama [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), podemos describir algunas características comunes y útiles.

Puede que sepas que las direcciones de Monero ofrecen _la funcionalidad de llave de vista_ , en la que puedes proporcionar una llave de vista a un dispositivo o a un tercero y permitirle que vigile las salidas entrantes en tu nombre, pero sin renunciar a la autoridad de gasto. Esto es útil para los monederos, que pueden permanecer actualizados mientras mantienen su clave de gasto a salvo. También es útil para los casos en los que se desea tener acceso a una vista externa, como una organización benéfica pública que ofrece transparencia o una empresa con un departamento de contabilidad.

La desventaja de las claves de vista de Monero es que no proporcionan un acceso completo o de grano fino a la vista. No es posible detectar de forma fiable cuando un monedero gasta fondos, lo que dificulta el cálculo adecuado de los saldos de los monederos cuando la clave de gasto no está disponible. Tampoco es posible actualmente detectar las salidas entrantes sin aprender también el valor contenido en esas salidas (lo que significa que cualquier tercero responsable de encontrar las salidas entrantes sabrá exactamente cuánto Monero estás adquiriendo).

Las construcciones de direccionamiento Seraphis pueden resolver esto. Con Seraphis, tu dirección viene equipada con diferentes llaves que pueden hacer diferentes cosas:

  * Vigilar las salidas entrantes, pero ocultar su valor
  * Vigilar las salidas entrantes, pero mostrar su valor
  * Vigilancia de las salidas
  * Ayudar a generar transacciones, pero no firmarlas
  * Generar nuevas direcciones (útil para minoristas o bolsas con muchos clientes)

Como titular de la dirección, puedes decidir cuánta autoridad delegas en otros dispositivos o en terceros.

## El panorama general

Seraphis es un cambio importante en el ecosistema de Monero. Aunque implica modificaciones en las direcciones y en los bloques de construcción de las transacciones, su diseño ofrece flexibilidad y funcionalidades útiles que no son posibles con el protocolo RingCT actual. Mientras que gran parte del diseño está finalizado y se está desarrollando en [una implementación](https://github.com/UkoeHB/monero/tree/seraphis_lib)el diseño de la dirección y el análisis de seguridad están en curso. Seraphis ofrece una excelente oportunidad para impulsar el ecosistema Monero.

Otras lecturas