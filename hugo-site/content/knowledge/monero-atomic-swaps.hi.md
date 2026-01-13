---
title: "Comment les échanges atomiques fonctionneront avec Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Dans la quête de la décentralisation et d'un système véritablement sans permission, peu de choses sont aussi convoitées dans le domaine des crypto-monnaies que les échanges décentralisés et les échanges atomiques. Depuis sa création, Monero a eu du mal à mettre en œuvre des « swaps atomiques », car les fonctionnalités de confidentialité créent des problèmes particuliers lors de la conception d'un protocole.

Mais d'abord, revenons en arrière. Que sont les « swaps atomiques » ? Un swap atomique est un protocole par lequel deux crypto-monnaies différentes, sur des blockchains différentes, peuvent être échangées sans confiance et sans intermédiaire. Cela signifie que si quelqu'un voulait échanger la crypto-monnaie A contre la crypto-monnaie B, il pourrait le faire sans service d'échange, centralisé ou décentralisé. Comme on peut l'imaginer, cela demande des recherches considérables, et tous les détails techniques qui rendent cela possible deviennent assez compliqués. Une fois de plus, LocalMonero est là pour vous aider et donner une explication simple au commun des mortels.

Pour commencer, considérons la forme la plus simple de swap atomique, telle qu'implémentée par Bitcoin. Si quelqu'un veut échanger du Bitcoin contre une autre crypto-monnqie qui utilise la même technologie de contrat de verrouillage de temps de hachage, il peut le faire de la manière suivante. Alice a du Bitcoin (BTC), et veut du Litecoin (LTC), et Bob a du LTC, et veut du BTC. Ils décident de faire un swap atomique afin que chacun obtienne la crypto-monnaie qu'il veut. Alice envoie son BTC à une adresse spéciale, en utilisant des scripts qui verrouillent les fonds afin que même elle ne puisse pas y accéder. Vous pouvez imaginer qu'Alice mette son BTC dans un coffre-fort. Lorsque le coffre-fort est créé, elle obtient une clé et envoie un hachage de cette clé à Bob. Maintenant, Bob n'a pas la clé elle-même, seulement le hachage, donc il ne peut pas encore accéder aux fonds.

Bob utilise ce hachage comme graine à partir de laquelle il génère son propre « coffre-fort », et y envoie son LTC, où il est également verrouillé. Étant donné que le hachage de la clé d'Alice a été utilisé comme graine par laquelle le coffre-fort de Bob a été créé, elle peut utiliser sa clé pour réclamer le LTC dans le coffre-fort de Bob. Sa clé convient ! Mais, en utilisant la magie mathématique vaudou, lorsqu'elle utilise sa clé pour ouvrir la serrure LTC, elle révèle la clé à Bob, qui peut ensuite l'utiliser pour réclamer le BTC qu'elle a mis dans son coffre-fort à elle. De cette façon, sans intermédiaire, Alice et Bob ont réussi à échanger leurs avoirs.

Mais il y a un léger problème. Et si Alice envoie dans son coffre-fort et que Bob décide qu'il ne veut plus échanger. Maintenant, puisqu'Alice ne peut pas accéder à son BTC qu'elle a enfermé et que Bob ne terminera pas sa part de la transaction, Alice perd son argent pour toujours. Eh bien, heureusement, Bitcoin a une petite technologie appelée transactions de remboursement, et donc après un certain temps, si le BTC n'est pas réclamé par Bob, les scripts ont une sécurité intégrée, où le BTC reviendra automatiquement à Alice. C'était le principal ralentisseur pour la mise en œuvre des swaps atomiques de Monero. En raison de la technologie de confidentialité [des signatures de cercle de Monero ](/knowledge/ring-signatures), l'expéditeur d'une transaction est toujours incertain. Comment le protocole peut-il effectuer une transaction de remboursement s'il ne sait même pas d'où provient la transaction ?

En 2017, un petit groupe de chercheurs a décrit une méthode différente par laquelle les swaps atomiques fonctionneraient dans Monero. Après plusieurs années de raffinement, les chercheurs ont finalisé un processus par lequel Monero serait capable de faire des échanges atomiques avec Bitcoin, même sans transactions de remboursement.

Comme pour beaucoup de choses de ce niveau de complexité technique, notre explication simplifiera excessivement certaines choses afin de transmettre l'idée, mais elle donnera toujours une idée solide des mécanismes par lesquels ce processus fonctionnerait.

Alice (qui a du XMR et veut du BTC) et Bob (qui a du BTC et veut du XMR) doivent télécharger et exécuter un programme qui prend en charge le swap atomique. Cela peut être implémenté dans des portefeuilles, des services d'échange décentralisés ou des programmes spéciaux et spécifiques, mais le logiciel doit exécuter le protocole de swap atomique. Dans la première étape, les clients d'Alice et de Bob se connectent et créent plusieurs secrets et clés partagés. Dans cette étape, une nouvelle adresse Monero est créée, Alice ayant une moitié de la clé et Bob ayant l'autre. Il n'y a pas encore de Monero sur cette adresse, donc il n'y a rien à dépenser. Une dernière chose à noter à propos de cette adresse, c'est qu'ils ont tous les deux la clé de vue de ce portefeuille, ils peuvent donc tous les deux jeter un coup d'œil à l'intérieur pour voir si ou et quand du Monero arrive.

