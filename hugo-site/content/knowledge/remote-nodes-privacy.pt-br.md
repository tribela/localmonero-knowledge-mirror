---
title: "Como os nós remotos impactam a privacidade de Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Uma das maiores vantagens que o Monero tem sobre outras criptomoedas é a privacidade na cadeia, mas você já se perguntou como a privacidade do Monero se mantém quando você usa um nó remoto? Que tal se você usar um servidor de “carteira leve” como o MyMonero?

Nesta postagem, vamos mergulhar em alguns detalhes por trás de como o Monero fornece privacidade na cadeia excepcional mesmo ao usar um nó remoto, bem como o que observar ao usar nós remotos.

## Qual é a função dos nós em Monero?

Para aqueles menos familiarizados com o funcionamento de Monero, os nós (ou servidores) da rede Monero podem ser executados por qualquer pessoa e permitir que o proprietário do nó - ou outros com quem eles escolham compartilhá-lo! - para sincronizar uma cópia da cadeia de bloqueio e fornecer essa cópia a outros na rede. Estes nós também verificam todas as transações que ocorrem na rede, assim como todos os blocos que são publicados e garantem que todos eles sigam as regras estabelecidas por consenso.

A outra função que os nós servem em Monero é como uma forma de fornecer todos os dados que sua carteira Monero favorita precisa para verificar corretamente as transações que lhe pertencem e fazer novas transações. Estes dados são fornecidos pelos nós de duas maneiras:

  * Os dados de cada bloco da cadeia de bloqueio são solicitados pela carteira, escaneados para transações pertencentes a você, e depois descartados uma vez verificados pela carteira. 
    * Este passo será drasticamente melhorado em breve, graças às etiquetas de visualização [](/knowledge/view-tags-reduce-monero-sync-time).
  * Ao enviar transações, o nó que você utiliza fornece uma lista de possíveis engodos (ou entradas falsas) para usar ao construir a transação, garantindo que você tenha uma boa multidão para se esconder em cada vez que passar Monero. 
    * Estes chamarizes fazem parte das assinaturas dos anéis [](/knowledge/ring-signatures)Uma parte importante da abordagem de Monero em relação à privacidade na cadeia.

## Qual é a maneira mais privada e segura de usar Monero?

A melhor coisa a fazer, mesmo com a forte privacidade na cadeia fornecida por Monero ao usar nós remotos, é rodar seu próprio nó Monero para garantir que você tenha uma cópia intacta da cadeia de bloqueio Monero à mão e que seu endereço IP esteja bem protegido. O outro benefício ao rodar seu próprio nó é que você pode contribuir de volta à rede, permitindo que outros nós se sincronizem a partir de seu nó ou mesmo permitindo que outros usuários se conectem a seu nó com suas carteiras.

