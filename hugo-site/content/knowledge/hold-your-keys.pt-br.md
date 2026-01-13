---
title: "Por que (e como!) você deve segurar suas próprias chaves"
slug: "hold-your-keys"
date: "2022-03-11"
image: "/images/keys.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Você já ouviu antes a frase "não suas chaves, não suas moedas"? Esta se tornou uma frase ubíqua na comunidade de moedas criptográficas, mas apesar de a maioria das pessoas ter ouvido a grande maioria das moedas criptográficas os usuários não possuem suas próprias chaves.

Os benefícios da moeda criptográfica que realmente a diferenciam da sistema financeiro tradicional só é realizado quando você tem completo custódia de seus fundos - segurando as chaves privadas de suas moedas.

Neste breve post vamos mergulhar no motivo pelo qual você deve segurar suas próprias chaves e dê algumas maneiras fáceis de auto-custódia a seu Monero _hoje_.

## Por que segurar suas próprias chaves é importante?

Um dos aspectos mais comumente incompreendidos da auto-custódia em Monero é que se você não tiver suas próprias chaves, você ganha pouco ou nenhum se beneficiar da privacidade que o Monero oferece. Como remetente de uma transação tem visibilidade total do gasto real, valor e endereço do destinatário, se não for você que está enviando a transação e, em vez disso, deixar isso para uma bolsa ou custodiante, eles têm _visibilidade total_ do maneiras de gastar seu Monero.

Felizmente, depois que eles enviam os fundos, a privacidade do Monero garante entrar em ação e fornecer um forte “segredo para a frente”, mas ficará claro para a bolsa ou custodiante para onde você enviou os fundos e quanto você enviou inicialmente.

Um dos aspectos fundamentais do Monero é permitir transações resistentes à censura – permitindo que você faça transações que pode ou não ser aprovado por “eles”, não importa o que eles tentem fazer para te parar. Embora a necessidade de resistência à censura possa ser um pouco perdido para aqueles de nós em países “livres”, o rápido deslizamento em direção autoritarismo e decadência política em muitas partes do mundo é tornando mais evidente a cada dia que precisamos de uma maneira de fazer transações com ou sem aprovação governamental.

Se você não tiver suas próprias chaves, no entanto, um governo ou regulador pode facilmente forçar uma bolsa ou custodiante a colocar seus fundos na lista negra, apreender ou censurar transações para endereços específicos. Isso já é acontecendo amplamente devido às sanções estaduais hoje, e será um tema crescente à medida que governos e reguladores percebem que as trocas e custodiantes são o caminho mais fácil para o controle da Monero uso.

Também pode chegar o dia em que um governo banirá a autocustódia de Monero, e se você ainda não retirou seu Monero de uma bolsa ou guardião que você pode nunca ser capaz de fazer.

