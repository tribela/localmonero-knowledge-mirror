---
title: "Ver tags: Como um byte reduzirá o tempo de sincronização da carteira Monero em mais de 40%."
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Uma das reclamações mais comuns ao usar Monero no dia-a-dia é o tempo que pode levar para sincronizar uma carteira antes de poder enviar Monero. Felizmente, os desenvolvedores e pesquisadores da comunidade Monero encontraram uma maneira brilhante de reduzir o tempo que leva para sincronizar sua carteira em mais de 40% sem nenhum inchaço adicional da cadeia de bloqueios, taxas, etc.

Digite "view tags", uma adição de um byte aos dados de cada transação - chegando a Monero na próxima atualização da rede!

## Por que a sincronização da carteira de Monero é mais lenta do que a de Bitcoin?

## Por que a sincronização da carteira de Monero é mais lenta do que a de Bitcoin?

Uma das primeiras perguntas que temos que responder para entender melhor a necessidade de uma solução como as etiquetas de visualização é porque a sincronização da carteira de Monero é mais lenta que as moedas criptográficas como Bitcoin.

Em Bitcoin, como todas as transações não são privadas e revelam as moedas que estão sendo gastas, os montantes e os endereços envolvidos na cadeia, as carteiras Bitcoin podem simplesmente procurar por qualquer saída de transação não gasta (UTXOs) ou endereços usados para uma determinada carteira, escaneando rapidamente a cadeia de bloqueio por apenas UTXOs pertencentes a esses endereços para descobrir quais moedas pertencem à sua carteira e podem ser gastas.

Em Monero, entretanto, todas as transações preservam a privacidade do usuário ao esconder o remetente, o receptor e os valores envolvidos em cada transação. Esta privacidade, embora vital para proteger os usuários da rede, também introduz uma sincronização mais lenta da carteira. Em Monero, sua carteira tem que comparar cada saída de transação (TXO) que existe na rede com as chaves privadas de sua carteira.

Esta comparação envolve muita matemática e criptografia complexa para validar que uma saída é realmente sua, já que todas as quantidades, endereços e saídas (ou moedas) gastas conhecidas estão escondidas na cadeia em Monero.

## O que são etiquetas de visão?

## O que são etiquetas de visão?

Como uma forma de ajudar a reduzir o tempo de sincronização das carteiras Monero, [um pesquisador chamado UkoeHB criou uma nova abordagem](https://github.com/monero-project/research-lab/issues/73) \- adicionar uma "tag" de 1 byte a cada transação usando um segredo compartilhado conhecido apenas pelo remetente e receptor dessa transação.

Este segredo compartilhado é gerado pelo remetente usando o endereço fornecido pelo destinatário, e não requer nenhuma colaboração ativa do remetente e do destinatário. O primeiro byte (ou caráter) deste segredo compartilhado é então adicionado aos dados da transação ao publicá-los na rede Monero.

Quando um dos participantes dessa transação quer sincronizar sua carteira com a cadeia de bloqueio Monero depois, em vez de precisar executar toda a matemática e criptografia complexa de cada TXO da rede, a carteira pode agora apenas verificar aquele campo de 1 byte em cada transação e só então executar a verificação demorada nas transações que têm aquela tag - 1/256 TXOs na rede, para ser mais preciso!

Esta etiqueta não revela nenhuma informação sobre a transação para espectadores externos, apenas adiciona 1 byte (uma quantidade insignificante) aos tamanhos da transação, e ainda nos permite reduzir os tempos de sincronização em mais de 40%, cortando as complexas verificações necessárias!

## Ver tags: um exemplo simplificado

## Ver tags: um exemplo simplificado

Imagine que você tem 4.096 caixas em uma sala, das quais apenas 5 caixas pertencem a você. As caixas são todas totalmente indistinguíveis do exterior, e a única maneira de saber se uma caixa é para você é abri-la e resolver um problema matemático demorado escrito por dentro para garantir que seja sua.

Agora, imagine que você decide que a pessoa que lhe envia essas 5 caixas gere um código especial usando seu endereço, e depois coloque apenas o primeiro caractere desse código gerado na parte externa de cada caixa que lhe é enviada. Todos os outros fazem a mesma coisa para suas caixas (para garantir que todas as caixas ainda sejam indistinguíveis), mas agora você pode simplesmente olhar para o código de um caractere no exterior da caixa, e abrir apenas as caixas que têm esse caractere nelas.

Enquanto outras caixas corresponderão ao seu código, mesmo algumas que não são de sua propriedade, o número de caixas que você precisa abrir e resolver um problema matemático agora é de apenas 16 (1/256 caixas!) em vez de todas as 4.096.

Agora você abre essas 16 caixas, resolve os problemas de matemática e mantém as 5 caixas que realmente pertencem a você desse grupo!

## Quando as etiquetas estarão disponíveis em Monero?

## Quando as etiquetas estarão disponíveis em Monero?

Ver tags são uma das características atualmente planejadas para inclusão na [próxima atualização da rede](https://github.com/monero-project/meta/issues/630). e deve ser lançado algum tempo nesta primavera. A comunidade [elevou 23,3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (no momento de escrever) para incentivar o desenvolvimento e a implementação de view tags, e como resultado, a grande maioria do trabalho para incluir view tags na base de código Monero já foi concluída por j-berman em colaboração com revisores e pesquisadores.

Uma vez que as etiquetas de visualização sejam aplicadas pela rede, todas as transações enviadas após a atualização da rede serão beneficiadas pelo tempo de sincronização da carteira drasticamente melhorado. Você não precisará fazer nada especial para começar a usar as etiquetas de visualização, sua carteira favorita para Monero simplesmente começará a usá-las após a atualização automática da rede!

## Como posso aprender mais?

## Como posso aprender mais?

Se isto despertou sua curiosidade em torno das tags de visão, dê uma olhada abaixo para alguns links adicionais que aprofundam o tópico:

  * [Reduzir os tempos de varredura com 'view tag' de 1 byte por saída](https://github.com/monero-project/research-lab/issues/73). 
  * [Adicionar etiquetas de visualização às saídas para reduzir o tempo de digitalização de carteiras](https://github.com/monero-project/monero/pull/8061)

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies)/

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por que (e como!) você deve segurar suas próprias chaves](/knowledge/hold-your-keys)/

  * [Contribuindo de volta para Monero](/knowledge/contributing-to-monero)/

  * [Como os nós remotos impactam a privacidade de Monero](/knowledge/remote-nodes-privacy)/

  * [Como Monero usa o hard-forks para atualizar a rede](/knowledge/network-upgrades)/

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

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx)/

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better)/

Leitura adicional