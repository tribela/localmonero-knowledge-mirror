---
title: "Como os endereços Monero Stealth protegem sua identidade"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero implementou uma abordagem de três frentes para a privacidade. Essas tecnologias são [assinaturas de anel](/knowledge/ring-signatures), que ocultam a saída real (remetente), RingCT que oculta os valores e endereços furtivos, que oculta o receptor. Hoje, estaremos discutindo a última dessas tecnologias mencionadas: endereços furtivos.

Existem muitos motivos pelos quais um indivíduo pode querer ocultar para quem está enviando. Nunca devemos deixar ninguém tentar nos convencer de que todos os exemplos disso são comportamentos desagradáveis. Coisas como enviar para um partido político impopular, doar para instituições de caridade ou apoiar aqueles que a cultura considera "cancelados" são todos exemplos de onde alguém pode querer esconder seus hábitos de consumo por medo de repercussão, mas são perfeitamente legítimos por natureza.

Em um blockchain transparente, os endereços para onde alguém envia suas transações são visíveis para todos. É importante considerar que, se os próprios mineradores discordarem sobre para onde o dinheiro está indo, eles podem escolher não minerá-lo em um bloco, censurando efetivamente essa transação em uma plataforma aparentemente resistente à censura. A única maneira de tornar isso, reconhecidamente improvável, a censura impossível é se os mineradores não conseguirem distinguir entre as transações porque todos os metadados na cadeia são obscurecidos por vários meios. Algo pelo qual Monero é conhecido.

Monero resolve este problema de endereços transparentes implementando endereços furtivos, uma tecnologia que foi inicialmente feita para Bitcoin em 2011 pelo usuário do fórum Bitcoin Talk ByteCoin (a relação com Bytecoin, que mais tarde integraria endereços furtivos, é desconhecida). A forma atual de endereços furtivos tem várias melhorias em relação à ideia inicial. Mas primeiro, para ver como funcionam, vamos falar sobre as chaves.

É difícil estar no espaço das criptomoedas e não ouvir sobre as chaves. Frases como 'faça backup de sua chave privada' são comuns, mas quando um Joe comum ouve as palavras "chave pública" e "chave privada", fica assustado e pensa que será muito técnico e confuso para entender. Mas não se preocupe. Iremos devagar e usaremos muitos exemplos.

Os dois tipos de chaves usadas em criptomoedas são, como acabamos de mencionar, pública e privada. Essas duas chaves geralmente vêm em um par, o que significa que uma determinada chave pública e privada estão vinculadas uma à outra. Na verdade, normalmente a chave pública é derivada da chave privada, o que significa que se você conhece a chave privada, sua carteira pode fazer algumas matemáticas bacanas e encontrar a chave pública correta todas as vezes.

Agora, como os nomes indicam, a chave pública pode ser pública sem consequências. Normalmente é uma parte do endereço que você compartilha para receber dinheiro em sua carteira de criptomoeda. Também seguindo seu homônimo, a chave privada não deve ser compartilhada. É o que permite que você assine e gaste uma transação, portanto, se ela for roubada ou compartilhada, o terceiro covarde pode gastar seu dinheiro, geralmente para si mesmo.

Uma analogia fácil para isso seria um cadeado e a chave necessária para desbloqueá-lo. O cadeado aberto pode ser compartilhado livremente e, de fato, qualquer coisa pode ser trancada com este cadeado, mas apenas a pessoa com a chave é capaz de abrir qualquer coisa em que o cadeado esteja fechado. O cadeado pode ser copiado e compartilhado, a chave não.

Essas chaves geralmente são abstraídas do usuário, então você nunca as vê de verdade. No Monero, eles não aparecem como uma sequência alfanumérica assustadora. No Monero, o usuário comum conhece a chave privada como sua semente. A semente (que você deve anotar se não tiver), é na verdade apenas uma chave privada legível por humanos. 

Veja? Afinal, não é tão assustador. De volta aos endereços secretos.

Como mencionado antes, os endereços secretos não foram feitos originalmente para Monero, mas para Bitcoin. Porém, como acontece com a maioria das ideias incipientes, essa primeira iteração teve problemas. A próxima tentativa veio quando o CryptoNote foi criado por Nicholas van Saberhagan para Bytecoin, o precursor do Monero ([veja nossa história de Monero e Bytecoin aqui](/knowledge/monero-history)), e embora tenha sido uma melhoria definitiva em relação ao original, mesmo ele tinha algumas falhas sutis.

Eventualmente, uma última iteração surgiu de um desenvolvedor para outra agora extinta, criptomoeda de privacidade, que corrigiu os problemas pendentes de privacidade e segurança com a ideia. Isso acabou chegando ao Monero e é o que é usado hoje.

Embora esses problemas de privacidade e segurança tenham sido resolvidos, os próprios endereços furtivos adicionaram um tipo diferente de peculiaridade às tecnologias de blockchain, uma que não existia antes. A necessidade de digitalizar. Como os endereços de recebimento não são exibidos publicamente no blockchain, o receptor nunca sabe se alguma transação é dele, então ele deve verificar todas as transações recebidas com sua chave privada para ver se é dele.

Com as moedas de transparência, tudo o que eles precisam fazer é verificar se uma transação está sendo enviada para o seu endereço. Uma pergunta fácil, sim ou não. Mas com endereços furtivos, cada transação pode ser potencialmente enviada para você, então você deve tentar desbloquear cada uma com sua chave privada para ver se ela abre.

Esta é uma etapa extra que o Bitcoin e seus derivados não têm, e faz a configuração inicial da carteira, juntamente com a sincronização de uma carteira quando você não a abre há um tempo, muito mais do que o Bitcoin. A compensação é necessária, porém, para desbloquear as garantias de privacidade que ele possui. Deve-se notar que, ao contrário do ponto mais fraco da trifeta de privacidade, assinaturas de anel, endereços furtivos não são suscetíveis a heurísticas. Ele se baseia na criptografia de curva elíptica testada e comprovada, da qual toda a Internet depende, portanto, quebrá-la significaria o fim da segurança do computador em geral, não apenas do Monero.

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