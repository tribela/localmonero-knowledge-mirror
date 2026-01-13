---
title: "Wired Magazine se trompe sur Monero, voici pourquoi"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Dans les sphères de la confidentialité et de la crypto-monnaie, la désinformation est souvent endémique. Nous avons [un article décrivant quinze hypothèses courantes incorrectes ou obsolètes sur Monero](/knowledge/monero-myths-debunked), mais nous voulons prendre le temps d'aborder un article en particulier qui est souvent cité et diffusé par les sceptiques de Monero.

La publication Wired a publié [un article](https://www.wired.com/story/monero-privacy/) le 27 mars 2018, qui lui-même a été écrit en réponse à un autre article tout juste sorti de presse, publié par divers universitaires, et intitulé « Une analyse empirique de traçabilité dans la blockchain Monero ». 

Bien que l'article ait été co-écrit par des personnes ayant un conflit d'intérêts clair (lire : ils sont des conseillers et ont une participation dans Zcash), l'article a été modérément bien accueilli par la communauté Monero comme confirmant des choses que la communauté savait déjà et écrits dans leurs propres articles Monero Research Lab ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) et [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) dont le plus ancien a été publié quatre ans auparavant. Cependant, il y avait aussi plusieurs frustrations, dont principalement le conflit d'intérêts, mais aussi le fait que les problèmes étaient déjà connus, discutés et - dans certains cas - résolus, et la mauvaise description des garanties de confidentialité de Monero à l'époque. La communauté a commenté la prépublication du travail, et nombre de leurs recommandations ont été transmises au document final.

Mais qu'est-ce qui a été mal interprété ? Le fait que Monero n'avait pas eu les défauts discutés dans le journal depuis plus d'un an. Les transactions antérieures à 2017 étaient en effet vulnérables à une forme de fuite de confidentialité, mais au moment de la publication, Monero avait répondu à la plupart des préoccupations. Pour être juste envers les auteurs, ils discutent des corrections apportées dans Monero dans une faible mesure, mais pas suffisamment pour influencer l'effet qu'il a eu sur le cycle médiatique de la crypto-monnaie à l'époque. D'où l'article de Wired.

Bien que nous puissions examiner l'article de Wired en question comme un article d'époque, et dans quelle mesure il était vrai ou faux à l'époque, le fait qu'il soit encore partagé aujourd'hui pour expliquer pourquoi les garanties de confidentialité de Monero sont faibles invite en fait à une analyse de la façon dont l'article tient dans le présent. Nous acceptons volontiers cette invitation.

Une lecture rapide de l'article montre plusieurs lignes sensationnalistes, telles que « [Les découvertes] ne devraient pas seulement inquiéter quiconque essaie de dépenser furtivement Monero aujourd'hui » et le ton entier de l'article qui postule que la recherche est « nouvelle », en se basant largement sur la publication. Le document académique lui-même contient des recommandations telles que l'avertissement des utilisateurs de Monero de la compromission potentielle de leur anonymat, malgré le fait que non seulement ces discussions avaient eu lieu depuis 2014, mais le cri de ralliement de la communauté était que les gens n'achètent pas de Monero et qu'il était très expérimental.

Mais qu'en est-il des critiques elles-mêmes ? La réalité est que de nombreux problèmes avec Monero en tant que crypto-monnaie de confidentialité ne sont plus vrais pour Monero, ou partagent des préoccupations concernant les crypto-monnaies de confidentialité en tant que catégorie de crypto-monnaies basées sur la blockchain. Commençons par les résoudre.

L'une des critiques les plus souvent citées à l'encontre de Monero est qu'en raison de la permanence et de l'immuabilité de la blockchain, si une future technologie venait à briser la confidentialité, toutes les transactions passées de Monero seraient mises à nu. En d'autres termes, votre confidentialité a un compte à rebours.

Nous ne saurions trop insister là-dessus. Littéralement, chaque crypto-monnaie de confidentialité qui utilise des méthodes en chaîne pour l'obscurcissement et la confidentialité a ce défaut, et pourtant il est souvent utilisé contre Monero (ironiquement, plusieurs fois par des crypto-monnaie de confidentialité concurrentes avec le même problème), et est également utilisé dans cet article. La réponse à cette critique pourrait surprendre certains, mais Monero peut en fait être moins vulnérable que d'autres crypto-monnaies de confidentialité en raison du fait qu'il a une approche à plusieurs volets de la confidentialité.

Monero masque les sorties (expéditeurs), les montants et les récepteurs via trois technologies différentes, respectivement les signatures de cercle, RingCT et les adresses furtives. Parmi celles-ci, les signatures de cercle sont les plus faibles et les plus sensibles à la fois aux heuristiques modernes et aux technologies théoriques futures qui brisent la confidentialité. Cela est connu de la communauté Monero depuis des années, et des recherches actives sont en cours pour améliorer ou remplacer entièrement le schéma de signature de cercle.

Cependant, même si la signature de cercle était entièrement brisée, seule la véritable sortie serait révélée. PAS l'expéditeur (en tant qu'individu), mais la sortie. Associer une sortie à une identité n'est pas impossible, mais cela nécessiterait plus de métadonnées et de ressources. Couplé au fait que RingCT et l'adresse furtive ne seraient PAS révélées, cela réduit encore plus l'impact.