Um cenário hipotético, mas possível, pode ser o pior caso para aqueles que optam por não ter suas próprias chaves - seu Monero recebendo roubado por um hacker ou confiscado por um governo com um [6102-like ordem](https://en.wikipedia.org/wiki/Executive_Order_6102).

[Quase US$ 500 milhões](https://blog.chainalysis.com/reports/2022-crypto-crime-report-introduction/) em criptomoedas foram roubados de exchanges centralizadas em 2021, e um total de US$ 3,2 bilhões roubados de usuários que desistiram da custódia de fundos por uma razão ou outra. Este é um dos maiores riscos usuários de criptomoedas e continua a crescer tanto em número de casos quanto em volume à medida que a criptomoeda ganha popularidade. Se uma bolsa detém as chaves aos seus fundos, esses fundos podem ser roubados por um hacker (ou a exchange eles mesmos!) a qualquer momento.

Se você possui suas próprias chaves, os únicos riscos reais de roubo ou confisco são golpes e ataques físicos, algo que é muito menos provável e geralmente só acontece com indivíduos de alto perfil ou aqueles prejudicado pelo roubo ou perda de dados de know-your-customer (KYC) de trocas centralizadas que vinculam seu ID e endereço com propriedade de criptomoedas.

Outro aspecto importante de ter suas próprias chaves é aquele que é menos pessoais e mais comunitários. Quando a grande maioria dos usuários do Monero detêm suas próprias chaves, as exchanges são menos capazes de mentir sobre a quantidade de Monero eles guardam e negociam “papel Monero”, pois os usuários não estão mantendo seu Monero em trocas.

Embora esse tipo de atividade não seja frequentemente confirmado publicamente, há muitos na comunidade estão preocupados que exchanges como a Binance estão aproveitando o Monero que seus usuários mantêm na bolsa para negociar contra Monero, inflando a quantidade de shorts Monero e causando preço supressão ao longo do tempo.

Esse comportamento também pode levar a crises de liquidez em que os usuários que __desejam manter suas próprias chaves não conseguem sacar do exchange, pois a exchange prometeu mais Monero para seus usuários do que realmente tem disponível. Quanto mais usuários do Monero tiverem suas próprias chaves e manter seu Monero fora das trocas, mais saudável e natural o mercado será teoricamente, e menos risco malicioso ou ganancioso exchanges podem representar para a estabilidade do preço do Monero.

##  Como eu seguro minhas próprias chaves com Monero?

Quando você começa a segurar suas próprias chaves, a coisa mais importante para lembrar é _salvar e manter sua frase de semente segura_! Este é o conjunto de 14 ou 25 palavras aleatórias que qualquer carteira Monero lhe dará quando criar uma carteira, e é tudo o que você precisará para obter seus fundos de volta se você perde seu telefone, seu desktop, seu laptop, ou você esquece um senha.

Trate esta frase de semente como se valesse todo o Monero em seu carteira, pois quem a receber terá acesso completo aos fundos em sua carteira. É ideal para mantê-la em um local seguro ou secreto, preservar múltiplas cópias em caso de incêndio ou desastre natural, e nunca mostrá-lo a qualquer pessoa.

Para saber mais sobre frases de sementes, veja [. Mnemonic Semente | Moneropedia](https://web.getmonero.org/resources/moneropedia/mnemonicseed.html).

Se você é principalmente um usuário desktop e não gasta/recebe Monero em movimento com muita freqüência, há algumas escolhas sólidas para manter sua própria chaves sem a necessidade de contar com terceiros.

  * [O Monero oficial carteira](https://getmonero.org/downloads)
    * Este é o software oficial de carteira Monero, e tem visto constante melhorias e acréscimos. Inclui um daemon Monero integrado (se você quer), é muito fácil de usar, e em breve apoiará a mineração [. via p2pool diretamente de sua carteira](/knowledge/p2pool-decentralizing-monero-mining/).
  * [Carteira de penas](https://featherwallet.org/)
    * Esta é uma excelente carteira na veia de [Elétrico para Bitcoin](https://electrum.org/)e fornece ambos usabilidade simples e características extremamente poderosas em um único carteira.

  * Esta é uma excelente carteira na veia de [Elétrico para Bitcoin](https://electrum.org/)e fornece ambos usabilidade simples e características extremamente poderosas em um único carteira.

Para aqueles de nós que gostam de poder usar nosso Monero em viagem ou gastar frequentemente, tendo uma sólida carteira Monero móvel que ainda mantém nossas chaves em nossas próprias mãos é imensamente importante.

  * [Carteira de bolo](https://cakewallet.com/)
    * Cake Wallet é uma carteira gratuita e de código aberto (FOSS) para Android e iOS que apóia Monero, Bitcoin, e Litecoin nativamente.
  * [Monerujo](https://www.monerujo.io/)
    * Monerujo é uma carteira FOSS para Android que tem alguns incríveis adicionados características e gráficos, suporte de nó Tor nativo, e muito mais.

  * Cake Wallet é uma carteira gratuita e de código aberto (FOSS) para Android e iOS que apóia Monero, Bitcoin, e Litecoin nativamente.

  * Monerujo é uma carteira FOSS para Android que tem alguns incríveis adicionados características e gráficos, suporte de nó Tor nativo, e muito mais.

## Conclusão

Espero que este posto tenha ajudado a cimentar a necessidade de manter seu chaves próprias, assim como apontou para algumas das excelentes carteiras do espaço.

Quanto mais você tomar Monero em suas próprias mãos e realmente usá-lo, o mais benefícios você pode obter tanto agora como no futuro. Monero não é apenas um ativo especulativo - é uma ferramenta poderosa para a liberdade e financeira privacidade que é muito necessária no mundo de hoje e no futuro de nós.

Agora vá tirar essas moedas de uma troca e mergulhe no que Monero era construído para.

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies/)

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

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

  * [Como Monero resolveu o problema do tamanho do bloco que assola o Bitcoin](/knowledge/dynamic-block-size/)

  * [Como o CLSAG melhorará a eficiência da Monero](/knowledge/what-is-clsag/)

  * [Por que Monero tem uma emissão de cauda](/knowledge/monero-tail-emission/)

  * [A história de Monero](/knowledge/monero-history/)

  * [Revista Wired está errada sobre Monero, aqui está o porquê](/knowledge/wired-article-debunked/)

  * [Os 15 principais mitos e preocupações de Monero desmascarados](/knowledge/monero-myths-debunked/)

  * [Como o Dandelion ++ mantém as origens da transação de Monero em sigilo](/knowledge/monero-dandelion/)

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx/)

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better/)