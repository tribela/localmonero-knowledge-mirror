---
title: "Como RingCT esconde valores de transação Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
A privacidade do Monero não depende de um único mecanismo que, se quebrado, revelaria a totalidade das transações, mas sim de três tecnologias diferentes que funcionam em conjunto para fornecer privacidade holística enquanto compensam as fraquezas das outras partes. Essa abordagem de três pontas consiste em assinaturas de anel, RingCT e endereços furtivos. Essas três tecnologias ocultam a saída real (emissor), quantidade e receptor, respectivamente. Hoje vamos falar sobre RingCT.

RingCT é indiscutivelmente o mais técnico dos três e pode ser difícil de entender, então não vamos cobrir como ele funciona exatamente, mas sim mostrar como é possível não saber uma quantidade e ainda confirmar coisas sobre ela . E não se preocupe, usaremos muitos exemplos, como sempre.

Primeiro, vamos explorar por que é importante verificar tudo sobre os valores. Por que não podemos simplesmente mantê-los em segredo? A resposta é: existem maneiras inteligentes pelas quais as pessoas podem criar dinheiro do nada, se tiverem a oportunidade. Como algo assim pode funcionar? Vejamos um exemplo.

Se você quiser comprar um item de seu amigo e ele quiser dez dólares por ele, você começa com dez dólares e ele começa com zero. Depois de dar a ele os dez dólares, ele tem dez dólares e você zero. Você começou com dez e agora ele tem dez. Nenhum dinheiro foi criado ou destruído nesta transação.

Com as criptomoedas, um indivíduo inteligente pode dar dez dólares pelo item e, em vez de receber zero dólares em troco, pode receber dois dólares de volta. Em vez de 0 e 10 levando a 10 e 0 (ou 10 = 10), agora é 0 e 10 leva a 10 e 2 (ou 10 = 12). Dois Monero acabou de ser criado do nada. Você pode imaginar que, se o indivíduo fizesse isso consigo mesmo várias vezes, seria capaz de acumular uma fortuna gigantesca em pouco tempo.

Com Bitcoin e outros, isso seria fácil de ver. Você olha as entradas que entram em uma transação e as saídas que saem e se certifica de que o que é enviado é igual ao que é recebido. Se esses valores estiverem criptografados e não estiverem visíveis, o usuário não terá como verificar se o que é enviado e o que é recebido são iguais.

Em uma tentativa de aumentar a privacidade do Bitcoin, Gregory Maxwell criou as Transações Confidenciais (CT), uma nova tecnologia que permitiria quantias criptografadas, ao mesmo tempo que provava que nada foi criado ou destruído no processo. Como acontece com a maioria das tecnologias de privacidade, não chegou ao Bitcoin, mas Monero estava ansioso para adotá-lo. Só havia um problema. A tecnologia de ring assinaturas já implementada era incompatível com a ideia proposta. Então, um dos pesquisadores do MRL na época, Shen Noether, modificou o CT em RingCT, uma versão do CT compatível com assinaturas de anel.

Mais uma vez, a maneira como isso funciona é bastante técnica e seria difícil de explicar em um artigo introdutório. Para o entusiasta da criptografia que simplesmente precisa saber, existem muitos artigos detalhados escritos na Internet sobre o funcionamento interno da TC. Para o restante de nós, este artigo mostrará como é possível ocultar os valores, mas ainda assim provar que nada foi criado ou destruído.

Digamos que Alice queira enviar dinheiro para Bob. Alice enviará 10 XMR para Bob, que receberá 10 XMR. 10 = 10, então nada está errado aqui. Mas Alice não quer que ninguém saiba quanto ela está enviando. Então, ela e Bob criam um segredo compartilhado. Basicamente, um número que só os dois conhecem. Digamos que esse número seja 22. Agora, Alice multiplica 10 (o que ela está realmente enviando) por 22 para obter 220. Este é o número que ela compartilha com a rede.

Os próprios mineradores não sabem o número secreto. Se o fizessem, eles poderiam dividir o número mostrado pelo número secreto e obter o valor real enviado. Mas uma vez que não, eles não podem. Eles veem que Bob receberá 220. 220 enviado. 220 recebidos. 220 = 220. Desta forma, a rede pode verificar se nenhum Monero foi criado ou destruído, tudo sem saber a quantidade real que Alice enviou a Bob.