Il convient de noter que l'article de Wired traite légèrement des informations ci-dessus dans la partie où ils ont contacté Riccardo « fluffypony » Spagni pour obtenir des commentaires, mais le temps qui lui est accordé est bref et semble presque faire fi de cette information cruciale. Le manque de compréhension est particulièrement apparent lorsque vous essayez de discuter de ces choses avec des personnes qui partagent l'article bon gré mal gré de nos jours.

Une autre critique beaucoup plus difficile à aborder concerne la façon dont le monde extérieur perçoit Monero, et son lien avec la façon dont la communauté autour de Monero perçoit la crypto-monnaie. Par exemple, les lecteurs n'ont pas besoin de regarder plus loin que le titre de l'article lui-même : « La monnaie préférée du Dark Web est moins intraçable qu'il n'y paraît ».

Toute personne qui passe beaucoup de temps dans la communauté Monero peut attester du fait que la communauté Monero se donne beaucoup de mal pour montrer à quel point la vraie confidentialité est difficile à atteindre, même au détriment des efforts de marketing ou d'adoption. Si la communauté fournit de nombreuses ressources pour discuter avec précision de la crypto-monnaie et de ses défauts, à un moment donné, l'ignorance devient la faute de l'utilisateur qui croit que la crypto-monnaie est tout ce dont il a besoin pour être 100% en confidentialité.

À ce stade, il devrait être évident que la communauté Monero prend au sérieux à la fois la confidentialité et l'honnêteté concernant les faiblesses et les améliorations ultérieures. Des articles, comme celui en question, manquent complètement cet esprit d'innovation chez Monero. Cela compare Monero aux hordes d'autres crypto-monnaies qui font des revendications grandioses, avec seulement une pensée pour le profit et pour s'attaquer à des investisseurs en herbe sans éducation sur le domaine.

La réalité ne pourrait pas être plus différente. Monero est parfaitement conscient de ses faiblesses, cherche à continuer de construire de manière à les améliorer, à resserrer les joints lâches et à atteindre l'objectif très réel mais très difficile de donner au monde une crypto-monnaie privée et fongible qui peut être utilisée par tous, et tout cela fait d'une manière équitable, décentralisée et axée sur la communauté. Il est peut-être temps de mettre de côté le sensationnalisme et le partage d'articles comme moyen de vendre des sacs et de promouvoir des concurrents. Il est peut-être temps de raconter une autre histoire.

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

  * [Comment les échanges atomiques fonctionneront avec Monero](/knowledge/monero-atomic-swaps)/

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

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

  * [Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)](/knowledge/why-monero-is-better)/

Ressources complémentaires