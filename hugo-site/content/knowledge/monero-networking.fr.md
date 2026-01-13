---
title: "Ce que chaque utilisateur de Monero doit savoir concernant le réseau"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Cela ne devrait surprendre personne que Monero, et en fait toutes les crypto-monnaies, fonctionnent sur Internet. Et pourtant, même si cette affirmation semble basique et évidente, beaucoup ne considèrent pas les implications de ce que cela signifie en ce qui concerne leur vie privée. En d'autres termes, il y a certaines choses contre lesquelles Monero peut et ne peut pas se protéger, simplement par la nature de son fonctionnement sur Internet. Certaines de ces considérations ne sont que de simples inconvénients, tandis que d'autres sont beaucoup plus graves dans un scénario où une confidentialité absolue est requise. Prenons le temps de nous familiariser avec la façon dont les utilisateurs de Monero interagissent les uns avec les autres sur le réseau et ce que cela signifie pour leur vie privée.

En partant du côté trivial des choses, si un utilisateur n'a pas accès à Internet, il ne peut pas télécharger de nouveaux blocs, propager des transactions au nom d'autres personnes ou envoyer ses propres transactions. Une chose intéressante à noter est qu'un utilisateur avec un nœud complet, sans accès à Internet, peut construire une transaction hors ligne qui peut être envoyée plus tard. En effet, une signature de cercle n'a besoin que des sorties de la blockchain pour se cacher. Un bref rappel sur [comment fonctionnent les signatures de cercle](/knowledge/ring-signatures), est qu'on cache la sortie réelle qu'un utilisateur envoie parmi une collection de sorties non affiliées choisies dans le passé. Si l'utilisateur a accès à ces sorties sous la forme d'une blockchain entièrement téléchargée (nœud complet), il peut créer la signature de cercle à partir des sorties précédentes et, une fois la connectivité Internet rétablie, propager la transaction sur le réseau.

Un utilisateur qui utilise un nœud distant ne peut pas le faire, car lorsqu'il construit sa signature de cercle, il contacte le nœud complet distant pour que les sorties soient incluses dans la signature de cercle. L'absence d'Internet signifie qu'ils ne peuvent pas atteindre ce nœud, ils n'ont donc pas de capacités de construction de transactions hors ligne.

Avant de continuer dans certaines des considérations de confidentialité, voyons un bref aperçu du fonctionnement d'Internet dans son ensemble. Tout Internet n'est rien de plus que des ordinateurs se connectant à d'autres ordinateurs. C'est ça. Le blog que vous aimez lire ? Juste quelques fichiers hébergés sur l'ordinateur de quelqu'un d'autre. Ce site Web sur lequel vous lisez cet article (LocalMonero) ? Des fichiers et du code hébergés sur un ordinateur quelque part. Même les grands sites les plus complexes fonctionnent de cette façon. Prenez YouTube par exemple. Juste des fichiers vidéo hébergés sur les gigantesques systèmes informatiques de Google, et vous vous y connectez pour télécharger la vidéo sur votre propre ordinateur afin de pouvoir la regarder.

Ces ordinateurs peuvent se différencier car chaque ordinateur connecté à Internet reçoit un numéro d'identification unique appelé « adresse IP ». Il s'agit généralement de quatre ensembles de nombres séparés par des points, par exemple : 172.66.35.7. Il est important de garder cela à l'esprit lorsque nous examinons comment les informations Monero transitent sur Internet. Monero est un réseau pair-à-pair (P2P), ce qui signifie que les ordinateurs se connectent directement les uns aux autres plutôt que d'utiliser un intermédiaire. Ainsi, lorsque le nœud complet d'un utilisateur télécharge un bloc nouvellement découvert, il ne le télécharge pas à partir d'un serveur central, mais à partir de ses pairs. L'inconvénient est que, puisque les utilisateurs se connectent directement les uns aux autres, ils connaissent les adresses IP des autres.

Eh bien ? Quel est le problème ? Ce n'est qu'un chiffre, n'est-ce pas ? Pas exactement. Les adresses IP elles-mêmes contiennent des informations sur l'utilisateur, telles que le pays d'origine et le fournisseur de réseau, mais, pire encore, les fournisseurs de services Internet (FAI) connaissent l'adresse IP de chaque personne utilisant leurs services. Cela signifie que ces FAI et ceux avec qui ils travaillent peuvent surveiller le trafic Internet d'un utilisateur et, en utilisant des tactiques astucieuses, découvrir qu'ils utilisent Monero. Maintenant, avant d'avoir peur, prenez le temps de lire la suite. Tout ce que ces fouineurs peuvent faire, c'est voir qu'une personne se connecte à d'autres nœuds du réseau Monero. En raison de la technologie de confidentialité de Monero, rien d'autre n'est divulgué sur l'individu. Pas s'ils exécutent ou non un nœud, ou si/quand ils envoient des transactions, et si une transaction est envoyée, aucune de ses informations n'est connue. Tout ce que ces FAI peuvent voir, c'est qu'un de leurs utilisateurs se connecte au réseau Monero.

Maintenant, pour certaines personnes, dans certains endroits du monde, ces informations peuvent à elles seules suffire à porter atteinte à la réputation ou à la liberté. Ou peut-être que l'idée que quelqu'un envahisse votre vie privée et ce que vous faites sur Internet, pour une raison quelconque, n'est pas acceptable pour vous. Ces personnes sont encouragées à se connecter uniquement au réseau Monero à l'aide de VPN, Tor ou I2P, qui sont tous des services qui cachent l'adresse IP d'un utilisateur aux autres et cachent ce qu'un utilisateur fait à son FAI. Les différences entre ces services dépassent le cadre de cet article, mais il existe de nombreux articles de haute qualité écrits sur le sujet, les utilisateurs concernés sont donc encouragés à étudier !

Pour le reste d'entre nous, nous pouvons penser que faire savoir aux autres que nous sommes connectés au réseau Monero n'est pas si grave. Après tout, le contenu réel de nos transactions, ou si nous en envoyons, est caché au public, alors quel est le mal ? Bien que cela puisse être vrai, les utilisateurs sont encouragés à considérer le fait que le principal attrait des crypto-monnaies est le fait que vous devenez votre propre banque. Lorsque vous détenez votre clé privée, et si quelque chose lui arrive, personne ne peut vous aider à récupérer vos fonds perdus.

Être sa propre banque, c'est tenir compte non seulement de sa sécurité numérique, mais aussi de sa sécurité physique. Il se pourrait très bien que la connaissance d'un individu se connectant au réseau Monero puisse attirer une attention indésirable, pas nécessairement de la part d'acteurs à grande échelle comme les États-nations, mais de plus petits avec un intérêt égoïste, comme les pirates qui cherchent à gagner facilement de l'argent. Il existe en effet d'innombrables histoires dans tout l'univers des crypto-monnaioes de tels scénarios qui se déroulent réellement.

Cet article n'a pas pour but de semer la peur ou d'effrayer, mais plutôt d'encourager les utilisateurs à faire des recherches sur les méthodes de protection de la navigation sur le Web qui leur conviennent. La bonne nouvelle est que ces compétences seront également transférées à l'utilisation générale d'Internet, pas seulement à l'utilisation de Monero, et en tant que tel, dans notre monde de plus en plus connecté à Internet, un utilisateur averti ne peut pas se tromper en accumulant les connaissances et les compétences appropriées pour rester en sécurité, et être vraiment leur propre banque.

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