Dans la deuxième étape, Bob envoie son BTC à une adresse spéciale, similaire au protocole de swap atomique Bitcoin dont nous avons déjà parlé. Après qu'Alice ait vu le BTC arriver à cette adresse sur la blockchain, elle envoie son Monero à l'adresse Monero pour laquelle elle et Bob ont tous deux la moitié d'une clé. Bob peut vérifier que le Monero est arrivé puisqu'il a également la clé de vue, et une fois qu'il voit que le Monero est en sécurité dans le portefeuille, il envoie à Alice un morceau de clé qui lui permettra de retirer le Bitcoin. Semblable à l'autre protocole, le processus de réclamation du Bitcoin révèle sa moitié de la clé Monero à Bob. Maintenant, Bob a les deux moitiés, donc il peut réclamer le Monero, tandis qu'Alice n'a que sa moitié, donc elle ne peut pas essayer de le prendre avant lui.

Donc, si vous avez lu tout cela et que vous êtes encore un peu confus quant à la façon dont Monero a pu contourner le problème des transactions de remboursement, la réponse est assez simple. Étant donné que Monero lui-même n'a pas de transactions de remboursement, le lecteur doit remarquer que le Bitcoin (qui a des transactions de remboursement) est envoyé en premier, et seulement après avoir été vérifié comme étant sur la blockchain, le Monero est envoyé. Cela permet à Monero d'utiliser la capacité de Bitcoin à écrire des scripts dans les transactions de remboursement et d'en tirer parti, sans avoir besoin de ces capacités lui-même.

Le swap atomique est maintenant terminé, mais à partir de là, Bob a quelques options pour son XMR nouvellement réclamé. Il peut utiliser ce portefeuille Monero tel quel ou déplacer le XMR vers un autre portefeuille qu'il possède déjà. Bob déplacera très probablement le Monero vers un autre portefeuille, car Alice a toujours la clé de vue et peut voir à l'intérieur.

La beauté de ce protocole est qu'il est encore assez nouveau et qu'il y a beaucoup de marge pour des optimisations. Il est également assez flexible dans son architecture, donc la mise en œuvre dans d'autres portefeuilles ou services d'échange décentralisés devrait être simple et s'adapter parfaitement à leur architecture existante.

Ressources complémentaires

  * [Comment Monero favorise de manière unique les économies circulaires](/knowledge/monero-circular-economies)/

  * [Les signatures de cercle de Monero face à CoinJoin comme dans Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Pourquoi (et comment !) vous devriez détenir vos propres clés](/knowledge/hold-your-keys)/

  * [Contribuer à Monero](/knowledge/contributing-to-monero)/

  * [Comment les nœuds distants affectent la confidentialité de Monero](/knowledge/remote-nodes-privacy)/

  * [Comment Monero utilise les « hard -forks » pour mettre à jour le réseau](/knowledge/network-upgrades)/

  * [Les balises de vue : comment un octet réduira les temps de synchronisation du portefeuille Monero de plus de 40%](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool et son rôle dans la décentralisation du minage sur Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis : ce qu'il apportera à Monero](/knowledge/seraphis-for-monero)/

  * [La conversion de Bitcoin en Monero est-elle aussi privée que l'achat direct de Monero ?](/knowledge/most-private-way-to-buy-monero)/

  * [Pourquoi Monero utilise une configuration sans confiance contrairement à Zcash](/knowledge/monero-trustless-setup)/

  * [Pourquoi Monero est une meilleure réserve de valeur que Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Comment Monero peut surmonter les effets de réseau de Bitcoin](/knowledge/network-effect)/

  * [Pourquoi Monero a la communauté qui a la pensée la plus critique](/knowledge/critical-thinking)/

  * [Escroqueries à surveiller lors de l'utilisation de Monero](/knowledge/monero-scams)/

  * [Ce que chaque utilisateur de Monero doit savoir concernant le réseau](/knowledge/monero-networking)/

  * [Comment RingCT masque les montants des transactions Monero](/knowledge/monero-ringct)/

  * [Comment les adresses furtives de Monero protègent votre identité](/knowledge/monero-stealth-addresses)/

  * [Comment les sous-adresses Monero empêchent la mise en correspondance d'identités](/knowledge/monero-subaddresses)/

  * [Explication des sorties Monero](/knowledge/monero-outputs)/

  * [Les meilleures pratiques d'utilisation de Monero pour les débutants](/knowledge/monero-best-practices)/

  * [Comment les signatures de cercle masquent les sorties de Monero](/knowledge/ring-signatures)/

  * [Comment Monero a résolu le problème de taille des blocs dont souffre Bitcoin](/knowledge/dynamic-block-size)/

  * [Comment CLSAG améliorera l'efficacité de Monero](/knowledge/what-is-clsag)/

  * [Pourquoi Monero a une émission résiduelle](/knowledge/monero-tail-emission)/

  * [Une brève histoire de Monero](/knowledge/monero-history)/

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires