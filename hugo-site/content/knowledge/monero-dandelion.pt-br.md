---
title: "Como o Dandelion ++ mantém as origens da transação de Monero em sigilo"
slug: "monero-dandelion"
date: "2020-04-28"
image: "/images/dandelion.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Privacidade como prioridade

Como uma criptomoeda, Monero pode parecer muito chato a olho nu. Ele não tem uma grande reivindicação à fama, como ser um 'computador mundial' ou 'revolucionar a indústria xyz'. Ele está apenas tentando ser um dinheiro privado, digital e fungível, e cada atualização e nova tecnologia favorecem esse objetivo.   
  
Aqueles que consideram esse objetivo muito restrito ou desinteressante geralmente não entendem o quão difícil é obter privacidade significativa, especialmente em um livro aberto e permanente como um blockchain. Qualquer caminho para o vazamento de metadados é um potencial para a erosão da privacidade.   
  
Monero toma precauções para ofuscar dados na cadeia, como remetente, destinatário e valores, por meio de endereços furtivos, assinaturas de anel e compromissos da Pedersen, respectivamente. Isso minimiza as chances de um observador casual deduzir informações críticas depois que as transações já foram enviadas e agora fazem parte do histórico registrado. No entanto, existem alguns ataques que podem ser feitos no momento em que ocorre uma transação que não pode ser executada posteriormente.

## Ataque para revelar o endereço IP

Esses ataques giram em torno da identificação de qual endereço IP de origem da transação. Se essas informações forem deduzidas, poderá revelar que um indivíduo enviou uma transação Monero. Não é possível mostrar quem e quanto, mas há alguns casos em que o conhecimento de alguém que usa o Monero é suficiente para causar danos.   
  
A boa notícia é que, se essas informações não forem coletadas no momento em que a transação for feita, elas não poderão ser aprendidas posteriormente, pois os endereços IP não são armazenados na blockchain. Também é reconfortante saber que é improvável que esse ataque seja visto na natureza, pois, para executá-lo, o invasor precisaria de uma grande maioria de nós na rede. Se uma pessoa fosse capaz de comandar essa grande maioria, no entanto, seria capaz de identificar a "direção" da qual a transação veio.   
  
Isso pode ser confuso, portanto, explicaremos aqui algumas informações básicas. Cada nó se conecta a outros nós na rede, para que eles possam manter sua blockchain atualizada e compartilhar o que sabem com outras pessoas. Essas conexões permitem aprender sobre novas transações, propagá-las e enviar as suas próprias. Como um nó só pode contar aos seus pares sobre transações que eles conhecem, é lógico que o primeiro nó que propaga uma transação é o nó que está realmente enviando o Monero.   
  
Se um invasor possuir uma grande maioria de nós na rede, cada nó ouvirá sobre uma transação de um de seus pares e, com base no tempo em que cada nó recebe essas informações, poderá deduzir possíveis candidatos para onde a transação foi iniciada.   
  
Se isso ainda é confuso, oferecemos este exemplo. Suponha que ambos tenhamos um amigo em comum que está se escondendo de nossa visão. Este amigo chama em voz alta. Eu ouço a ligação dele primeiro, e ouço mais alto do que você. Com essas informações, podemos saber que provavelmente estou mais perto de nosso amigo do que você. O fato de você ouvir o som mais tarde (mesmo por apenas uma fração de segundo) e o som ficar mais fraco significa que devemos iniciar nossa pesquisa na minha área, não na sua.   
  
Se um invasor conseguir adivinhar com êxito quais de seus pares enviaram a transação, já que eles têm o endereço IP conectado ao nó e o encaminharam para ele, eles podem ter certeza do endereço IP que a enviou. Essas são informações poderosas, pois os endereços IP contêm informações sobre o país e o provedor de serviços de Internet (ISP) do usuário, e o próprio ISP sabe qual usuário está vinculado a qual endereço IP exato, efetivamente desinteressando o usuário Monero.

## A (s) mitigação (ões)

Uma possível mitigação para esse ataque é o uso de uma rede de sobreposição, como Tor ou I2P. Isso faz com que, mesmo que um invasor possa deduzir um endereço IP de origem, provavelmente não é o responsável pela transação, mas sim o nó externo (I2P) ou de saída (Tor) da rede de sobreposição. Entretanto, essa não é uma solução abrangente, pois redes de sobreposição, VPNs e software similar são proibidos em muitos países, e esperar que todos usem, sincronizem e se propagem nessas redes é irreal. É preciso haver uma solução que não exija o uso de software e redes externos; um que está disponível para a pessoa comum.   
  
Esta solução é o Dandelion ++ (DPP), que é um protocolo atualizado para a proposta original do Dandelion para Bitcoin. Neste protocolo, existem duas fases, a fase tronco e a fase fluff; os dois juntos representam a forma de um dente-de-leão.   
  
Na fase do tronco, a cada poucos minutos, o nó de envio escolhe aleatoriamente dois pares de todos os nós aos quais está conectado. Quando o nó de envio envia uma transação, por conta própria ou apenas encaminhar a transação de outro nó na fase-tronco, ele escolhe aleatoriamente um desses dois pares selecionados e envia a transação para ele.   
  
A fase de cotão é quando um nó recebe uma transação e a transmite a todas as conexões de saída, e não apenas a uma escolhida aleatoriamente, isso permite a verdadeira propagação da transação. A cada poucos minutos, um nó se define como aquele que se propaga aleatoriamente via haste ou buço, de modo que uma fase tronco pode ser bastante longa se cada nó de conexão se definiu como um nó tronco, mas assim que a transação atinge a fase buço, fica lá.   
  
Isso significa que um invasor não poderá mais simplesmente escutar a direção de uma transação, porque antes de ser propagada para todos, passava pela fase-tronco, e o nó de origem da fase de cotão não é o nó de origem da transação. , e não se sabe quantos saltos ao longo do tronco a transação foi submetida.   
  
Obviamente, combinar as soluções acima (DPP mais uma rede de sobreposição) fornecerá garantias ainda mais fortes de privacidade e proteção contra rastreamento de IP. Também deve ser observado que o DPP não se defende contra outra forma de ataque de rastreamento de rede que pode ser feito com os ISPs, mas isso está além do escopo deste artigo.   
  
O Dandelion ++ está definido para entrar em operação na rede Monero e ser usado por padrão no cliente de referência, na versão 0.16. Essa pequena alteração mitigará ainda mais os ataques possíveis na rede Monero e exemplifica por que a Monero lidera o grupo em tecnologias práticas e aplicadas de privacidade.

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

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx)/

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better)/