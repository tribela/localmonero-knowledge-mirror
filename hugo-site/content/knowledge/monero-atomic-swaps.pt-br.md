---
title: "Como as trocas atômicas funcionarão no Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Na busca pela descentralização e por um sistema verdadeiramente sem permissão, poucas coisas são tão cobiçadas no espaço das criptomoedas quanto as trocas descentralizadas e as trocas atômicas. Desde o seu início, Monero tem lutado para implementar trocas atômicas, já que os recursos de privacidade criam problemas exclusivos ao tentar projetar um protocolo.

Mas primeiro, vamos voltar. O que são trocas atômicas? Uma troca atômica é um protocolo pelo qual duas criptomoedas diferentes, em cadeias de blocos diferentes, podem ser trocadas de maneira confiável e sem intermediários. Isso significa que se alguém quisesse trocar a criptomoeda A pela criptomoeda B, seria capaz de fazer isso sem uma troca, centralizada ou descentralizada. Como se pode imaginar, isso requer uma pesquisa considerável e todos os detalhes técnicos que o tornam possível se tornam bastante complicados. Mais uma vez, LocalMonero está aqui para ajudar e dar uma explicação simples para o cidadão comum.

Para começar, vamos considerar a forma mais simples de troca atômica, conforme implementada pelo Bitcoin. Se alguém quiser trocar o Bitcoin por outra moeda que usa a mesma tecnologia de contrato de hash time lock, pode fazer isso da seguinte maneira. Alice tem Bitcoin (BTC), mas quer Litecoin (LTC), e Bob tem LTC, mas quer BTC. Eles decidem fazer uma troca atômica para que cada um receba a moeda que deseja. Alice envia seu BTC para um endereço especial, utilizando scripts que bloqueiam os fundos para que nem ela possa acessá-los. Você pode pensar nisso como se Alice colocasse seu BTC em um cofre. Quando o cofre é feito, ela pega uma chave e envia um hash dessa chave para Bob. Agora, Bob não tem a chave em si, apenas o hash, então ele ainda não pode acessar os fundos.

Bob usa esse hash como uma semente a partir da qual ele gera seu próprio cofre e envia seu LTC para lá, onde também está bloqueado. Como o hash da chave de Alice foi usado como a semente pela qual o cofre de Bob foi feito, ela pode usar sua chave para reivindicar o LTC no cofre de Bob. Sua chave se encaixa! Mas, usando magia vodu matemática, quando ela usa sua chave para abrir a fechadura LTC, ela revela a chave para Bob, que pode então usá-la para reivindicar o BTC que ela colocou em seu cofre. Dessa forma, sem intermediários, Alice e Bob trocaram seus ativos com sucesso.

Mas há um pequeno problema. E se Alice enviar para seu cofre e Bob decidir que não quer mais negociar. Agora, como Alice não pode acessar seu BTC que ela trancou e Bob não vai concluir sua parte na transação, Alice simplesmente perde seu dinheiro para sempre. Bem, felizmente, o Bitcoin tem um pouco de tecnologia chamada transações de reembolso e, portanto, após um período de tempo, se o BTC não for reivindicado por Bob, os scripts têm um sistema de segurança embutido, onde o BTC voltará automaticamente para Alice. Este foi o principal aumento de velocidade para a implementação das trocas atômicas do Monero. Por causa da [tecnologia de privacidade de assinaturas de anel da Monero](/knowledge/ring-signatures), o remetente de uma transação é sempre incerto. Como o protocolo pode fazer uma transação de reembolso se mesmo não sabe de onde veio a transação?

Em 2017, um pequeno grupo de pesquisadores descreveu um método diferente pelo qual as trocas atômicas funcionariam em Monero. Após vários anos de aperfeiçoamento, os pesquisadores finalizaram um processo pelo qual Monero seria capaz de fazer trocas atômicas com Bitcoin, mesmo sem transações de reembolso.

Como acontece com muitas coisas desse nível de complexidade técnica, nossa explicação simplificará excessivamente algumas coisas para transmitir a ideia, mas ainda dará uma ideia sólida dos mecanismos pelos quais esse processo funcionaria.

Tanto Alice (que tem XMR e deseja BTC) quanto Bob (que tem BTC e deseja XMR) devem baixar e executar um programa que ofereça suporte à troca atômica. Isso pode ser implementado em carteiras, trocas descentralizadas ou programas especiais e específicos, mas o software deve estar executando o protocolo de troca atômica. Na primeira etapa, os clientes de Alice e Bob se conectam e fazem vários segredos e chaves compartilhados. Nesta etapa, um novo endereço Monero é criado, com Alice tendo uma metade da chave e Bob a outra. Porém, nenhum Monero está lá ainda, então não há nada para gastar. Uma última coisa a se notar sobre este endereço, é que ambos têm a chave de visualização desta carteira, então ambos podem dar uma olhada dentro para ver se ou quando Monero chegar.

Na segunda etapa, Bob envia seu BTC para um endereço especial, semelhante ao protocolo de troca atômica Bitcoin que já discutimos. Depois que Alice vê o BTC chegar a este endereço na blockchain, ela envia seu Monero para o endereço Monero para o qual ela e Bob têm metade de uma chave. Bob pode verificar se o Monero chegou, já que ele também tem a chave de visualização, e quando vê que o Monero está seguro na carteira, ele envia a Alice um pedaço de uma chave que permitirá que ela retire o Bitcoin. Semelhante ao outro protocolo, o processo de reivindicação do Bitcoin revela sua metade da chave Monero para Bob. Agora Bob tem as duas metades, então ele pode reivindicar o Monero, enquanto Alice tem apenas a sua metade, então ela não pode tentar pegá-lo antes dele.

Então, se você analisou tudo isso e ainda está um pouco confuso sobre como o Monero conseguiu contornar o problema das transações de reembolso, a resposta é bastante simples. Como o próprio Monero não possui transações de reembolso, o leitor deve notar que o Bitcoin (que possui transações de reembolso) é enviado primeiro, e somente após ser verificado como estando no blockchain o Monero é enviado. Isso permite que o Monero utilize a capacidade do Bitcoin de criar scripts em transações de reembolso e tirar proveito delas, sem precisar ter esses recursos.

A troca atômica agora está completa, mas a partir daqui, Bob tem algumas opções para seu XMR recém-reivindicado. Ele pode usar a carteira Monero como está ou mover o XMR para outra carteira que ele já possui. Provavelmente, Bob irá mover o Monero para outra carteira, porque Alice ainda tem a chave de visualização e pode ver o interior.

A beleza deste protocolo é que ele ainda é bastante novo e há muito espaço para otimizações. Também é bastante flexível em sua arquitetura, portanto, a implementação em outras carteiras ou bolsas descentralizadas deve ser simples e se ajustar perfeitamente à arquitetura existente.

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