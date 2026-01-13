---
title: "Seraphis: O que fará por Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: uma atualização de projeto modular para transações Monero

## Seraphis: uma atualização de projeto modular para transações Monero

Seraphis

## Transações em Monero

## Transações em Monero

Protocolos como Bitcoin e Monero e outros contam com um chamado "modelo de saída" de operação, onde uma _saída_ é uma representação de valor que pode ser transferida.  
As transações consomem uma ou mais saídas controladas por um remetente e geram novas saídas direcionadas aos destinatários (ou de volta ao remetente como troco); a transação deve equilibrar em que as saídas consumidas devem conter um valor total exatamente igual ao valor das novas saídas (mais uma taxa imposta pela rede).  
Em muitos protocolos como o Bitcoin, o valor contido em uma saída é escrito de forma clara, assim como o destinatário.  
Além disso, olhando para o blockchain, é trivial ver se e quando uma saída foi gasta (ou seja, se foi consumida em uma transação posterior e qual transação a gastou).

Por outro lado, protocolos como Monero apresentam um design diferente:

  * Os valores de saída estão ocultos e não visíveis no blockchain
  * Os endereços de destinatários estão ocultos pelo uso de um protocolo de endereçamento único
  * Se uma saída foi gasta ou não é obscurecido pelo uso de assinaturas ambíguas

O resultado é que, na ausência de informações externas, é difícil determinar se uma determinada saída foi gasta, qual é seu valor e quem é seu destinatário.

O protocolo de transação atual do Monero é chamado _RingCT_ e usa vários blocos de construção criptográficos para atingir esses objetivos de design.

  * _Compromissos_ ocultam valores de maneira matematicamente útil
  * _Provas de intervalo_ evitam estouro que pode inflar a oferta
  * _Assinaturas em anel vinculáveis_ fornecem ambiguidade ao signatário e evitam tentativas de gastos duplos
  * _Compensações de compromisso_ confirmam que as transações equilibram

Esses blocos de construção são cuidadosamente entrelaçados para construir o protocolo RingCT.

