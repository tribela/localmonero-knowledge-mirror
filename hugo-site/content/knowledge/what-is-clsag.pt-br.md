---
title: "Como o CLSAG melhorará a eficiência da Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Como protocolo, o Monero está atualmente em constante estado de inovação. Utilizando pesquisas em soluções dentro e fora da rede, a comunidade Monero procura áreas para melhorar para tornar o Monero mais privado, mais escalonável e mais acessível a todos. Uma das inovações mais recentes é a substituição do esquema de assinatura de anel vinculável, MLSAG, por um CLSAG substituto imediato, que significa Concise Linkable Spontaneous Anonymous Group. 

A nível superficial, a implementação do CLSAG diminuirá as 2 transações de entrada e de saída mais comuns em 25%. Também veremos uma redução de 10% no tempo de verificação. 

Mas o que exatamente é CLSAG? O que ele faz e em que difere da versão anterior, MLSAG? Vamos tomar um minuto para nos lembrar do porquê e como usar assinaturas de anel para que possamos entender melhor este conceito. As assinaturas de anel permitem entradas indistinguíveis de testemunhas não interativas pelo uso de conjuntos de anonimato selecionados pelo signatário de saídas anteriores. Em termos leigos, permite que um usuário esconda suas saídas usadas em uma transação junto com saídas não relacionadas, e eles podem fazer tudo isso sem a necessidade de ninguém para participar. Tudo que você precisa é uma cópia do blockchain. Cada uma dessas saídas parece ser igualmente provável de ser a que está sendo enviada, ocultando metadados sobre o remetente. 

Isso gera um pequeno problema, no entanto. E se um usuário fosse construir uma assinatura de anel com todas as saídas de chamariz? Como alguém saberia que o remetente desconhecido não tem autoridade para enviar nenhum deles? Este usuário poderia gastar dinheiro falso? A resposta é não. A assinatura do anel inclui um método para provar que pelo menos uma das saídas pertence ao remetente desconhecido, sem revelar qual é. Na verdade, tanto CLSAG quanto MLSAG (doravante conhecidos como SAGs) são a parte da assinatura do anel que prova isso. Curiosamente, ao mesmo tempo, isso prova que o valor da transação, embora oculto por trás de transações confidenciais (RingCT), é equilibrado. Que os SAGs provam duas coisas, que uma saída pertence a alguém no ringue e que o saldo da transação é importante e, na verdade, onde reside o tamanho e a economia na verificação. Se isso está ficando confuso, não se preocupe, vamos chegar a uma analogia divertida e fácil de entender em breve. 

O esquema de assinatura antigo, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) prova as duas coisas acima mencionadas em uma assinatura de anel, mas faz cada uma separadamente. O uso de cálculos separados para chaves de assinatura e confirmação significa operações mais lentas. Um computador moderno pode fazer esses cálculos em questão de milissegundos, o que não parece muito e, de fato, para uma transação não é. Mas quando consideramos o grande número de transações no blockchain Monero, e que um nó de sincronização do zero terá que baixar e verificar cada uma delas, os bytes e milissegundos começam a se acumular rapidamente. 

O CLSAG combina a matemática necessária para provar os dois em um, bem como calcula os dois ao mesmo tempo, e o faz de maneira segura. O que isso significa de maneira segura? Bem, para esclarecer isso, bem como, esperançosamente, fazer tudo fazer mais sentido, vamos explorar aquela analogia divertida prometida. 

Digamos que você precise ir ao supermercado e à loja de ferragens para comprar duas coisas diferentes: alimentos e produtos químicos de limpeza tóxicos. Você não quer que eles se misturem, como se houvesse um acidente, os produtos químicos vão derramar na comida, tornando-os intragáveis. Você decide ficar super seguro e dirigir de sua casa ao supermercado, comprar a comida e depois dirigir de volta para sua casa. Só depois de descarregar a comida você volta para o carro, vai até a loja de ferragens e volta para casa com os produtos químicos. Você fez duas viagens diferentes para garantir a segurança de todas as compras. Embora seja realmente seguro, é ineficiente. Isso representa MLSAG, onde dois conjuntos diferentes de matemática são armazenados e duas 'viagens' diferentes são feitas para computá-los. 

Você decide que deseja uma maneira mais rápida de fazer isso, no entanto. É muito tempo perdido. Claro que fazer isso uma ou duas vezes não vai roubar sua vida, mas tendo que fazer isso repetidamente, as horas começam a se somar. Você começa a se perguntar se pode fazer uma viagem em vez disso. De sua casa, ao supermercado, à loja de ferramentas e de volta para casa. Você não pode simplesmente jogar tudo em seu carro ao acaso. Não é seguro. Em vez disso, você designa pontos diferentes em seu carro para coisas diferentes e garante que tudo se encaixe perfeitamente em seu lugar. Ao fazer isso, você pode fazer uma viagem com segurança a ambas as lojas e manter as coisas longe uma da outra. Isso representa CLSAG. Agora há apenas um conjunto de matemática armazenado nesta transação para provar essas duas coisas, e isso é feito de forma que não interfiram uma com a outra. Uma viagem ainda precisa ser feita, mas você reduziu o número delas drasticamente. 

Tudo isso parece muito emocionante. É isso possível, podemos encontrar outros atalhos, ou outras formas de economizar tempo e espaço? A resposta é sim e não. De acordo com os pesquisadores atuais do MRL, provavelmente não é possível modificar ainda mais as construções do tipo SAG para melhor tamanho ou velocidade; no entanto, outras construções como Arcturus, Omniring, RCT3 ou Triptych produzem um dimensionamento de tamanho muito melhor e benefícios de verificação usando diferentes métodos matemáticos. No entanto, cada uma dessas abordagens de 'próxima geração' para protocolos ambíguos de assinantes vem com suas próprias compensações em detalhes de implementação e estão passando por pesquisas e investigações ativas. 

Afinal, Monero está sempre inovando. 

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

  * [O que todo usuário Monero precisa saber quando se trata de rede](/knowledge/monero-networking/)

  * [Como RingCT esconde valores de transação Monero](/knowledge/monero-ringct/)

  * [Como os endereços Monero Stealth protegem sua identidade](/knowledge/monero-stealth-addresses/)

  * [Como os subendereços do Monero evitam o vínculo de identidade](/knowledge/monero-subaddresses/)

  * [Saídas Monero explicadas](/knowledge/monero-outputs/)

  * [Práticas recomendadas Monero para iniciantes](/knowledge/monero-best-practices/)

  * [Como as assinaturas de toque obscurecem as saídas do Monero](/knowledge/ring-signatures/)

  * [Como Monero resolveu o problema do tamanho do bloco que assola o Bitcoin](/knowledge/dynamic-block-size/)

  * [Por que Monero tem uma emissão de cauda](/knowledge/monero-tail-emission/)

  * [A história de Monero](/knowledge/monero-history/)

  * [Revista Wired está errada sobre Monero, aqui está o porquê](/knowledge/wired-article-debunked/)

  * [Os 15 principais mitos e preocupações de Monero desmascarados](/knowledge/monero-myths-debunked/)

  * [Como o Dandelion ++ mantém as origens da transação de Monero em sigilo](/knowledge/monero-dandelion/)

  * [Por que o Monero é de código aberto e descentralizado](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: O que torna o RandomX tão especial](/knowledge/monero-mining-randomx/)

  * [Por que Monero é melhor que Dash, Zcash, Zcoin (Even with Lelantus), Grin e Bitcoin Mixers como Wasabi (Atualizado em maio de 2020)](/knowledge/why-monero-is-better/)