---
title: "Explication des sorties Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, comme d'autres crypto-monnaies, utilise les « sorties » comme moyen de comptabiliser les fonds. Les utilisateurs s'intéressant au fonctionnement du domaine crypto ont probablement déjà entendu ce terme, mais tout le monde ne comprend pas ce que cela signifie et comment cela fonctionne. Comme exploré dans notre [article sur les signatures de cercle](/knowledge/ring-signatures), les sorties sont l'unité réelle échangée sur la blockchain entre les acteurs effectuant une transaction. Semblable à un billet d'un euro, mais le montant n'est pas dans une dénomination fixe.

Si vous êtes payé 35€ pour un travail, vous pourriez recevoir un billet de 5 euros, un billet de 10 euros et un billet de 20 euros. Vous avez 35€, mais vous avez également trois billets différents dans votre portefeuille. Si vous souhaitez payer 13€ à quelqu'un, vous pouvez utiliser les billets de 5 et de 10 euros, mais si vous souhaitez payer 18€ à quelqu'un, vous ne pouvez utiliser que le billet de 10 euros et donc recevoir 2 euros en retour. Enfin, si vous souhaitez payer 33€ à quelqu'un, vous devez utiliser les trois billets et donc vous recevez 2€ en retour, mais pendant un moment, lorsque vous remettez les trois billets, vous n'avez pas d'argent dans votre portefeuille jusqu'à ce que vous obteniez le reste de la monnaie vous revenant.

Monero fonctionne de la même manière. Supposons que vous dirigiez un magasin et réalisiez trois ventes sur trois articles différents. Vous pouvez recevoir 1,5 XMR, 2,25 XMR et 5,25 XMR pour un total de 9 XMR, mais vous avez également dans votre portefeuille trois sorties, dont les montants sont différents des transactions indiquées précédemment. Tout comme avec les euros, vous voudrez peut-être payer 3 XMR à quelqu'un. Vous pouvez utiliser uniquement la sortie 5,25 XMR et recevoir 2,25 XMR en retour, ou vous pouvez combiner les sorties 1,5 et 2,25 XMR et obtenir 0,75 XMR en retour.

Mais, dès que vous envoyez la transaction, les sorties que vous utilisez sont mises dans un état « verrouillé », ce qui signifie qu'elles sont inaccessibles jusqu'à ce que vous receviez le change. Le protocole débloque les fonds (c'est-à-dire vous rend la monnaie) après 10 confirmations, soit environ 20 minutes. Tout comme une fois que vous avez donnez les billets en euros depuis votre portefeuille, vous ne pouvez plus utiliser l'argent tant que vous n'avez pas reçu la monnaie, votre Monero est inaccessible jusqu'à ce que vous receviez la monnaie.

Revenons à l'exemple de l'envoi de 3 XMR à quelqu'un, et vous utilisez la sortie 5,25 XMR. Pendant que vous attendez de recevoir 1,75 XMR en retour, vous ne pouvez pas l'utiliser. Ces 1,75 XMR vous sont inaccessibles. Mais vous pouvez toujours utiliser les sorties 1,5 XMR et 2,25 XMR, car elles n'ont pas été dépensées. Pour en revenir à l'exemple avec les euros, si vous payez quelqu'un 13€, comme dans l'exemple précédent, vous ne pourrez pas utiliser les 2€ que vous attendez en retour jusqu'à ce qu'ils vous soient donnés, mais dans cet exemple, vous avez toujours un billet de 20 euros inutilisé dans votre portefeuille. Il peut toujours être utilisé pour acheter ce que vous voulez pendant que vous attendez le change. C'est la même chose avec Monero.

C'est souvent un point de confusion pour les nouveaux utilisateurs de Monero. Souvent, un utilisateur peut n'avoir qu'une seule sortie dans son portefeuille, reçue d'un échange ou d'un ami. Disons que cette sortie est de 20 XMR. Ils n'ont pas d'autres sorties dans leur portefeuille. Ils veulent maintenant faire un don à deux de leurs organismes de bienfaisance préférés. Ils envoient 5 XMR au premier organisme de bienfaisance et sont ensuite confus car, même s'il leur reste 15 XMR, ils ne peuvent pas envoyer immédiatement le prochain don au deuxième organisme de bienfaisance. Comme vous l'avez peut-être deviné, c'est parce que les 15 XMR sont verrouillés. Ils ne peuvent pas être dépensés tant qu'ils ne sont pas rendus en tant que monnaie (10 confirmations, soit environ 20 minutes). Une fois leurs fonds débloqués, ils pourront envoyer leur deuxième don.

Juste pour réitérer le point, ils n'auraient pas eu ce problème s'ils avaient eu plusieurs sorties à la place, comme par exemple deux sorties de 10 XMR. Ils pourraient envoyer les deux dons l'un après l'autre, car le premier don utiliserait l'une des deux sorties de 10 XMR (et attendrait 10 confirmations pour recevoir 5 XMR en retour), et le deuxième don utiliserait l'autre sortie de 10 XMR.

Certains portefeuilles de crypto-monnaie ont une fonctionnalité appelée « gestion des sorties », qui montre simplement à un utilisateur les sorties dont il dispose actuellement (en plus de leur somme totale), et lui permet de choisir celles qu'il souhaite utiliser lorsqu'il dépense de la crypto-monnaie.

À partir de maintenant, le portefeuille officiel Monero GUI (avec interface graphique) sélectionne automatiquement les sorties pour les utilisateurs, car les utilisateurs sélectionnant leurs propres sorties entraînent souvent une confusion ou, dans certains cas, une atteinte à la confidentialité. Il existe cependant des portefeuilles en cours de construction, tels que le nouveau projet de portefeuille Feather, qui contiendront ces fonctionnalités de gestion des sorties par l'utilisateur.

Nous avons beaucoup parlé de la partie envoi, mais quelque chose de fascinant se produit du côté de la réception. Pour en revenir à notre exemple d'envoi de 3 XMR à une personne, et en utilisant vos sorties de 1,5 XMR et 2,25 XMR dans la transaction (tout en s'attendant à recevoir un change de 0,75 XMR), elle ne reçoit PAS deux sorties de 1,5 XMR et 2,25 XMR. Elle reçoit à la place UNE seule sortie de 3 XMR.

En arrière-plan, le protocole combine toutes les sorties utilisées pour les dépenses, donne au destinataire une sortie du montant payé et renvoie une sortie de modification à l'expéditeur. Ainsi, l'expéditeur recevra également une sortie en tant que monnaie, qu'il ait utilisé deux, trois ou dix sorties pour envoyer la transaction.

Nous espérons que cela a dissipé une certaine confusion concernant les sorties et le fonctionnement de la comptabilité interne du protocole, ainsi que le problème de confusion rencontré par l'utilisateur courant lorsqu'il fait face à des fonds bloqués. Dans un autre article, nous explorerons la gestion de vos sorties afin de minimiser le risque de devoir attendre le déblocage des fonds avant d'effectuer d'autres transactions.

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