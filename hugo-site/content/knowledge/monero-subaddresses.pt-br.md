---
title: "Como os subendereços do Monero evitam o vínculo de identidade"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero sempre encontrou maneiras inovadoras de resolver difíceis problemas de privacidade. Muitas vezes, essas inovações levam a outras inovações e, às vezes, essas tecnologias resultantes podem até mesmo ser usadas para casos de uso não considerados anteriormente. Em nenhum lugar isso é mais exemplificado do que no caso da tecnologia de subendereço de Monero.

Considere um hipotético problema de privacidade, em que o uso de um endereço em várias plataformas de pessoas aparentemente não relacionadas pode levar à vinculação e à anonimização dessas pessoas. Simplificando, se você fosse uma pessoa chamada Billy Joe Bob e vendesse maçãs por Bitcoin, você poderia postar seu endereço de Bitcoin em um local público para que os clientes paguem a você. Digamos que o endereço comece com a string alfanumérica 7XybV3 ... Mas, deixando de lado o risco óbvio de privacidade de qualquer pessoa poder verificar seu saldo de Bitcoin e ver quanto você vendeu, há um segundo, raramente falado sobre risco de privacidade. Digamos que você também fosse um hacker clandestino chamado l33tz0r. Você faz denúncias, informando a uma população desavisada sobre a corrupção no governo, e é imperativo que você mantenha sua identidade em segredo. Você aceita doações de Bitcoins pelo seu trabalho e publica o endereço em um fórum público. É o mesmo endereço em que você aceita dinheiro de seus clientes da Apple. O 7XybV3 ... um.

Um ataque simples, mas devastador de desanonimização, seria usar um mecanismo de busca da Internet para pesquisar seu endereço Bitcoin. Colocar o endereço de 7XybV3 ... no motor traz dois resultados diferentes. O negócio da maçã e l33tz0r. Isso é o suficiente para ligar as duas identidades e desanonimizar l33tz0r, com consequências potencialmente assustadoras dos poderes constituídos.

É importante notar que este ataque TAMBÉM é possível com o Monero. Embora Monero oculte a maioria dos dados em cadeia, este ataque não usa nenhum. Ele usa apenas o endereço, que deve ser compartilhado para receber o pagamento. Publicamente, no caso de doações anônimas. Esta é uma forma potencial pela qual os usuários do Monero podem involuntariamente prejudicar sua privacidade e também é um exemplo de como, embora o Monero seja o primeiro em relação à retenção de privacidade, ele não é à prova de balas.

A maneira usual de contornar esse problema era possuir várias carteiras. Com endereços diferentes postados para cada identidade (ou caso de uso), eles não podem ser vinculados. Mas essa privacidade só se mantém se o usuário nunca os confundir. A postagem acidental do endereço incorreto teria os mesmos efeitos de ligação. Da mesma forma, o seed de cada endereço deve ser mantido seguro, aumentando o trabalho de infosec necessário a cada nova carteira feita.

A solução de Monero eram subendereços. A capacidade de criar um número absolutamente grande de endereços abaixo do endereço principal, usando-o como uma espécie de semente. Cada subendereço gerado pode aceitar Monero, e tudo vai para a mesma carteira. Usando esse método, o número de identidades que podem ser operadas em um endereço é enorme, ao mesmo tempo em que reduz o trabalho de informação ao mínimo. Esses endereços também não são matematicamente vinculáveis, portanto, a menos que o usuário grite sua conexão com o mundo, um observador externo terá grande dificuldade em vinculá-los.

Mas outro caso de uso interessante emergiu de subendereços; como uma opção de substituição dos IDs de pagamento odiados universalmente.

IDs de pagamento eram uma forma de os comerciantes identificarem qual cliente enviou qual pagamento. Como as informações do Monero são obscurecidas na cadeia, o destinatário de uma transação não consegue ver qual endereço a enviou. Isso significa que, se houver itens com preços semelhantes e vários pedidos, pode ser impossível identificar quem enviou o quê. IDs de pagamento são uma string única e aleatória gerada pelo comerciante e fornecida ao cliente. O cliente adiciona isso como um campo separado ao enviar a transação. Essa string aleatória é colocada no blockchain como parte da transação e, dessa forma, o comerciante é capaz de identificar e classificar as transações recebidas.

Este método apresentava falhas de várias maneiras. Em primeiro lugar, diminui a uniformidade dos dados em cadeia. Metadados adicionais e exclusivos podem fazer com que algumas transações se destaquem da multidão, permitindo assim a análise heurística. Isso é especialmente verdadeiro quando esses metadados não são impostos como obrigatórios para todos. Tornar isso obrigatório para todos adicionaria espaço desnecessário ao blockchain e não foi levado em consideração. Da mesma forma, se um ID de pagamento fosse reutilizado por qualquer motivo, seria trivial vincular duas transações como conectadas. Isso normalmente ocorria com depósitos de câmbio, e qualquer pessoa poderia facilmente vincular as transações como sendo um depósito em uma troca e de um indivíduo em particular.

Em segundo lugar, de uma perspectiva de UX, os IDs de pagamento criam uma segunda etapa com a qual os usuários de criptomoedas que vêm de outras moedas não estão acostumados e, se forem esquecidos, isso causa uma enorme dor de cabeça para o comerciante, que deve identificar essas transações por outros meios . Normalmente, isso era feito falando diretamente com cada cliente que se esquecia de colocar o ID de pagamento e confirmando outras informações de identificação que somente eles poderiam saber, como uma combinação de valor, data de envio e ID da transação.

Essa etapa extra foi perdida por muitos, e chegou ao ponto em que algumas trocas começaram a cobrar dinheiro dos clientes se o dinheiro deles tivesse que ser recuperado manualmente por esquecimento de um ID de pagamento. Outros cerraram os dentes e comeram os custos extras de suporte, mas ninguém gostou disso.

Havia uma solução para isso, endereços integrados, que mesclavam o endereço e o ID de pagamento em uma string, para que não pudesse ser esquecido, mas a adoção foi bastante fraca, apesar dos benefícios que os comerciantes teriam recebido ao incluí-lo.

Em uma reviravolta interessante de eventos, subaddresses vieram para salvar o dia. A capacidade de gerar grandes quantidades de subendereços por endereço principal e identificar quais transações entraram em quais subendereços permitiu que os comerciantes se livrassem de IDs de pagamento de maneira elegante, ao mesmo tempo que adotavam a próxima geração da tecnologia Monero. Desde então, a maioria das trocas e ferramentas comerciais mudaram para subendereços como a principal forma de identificação de transações.

O que começou como uma solução para um problema de privacidade se transformou em algo muito mais, que resolveu um grande problema de UX para comerciantes e clientes. A inovação gera mais inovação, o que muitas vezes pode resultar em vitórias inesperadas para todos. Monero viu isso uma e outra vez e se esforça para inovar o que é possível no blockchain. Quem sabe que outras coisas podemos desbloquear juntos?

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