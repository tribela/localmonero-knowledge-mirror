---
title: "Monero Mining: O que torna o RandomX tão especial"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Em 30 de novembro de 2019, a Monero teve seu hard fork semestral, com a mudança mais esperada sendo uma mudança do antigo algoritmo PoW, cryptonight, para o completamente novo e desenvolvido internamente, o RandomX. A comunidade Monero acredita que o RandomX é um grande passo em direção à mineração igualitária, mas vamos nos aprofundar para ver se esse é o caso.

## Objectivo

Para julgar se o RandomX é uma melhoria, precisamos primeiro entender qual é o objetivo da mineração. A mineração protege uma blockchain de gastos duplos via consenso de Nakamoto. Os meandros exatos de como isso é feito estão além do escopo deste artigo, mas podem ser aprendidos em várias fontes diferentes da Internet. O que importa é que a segurança provenha de hashes gerados por computadores (mineradores), em concorrência entre si para encontrar a solução matemática necessária para criar outro bloco. Ao fazer isso, eles adicionam novas transações ao blockchain. Em troca de seu trabalho (hashes), são compensados com moedas recém-cunhadas.   
  
Há vários problemas que podem ocorrer com essa configuração e exigem incentivos adequados para funcionar corretamente, mas vamos nos concentrar em um problema específico que possa surgir. Se a mineração é uma competição, o que acontece quando um minerador obtém uma vantagem?

## Fundo

Para contextualizar, vamos falar um pouco sobre hardware de mineração. Os mineiros usam computadores para fazer o trabalho, mas todos sabemos que nem todos os computadores são feitos da mesma forma. Alguns computadores são poderosos o suficiente para executar redes de IA ou jogos intensos, enquanto outros enfrentam dificuldades até mesmo com tarefas simples. Essas diferenças no poder de computação também afetam a taxa de hash, ou a taxa com que procuram soluções de bloco.   
  
Mas mesmo essas diferenças entre computadores são insignificantes em comparação com as taxas de hash de hardware especializado, também conhecidos como Circuitos Integrados de Aplicação Específica (ASICs), que superam os computadores normais em várias ordens de magnitude.  
  
Vamos explorar o que torna os ASICs tão poderosos. Imagine todos os computadores como se estivessem em algum lugar de um espectro, que vai desde ser capaz de fazer muitas coisas, mas nada bem, até fazer apenas uma coisa, mas fazê-la muito bem. CPUs e ASICs estão em extremos opostos desse espectro.  
  
As CPUs que estão em todos os computadores padrão estão na primeira extremidade. Eles podem fazer muitas coisas, como navegar na web, jogar ou renderizar vídeos, mas não fazem nenhuma delas particularmente bem. Mas essa flexibilidade tem um custo de eficiência.  
  
Os ASICs estão do outro lado, onde podem fazer apenas uma coisa, mas a um ritmo incrível. Eles só podem executar uma função matemática, mas como podem ignorar todo o resto, os ganhos de desempenho são astronômicos. Essa eficiência, no entanto, tem o custo da flexibilidade, portanto, se a função mudar, mesmo que ligeiramente – um exemplo é x + y = z muda para 2x + y = z – então o ASIC deixará de funcionar completamente.   
  
Nem todo mundo possui um ASIC, mas todo mundo possui computadores. Isso pode levar a uma vantagem injusta.

## Uma analogia divertida

Se isso ainda é confuso, talvez a analogia a seguir ajude. Imagine uma loteria em que mil dólares são concedidos a cada hora, e essa loteria permite imprimir seus próprios bilhetes! Você começa a imprimir o maior número possível de tickets na impressora doméstica, que pode imprimir um ticket por segundo. Depois de subtrair os custos de eletricidade e tinta, você percebe que ainda pode obter lucro, mesmo que ganhe na loteria apenas uma vez a cada poucas semanas.  
  
Com o tempo, você expande sua operação até ter uma sala inteira dedicada às impressoras. 20 no total. Está tudo bem ... até um dia fatídico.  
  
