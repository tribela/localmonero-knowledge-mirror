---
title: "Saídas Monero explicadas"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, como outras criptomoedas, usa saídas como um meio de contabilizar fundos. Muitos usuários experientes em criptografia provavelmente já ouviram esse termo antes, mas nem todos entendem o que ele significa e como funciona. Conforme explorado em nosso [artigo sobre assinaturas de anel](/knowledge/ring-signatures), as saídas são a unidade real trocada no blockchain entre as partes em transação. Semelhante a uma nota de dólar, mas o valor não tem denominação fixa.

Se você receber $ 16 por um trabalho, poderá receber uma nota de um dólar, uma nota de cinco dólares e uma nota de dez dólares. Você tem $ 16, mas também tem três notas diferentes na carteira. Se você quisesse pagar a alguém 6 dólares, poderia usar a nota de 5 e 1, mas se quisesse pagar a alguém $ 8, só poderia usar os $ 10 e receber $ 2 em troco. Por último, se você quisesse pagar a alguém $ 14, você teria que usar todas as três notas e receber $ 2 de volta em trocos, mas por um momento, quando você entrega as três notas, não tem dinheiro na carteira até receber o mudar de volta.

Monero funciona de forma semelhante. Suponha que você administre uma loja e faça três vendas de três itens diferentes. Você pode receber 1,5 XMR, 2,25 XMR e 5,25 XMR para um total de 9 XMR, mas também tem três saídas diferentes em sua carteira com as denominações declaradas anteriormente. Assim como com os dólares, você pode querer pagar 3 XMR a alguém. Você poderia usar apenas a saída 5,25 XMR e receber 2.25 XMR de volta com mudança, ou você poderia combinar as saídas 1,5 e 2,25 XMR e obter 0,75 XMR de volta com mudança.

Mas, assim que você envia a transação, as saídas que você usa são colocadas em um estado "bloqueado", o que significa que ficam inacessíveis até que você receba o troco. O protocolo desbloqueia os fundos (ou seja, devolve o troco) após 10 confirmações ou cerca de 20 minutos. Assim como quando você entrega as notas de dólar de sua carteira, você não pode usar o dinheiro novamente até receber o troco de volta do caixa, seu Monero fica inacessível até que você receba o troco.

Vamos voltar ao exemplo de enviar 3 XMR para alguém e usar a saída 5.25 XMR. Agora, enquanto você espera 1,75 XMR de volta à mudança, você não pode usá-lo. Este 1.75 XMR está inacessível para você. Mas você ainda pode usar as saídas 1.5 XMR e 2.25 XMR, já que elas não foram gastas. Voltando ao exemplo do dólar, se você pagou a alguém $ 8, como no exemplo anterior, você não seria capaz de usar os $ 2 que espera em troco até que seja dado a você, mas neste exemplo, você ainda tem um Nota de $ 10 não utilizada em sua carteira. Isso ainda pode ser usado para comprar o que quiser enquanto espera pela mudança. O mesmo com Monero.

Isso costuma ser um ponto de confusão para novos usuários do Monero. Freqüentemente, um usuário pode ter apenas uma saída em sua carteira, recebida de uma bolsa ou de um amigo. Digamos que esta saída seja 20 XMR. Eles não têm outras saídas em sua carteira. Eles agora querem fazer uma doação para duas de suas instituições de caridade favoritas. Eles enviam 5 XMR para a primeira instituição de caridade e ficam confusos porque, embora devam ter 15 XMR restantes, eles não podem enviar imediatamente a próxima doação para a segunda instituição de caridade. Como você deve ter adivinhado, isso ocorre porque o 15 XMR está bloqueado. Não pode ser gasto até que seja devolvido como troco (10 confirmações ou cerca de 20 minutos). Depois que seus fundos forem desbloqueados, eles poderão enviar sua segunda doação.

Apenas para reiterar o ponto, eles não teriam esse problema se tivessem várias saídas, como duas saídas 10 XMR ou semelhantes. Eles seriam capazes de enviar as duas doações uma após a outra, porque a primeira doação usaria uma das 10 saídas de XMR (e esperaria 10 confirmações para receber 5 XMR de volta em troco), e a segunda doação usaria os outros 10 XMR resultado.

Algumas carteiras de criptomoeda têm um recurso chamado 'gerenciamento de saída', que simplesmente mostra ao usuário quais saídas ele tem atualmente (além de sua soma total), bem como permite que ele escolha quais deseja usar quando gastar sua criptomoeda.

A partir de agora, a GUI do Monero faz a seleção de saída para os usuários automaticamente, já que os usuários que selecionam suas próprias saídas costumam causar confusão ou, em alguns casos, prejudicar a privacidade. No entanto, há carteiras em construção, como o novo projeto de carteira Feather, que conterá esses recursos de gerenciamento de saída.

Temos falado muito sobre a parte de envio, mas algo fascinante acontece na extremidade de recepção. Voltando ao nosso exemplo de envio de 3 XMR para alguém e usando suas saídas 1.5 XMR e 2.25 XMR na transação (enquanto esperava 0.75 XMR na mudança), o receptor NÃO recebe duas saídas de 1.5 XMR e 2.25 XMR. Em vez disso, recebem UMA saída 3 XMR.

Em segundo plano, o protocolo combina todas as saídas usadas para gastar e dá ao receptor uma saída da quantia paga e envia uma saída de mudança de volta ao remetente. Portanto, o remetente também receberá uma saída de volta como alteração, independentemente de terem usado duas, três ou dez saídas para enviar a transação.

Esperamos que isso tenha esclarecido alguma confusão sobre os resultados e como funciona a contabilidade interna do protocolo, bem como o problema comum de confusão que o usuário enfrenta ao encontrar fundos bloqueados. Em outro artigo, exploraremos o gerenciamento de seus resultados de modo a minimizar a chance de ter que esperar por fundos desbloqueados antes de enviar transações futuras.

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