Como Bob sabe o número secreto compartilhado, quando recebe o dinheiro, ele apenas divide por 22 para obter a quantia real que Alice enviou, 10. Alice e Bob sabem quanto foi enviado e quanto foi recebido, o tempo todo todos os outros recebem um número falso.

Mais uma vez, esta não é a maneira real em que a TC funciona, mas dá uma ideia de como algo assim pode ser possível. O caminho real envolve coisas como compromissos Pedersen, dois valores enviados (um valor criptografado para o receptor e um valor de compromisso para a rede) e ... sim, já é fácil ver como alguém pode se perder em tudo isso.

Uma coisa a observar, entretanto, é que, embora o RingCT oculte o valor transacionado entre duas partes em uma transação, ele não oculta dois outros conjuntos de números.

O primeiro são as transações coinbase. Se este termo não for familiar para você, significa basicamente a recompensa que os mineradores recebem por encontrar o próximo bloco. Este número não está oculto. Qualquer um pode ver o quanto o protocolo premiou um minerador por seu serviço. Desta forma, a quantidade atual de Monero existente pode ser conhecida somando todas as transações coinbase. A soma deles será igual ao atual Monero em circulação.

O segundo número não oculto é a taxa paga aos mineradores quando um usuário envia uma transação. As taxas devem ser claras para que os mineradores possam saber quem priorizar. No entanto, essa é uma maneira de os usuários prejudicarem sua privacidade, pois se alguém usar uma taxa única de minerador cada vez que enviar uma transação (como 0,12345), então suas transações podem ser vinculadas.

Além desses casos, a RingCT esconde valores de Monero desde 2017, e nossa privacidade coletiva é ainda mais forte por causa disso.

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies)/

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por que (e como!) você deve segurar suas próprias chaves](/knowledge/hold-your-keys)/

  * [Contribuindo de volta para Monero](/knowledge/contributing-to-monero)/

  * [Como os nós remotos impactam a privacidade de Monero](/knowledge/remote-nodes-privacy)/

  * [Como Monero usa o hard-forks para atualizar a rede](/knowledge/network-upgrades)/

  * [Ver tags: Como um byte reduzirá o tempo de sincronização da carteira Monero em mais de 40%.](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool e seu papel na descentralização da mineração Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: O que fará por Monero](/knowledge/seraphis-for-monero)/

  * [Converter Bitcoin em Monero é tão privado quanto comprar Monero diretamente?](/knowledge/most-private-way-to-buy-monero)/

  * [Por que Monero usa uma configuração sem confiança ao contrário de Zcash](/knowledge/monero-trustless-setup)/

  * [Por que Monero é uma reserva de valor melhor do que Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Como Monero pode superar os efeitos de rede do Bitcoin](/knowledge/network-effect)/

  * [Por que Monero tem a comunidade de pensamento mais crítico](/knowledge/critical-thinking)/

  * [Golpes a serem observados ao usar o Monero](/knowledge/monero-scams)/

  * [Como as trocas atômicas funcionarão no Monero](/knowledge/monero-atomic-swaps)/

  * [O que todo usuário Monero precisa saber quando se trata de rede](/knowledge/monero-networking)/

  * [Como os endereços Monero Stealth protegem sua identidade](/knowledge/monero-stealth-addresses)/

  * [Como os subendereços do Monero evitam o vínculo de identidade](/knowledge/monero-subaddresses)/

  * [Saídas Monero explicadas](/knowledge/monero-outputs)/

  * [Práticas recomendadas Monero para iniciantes](/knowledge/monero-best-practices)/

  * [Como as assinaturas de toque obscurecem as saídas do Monero](/knowledge/ring-signatures)/

  * [Como Monero resolveu o problema do tamanho do bloco que assola o Bitcoin](/knowledge/dynamic-block-size)/

  * [Como o CLSAG melhorará a eficiência da Monero](/knowledge/what-is-clsag)/

  * [Por que Monero tem uma emissão de cauda](/knowledge/monero-tail-emission)/

  * [A história de Monero](/knowledge/monero-history)/

  * [Revista Wired está errada sobre Monero, aqui está o porquê](/knowledge/wired-article-debunked)/

  * [Os 15 principais mitos e preocupações de Monero desmascarados](/knowledge/monero-myths-debunked)/

  * [Como o Dandelion ++ mantém as origens da transação de Monero em sigilo](/knowledge/monero-dandelion)/

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx)/

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better)/

Leitura adicional