Há boas notícias. Alguém inventou um novo tipo de impressora. Só pode imprimir bilhetes de loteria. Não pode imprimir fotos, documentos de escritório ou imprimir em frente e verso. Apenas bilhetes de loteria. Mas pode imprimi-los a uma taxa de 1000 tickets por segundo. Você olha na sua pequena sala de impressoras. 20 impressoras. Você precisa de mais 980 impressoras apenas para acompanhar UMA dessas impressoras monstruosas, e se alguém tiver duas…?  
  
Infelizmente você sai do jogo da loteria, pois não pode mais justificar os custos de eletricidade e tinta.  
  
Mas espere! Algumas semanas há mais novidades! O design do ticket foi alterado. Agora, os números, que costumavam estar no topo, agora estão no fundo. As novas impressoras monstruosas são tão inflexíveis que não conseguem. Eles só podiam fazer o design anterior. Não demorou muito para que você novamente imprimisse com satisfação. Pelo menos até que alguém faça uma nova impressora monstro para o novo design.

## RandomX

Onde o RandomX se encaixa em tudo isso? Ele procura equilibrar a vantagem dos ASICs, tornando-os muito difíceis de fazer. Isso é feito exigindo que os mineradores criem e executem códigos aleatórios no lugar de hash com base em um algoritmo.  
  
Pode ser confuso como isso realmente ajuda em algo, então vamos voltar à analogia da nossa impressora. Lembra do que aconteceu quando o design mudou? As antigas impressoras monstruosas ficam obsoletas todas as noites, e novas precisam ser desenvolvidas com o novo design em mente. O que aconteceria se cada novo bilhete de prêmio da loteria tivesse que aderir a um novo padrão de design para cada novo jackpot?   
  
Criar uma nova impressora monstro se tornaria incrivelmente difícil. Você não pode mais planejar apenas um design de ingresso. Como o design é aleatório, os fabricantes de impressoras monstruosas teriam que adicionar recursos de cores, maneiras de imprimir diferentes letras, bordas, formas e muito mais. Em suma, a máquina que acabaram inventando seria uma impressora comum e padrão. Assim como todo mundo tem.  
  
Ao simplesmente implementar essa aleatoriedade no design do ticket, reduzimos substancialmente a grande vantagem obtida com o hardware especializado. RandomX faz o mesmo, mas com mineração.  
  
Dessa forma, as vantagens obtidas por algumas poucas pessoas ricas são minimizadas, como se investissem na criação de “ASICs” para minerar o RandomX, na verdade, apenas inventariam CPUs melhores e mais fortes, o que beneficia o mundo em geral.  
  
Isso significa que o rapaz com suas 20 impressoras de ingressos está de volta ao jogo. Ele ainda pode ter mais dificuldade, pois esses indivíduos ricos ainda podem comprar mais impressoras do que ele, mas pelo menos agora ele não é superado por ordens de magnitude simplesmente de uma máquina. Ele é competitivo em sua pequena maneira.  
  
Sabendo que até o rapaz pode ser competitivo na mineração do Monero, incentivamos todos a dar uma volta, na carteira da GUI Monero, que oferece suporte à mineração individual ou no download de software mantido pela comunidade. É fácil, competitivo e aberto a todos.

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

  * [Como as assinaturas de toque obscurecem as saídas do Monero](/knowledge/ring-signatures)/

  * [Como Monero resolveu o problema do tamanho do bloco que assola o Bitcoin](/knowledge/dynamic-block-size)/

  * [Como o CLSAG melhorará a eficiência da Monero](/knowledge/what-is-clsag)/

  * [Por que Monero tem uma emissão de cauda](/knowledge/monero-tail-emission)/

  * [A história de Monero](/knowledge/monero-history)/

  * [Revista Wired está errada sobre Monero, aqui está o porquê](/knowledge/wired-article-debunked)/

  * [Os 15 principais mitos e preocupações de Monero desmascarados](/knowledge/monero-myths-debunked)/

  * [Como o Dandelion ++ mantém as origens da transação de Monero em sigilo](/knowledge/monero-dandelion)/

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better)/