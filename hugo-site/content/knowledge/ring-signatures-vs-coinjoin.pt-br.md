---
title: "Assinaturas do anel de Monero vs CoinJoin como em Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Como as ferramentas de privacidade Bitcoin ganharam mais atenção e uso, elas passaram a estar mais sob escrutínio regulatório. Este exame levou a um [recente anúncio](https://twitter.com/wasabiwallet/status/1503091503207432193) por uma ferramenta de privacidade Bitcoin, Wasabi Wallet, de que eles começarão a censurar e rejeitarão entradas para misturar que eles consideram ilícitas ou contra seus ToS, e pagarão uma empresa de análise de cadeia para "vetar" as entradas dos participantes da mistura.

O uso de transações CoinJoin para ofuscar a fonte de fundos no Bitcoin tem sido o núcleo da privacidade do Bitcoin há muitos anos, e as questões e riscos inerentes ao seu uso são algumas das questões centrais que as assinaturas do anel de Monero corrigem e evitam.

Neste post de blog vamos mergulhar brevemente em uma comparação de CoinJoin e assinaturas de anéis, assim como a razão pela qual a abordagem adotada em Monero leva a uma maior resistência à censura, maior privacidade e menos aborrecimentos para os usuários.

## O que é uma transação de CoinJoin?

Como todas as transações são completamente transparentes em Bitcoin - revelando o remetente, o receptor e os valores - os usuários devem tomar medidas extras para preservar sua privacidade de remetentes anteriores e futuros destinatários de seus fundos ou arriscar a censura, vigilância ou roubo de fundos através de violência física.

