---
title: "O que todo usuário Monero precisa saber quando se trata de rede"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Não deve ser surpresa para ninguém que o Monero, e na verdade todas as criptomoedas, é executado na Internet. E ainda, embora esta afirmação pareça básica e óbvia, muitos não consideram as implicações do que isso significa em relação à sua privacidade. Em outras palavras, existem algumas coisas contra as quais o Monero pode e não pode proteger, apenas por ser executado na Internet. Algumas dessas considerações são meros inconvenientes, enquanto outras são muito mais sérias em um cenário onde a privacidade absoluta é necessária. Vamos nos familiarizar com a forma como os usuários do Monero interagem entre si na rede e o que isso significa para sua privacidade.

Começando pelo lado trivial das coisas, se um usuário não tiver acesso à internet, ele não poderá baixar novos blocos, propagar transações em nome de terceiros ou enviar transações por conta própria. Uma coisa interessante a se notar é que um usuário com um nó cheio, sem acesso à internet, pode construir uma transação offline que pode ser enviada posteriormente. Isso ocorre porque uma assinatura de anel só precisa de saídas do blockchain para se esconder. Um breve lembrete sobre [como as assinaturas de anel funcionam](/knowledge/ring-signatures), ele oculta a saída real que um usuário está enviando entre uma coleção de saídas não afiliadas escolhidas no passado. Se o usuário tiver acesso a essas saídas na forma de um blockchain totalmente baixado (nó completo), ele pode criar a assinatura de anel a partir das saídas anteriores e, quando a conectividade com a Internet for retomada, propagar a transação para a rede.

Um usuário que está usando um nó remoto não pode fazer isso, pois quando constrói sua assinatura de anel, ele contata o nó completo remoto para saídas a serem incluídas na assinatura de anel. Sem internet significa que eles não podem alcançar este nó, então eles não têm recursos de construção de transações offline.

Antes de continuarmos em algumas das considerações de privacidade, vamos dar uma breve introdução sobre como a Internet funciona como um todo. Toda a Internet nada mais é do que computadores conectados a outros computadores. É isso aí. O blog que você gosta de ler? Apenas alguns arquivos hospedados no computador de outra pessoa. Qual site você está lendo este artigo (LocalMonero)? Arquivos e códigos hospedados em um computador em algum lugar. Mesmo os grandes sites malucos funcionam assim. Veja o YouTube, por exemplo. Apenas arquivos de vídeo hospedados nos gigantescos sistemas de computador do Google, e você se conecta a eles para baixar o vídeo em seu próprio computador para poder assisti-lo.

Esses computadores podem se diferenciar porque cada computador conectado à Internet recebe um número de identificação exclusivo chamado endereço IP. Normalmente, são quatro conjuntos de números separados por pontos, por exemplo: 172.66.35.7. É importante manter isso em mente ao considerar como as informações do Monero são movidas pela Internet. Monero é uma rede ponto a ponto (P2P), o que significa que os computadores se conectam diretamente entre si, em vez de usar um intermediário. Portanto, quando o nó completo de um usuário está baixando um bloco recém-descoberto, eles não o estão baixando de um servidor central, mas de seus pares. A desvantagem disso é que, como os usuários se conectam diretamente uns aos outros, eles conhecem os endereços IP uns dos outros.

Bem? Qual é o problema? É apenas um número, certo? Não exatamente. Os próprios endereços IP contêm informações sobre o usuário, como o país de origem e o provedor de rede, mas, pior ainda, os provedores de serviços de Internet (ISPs) sabem o endereço IP de cada pessoa que usa seus serviços. Isso significa que esses ISPs e aqueles com quem trabalham podem observar o tráfego de um usuário na Internet e, usando algumas táticas inteligentes, descobrir que estão usando o Monero. Agora, antes de ficar com medo, observe as palavras ali. Tudo o que esses bisbilhoteiros podem fazer é ver se uma pessoa está se conectando a outros nós da rede Monero. Por causa da tecnologia de privacidade do Monero, nada mais é divulgado sobre o indivíduo. Não se eles estão ou não executando um nó, ou se / quando eles enviam transações, e se uma transação é enviada, nenhuma de suas informações é conhecida. Tudo o que esses ISPs podem ver é que um de seus usuários está se conectando à rede Monero.

Agora, para algumas pessoas, em alguns locais, esta informação por si só pode ser suficiente para causar danos à reputação ou à liberdade. Ou talvez a ideia de alguém invadir sua privacidade e o que você faz na internet, por qualquer motivo, não seja aceitável para você. Esses indivíduos são encorajados a se conectar apenas à rede Monero usando VPNs, Tor ou I2P, todos os quais são serviços que ocultam o endereço IP de um usuário de outros, bem como ocultam o que um usuário está fazendo de seu ISP. As diferenças entre esses serviços estão além do escopo deste artigo, mas há muitos artigos de alta qualidade escritos sobre o assunto, então os usuários preocupados são incentivados a estudar!

Para o resto de nós, podemos pensar que não é grande coisa ter outras pessoas sabendo que estamos conectados à rede Monero. Afinal, o conteúdo real de nossas transações, ou se estamos enviando algum, está oculto ao público, então qual é o problema? Embora isso possa ser verdade, os usuários são incentivados a considerar o fato de que a principal atração das criptomoedas é ser seu próprio banco. Quando você segura sua chave privada e se algo acontecer com ela, ninguém pode ajudá-lo a recuperar seus fundos perdidos.

Ser seu próprio banco significa considerar não apenas sua segurança digital, mas também sua segurança física. Pode muito bem ser que o conhecimento de um indivíduo se conectando à rede Monero possa atrair atenção indesejada, não necessariamente de atores em grande escala como Estados-nação, mas de atores menores com interesses egoístas, como hackers que procuram ganhar dinheiro fácil. De fato, existem inúmeras histórias em todo o espaço criptográfico de tais cenários realmente ocorrendo.

Este artigo não tem como objetivo fomentar ou assustar, mas sim encorajar os usuários a pesquisarem quais métodos de proteção de navegação na web são adequados para eles. A boa notícia é que essas habilidades também serão transferidas para o uso geral da Internet, não apenas para o uso do Monero e, como tal, em nosso mundo cada vez mais conectado à Internet, um usuário experiente não pode errar ao acumular o conhecimento e as habilidades adequadas para se manter seguro e ser verdadeiramente seu próprio banco.

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