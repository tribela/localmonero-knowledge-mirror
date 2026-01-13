---
title: "Como Monero resolveu o problema do tamanho do bloco que assola o Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Nota:** É altamente recomendável que o leitor leia nossos artigos ["Por que o Monero tem uma emissão de cauda"](/knowledge/monero-tail-emission) e [“Mineração de Monero: o que torna o RandomX tão especial”](/knowledge/monero-mining-randomx). Este artigo baseia-se nos conceitos apresentados nele._

Sempre que as pessoas discutem os problemas com o blockchain, uma das primeiras palavras a aparecer será “escalonamento”. Não é segredo que blockchains não escalam bem, mas a maioria das pessoas não sabe por quê.

A verdade é que escalar é na verdade um termo abrangente que abrange duas categorias diferentes: suporte a protocolo e suporte tecnológico em um determinado momento. Neste artigo, vamos concentrar nossa atenção em um: O suporte ao protocolo é basicamente uma medida de quantas transações o protocolo pode manipular em um determinado momento.

O Bitcoin tem um limite de tamanho de bloco, o que significa que uma vez que transações suficientes sejam incluídas em um bloco, quaisquer transações adicionais terão que esperar na fila pelo próximo bloco. Uma analogia útil seria pensar em um trem. Um trem chega à estação e os que estão na fila entram. Quando o trem estiver cheio, qualquer pessoa que ficar de fora terá que esperar pelo próximo.

O Bitcoin usa taxas para determinar quem entra ou não no bloco. Voltando à analogia do trem, pode-se imaginar que um passageiro em potencial, que está prestes a ser deixado para trás, oferece ao maquinista cinco dólares para lhe dar um assento. Outros passageiros seguem o exemplo e, eventualmente, há uma guerra de lances para ver quem fica com quais assentos. Cabe ao motorista decidir se deseja honrar a política de ordem de chegada, mas é do seu interesse financeiro maximizar sua receita aceitando os licitantes com lance mais alto.

Nesta analogia, os mineiros são os maquinistas. Eles podem incluir quaisquer transações que desejarem no bloco, mas geralmente escolherão aquelas que têm as taxas pagas mais altas.

Alternativamente, se os blocos não estiverem muito cheios, as pessoas não terão incentivos para pagar taxas elevadas porque há muitos lugares livres disponíveis.

No auge do boom das criptomoedas de 2017, o Bitcoin foi inundado com transações, e as taxas dispararam para aqueles que queriam ser incluídos no próximo bloco, ou em qualquer bloco em um futuro próximo. Aqueles que não estavam dispostos a pagar taxas altas viram suas transações adiadas por horas, dias ou até mesmo saírem completamente da fila.

Esta foi uma visão angustiante de como o Bitcoin se sairia se ocorresse a tão falada “adoção em massa”. Se o Bitcoin fosse usado pelas massas, as coisas seriam ainda piores do que em 2017, e o Bitcoin seria inacessível a qualquer pessoa, exceto aos ricos, simplesmente porque o rendimento é pequeno devido a um tamanho de bloco fixo, fazendo com que o mercado de taxas assumisse o controle. .

Monero previu isso e queria fazer algo diferente. Portanto, os desenvolvedores do Monero implementaram um tamanho de bloco dinâmico.

Basicamente, Monero também tem um limite de tamanho de bloco, mas é um limite flexível. Quando a fila de transações em espera fica muito longa, os mineradores podem aumentar o tamanho dos blocos. Com nossa analogia com o trem, você pode imaginar a adição de mais vagões para acomodar os passageiros extras. Depois que a fila estiver vazia, os blocos voltarão ao tamanho original daqui para frente.

Se esta parece uma ideia interessante, parece razoável perguntar por que o Monero é a única criptomoeda que implementou isso. Por que não adicioná-lo ao Bitcoin para acabar com os problemas de rendimento?

Infelizmente, isso não é possível. Existem vários motivos e faremos o possível para explicar.

É sempre do interesse do mineiro ter blocos grandes. Com blocos grandes, eles podem realizar mais transações e ganhar mais dinheiro com as taxas, bem como com as recompensas do bloco. Isto tem o potencial de levar a ataques de spam, onde alguém envia muitas pequenas transações, com pequenas taxas, para aumentar a cadeia. Os mineradores apenas aumentariam o tamanho do bloco e incluiriam todos eles, porque dinheiro é dinheiro, não importa quão pequeno seja. Isto levaria a blocos consistentemente grandes com poucos benefícios económicos. O Bitcoin resolve isso restringindo artificialmente o tamanho do bloco, gerando assim um mercado de taxas. Os invasores de spam teriam que pagar mais que os outros usuários em taxas, e isso não é mais barato. Mas isso significa que os blocos ficam cheios, deixando algumas transações aguardando conforme mencionado acima.

