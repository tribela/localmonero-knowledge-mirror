---
title: "Revista Wired está errada sobre Monero, aqui está o porquê"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nas esferas de privacidade e criptomoeda, as informações erradas geralmente são desenfreadas. Temos [um artigo descrevendo quinze suposições comuns incorretas ou desatualizadas sobre o Monero](/knowledge/monero-myths-debunked), mas queremos reservar um tempo para abordar um artigo específico que é frequentemente citado e circulado pelos céticos da Monero.

A publicação da Wired publicou [um artigo](https://www.wired.com/story/monero-privacy/) em 27 de março de 2018, que foi escrito em resposta a outro artigo publicado recentemente por vários acadêmicos intitulado: “Uma Análise Empírica Rastreabilidade no Monero Blockchain ”.

Embora o artigo tenha sido coautor por indivíduos com claro conflito de interesses (leia-se: eles são consultores e têm uma participação no Zcash), o artigo foi moderadamente bem recebido pela comunidade Monero como confirmação de coisas que a comunidade já sabia e escritos em seus próprios artigos do Monero Research Lab ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) e [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), o mais antigo dos quais foi publicado quatro anos antes. No entanto, também houve várias frustrações, principalmente o conflito de interesses, o fato de os problemas já serem conhecidos, discutidos e - em alguns casos - sanados, e a descaracterização grosseira das garantias de privacidade de Monero na época. A comunidade comentou a pré-impressão do trabalho e muitas de suas recomendações chegaram ao trabalho final.

Mas o que exatamente foi descaracterizado? O fato de Monero não ter as falhas discutidas no jornal há mais de um ano. As transações anteriores a 2017 eram realmente vulneráveis a uma forma de vazamento de privacidade, mas na época da publicação, Monero havia abordado a maioria das preocupações. Para ser justo com os autores, eles discutem os remédios de Monero em um pequeno grau, mas não o suficiente para influenciar o efeito que teve no ciclo da mídia de criptomoedas na época. Daí o artigo Wired.

Embora possamos examinar o artigo da Wired em questão como uma peça de época, e quão verdadeiro ou falso era no momento, o fato de ele ainda estar sendo compartilhado hoje como raciocínio do porquê as garantias de privacidade de Monero são fracas, na verdade, convidam a uma análise sobre como a peça se mantém no presente. É com satisfação que recebemos este convite.

Uma leitura rápida do artigo mostra várias linhas sensacionalistas, como "[As descobertas] não devem apenas preocupar alguém que esteja tentando gastar furtivamente o Monero hoje" e todo o tom do artigo que postula a pesquisa como 'nova', baseado amplamente fora da publicação. O artigo acadêmico em si tem recomendações como alertar os usuários do Monero sobre o comprometimento potencial de seu anonimato, apesar do fato de que essas discussões não só aconteciam desde 2014, mas o grito de guerra da comunidade era que as pessoas não compravam o Monero e que foi muito experimental.

Mas e as críticas em si? A realidade é que muitos problemas com o Monero como moeda de privacidade não são mais verdadeiros para o Monero ou preocupações compartilhadas com moedas de privacidade como uma categoria de criptomoedas baseadas em blockchain. Vamos começar a abordar isso.

Uma das críticas mais citadas a Monero é que, devido à permanência e imutabilidade do blockchain, se uma tecnologia futura quebrar a privacidade, todas as transações passadas de Monero seriam expostas. Em outras palavras, sua privacidade tem um relógio.

Não podemos enfatizar isso o suficiente. Literalmente, todas as moedas de privacidade que empregam métodos on-chain de ofuscação e privacidade têm essa falha, e ainda assim são frequentemente usadas contra Monero (ironicamente, muitas vezes, competindo com moedas de privacidade com o mesmo problema), e também são usadas neste artigo. A resposta a essas críticas pode ser surpreendente para alguns, mas Monero, na verdade, pode ser menos vulnerável do que outras moedas de privacidade, devido ao fato de ter uma abordagem multifacetada à privacidade.

Monero oculta saídas (remetentes), quantidades e receptores por meio de três tecnologias diferentes, assinaturas de toque, RingCT e endereços furtivos, respectivamente. Destas, as assinaturas de anel são as mais fracas e mais suscetíveis às heurísticas modernas e às tecnologias teóricas, futuras e de quebra de privacidade. Isso é conhecido pela comunidade Monero há anos, e pesquisas ativas estão em andamento para melhorar ou substituir completamente o esquema de assinatura de anéis.

No entanto, mesmo que a assinatura do anel fosse quebrada completamente, apenas a saída verdadeira seria revelada. NÃO o remetente (como no indivíduo), mas a saída. Acoplar uma saída com uma identidade não é impossível, mas exigiria mais metadados e recursos. Juntamente com o fato de que o RingCT e o endereço secreto NÃO seriam revelados, diminui ainda mais o impacto.

Deve-se notar que o artigo da Wired discute levemente as informações acima na parte em que chegaram a Riccardo 'fluffypony' Spagni para comentar, mas o tempo dado a ele é breve e quase parece acenar com a mão. esta informação crucial. A falta de entendimento é especialmente aparente quando se tenta discutir essas coisas com pessoas que compartilham o artigo, quer ou não, nos dias modernos.

Outra crítica muito mais difícil de abordar é a maneira como o mundo exterior vê Monero e como isso se relaciona com a maneira como a comunidade em torno de Monero vê a moeda. Para um exemplo disso, os leitores não precisam ir além do título do artigo: "A moeda favorita da Dark Web é menos rastreável do que parece".

Qualquer pessoa que gaste uma quantidade significativa de tempo na comunidade Monero pode atestar o fato de que a comunidade Monero se esforça bastante para mostrar o quão difícil é a privacidade real, mesmo em detrimento dos esforços de marketing ou adoção. Se a comunidade fornecer amplos recursos para discutir a moeda e suas deficiências com precisão, em algum momento, a ignorância se tornará culpa do usuário que acredita que a moeda é tudo o que precisa para ser 100% privado.

A essa altura, deve ser evidente que a comunidade Monero leva a sério tanto sua privacidade quanto sua honestidade sobre as fraquezas nela contidas e as melhorias subseqüentes. Artigos, como o em questão, perdem completamente esse espírito de inovação em Monero. Ele compara Monero aos montes de outras criptomoedas que fazem reivindicações grandiosas, com apenas o objetivo de lucrar e atacar investidores sem educação.

A realidade não poderia ser mais diferente. O Monero está ciente de suas fraquezas, procura continuar construindo para melhorá-las, apertar as articulações soltas e alcançar o objetivo muito real, mas muito difícil, de fornecer ao mundo uma criptomoeda privada e fungível que possa ser usada por todos, e faça tudo de maneira justa, descentralizada e direcionada à comunidade. Talvez seja a hora de deixar de lado a sensacionalização e o compartilhamento de artigos como um meio de trocar malas e promover concorrentes. Talvez seja hora de contar outra história.

Leitura adicional