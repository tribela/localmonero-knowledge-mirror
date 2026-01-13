---
title: "Como as assinaturas de toque obscurecem as saídas do Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero é conhecido por todo o espaço criptográfico como o rei das moedas de privacidade. Embora todos saibam que o Monero oferece boa privacidade, poucos entendem como a privacidade funciona.

Muitas outras moedas de privacidade publicam infográficos de gráfico de comparação, que listam os nomes da tecnologia de privacidade de cada moeda e, na maioria, rotulam a tecnologia de Monero como RingCT, mas isso é apenas parcialmente verdadeiro. Monero, na verdade, tem uma abordagem tripla para a privacidade. Uma tecnologia para ocultar o destinatário de uma transação, uma para ocultar a quantidade enviada e outra para ocultar a saída usada, são endereços furtivos, RingCT e assinaturas de anel, respectivamente.

Essa abordagem tripla significa que, se uma das tecnologias for quebrada, as outras não terão necessariamente o mesmo destino. As assinaturas de anel são o elo mais fraco no esquema de privacidade; a palavra fraco aqui significa o mais suscetível a ataques heurísticos. Vamos tirar algum tempo para explorá-los, certo?

Conforme mencionado acima, o objetivo das assinaturas de anel é obscurecer uma saída usada em uma transação. Se a terminologia de 'entrada / saída' da criptomoeda é confusa para você, não se preocupe. Na verdade, não é tão complicado. Quando você ouvir 'saída', pense em um cheque. Uma daquelas coisas, que não são mais tão comuns, com que as pessoas costumam pagar. Como um cheque, ele pode ser denotado em qualquer valor - $ 10, $ 32,50, etc. - e é trocado entre as partes na transação. Para criptomoedas, as saídas atendem a essas funções.

Quando alguém lhe paga 10 Monero, você recebe uma saída de 10 XMR. Esta saída tem um valor (10), e é o que é retirado da carteira do remetente, da mesma forma que quando você paga por um serviço, uma conta sai de sua carteira física e é entregue à pessoa de quem você está comprando.

A forma como a saída é oculta é pela construção de um anel (daí o nome) de saídas chamariz. Mas essas iscas não são saídas 'falsas'. Eles são saídas passadas reais do blockchain que não têm nada a ver com a transação presente, mas para um observador externo, cada uma dessas saídas pode parecer tão provável quanto a real. O tamanho do conjunto de saídas de engodo, mais o real, é chamado de tamanho do anel, e atualmente o de Monero é de onze. Portanto, há dez saídas de engodo e uma real.

Por que simplesmente não aumentamos esse número para 100 ou até 1000? Quanto mais, melhor, certo? Bem, do ponto de vista da privacidade, sim, mas há outras coisas a serem consideradas. Vamos voltar a um exemplo físico para ver o que quero dizer. Se você quisesse esconder uma de suas notas de um dólar entre dez iscas, precisaria carregar cerca de onze dólares na carteira para cada dólar que quisesse gastar. Um dólar real e dez falsos. Isso já fica muito complicado se você quiser gastar até mesmo alguns dólares. Agora imagine que aumentamos o valor do chamariz para 1000. Para cada dólar que você quisesse gastar, seria necessário carregar cerca de 1001 dólares. Você precisaria carregar uma pasta apenas para comprar uma barra de chocolate! É importante observar que as assinaturas de anel não funcionam exatamente dessa maneira, por exemplo, os próprios chamarizes não fazem parte da assinatura, apenas referências a eles, mas esperamos que essa analogia possa ser de alguma forma útil para ilustrar os conceitos básicos.

Os chamarizes no blockchain funcionam de forma semelhante. Cada engodo adicionado aumenta o tempo e o custo de verificação da transação. Cada nó deve fazer o download de toda a assinatura do anel para cada transação, e cada assinatura do anel contém a saída real, bem como os chamarizes. Não apenas isso, mas tem que verificar a matemática de que pelo menos uma dessas saídas é real, e o tempo de verificação matemática também aumenta a cada engodo. Isso significa que temos que encontrar um meio termo feliz, onde o tamanho do anel é grande o suficiente para obscurecer adequadamente a saída real, mesmo contra muitos ataques heurísticos, mas pequeno o suficiente para não fazer com que o blockchain aumente em uma taxa massiva. Não é suficiente escolher um número arbitrário ou apenas aumentar o tamanho do anel quando tornamos a assinatura menor (como com CLSAG). A comunidade Monero quer evidências matemáticas concretas sobre as quais o tamanho do anel ofereça as melhores compensações. Um número muito pequeno e a privacidade não será forte o suficiente contra ataques heurísticos. Muito grande, podemos estar obtendo apenas um benefício marginal no lado da privacidade e sofrendo desnecessariamente em relação ao dimensionamento.

Uma última coisa a mencionar. Alguma literatura de Monero simplifica e diz que as assinaturas de anel escondem o remetente, mas isso não é inteiramente verdade, e a diferença não é apenas pedante. A diferença entre o remetente (um ser humano) e uma saída (uma conta) é grande quando se trata de preservar a privacidade. Embora uma saída possa ter vínculos com um remetente, uma saída em si não é igual a um remetente. Portanto, mesmo que uma assinatura de anel deva ser quebrada, ela não está necessariamente vinculada à identidade de uma pessoa, e tanto o valor quanto o destinatário ainda estão ocultos, minimizando o dano causado à privacidade de todas as partes.

Isso não quer dizer que uma assinatura de anel quebrado seja insignificante. Qualquer metadado vazado é ruim e tem o potencial de revelar mais informações do que pensamos, especialmente quando usado em conjunto com outros metadados. Portanto, fazemos o nosso melhor para garantir que o tamanho do anel escolhido tenha rigor acadêmico por trás da decisão, outro vazamento de metadados seja minimizado e as experiências do usuário sejam padronizadas para as melhores ações possíveis.

Mas se a probabilidade de uma assinatura quebrada ainda é preocupante para você, bem, há algumas notícias incríveis no horizonte. A próxima geração de protocolos de privacidade em que está sendo trabalhada, como Triptych, Arcturus e Lelantus, tem recursos realmente interessantes. Nesses protocolos, o tamanho é dimensionado logaritmicamente, não linearmente, conforme o tamanho do anel aumenta. Isso significa que podemos acomodar 100 iscas, mas o espaço usado é mais próximo do tamanho de 10 anéis na tecnologia antiga. Essa é a grande diferença e irá melhorar significativamente a privacidade em todos os lugares.

No jogo de gato e rato que é privacidade, Monero inova continuamente para ficar à frente da curva e garantir a melhor privacidade prática para todos.

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

  * [Como RingCT esconde valores de transação Monero](/knowledge/monero-ringct)/

  * [Como os endereços Monero Stealth protegem sua identidade](/knowledge/monero-stealth-addresses)/

  * [Como os subendereços do Monero evitam o vínculo de identidade](/knowledge/monero-subaddresses)/

  * [Saídas Monero explicadas](/knowledge/monero-outputs)/

  * [Práticas recomendadas Monero para iniciantes](/knowledge/monero-best-practices)/

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