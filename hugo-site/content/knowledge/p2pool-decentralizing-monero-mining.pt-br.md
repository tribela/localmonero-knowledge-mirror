---
title: "P2Pool e seu papel na descentralização da mineração Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Um dos principais objetivos do projeto Monero é permitir uma rede justa, descentralizada e segura através de abordagens novas e inovadoras à mineração de prova de trabalho (PoW), a principal forma de garantir hoje as redes de moeda criptográfica.

Enquanto um algoritmo único de mineração [como o RandomX](/knowledge/monero-mining-randomx) é extremamente importante para este objetivo, pois ajuda a garantir que qualquer pessoa com um computador possa contribuir com uma quantia justa para a segurança da rede, o RandomX não resolve os problemas que podem ocorrer devido à mineração de pool. A mineração de pool é de longe a forma mais comum de mineração de moedas criptográficas hoje em dia, incluindo Monero, mas felizmente o surgimento da mineração p2pool está mudando isso rapidamente.

## O que é mineração de piscina?

A mineração de piscina é uma forma de os mineiros compartilharem a tarefa de tentar resolver um bloco na rede e depois compartilhar as recompensas uniformemente para todos os blocos que a piscina encontrar. Embora isto ajude imensamente a nivelar a freqüência com que os mineiros são pagos contra a mineração Monero sozinha, não é isento de sérios problemas de centralização.

Como cada mineiro contribui com trabalho para a piscina, eles desistem do controle de qualquer trabalho que fazem e bloqueiam o que encontram para a própria piscina, confiando que a piscina irá honesta e justamente compartilhar as recompensas entre todos os mineiros com base na quantidade de trabalho que cada um realizou. Se tudo correr bem, o operador do pool coleta o trabalho de todos os mineiros, o submete à rede e compartilha as recompensas igualmente.

## Qual é o problema com a mineração de piscinas?

Infelizmente, isto depende inteiramente da confiança e permite que o operador da piscina faça coisas nefastas com o trabalho que está sendo feito pelos mineiros. O operador do pool poderia usar o trabalho que está sendo feito para atacar a rede, tentar duplicar os fundos (se o pool for suficientemente grande), ou simplesmente usar o trabalho que está sendo feito pelos mineiros para pagar a si mesmos e nunca recompensar devidamente os mineiros por seu trabalho.

O maior risco para a rede é o de um pool (ou múltiplos pools trabalhando juntos) ter mais de 51% das redes com hashrate sob seu controle, pois poderiam usar isso para enganar e gastar fundos duas vezes (um ataque de gasto duplo) ou tentar mudar as regras da rede.

## O que é p2pool?

p2pool é um conceito que foi originalmente criado para mineração de Bitcoin em 2011, mas nunca teve ampla adoção e permanece praticamente sem uso no Bitcoin. Felizmente, um dos principais desenvolvedores por trás do RandomX, SChernykh, passou suas férias criando soluções para alguns dos problemas com a implementação do p2pool no Bitcoin e reescrevendo todo o software do zero.

O p2pool no Monero permite uma maneira completamente sem confiança para os mineradores trabalharem juntos para resolver blocos e proteger a rede Monero usando software de nó especial para p2pool para compartilhar o trabalho.

Isso é feito usando um novo blockchain (uma "cadeia lateral") que mantém um registro do trabalho que cada minerador realiza, seu endereço de carteira e quanto Monero eles ganharam e, em seguida, paga a recompensa em um fundo -menos e descentralizada. Como essa cadeia lateral tem muito menos mineradores, é muito mais fácil encontrar e enviar blocos nela do que na rede principal do Monero, tornando mais fácil para os mineradores obter pagamentos consistentes em comparação com a mineração do Monero sozinho.

## Como a p2pool resolve os problemas da mineração de piscinas?

No p2pool, não há pool centralizado, operador de pool centralizado, ou uma única pessoa retendo os fundos e distribuindo os pagamentos. Todo o trabalho que está sendo feito coletivamente por aqueles mineradores via p2pool é verificado pela cadeia de bloqueio p2pool e outros operadores de nós para garantir que seja legítimo, e todos os mineiros são pagos de acordo com o trabalho que fizeram imediatamente quando um bloco é encontrado diretamente das recompensas naquele bloco encontrado.

Quando os mineiros escolhem usar o p2pool em vez de um pool centralizado, eles retiram todo o poder e confiança dos operadores do pool e garantem que seu trabalho contribua para o bem da rede e para suas próprias recompensas, reduza o risco de ataques à rede, mau uso de seu trabalho ou roubo de recompensas que lhes são devidas.

Isto não apenas os ajuda a proteger seus próprios interesses, mas também reduz o risco que os pools centralizados podem representar para a rede Monero como um todo. O uso do pool p2pool também ajuda imensamente a reduzir o risco que os estados nacionais ou reguladores poderiam representar para a saúde da rede, já que não há operadores de pool centralizados para pressionar, nenhuma concentração geográfica de pools para se apoiar, ou qualquer outro ponto fácil de pressão para que eles usem contra Monero.

## Quais são os inconvenientes?

Felizmente, o p2pool no Monero foi bem projetado e bem construído e funciona muito bem! No entanto, a principal desvantagem da mineração p2pool é que cada minerador que deseja usar o p2pool precisa executar seu próprio nó Monero, fazendo com que o processo de início seja um pouco mais complicado. No entanto, esse nó é usado para calcular todas as informações necessárias para construir e verificar blocos e garante que o minerador tenha controle total de seu trabalho. O nó também pode funcionar como um nó remoto para a carteira do próprio minerador, contribui para a rede e muito mais.

A outra diferença importante da mineração centralizada é que pequenos mineradores usando p2pool terão um pouco mais de "variação", ou tempo entre pagamentos, do que um grande pool centralizado -- mas's _extremamente_ importante notar que isso não levará a ganhar menos Monero ao longo do tempo! O p2pool será tão lucrativo para os pequenos mineradores ao longo do tempo quanto os pools centralizados. Parte dessa variação também é compensada pelo p2pool ter taxas nativas de 0%, pois não há um operador de pool centralizado para pagar por seus serviços!

## Como posso começar?

Felizmente, devido ao excelente projeto da implementação da p2pool Monero'e às muitas pessoas da comunidade que dedicaram tempo para ajudar a simplificar o processo de mineração via p2pool, começar é cada vez mais simples com o tempo. Há várias maneiras de começar a mineração com p2pool, mas como os detalhes técnicos estão além do escopo deste artigo, sinta-se à vontade para pular para um link abaixo, dependendo de seu sistema operacional:

  * [Janelas](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Como posso aprender mais?

Se isso despertou sua curiosidade em torno da mineração p2pool, dê uma olhada abaixo para alguns links adicionais e explique como funciona e o que significa para Monero:

  * [O Github oficial do p2pool](https://github.com/SChernykh/p2pool)
  * [Os documentos oficiais sobre o uso do p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool está agora ao vivo](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, um "explorador de blocos" de tipos para p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Sobre seu desenvolvimento do P2Pool a Descentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Leitura adicional