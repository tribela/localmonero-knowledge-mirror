---
title: "Comment Monero a résolu le problème de taille des blocs dont souffre Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Remarque :** Il est fortement recommandé au lecteur de lire nos articles « [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission) » et « [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx) ». Cet article s'appuie sur les concepts qui y sont présentés._

Chaque fois que des individus discutent des problèmes liés à la blockchain, l'un des premiers mots qui apparaît sera « passage à l'échelle ». Ce n'est un secret pour personne que les blockchains ne passent pas très bien à l'échelle (c'est-à-dire avoir ici un très grand nombre d'utilisateurs et de transactions), mais la plupart des gens ne savent pas pourquoi.

La vérité est que le passage à l'échelle est en fait un terme générique qui couvre deux catégories différentes : la charge du protocole et le support technologique à un moment donné. Dans cet article, nous allons concentrer notre attention sur l'un d'entre eux : la charge du protocole est essentiellement une mesure du nombre de transactions que le protocole peut gérer à un moment donné.

Bitcoin a une limite de taille de bloc, ce qui signifie qu'une fois que suffisamment de transactions sont incluses dans un bloc, toute transaction supplémentaire devra attendre en ligne pour le bloc suivant. Une analogie utile serait de penser à un train. Un train arrive à la gare et ceux qui font la queue entrent. Une fois le train plein, toute personne restée à l'extérieur devra attendre le suivant.

Bitcoin utilise des frais pour déterminer qui entre ou non dans le bloc. Revenant à l'analogie du train, on peut imaginer qu'un passager potentiel, qui est sur le point d'être laissé pour compte, offre cinq dollars au contrôleur du train pour lui donner un siège. D'autres passagers emboîtent le pas, et finalement il y a une guerre d'enchères pour déterminer qui obtient quels sièges. C'est au contrôleur de décider s'il veut respecter la politique du premier arrivé, premier servi, mais il est dans son intérêt financier de maximiser ses revenus en acceptant les plus offrants.

Dans cette analogie, les mineurs sont les contrôleurs de train. Ils peuvent inclure toutes les transactions qu'ils souhaitent dans le bloc, mais ils choisiront généralement celles qui ont les frais les plus élevés.

Alternativement, si les blocs ne sont pas très remplis, les gens ne sont pas incités à payer des frais élevés car il y a beaucoup de places libres à revendre.

Au plus fort du boom de la crypto-monnaie en 2017, Bitcoin a été inondé de transactions et les frais ont grimpé en flèche pour ceux qui souhaitaient être inclus dans le bloc suivant, ou dans tout bloc à venir d'ailleurs. Ceux qui n'étaient pas disposés à payer des frais élevés ont vu leurs transactions repoussées pendant des heures, des jours ou même complètement abandonnées.

C'était un aperçu déchirant de la façon dont Bitcoin se comporterait si l'« adoption massive » dont on parle souvent devait se produire. Si Bitcoin devait être utilisé par les masses, les choses seraient encore pires qu'en 2017, et Bitcoin serait inaccessible à quiconque sauf aux riches, simplement parce que le débit est faible en raison d'une taille de bloc fixe, ce qui fait que le marché des frais prend le dessus. .

Monero avait prévu cela et voulait faire quelque chose de différent. Les développeurs de Monero ont donc implémenté une taille de bloc dynamique.

Fondamentalement, Monero a également un plafond de taille de bloc, mais c'est un plafond souple. Lorsque la file des transactions en attente devient trop longue, les mineurs peuvent augmenter la taille des blocs. Avec notre analogie avec le train, vous pouvez imaginer ajouter plus de wagons pour accueillir les passagers supplémentaires. Une fois la file d'attente vide, les blocs reviennent à leur taille d'origine.

Si cela semble être une bonne idée, il semble raisonnable de se demander pourquoi Monero est la seule crypto-monnaie à l'avoir implémentée. Pourquoi ne pas l'ajouter sur Bitcoin afin de mettre un terme aux problèmes de débit ?

Malheureusement, ce n'est pas possible. Il y a plusieurs raisons à cela, et nous ferons de notre mieux pour vous les expliquer.