A melhor solução hoje para a privacidade no Bitcoin é uma ferramenta chamada [. "CoinJoin"](https://bitcoiner.guide/qna/coinjoin/)A partir de então, a empresa tem uma rede de escritórios, onde 2 ou mais usuários trabalham juntos (geralmente através de um coordenador centralizado) para criar uma transação especial que dificulta a conexão das entradas com as saídas por parte de observadores externos. Cada participante se comunica para construir conjuntamente a transação sem ceder a custódia de seus fundos, e recebe uma saída no final cujo histórico anterior agora não está claro (ou ofuscado) para observadores externos.

Isto quebra a história de UTXOs específicos, permitindo que os usuários de Bitcoin ganhem um pouco de segurança na hora de fazer transações. Entretanto, o CoinJoin (como implementado no Wasabi Wallet e no Samourai Wallet, as duas ferramentas CoinJoin mais utilizadas para Bitcoin) tem alguns grandes inconvenientes:

  * Como as transações CoinJoin são completamente opt-in e requerem participação ativa, qualquer participante necessariamente mostra que busca maior privacidade do que a dos usuários "normais" de Bitcoin, potencialmente os destacando e causando problemas de gastos de fundos em muitas bolsas ou entidades regulamentadas. Cada usuário não pode negar que participou de uma transação de CoinJoin.
  * A fim de encontrar outros para o CoinJoin, a maioria das abordagens ao CoinJoin (incluindo a Carteira Wasabi) utiliza um coordenador centralizado que conecta os participantes e os ajuda a se comunicar e construir uma transação CoinJoin adequada. Este coordenador centralizado nunca tem a custódia dos fundos dos usuários, mas ganha uma ampla visão das transações que eles coordenam, pode censurar entradas (como no caso da Carteira Wasabi), e pode ser pressionado a coletar ou compartilhar informações sobre os participantes do CoinJoin.
  * Os usuários com grandes quantidades de fundos para o CoinJoin podem frequentemente ter que esperar horas (ou mesmo dias!) para encontrar participantes suficientes para o CoinJoin, levando a grandes atrasos desde o momento em que um usuário recebe fundos até quando pode gastá-los privadamente.
  * A privacidade proporcionada por uma transação CoinJoin se degrada com o tempo à medida que outros participantes gastam fundos ou vinculam seus resultados à sua identidade através de trocas KYC, identidade que exige comerciantes, etc. Isto significa que o ideal é que os usuários mantenham seus fundos constantemente agitados nas transações de CoinJoin para manter seu anonimato ("multidão para se esconder") o mais fresco possível.
  * Na maioria das abordagens do CoinJoin, os participantes devem usar um UTXO de tamanho fixo (ou seja, 0,1 BTC) para tornar mais difícil a conexão de entradas e saídas de transações de CoinJoin. Isto leva a taxas mais altas (mais transações separadas necessárias por grande entrada), mais "mudança tóxica" (fundos que não podem ser gastos sem sérios riscos à privacidade), e pode impedir que usuários menores possam se misturar se não tiverem o saldo mínimo exigido.

## Como as assinaturas de anéis resolvem esses problemas?

Como [, analisamos profundamente quais são as assinaturas de anel nos últimos](/knowledge/ring-signatures), não entrarei em detalhes sobre os aspectos técnicos de como eles funcionam neste post no blog. Em vez disso, veremos como as abordagens tomadas em Monero resolvem os problemas com o CoinJoin discutidos acima.

> CoinJoin é opt-in e requer participação

CoinJoin é opt-in e requer participação

as assinaturas do anel do Monero são uma característica central do protocolo de privacidade, e _cada transação_ na rede as usa. Isso significa que nenhuma transação de usuário se destaca por buscar maior privacidade do que os usuários "normais" do Monero, e todos os usuários ganham negação plausível de que eles gastaram fundos em qualquer transação. Como os fundos de gastos do usuário não coordenam ou participam com os insumos de isca em uma transação, aqueles usuários que possuem insumos que por acaso são selecionados como isca podem dizer honestamente que não estavam participando dessa transação, fortalecendo sua privacidade.

> Uso de um coordenador centralizado

Uso de um coordenador centralizado

Como as assinaturas do anel de Monero são totalmente não coordenadas e exigem apenas o verdadeiro gastador de recursos para criar a transação, não há necessidade de um coordenador centralizado em Monero. Isso garante que _ninguém_ possa negar acesso à privacidade em Monero, e não há nenhuma entidade centralizada que possa ser pressionada, nenhum ataque fácil da Sybil à liquidez, etc. Desde que sua transação pague as taxas adequadas, você ganha acesso sem censura à privacidade, segurança e anonimato em Monero.

> CoinJoin requer liquidez

CoinJoin requer liquidez

A "liquidez" disponível para quem gastar o Monero para usar como isca é sempre o conjunto total de saídas em cadeia, então nunca há escassez de isca para se esconder com o Monero. Alguém que procura gastar o Monero pode fazê-lo ~20min depois de receber fundos, e não precisa realizar quaisquer etapas adicionais para ganhar forte privacidade em Monero.

> a privacidade do CoinJoin degrada-se com o tempo

a privacidade do CoinJoin degrada-se com o tempo

Como as saídas do Monero nunca são conhecidas pela rede, a privacidade fornecida pelas assinaturas de anel é muito menos suscetível à degradação ao longo do tempo. Um usuário não precisa constantemente agitar saídas em Monero, e fora de circunstâncias extremamente raras, não perde privacidade com o passar do tempo.

Se um usuário quiser "atualizar" as iscas usadas com uma saída, no entanto, ele pode simplesmente enviar os fundos de volta para si mesmos e ser capaz de gastá-los ~20min mais tarde, como de costume.

> CoinJoin geralmente requer entradas de tamanho fixo

CoinJoin geralmente requer entradas de tamanho fixo

Como os valores estão escondidos em cada transação usando ["Transações Confidenciais"](/knowledge/monero-ringct) (uma parte do "RingCT"), as iscas usadas em qualquer transação podem ser de qualquer tamanho. Não há razão para se preocupar com a heurística baseada em quantidade em Monero, e por isso as transações são muito mais simples de construir e podem alavancar isca de qualquer ponto no tempo e de qualquer quantidade na blockchain Monero.

## Como posso aprender mais?

Se você estiver curioso e quiser entender melhor as assinaturas de anéis ou as transações de CoinJoin, veja os links abaixo para obter excelentes lugares para começar:

  * [Como as assinaturas de anéis obscurecem as saídas de Monero](/knowledge/ring-signatures)
  * [Assinatura do Anel - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Visão geral do CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies/)

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