Uma propriedade útil do protocolo RingCT é que alguns componentes básicos podem ser alterados ou atualizados de forma a manter o design geral e as propriedades intactas, mas que pode fornecer melhorias de eficiência ou segurança. Na verdade, esses tipos de atualizações ocorreram (ou estão planejados para ocorrer) várias vezes na história do Monero. As provas de alcance no protocolo RingCT original eram volumosas e lentas; eles foram posteriormente atualizados para uma construção chamada [Bulletproofs](https://eprint.iacr.org/2017/1066) que tornou as transações menores e mais rápidas com melhor análise de segurança, e estão planejadas para serem atualizadas para uma construção mais recente chamada [Bulletproofs+](https://eprint.iacr.org/2020/735) para benefícios de eficiência ainda maiores.

Um processo semelhante foi realizado com o bloco de construção de assinatura em anel vinculável. No protocolo original, foi usada uma construção chamada [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) . Isso foi posteriormente atualizado para uma construção mais recente chamada [CLSAG](https://eprint.iacr.org/2019/654) que é mais rápida, resulta em transações menores e tem melhor análise de segurança. Uma construção de assinatura de anel vinculável ainda mais nova baseada em [Triptych](https://eprint.iacr.org/2020/018) foi proposta, mas isso não foi selecionado para implantação devido a seus impactos nas operações de multiassinatura.

## Seraphis

## Seraphis

Seraphis leva esta idéia um passo adiante.  
Em vez de atualizar blocos de construção individuais do protocolo de transações RingCT existente, ele introduz um protocolo diferente que pode tirar proveito de blocos de construção diferentes e oferecer uma funcionalidade melhorada.

## Blocos de construção

## Blocos de construção

A Seraphis usa um conjunto diferente de blocos de construção criptográficos para alcançar seus objetivos de projeto.

  * _Compromissos_ ainda escondem quantidades
  * _As provas de alcance_ ainda impedem o transbordamento e a inflação de fornecimento
  * _As provas de associação_ fornecem ambigüidade do signatário
  * _Compensações de compromisso_ ainda afirmam equilíbrio
  * _As provas de autorização_ evitam tentativas de gasto duplo

Observe a mudança aqui: as assinaturas de anéis de ligação são substituídas por uma combinação de provas de associação e provas de autorização. Grosso modo, as provas de associação mostram que uma produção consumida faz parte de um conjunto maior, semelhante ao que acontece no RingCT. Mas, ao contrário do RingCT, as provas de associação não envolvem de forma alguma a etiqueta de vinculação! As provas de autorização mostram que a etiqueta de vinculação é válida e é usada para assinar a transação final.

Como o RingCT faz a ligação da tag na assinatura ambígua, as operações de assinatura (e multisignature) são mais intensivas em termos computacionais, e torna-se mais desafiador construir outras funcionalidades relacionadas à tag. Mas no Seraphis, a construção de provas de associação pode ser delegada com segurança de dispositivos altamente confiáveis (que podem ter um poder computacional limitado, como uma carteira de hardware) a um dispositivo menos confiável, e as operações de assinatura (e multisignature) são muito mais fáceis usando a prova de autorização muito mais simples.

Felizmente, alguns dos blocos de construção exigidos pela Seraphis já existem em outros lugares e não precisam ser projetados a partir do zero. Tanto as construções Bulletproofs como Bulletproofs+ podem ser usadas como provas de alcance. Modificações nos sistemas de prova tipo Schnorr podem ser usadas para autorizar provas. E um eficiente sistema de prova [](https://eprint.iacr.org/2015/643) usado já como base para o Tríptico, [Lelantus](https://eprint.iacr.org/2019/373)e [Centelha](https://eprint.iacr.org/2021/1173)* pode ser modificado para prova de associação.

* Cypher Stack recebe financiamento para o desenvolvimento da Spark.

## Endereçando

## Endereçando

Infelizmente, os endereços Monero atualmente em uso não são compatíveis com o Seraphis. Os usuários precisariam gerar novos endereços a partir de suas chaves de carteira para receber o Monero se o Seraphis fosse implementado. No entanto, este custo do ecossistema vem com uma série de benefícios.

Além dos benefícios estruturais discutidos acima, o projeto do Seraphis é passível de muitas possibilidades de construção de endereços diferentes, cada uma das quais vem com tradeoffs. Enquanto a construção do endereço final a ser usado no Seraphis está [ainda sendo decidida](https://github.com/monero-project/research-lab/issues/92) . (um esquema que recebe muita atenção é chamado [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), podemos descrever algumas características comuns e úteis.

Você deve saber que os endereços Monero oferecem a funcionalidade _view key_ , onde você pode fornecer uma chave de visualização para um dispositivo ou terceiro e permitir que ele observe as saídas recebidas em seu nome, mas sem abrir mão da autoridade de gastos. Isto é útil para carteiras, que podem permanecer atualizadas enquanto mantém sua chave de gastos trancada com segurança. Também é útil para os casos em que você deseja acesso de visão externa, como uma instituição pública de caridade oferecendo transparência ou uma empresa com um departamento de contabilidade.

A desvantagem das teclas de visão Monero é que elas não fornecem acesso à visão completa ou de granulação fina. Não é possível detectar de forma confiável quando uma carteira gasta fundos, o que dificulta o cálculo correto dos saldos da carteira quando a chave de gasto não está disponível. Também não é possível atualmente detectar as saídas recebidas sem também aprender o valor contido nessas saídas (o que significa que qualquer terceiro responsável por encontrar as saídas recebidas aprenderá exatamente quanto Monero você está adquirindo).

Seraphis endereçando construções pode resolver isto. Com o Seraphis, seu endereço vem equipado com chaves diferentes que podem fazer coisas diferentes:

  * Cuidado com as saídas recebidas, mas esconda seu valor
  * Preste atenção às saídas recebidas, mas mostre seu valor
  * Cuidado com as saídas
  * Ajudá-lo a gerar transações, mas não assiná-las
  * Gerar novos endereços (úteis para varejistas ou trocas com muitos clientes)

Como detentor do endereço, você decide quanta autoridade você delega a outros dispositivos ou a terceiros.

## O quadro geral

## O quadro geral

O Seraphis é uma grande mudança no ecossistema Monero. Embora envolva modificações nos endereços e blocos de construção de transações, seu projeto oferece flexibilidade e funcionalidade útil que não são possíveis com o protocolo RingCT de hoje. Enquanto grande parte do projeto está finalizado e sendo desenvolvido em [uma implementação](https://github.com/UkoeHB/monero/tree/seraphis_lib). A análise de segurança e o projeto do endereço estão em andamento. Seraphis oferece uma excelente oportunidade para impulsionar o ecossistema Monero!

Leitura adicional

  * [Como Monero permite de forma única economias circulares](/knowledge/monero-circular-economies)/

  * [Assinaturas do anel de Monero vs CoinJoin como em Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Por que (e como!) você deve segurar suas próprias chaves](/knowledge/hold-your-keys)/

  * [Contribuindo de volta para Monero](/knowledge/contributing-to-monero)/

  * [Como os nós remotos impactam a privacidade de Monero](/knowledge/remote-nodes-privacy)/

  * [Como Monero usa o hard-forks para atualizar a rede](/knowledge/network-upgrades)/

  * [Ver tags: Como um byte reduzirá o tempo de sincronização da carteira Monero em mais de 40%.](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool e seu papel na descentralização da mineração Monero](/knowledge/p2pool-decentralizing-monero-mining)/

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