Il est toujours dans l'intérêt d'un mineur d'avoir de gros blocs. Avec de gros blocs, ils peuvent s'adapter à plus de transactions et gagner plus d'argent sur les frais, ainsi que sur les récompenses de bloc. Cela a le potentiel de conduire à des attaques de spam, où quelqu'un envoie de nombreuses petites transactions, avec de petits frais, pour gonfler la chaîne. Miner augmenterait simplement la taille du bloc pour les inclure tous parce que l'argent est de l'argent, aussi petit soit-il. Cela conduirait à des blocs toujours grands avec peu d'avantages économiques. Bitcoin résout ce problème en limitant artificiellement la taille des blocs, générant ainsi un marché des frais. Les attaquants de spam devraient payer plus que les autres utilisateurs en frais, et ce n'est plus bon marché. Mais cela signifie que les blocs sont pleins, laissant certaines transactions en attente, comme mentionné ci-dessus.

Alors, comment Monero peut-il avoir des tailles de bloc dynamiques tout en évitant les attaques de spam ? La réponse est simple, mais astucieuse. Une pénalité sur la récompense de bloc est introduite lorsqu'un bloc est plus grand que la normale. Si un mineur veut augmenter la taille de bloc, la récompense qu'il obtiendra en trouvant ce bloc sera inférieure à ce qu'il recevrait autrement. Ainsi, ils n'augmenteront la taille de bloc que lorsque les frais de transaction payés par les utilisateurs l'emporteront sur la partie perdue de la récompense de bloc. Par exemple, si le mineur perdait 0,5 XMR en augmentant la taille du bloc et que la somme des frais de transaction payés serait de 0,4 XMR, alors il y aurait une perte nette de 0,1 XMR s'il augmentait la taille, donc il le ferait ne le fais pas. Inversement, si les frais de transaction totaux s'élevaient à 0,7 XMR, il y aurait un gain net de 0,2 XMR, même s'il perdait les 0,5 XMR de la pénalité de récompense globale, de sorte que le mineur augmenterait la taille.

Ces blocs dynamiques permettent au réseau de se développer de manière organique, sans restreindre artificiellement la taille des blocs pour créer un marché à frais forcés, tout en évitant les attaques de spam. Il y a plusieurs autres angles sous lesquels nous pouvons voir cette idée, et plus de raisons pour lesquelles il ne serait pas possible de l'ajouter à Bitcoin, mais pour l'instant, nous espérons que le lecteur comprend comment Monero évite plusieurs des problèmes de Bitcoin et de ses dérivés et comment il prévoit d'adapter son débit à l'avenir.

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies/)

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys/)

  * [Contribuer à Monero](/knowledge/contributing-to-monero/)

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy/)

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades/)

  * [Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool et son rôle dans la décentralisation du minage sur Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis : ce qu'il apportera à Monero](/knowledge/seraphis-for-monero/)

  * [La conversion de Bitcoin en Monero est-elle aussi privée que l'achat direct de Monero ?](/knowledge/most-private-way-to-buy-monero/)

  * [Pourquoi Monero utilise une configuration sans confiance contrairement à Zcash](/knowledge/monero-trustless-setup/)

  * [Pourquoi Monero est une meilleure réserve de valeur que Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Comment Monero peut surmonter les effets de réseau de Bitcoin](/knowledge/network-effect/)

  * [Pourquoi Monero a la communauté qui a la pensée la plus critique](/knowledge/critical-thinking/)

  * [Escroqueries à surveiller lors de l'utilisation de Monero](/knowledge/monero-scams/)

  * [Comment les échanges atomiques fonctionneront avec Monero](/knowledge/monero-atomic-swaps/)

  * [Ce que chaque utilisateur de Monero doit savoir concernant le réseau](/knowledge/monero-networking/)

  * [Comment RingCT masque les montants des transactions Monero](/knowledge/monero-ringct/)

  * [Comment les adresses furtives de Monero protègent votre identité](/knowledge/monero-stealth-addresses/)

  * [Comment les sous-adresses Monero empêchent la mise en correspondance d'identités](/knowledge/monero-subaddresses/)

  * [Explication des sorties Monero](/knowledge/monero-outputs/)

  * [Les meilleures pratiques d'utilisation de Monero pour les débutants](/knowledge/monero-best-practices/)

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures/)

  * [Comment CLSAG améliorera l'efficacité de Monero](/knowledge/what-is-clsag/)

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission/)

  * [Une brève histoire de Monero](/knowledge/monero-history/)

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked/)

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked/)

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion/)

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx/)

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better/)