Dito isto, Monero ainda proporciona excelente privacidade ao utilizar um nó remoto. Se você estiver interessado em administrar seu próprio nó Monero, aqui está um guia fácil de seguir para fazer isso:

  * [Executar um Nó Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## O que um nó remoto pode aprender sobre mim?

Ao usar um nó remoto, há algumas informações importantes que são expostas a um nó remoto e algumas maneiras principais pelas quais o nó pode atacá-lo, impedir que você faça transações e muito mais.

A primeira coisa que um nó remoto pode aprender sobre você é seu endereço IP público. Embora isso seja ocultado por meio de uma VPN ou Tor, o nó remoto pode associar seu endereço IP público à transação, ajudando-os a restringir de onde você está fazendo a transação. O nó remoto também pode aprender o último bloco que sua carteira sincronizou e usar isso para tentar fazer suposições educadas sobre você, como quando você normalmente usa o Monero e quando gastou o Monero pela última vez. Isso é especialmente verdadeiro se você estiver sempre vindo do mesmo endereço IP (como sua casa). A última coisa importante que um nó remoto pode aprender sobre você são informações básicas sobre as transações que você envia por meio dele. Embora esses possam ser os dados mais óbvios que o operador de nó remoto obtém sobre você, é importante entender que isso pode ser usado para ajudar a rastrear o remetente da transação ao combinar essas informações com outros dados fora da cadeia. Isso pode ser especialmente perigoso se o nó remoto for executado por uma entidade maliciosa, uma empresa de análise de blockchain ou um estado-nação opressivo.

Um nó remoto também pode tentar causar problemas ocultando blocos de você, fazendo sua carteira pensar que foi sincronizada quando não estava. Isso pode fazer você pensar que os fundos estão perdidos ou impedir que você gaste fundos até se conectar a outro nó. A última coisa importante que um nó remoto pode fazer é alimentar sua carteira com uma lista manipulada de iscas. Isso pode fazer com que sua carteira falhe completamente ao criar transações (tornando você incapaz de gastar fundos) ou pode permitir que o nó remoto tente fornecer iscas que ele sabe que são gastas para reduzir o anonimato que você recebe em cada transação.

## Que garantias de privacidade ainda existem quando se usa um nó remoto?

Embora este artigo possa tê-lo assustado um pouco, é importante perceber que a privacidade proporcionada por Monero é excelente mesmo quando se usa um nó remoto, e ultrapassa de longe qualquer outra moeda criptográfica quando usada desta forma. Você ainda ganha a forte privacidade na cadeia fornecida por Monero, pois o nó remoto nunca sabe a verdadeira entrada (que moedas você está gastando), a quantidade de Monero gasta na transação, ou o endereço do destinatário da transação. Observadores externos também não podem ver a verdadeira entrada, quantidade ou endereços envolvidos (não importa o tipo de nó que você escolher usar!), garantindo que fora do nó remoto até mesmo seu endereço IP, informações de sincronização de carteira e transações tenham fortes garantias de privacidade.

O nó remoto também nunca tem acesso às transações anteriores que você enviou ou recebeu ou à quantidade de Monero atualmente em sua carteira, e perde toda a visibilidade em suas transações no momento em que você começa a usar outro nó. Nenhuma chave privada (seja gasta ou de visualização) é fornecida ao nó remoto, e assim sua carteira permanece privada, segura e utilizável. Não importa o nó remoto, você também nunca corre o risco de perder Monero ou de tê-lo roubado, pois o nó não pode editar o endereço do destinatário, nunca tem acesso às suas carteiras de chaves privadas e não pode confiscar seu Monero de nenhuma forma.

## Que tal "carteiras leves" como MyMonero?

Embora o tema esteja um pouco fora do escopo deste artigo, eu queria abordar um tipo único de carteira em Monero - carteiras leves. O nome carteira leve vem do fato de que sua carteira (em seu telefone ou computador) não precisa realizar nenhuma das sincronizações da cadeia de bloqueio, tornando a experiência mais rápida e fluida.

Entretanto, carteiras como esta vêm com uma severa troca de privacidade por enquanto - sua carteira envia a chave de visão privada para o servidor remoto que você usa (como o padrão no MyMonero), dando ao servidor remoto total visibilidade sobre qualquer fundo recebido desde a criação de sua carteira (e até que você pare de usar essa carteira ou semente). Isto reduz drasticamente a privacidade que você recebe do operador do nó, e deve ser abordado com cautela.

Felizmente, a comunidade Monero está trabalhando para melhorar o software que você pode usar para hospedar seu próprio Light Wallet Server (LWS), o que permitirá que você tenha uma rápida sincronização sem confiar em terceiros com suas chaves de visualização privadas - pois você executará o software para o qual sua carteira envia as chaves de visualização privadas!

Para mais informações sobre o servidor de carteiras leve personalizado, veja o repositório Github abaixo:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Como posso aprender mais?

Se você está curioso e gostaria de entender melhor os nós em Monero e procurar usar um nó remoto ou rodar o seu próprio, veja os links abaixo para obter ótimos lugares para começar:

  * [Monero World, uma lista de nós remotos geridos pela comunidade que podem ser utilizados](https://moneroworld.com/#nodes). 
  * [Monero nodes dirigido por Seth For Privacy, o autor deste artigo](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, uma lista de nós remotos com status frequentemente verificado](https://monero.fail/)
  * [Como se conectar a um nó remoto dentro da carteira da GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Nó Remoto](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies/)

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Por que (e como!) você deve segurar suas próprias chaves](/knowledge/hold-your-keys/)

  * [Contribuindo de volta para Monero](/knowledge/contributing-to-monero/)

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