Então, como o Monero pode ter tamanhos de bloco dinâmicos, mas evitar ataques de spam? A resposta é simples, mas inteligente. Uma penalidade na recompensa do bloco é introduzida quando um bloco é maior que o normal. Se um minerador quiser aumentar o tamanho do bloco, a recompensa que receberá ao encontrar esse bloco será menor do que receberia de outra forma. Portanto, eles só aumentarão o tamanho do bloco quando as taxas de transação pagas pelos usuários superarem a parte perdida da recompensa do bloco. Por exemplo, se o minerador perdesse 0,5 XMR ao aumentar o tamanho do bloco, e a soma das taxas de transação pagas fosse 0,4 XMR, então haveria uma perda líquida de 0,1 XMR se aumentasse o tamanho, então eles não faça isso. Por outro lado, se o total das taxas de transação somasse 0,7 XMR, então haveria um ganho líquido de 0,2 XMR, mesmo que eles perdessem 0,5 XMR da penalidade de recompensa do bloco, então o minerador aumentará o tamanho.

Esses blocos dinâmicos permitem que a rede cresça organicamente, sem restringir artificialmente o tamanho do bloco para criar um mercado de taxas forçadas, ao mesmo tempo que evita ataques de spam. Existem vários outros ângulos pelos quais podemos ver essa ideia e mais razões pelas quais não seria possível adicioná-la ao Bitcoin mas por enquanto esperamos que o leitor tenha uma compreensão de como o Monero contorna vários dos problemas no Bitcoin e seus derivados e como planeja escalar seu rendimento no futuro.

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies/)

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Por que (e como!) você deve segurar suas próprias chaves](/knowledge/hold-your-keys/)

  * [Contribuindo de volta para Monero](/knowledge/contributing-to-monero/)

  * [Como os nós remotos impactam a privacidade de Monero](/knowledge/remote-nodes-privacy/)

  * [Como Monero usa o hard-forks para atualizar a rede](/knowledge/network-upgrades/)

  * [Ver tags: Como um byte reduzirá o tempo de sincronização da carteira Monero em mais de 40%.](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool e seu papel na descentralização da mineração Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: O que fará por Monero](/knowledge/seraphis-for-monero/)

  * [Converter Bitcoin em Monero é tão privado quanto comprar Monero diretamente?](/knowledge/most-private-way-to-buy-monero/)

  * [Por que Monero usa uma configuração sem confiança ao contrário de Zcash](/knowledge/monero-trustless-setup/)

  * [Por que Monero é uma reserva de valor melhor do que Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Como Monero pode superar os efeitos de rede do Bitcoin](/knowledge/network-effect/)

  * [Por que Monero tem a comunidade de pensamento mais crítico](/knowledge/critical-thinking/)

  * [Golpes a serem observados ao usar o Monero](/knowledge/monero-scams/)

  * [Como as trocas atômicas funcionarão no Monero](/knowledge/monero-atomic-swaps/)

  * [O que todo usuário Monero precisa saber quando se trata de rede](/knowledge/monero-networking/)

  * [Como RingCT esconde valores de transação Monero](/knowledge/monero-ringct/)

  * [Como os endereços Monero Stealth protegem sua identidade](/knowledge/monero-stealth-addresses/)

  * [Como os subendereços do Monero evitam o vínculo de identidade](/knowledge/monero-subaddresses/)

  * [Saídas Monero explicadas](/knowledge/monero-outputs/)

  * [Práticas recomendadas Monero para iniciantes](/knowledge/monero-best-practices/)

  * [Como as assinaturas de toque obscurecem as saídas do Monero](/knowledge/ring-signatures/)

  * [Como o CLSAG melhorará a eficiência da Monero](/knowledge/what-is-clsag/)

  * [Por que Monero tem uma emissão de cauda](/knowledge/monero-tail-emission/)

  * [A história de Monero](/knowledge/monero-history/)

  * [Revista Wired está errada sobre Monero, aqui está o porquê](/knowledge/wired-article-debunked/)

  * [Os 15 principais mitos e preocupações de Monero desmascarados](/knowledge/monero-myths-debunked/)

  * [Como o Dandelion ++ mantém as origens da transação de Monero em sigilo](/knowledge/monero-dandelion/)

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx/)

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better/)