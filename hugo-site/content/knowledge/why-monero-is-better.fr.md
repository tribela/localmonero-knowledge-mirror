---
title: "Pourquoi Monero est meilleur que Dash, Zcash, Zcoin (même avec Lelantus), Grin et les mélangeurs Bitcoin comme Wasabi (mis à jour en mai 2020)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Toutes les crypto-monnaies centrées sur la confidentialité ne peuvent pas offrir 100% de confidentialité, d'intraçabilité, de sécurité et de fongibilité dans une crypto-monnaie 100% décentralisée avec une configuration sans confiance. Voici quels sont ces attributs et pourquoi ils sont importants :

Privé
    Vos finances ne sont pas visibles par le public. Une personne regardant la blockchain ne pourra pas voir combien d'argent vous avez.
Intraçable
    Les jetons ne peuvent pas être tracés par de l'analyse de la blockchain ou de la surveillance de la blockchain.
Sécurisé
    Toutes les transactions sont chiffrées et le portefeuille qui contient vos fonds est chiffré.
Fongible
    Toutes les jetons sont égaux et ont la même valeur.
Décentralisé
    Tous les nœuds (un nœud est une instance en cours d'exécution de la blockchain de la crypto-monnaie) du réseau sont égaux. Il n'y a pas de superclasse de nœuds qui aient plus d'influence ou de contrôle sur les transactions ou le système que les autres nœuds.

## Analyse des crypto-monnaies

Voici une analyse des crypto-monnaies bien connues qui revendiquent l'anonymat et/ou l'intraçabilité comme principal différenciateur. Bitcoin lui-même n'entre pas dans le cadre de cette analyse car il n'a jamais prétendu être anonyme.

Ce site a été créé par des utilisateurs de Monero. Il fut un temps où nous n'étions pas des utilisateurs de Monero mais étions préoccupés par la confidentialité financière. Nous avons recherché les crypto-monnaies qui prétendaient être privées et cette page est le résultat de nos recherches. C'est pourquoi nous avons choisi Monero par rapport au reste. Donc, si nous semblons être partiaux, nous le sommes, mais nous pensons que ce parti pris est basé sur des faits que vous pouvez lire ci-dessous et vérifier par vous-même.

### Aperçu

Sélectionnez un logo pour passer à l'analyse de cette crypto-monnaie.

| Privé| Intraçable| Sécurisé| Fongible| Décentralisé  
---|---|---|---|---|---  
Monero| Oui| Oui| Oui| Oui| Oui  
DASH| Non| Non| Oui| Non| Non  
Zcash| Non| Pas complètement| Oui| Non| Non  
| Oui| Oui| Oui| Oui| Non  
| Parfois| Non| Oui| Incertain| Oui  
Bitcoin mixers| Non| Non| Oui| Non| Parfois  
  
### Monero

Privé
    Monero utilise un système cryptographique solide qui vous permet d'envoyer et de recevoir des fonds sans que vos transactions soient visibles publiquement sur la blockchain (le registre distribué des transactions). Cela garantit que vos achats, reçus et autres transferts restent **privés par défaut**. L'expéditeur, le destinataire et le montant de la transaction sont tous privés. Certaines crypto-monnaies ont une « liste des riches » qui permet à quiconque de voir quel compte a le plus de jetons. Étant donné que Monero est privé, une [liste de riches en Monero](http://moneroblocks.info/richlist) ne peut pas exister.
Intraçable
    En tirant parti des signatures de cercle (une propriété spéciale de certains types de cryptographie), Monero permet des transactions intraçables. Cela signifie qu'il est ambigu de savoir quels fonds ont été dépensés, et donc extrêmement peu probable qu'une transaction puisse être liée à un utilisateur en particulier.
Sécurisé
    À l'aide d'un réseau de consensus pair-à-pair distribué, chaque transaction est sécurisée par cryptographie. Les comptes individuels ont une phrase mnémonique de 25 mots affichée lors de la création, qui peut être écrite pour sauvegarder le compte. Un mot de passe est obligatoire lors de la création d'un portefeuille, et les fichiers de compte sont chiffrés avec une phrase de passe pour s'assurer qu'ils sont sans valeur en cas de vol.
Fongible
    Tous les jetons sont égaux et ont la même valeur. Un utilisateur, un fournisseur ou toute autre entité ne peut pas bloquer ou mettre sur liste noire certains jetons Monero car l'historique des transactions des jetons Monero est ambigu.
Décentralisé
    Tous les nœuds Monero sont égaux. Il n'y a pas de superclasse de nœuds qui ont plus d'influence ou de contrôle sur les transactions que les autres nœuds. Aucune personne ou entité ne peut retracer les transactions en possédant plusieurs nœuds. De plus, il n'y a pas de configuration de confiance. Cela signifie que le besoin de faire confiance à une personne ou à une entité n'est pas un facteur. Les seules choses qui doivent être fiables sont le code source (qui peut être vérifié par n'importe qui) et les mathématiques.

Monero est 100% Open Source depuis sa création, ce qui signifie que n'importe qui peut voir le [code source](https://github.com/monero-project/bitmonero) du logiciel pour vérifier qu'aucune porte dérobée n'existe et que le logiciel est sécurisé.

Monero a également [des articles de recherche évalués par des pairs](https://lab.getmonero.org/) qui vérifient mathématiquement et systématiquement toutes ses propriétés énumérées ci-dessus.

### DASH

Privé
    

DASH a une [liste des riches](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), donc ce n'est pas une crypto-monnaie privée. Les détails financiers des adresses des jetons sont visibles pour toute personne examinant la blockchain.

> DASH n'est pas du tout cryptographiquement privé. En fait, j'avais une diapositive qui ressemblait à « DASH, LOL >>, et comme rien d'autre … c'est de l'huile de serpent et je suis juste un peu hors de moi à ce sujet, personnellement. 
> 
> **Gregory Maxwell** , développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , un autre développeur et cryptographe Bitcoin Core, a fait une [déclaration similaire](https://twitter.com/petertoddbtc/status/622022840330682368).

Intraçable
    Les transactions sont acheminées via une série de [Masternodes](https://www.dash.org/masternodes/) (nœuds maîtres) pour les rendre intraçables. Cette pratique pourrait fonctionner si tous les opérateurs de masternode n'avaient que des motifs purs. Cependant, si un gouvernement, un groupe de pirates informatiques, une autre entité ou même un individu achetait de nombreux masternodes (il n'y aurait aucun moyen de savoir si cela s'était produit) et si la transaction passait par une route où tous les masternodes appartenaient à cette entité, la transaction pourrait alors être tracée par cette entité. Compte tenu du coût relativement faible des masternodes et de l'énorme budget des gouvernements et de certaines organisations, la possibilité que les jetons puissent être tracés est réelle.
Sécurisé
    Les transactions sont cryptographiquement sécurisées.
Fongible
    Étant donné que les transactions ne sont pas privées, il est possible qu'une entité bloque ou mette sur liste noire certains jetons, les rendant moins précieux que les autres. Voir la note sur le manque de fongibilité de Bitcoin ci-dessous puisque le même principe s'applique au DASH.
Décentralisé
    Tous les nœuds DASH ne sont pas égaux. Il existe une superclasse de nœuds, appelés _Masternodes_ dont les propriétaires ont plus d'influence sur le système que les opérateurs de nœuds normaux. Cela rend DASH semi-centralisé au lieu du système idéal 100% décentralisé.

### Zcash

Privé
    

Les transactions Zcash sont visibles sur leur blockchain. Il est possible de masquer les transactions, mais [ moins de 1% des transactions sont entièrement protégées](http://stat.bloxy.info/superset/dashboard/zcash/). Étant donné que les transactions cachées sont facultatives et non par défaut (pour ne pas dire rarement utilisées), les transactions cachées [se démarquent sur leur blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/), attirant l'attention sur elles-mêmes.

> Et au fait, je pense que nous pouvons réussir à rendre Zcash suffisamment traçable pour les criminels comme WannaCry, mais toujours complètement privé & fongible. 
> 
> **Zooko Wilcox** , PDG de Zcash, dans un tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Si Zcash peut être « suffisamment traçable », alors il ne peut pas être complètement privé ou fongible. 

Intraçable
    

Les transactions régulières sont transparentes. Les transactions cachées utilisent zk-SNARKS, qui présentent de solides garanties de confidentialité sous certaines conditions. La question est de savoir si ces conditions sont remplies, et vu le nombre infime de personnes utilisant les capacités blindées, cela reste incertain.

Sécurisé
    Les transactions sont cryptographiquement sécurisées.
Fongible
    Étant donné que toutes les transactions ne sont pas privées, il est possible qu'une entité bloque ou mette sur liste noire certains jetons, les rendant moins précieux que les autres. Vous pouvez aussi consulter la note sur le manque de fongibilité de Bitcoin ci-dessous puisque le même principe s'applique à Zcash.
Décentralisé
    

Zcash est une entreprise et actuellement, elle [prend 20% de toutes les ZEC minés en tant que récompense pour les fondateurs](https://z.cash/blog/funding.html). 

Zcash nécessitait une **configuration sécurisée**. Cela signifie que vous devez avoir confiance que le système a été mis en place honnêtement. S'il n'était pas mis en place honnêtement, [des quantités illimitées de ZEC pourraient être créées sans que personne ne le sache](https://blog.okturtles.com/2016/03/the-zcash-catch/). Cela rendrait le pirate riche et dévaloriserait ZEC. Il n'y a aucun moyen de savoir si la configuration sécurisée a été exécutée honnêtement. Nous devons les croire sur parole. Cela introduit un point de défaillance humain dans le système qui est contraire à presque toutes les autres crypto-monnaies. Vous ne devriez avoir à faire confiance qu'aux mathématiques et au code source vérifiable des crypto-monnaies, pas aux humains. Comme nous l'avons vu avec pratiquement toutes les grandes sociétés de logiciels, telles que [Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), et même les gouvernements, il ne faut pas leur faire confiance. 

Peter Todd, un développeur Bitcoin Core qui [a participé ](https://github.com/zcash/mpc/blob/master/README.md) à la configuration sécurisée de Zcash, l'a appelée " [porte dérobée (backdoor)](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash n'est pas incontestablement sécurisé, et ne peut pas l'être avec la technologie actuelle ... il faut une configuration de confiance … il faudra refaire la procédure [Configuration de confiance] pour mettre à jour la cryptographie au fil du temps, ce qui constitue donc une vulnérabilité. 
> 
> Gregory Maxwell, développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Remarque :** Zcoin passe de son modèle actuel Sigma à un nouveau protocole qui s'appuie sur son nouveau travail, Lelantus. Lelantus va être mis en œuvre par étapes, et cet article suppose que toutes les étapes sont terminées et mises en œuvre pour des comparaisons appropriées parallèlement aux temps de mise en œuvre prévus.

La raison pour laquelle Zcoin s'est offert le luxe d'être jugé sur son futur protocole, et non sur Zcash, est que Zcoin a une feuille de route avec des délais généraux d'activation, alors que les plans de « confidentialité par défaut » de Zcash sont et continuent d'être nébuleux.

Privé
    

Zcoin (XZC) n'aura pas de liste riche, il sera donc privé. Par défaut, la confidentialité obligatoire devrait être mise en place en 2021. Une fois mise en œuvre, il ne sera pas possible de créer une liste enrichie (bien qu'actuellement [il en ait une](https://www.coinexplorer.net/XZC/richlist)).

Intraçable
    Avec la dernière étape de Lelantus mise en œuvre en 2021, Zcoin ne devrait pas être traçable, bien que les attaques théoriques n'aient pas encore été explorées puisqu'il n'a pas encore été publié ou n'a pas encore passé de temps dans la nature. À l'heure actuelle, Zcoin est traçable si l'on met une [adresse Zcoin](https://explorer.zcoin.io/) dans un explorateur de blockchain et ainsi vous pouvez voir son solde et les transactions associées.
Sécurisé
    Les transactions sont cryptographiquement sécurisées.
Fongible
    Après la mise en service de la dernière étape de Lelantus en 2021, il est supposé que Zcoin sera fongible en raison de l'application obligatoire de la confidentialité. À cet égard, il sera un véritable concurrent de Monero. Cependant …
Décentralisé
    Zcoin a implémenté des Znodes, qui agissent de la même manière que les masternodes Dash, et ont une plus grande puissance que les autres nœuds du réseau. Étant donné que tous les nœuds ne sont pas créés égaux et que le facteur de différenciation entre eux est la somme d'argent dont dispose un individu (les nœuds Z coûtent 1000 XZC), le réseau est semi-centralisé.

Privé
    Grin n'a pas de « liste des riches », ce qui indiquerait une certaine forme de confidentialité. En effet, les attaquants passifs scannant la chaîne ne peuvent pas voir quelle adresse contient combien d'argent, en partie parce que les montants sont obscurcis via des transactions confidentielles, en partie parce que les données d'adresse ne sont pas stockées sur la chaîne, et en partie à cause de la technologie de transition de Mimblewimble, où les transactions intermédiaires peuvent être retirées de la chaîne, laissant peu de métadonnées des transactions passées.
Intraçable
    Grin ne se défend pas contre un attaquant actif construisant un graphe de transaction. Il est possible à la fois pour les mineurs et pour un nœud légèrement modifié de surveiller chaque transaction, de la sauvegarder avant que la technologie de transition n'entre en vigueur et de créer un graphe des transaction complet à partir d'ici, tout en conservant toutes les données « transparentes ». Ils ne seraient pas en mesure de discerner des informations avant qu'ils commencent, mais tout ce qui se produira après leur démarrage constituera des métadonnées précieuses avec lesquelles ils pourraient potentiellement lier des transactions.
Sécurisé
    Les transactions sont cryptographiquement sécurisées.
Fongible
    Étant donné que toutes les transactions sont privées d'une manière questionnable, et donc potentiellement traçables, il existe la possibilité de créer un graphe de transactions, à partir duquel peuvent être glanées de précieuses informations qui peuvent être utilisées contre un individu concernant ses habitudes de dépenses. Les sorties peuvent alors être liées à des identités, et, même si les montants ne sont pas visibles, le fait qu'une sortie puisse être liée à une identité signifie que la sortie peut être comme marquée, simplement sur la base de qui l'a détenue. Nous pensons que cela signifie que Grin n'est pas fongible, car certaines sorties peuvent être marquées tandis que d'autres ne le seront pas.
Décentralisé
    Grin n'a pas de jetons pré-minés, de récompense pour les fondateurs, de masternodes ou de trésorerie. Ils n'avaient pas d'ICO et sont gérés d'une manière digne d'une communauté décentralisée. Grin est décentralisé.

### Bitcoin Mixers

Privé
    

Toutes les transactions Bitcoin sont visibles sur la blockchain et il existe une [liste des riches en Bitcoins](http://www.bitcoinrichlist.com/top100), donc Bitcoin n'est pas privé. Bitcoin est [pseudonyme](https://bitcoin.org/en/you-need-to-know), pas anonyme. 

Pour les **mélangeurs de Bitcoin** , vous devez avoir confiance qu'ils peuvent protéger leurs données et qu'ils ne sont pas la propriété d'un gouvernement, de pirates informatiques ou d'autres entités ou ne coopèrent pas avec eux. 

En juillet 2017, le fondateur du plus grand service de mélange de Bitcoin, BITMIXER.IO, a annoncé sa fermeture et en a donné la raison : 

> … Maintenant, j'ai compris que Bitcoin est un système transparent non anonyme **de par sa conception**. La blockchain est un grand livre ouvert… 
> 
> BITMIXER.IO, dans une annonce de clôture sur [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphase dans l'original). 

Quelques semaines plus tard, après avoir examiné les différentes crypto-monnaies centrées sur la confidentialité, il a déclaré ceci : 

> Après une enquête approfondie, je confirme que MONERO est la meilleure devise de confidentialité. Je recommande donc fortement MONERO à toutes les personnes qui ont besoin de plus de confidentialité. 
> 
> BITMIXER.IO, dans un post de suivi [](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Intraçable
    

Étant donné que toutes les transactions Bitcoin sont visibles sur la blockchain, TOUTES les transactions Bitcoin peuvent être tracées. Un mélangeur Bitcoin peut fortement obscurcir les transactions, ce qui rend beaucoup plus difficile pour quelqu'un de retracer les Bitcoins, mais pas impossible. Au fur et à mesure que la technologie progresse et que les entreprises spécialisées dans le traçage des transactions Bitcoin deviennent plus répandues, les transactions autrefois très obscurcies deviendront relativement facilement traçables : 

  * [Les forces de l'ordre continuent d'investir dans les services de suivi Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [Time.com : les Bitcoins sont plus faciles à suivre que vous ne le pensez ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic : une entreprise spécialisée dans le traçage de Bitcoin pour les forces de l'ordre ](https://www.elliptic.co/)

Une recherche Google révélera des dizaines d'articles comme ceux ci-dessus. Et rappelez-vous, toute transaction qui s'est produite à un moment dans le passé est sur la blockchain et a le potentiel d'être tracée, même si un service de mélange a été utilisé. En fait, l'utilisation d'un service de mélange est susceptible d'attirer l'attention sur ces transactions. 

Sécurisé
    Les transactions sont cryptographiquement sécurisées.
Fongible
    

Tous les Bitcoins ne sont pas égaux et n'ont pas la même valeur. Certains Bitcoins ont été mis sur liste noire et bloqués par plusieurs entités, ce qui rend ces jetons moins précieux que les autres. Si vous recevez des Bitcoins qui ont été utilisés dans le passé à des fins illégales, vos Bitcoins pourraient être mis sur liste noire même si vous n'avez rien à voir avec l'activité illégale. Ou, disons qu'un gouvernement, un employeur ou une autre entité décide de mettre vos Bitcoins sur liste noire à l'avenir, un peu comme ils le font avec le gel ou la confiscation des avoirs. Il n'y aurait rien que vous puissiez faire. Étant donné qu'un mélangeur ne fait que compliquer la traçabilité de vos Bitcoins, cette catégorie a été marquée comme « non fongible ». 

  * Andreas Antonopoulos, un ancien développeur de Bitcoin Core très respecté dans les communautés de Bitcoin et d'autres crypto-monnaies, reconnaît le problème de fongibilité de Bitcoin dans une [vidéo YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Discussion du problème de fongibilité Bitcoin sur [Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

Décentralisé
    Bitcoin lui-même est décentralisé, mais la plupart des services de mixage sont centralisés. Cela signifie que vous devez leur faire confiance. Cependant, certains plus récents, comme le portefeuille Wasabi, ne le sont pas.

## Résumé

À notre avis, Monero est le choix évident si vous recherchez une crypto-monnaie privée, sécurisée, intraçable, fongible et décentralisée sans configuration de confiance requise. Tout le reste met votre vie privée et votre sécurité en danger. Mais ne vous contentez pas de prendre notre avis. Faites vos propres recherches et voyez par vous-même. Considérez que Monero est approuvé et utilisé par des entités qui dépendent de la confidentialité et de l'intraçabilité, telles que : 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) a été fermé en juillet 2017. La [plainte de confiscation fédérale](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) contre AB montre que : 
    * **Monero est la seule crypto-monnaie privée et intraçable :**   
"Au total, les portefeuilles de CAZES et les agents informatiques ont pris le contrôle d'environ 8 800 000 $ en Bitcoin, Ethereum, Moreno [sic] et Zcash, répartis comme suit : 1 605,0503851 Bitcoin, 8 309,271639 Ethereum, 3 691,98 Zcash, _et un quantité inconnue de Monero._ " (bas de la p. 20 et haut de la p. 21, emphase ajoutée) 
    * **Les transactions Bitcoin ne sont pas privées et peuvent être tracées :**   
"Les agents fédéraux ont obtenu les mandats après avoir retracé un certain nombre de transactions en bitcoins provenant d'AlphaBay vers des comptes en monnaie numérique, et finalement des comptes bancaires et d'autres actifs tangibles, détenus par CAZES et son épouse.." (p. 17, lignes 24-26) 

LocalMonero ne préconise ni n'encourage aucune activité illégale. 

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

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

Toutes les crypto-monnaies centrées sur la confidentialité ne peuvent pas offrir 100% de confidentialité, d'intraçabilité, de sécurité et de fongibilité dans une crypto-monnaie 100% décentralisée avec une configuration sans confiance. Voici quels sont ces attributs et pourquoi ils sont importants :

## Analyse des crypto-monnaies

Voici une analyse des crypto-monnaies bien connues qui revendiquent l'anonymat et/ou l'intraçabilité comme principal différenciateur. Bitcoin lui-même n'entre pas dans le cadre de cette analyse car il n'a jamais prétendu être anonyme.

Ce site a été créé par des utilisateurs de Monero. Il fut un temps où nous n'étions pas des utilisateurs de Monero mais étions préoccupés par la confidentialité financière. Nous avons recherché les crypto-monnaies qui prétendaient être privées et cette page est le résultat de nos recherches. C'est pourquoi nous avons choisi Monero par rapport au reste. Donc, si nous semblons être partiaux, nous le sommes, mais nous pensons que ce parti pris est basé sur des faits que vous pouvez lire ci-dessous et vérifier par vous-même.

Ce site a été créé par des utilisateurs de Monero. Il fut un temps où nous n'étions pas des utilisateurs de Monero mais étions préoccupés par la confidentialité financière. Nous avons recherché les crypto-monnaies qui prétendaient être privées et cette page est le résultat de nos recherches. C'est pourquoi nous avons choisi Monero par rapport au reste. Donc, si nous semblons être partiaux, nous le sommes, mais nous pensons que ce parti pris est basé sur des faits que vous pouvez lire ci-dessous et vérifier par vous-même.

### Aperçu

Sélectionnez un logo pour passer à l'analyse de cette crypto-monnaie.

### Monero

Monero est 100% Open Source depuis sa création, ce qui signifie que n'importe qui peut voir le [code source](https://github.com/monero-project/bitmonero) du logiciel pour vérifier qu'aucune porte dérobée n'existe et que le logiciel est sécurisé.

Monero a également [des articles de recherche évalués par des pairs](https://lab.getmonero.org/) qui vérifient mathématiquement et systématiquement toutes ses propriétés énumérées ci-dessus.

### DASH

DASH a une [liste des riches](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), donc ce n'est pas une crypto-monnaie privée. Les détails financiers des adresses des jetons sont visibles pour toute personne examinant la blockchain.

> DASH n'est pas du tout cryptographiquement privé. En fait, j'avais une diapositive qui ressemblait à « DASH, LOL >>, et comme rien d'autre … c'est de l'huile de serpent et je suis juste un peu hors de moi à ce sujet, personnellement. 
> 
> **Gregory Maxwell** , développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH n'est pas du tout cryptographiquement privé. En fait, j'avais une diapositive qui ressemblait à « DASH, LOL >>, et comme rien d'autre … c'est de l'huile de serpent et je suis juste un peu hors de moi à ce sujet, personnellement. 

DASH n'est pas du tout cryptographiquement privé. En fait, j'avais une diapositive qui ressemblait à « DASH, LOL >>, et comme rien d'autre … c'est de l'huile de serpent et je suis juste un peu hors de moi à ce sujet, personnellement. 

**Gregory Maxwell** , développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , un autre développeur et cryptographe Bitcoin Core, a fait une [déclaration similaire](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Les transactions Zcash sont visibles sur leur blockchain. Il est possible de masquer les transactions, mais [ moins de 1% des transactions sont entièrement protégées](http://stat.bloxy.info/superset/dashboard/zcash/). Étant donné que les transactions cachées sont facultatives et non par défaut (pour ne pas dire rarement utilisées), les transactions cachées [se démarquent sur leur blockchain](http://weuse.cash/2016/06/09/btc-xmr-zcash/), attirant l'attention sur elles-mêmes.

> Et au fait, je pense que nous pouvons réussir à rendre Zcash suffisamment traçable pour les criminels comme WannaCry, mais toujours complètement privé & fongible. 
> 
> **Zooko Wilcox** , PDG de Zcash, dans un tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Et au fait, je pense que nous pouvons réussir à rendre Zcash suffisamment traçable pour les criminels comme WannaCry, mais toujours complètement privé & fongible. 

Et au fait, je pense que nous pouvons réussir à rendre Zcash suffisamment traçable pour les criminels comme WannaCry, mais toujours complètement privé & fongible. 

**Zooko Wilcox** , PDG de Zcash, dans un tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Si Zcash peut être « suffisamment traçable », alors il ne peut pas être complètement privé ou fongible. 

Les transactions régulières sont transparentes. Les transactions cachées utilisent zk-SNARKS, qui présentent de solides garanties de confidentialité sous certaines conditions. La question est de savoir si ces conditions sont remplies, et vu le nombre infime de personnes utilisant les capacités blindées, cela reste incertain.

Zcash est une entreprise et actuellement, elle [prend 20% de toutes les ZEC minés en tant que récompense pour les fondateurs](https://z.cash/blog/funding.html). 

Zcash nécessitait une **configuration sécurisée**. Cela signifie que vous devez avoir confiance que le système a été mis en place honnêtement. S'il n'était pas mis en place honnêtement, [des quantités illimitées de ZEC pourraient être créées sans que personne ne le sache](https://blog.okturtles.com/2016/03/the-zcash-catch/). Cela rendrait le pirate riche et dévaloriserait ZEC. Il n'y a aucun moyen de savoir si la configuration sécurisée a été exécutée honnêtement. Nous devons les croire sur parole. Cela introduit un point de défaillance humain dans le système qui est contraire à presque toutes les autres crypto-monnaies. Vous ne devriez avoir à faire confiance qu'aux mathématiques et au code source vérifiable des crypto-monnaies, pas aux humains. Comme nous l'avons vu avec pratiquement toutes les grandes sociétés de logiciels, telles que [Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), et même les gouvernements, il ne faut pas leur faire confiance. 

Peter Todd, un développeur Bitcoin Core qui [a participé ](https://github.com/zcash/mpc/blob/master/README.md) à la configuration sécurisée de Zcash, l'a appelée " [porte dérobée (backdoor)](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash n'est pas incontestablement sécurisé, et ne peut pas l'être avec la technologie actuelle ... il faut une configuration de confiance … il faudra refaire la procédure [Configuration de confiance] pour mettre à jour la cryptographie au fil du temps, ce qui constitue donc une vulnérabilité. 
> 
> Gregory Maxwell, développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash n'est pas incontestablement sécurisé, et ne peut pas l'être avec la technologie actuelle ... il faut une configuration de confiance … il faudra refaire la procédure [Configuration de confiance] pour mettre à jour la cryptographie au fil du temps, ce qui constitue donc une vulnérabilité. 

Zcash n'est pas incontestablement sécurisé, et ne peut pas l'être avec la technologie actuelle ... il faut une configuration de confiance … il faudra refaire la procédure [Configuration de confiance] pour mettre à jour la cryptographie au fil du temps, ce qui constitue donc une vulnérabilité. 

Gregory Maxwell, développeur et cryptographe Bitcoin Core, dans une présentation [à Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Remarque :** Zcoin passe de son modèle actuel Sigma à un nouveau protocole qui s'appuie sur son nouveau travail, Lelantus. Lelantus va être mis en œuvre par étapes, et cet article suppose que toutes les étapes sont terminées et mises en œuvre pour des comparaisons appropriées parallèlement aux temps de mise en œuvre prévus.

La raison pour laquelle Zcoin s'est offert le luxe d'être jugé sur son futur protocole, et non sur Zcash, est que Zcoin a une feuille de route avec des délais généraux d'activation, alors que les plans de « confidentialité par défaut » de Zcash sont et continuent d'être nébuleux.

Zcoin (XZC) n'aura pas de liste riche, il sera donc privé. Par défaut, la confidentialité obligatoire devrait être mise en place en 2021. Une fois mise en œuvre, il ne sera pas possible de créer une liste enrichie (bien qu'actuellement [il en ait une](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

Toutes les transactions Bitcoin sont visibles sur la blockchain et il existe une [liste des riches en Bitcoins](http://www.bitcoinrichlist.com/top100), donc Bitcoin n'est pas privé. Bitcoin est [pseudonyme](https://bitcoin.org/en/you-need-to-know), pas anonyme. 

Pour les **mélangeurs de Bitcoin** , vous devez avoir confiance qu'ils peuvent protéger leurs données et qu'ils ne sont pas la propriété d'un gouvernement, de pirates informatiques ou d'autres entités ou ne coopèrent pas avec eux. 

En juillet 2017, le fondateur du plus grand service de mélange de Bitcoin, BITMIXER.IO, a annoncé sa fermeture et en a donné la raison : 

> … Maintenant, j'ai compris que Bitcoin est un système transparent non anonyme **de par sa conception**. La blockchain est un grand livre ouvert… 
> 
> BITMIXER.IO, dans une annonce de clôture sur [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphase dans l'original). 

… Maintenant, j'ai compris que Bitcoin est un système transparent non anonyme **de par sa conception**. La blockchain est un grand livre ouvert… 

… Maintenant, j'ai compris que Bitcoin est un système transparent non anonyme **de par sa conception**. La blockchain est un grand livre ouvert… 

BITMIXER.IO, dans une annonce de clôture sur [Bitcointalk.org](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (emphase dans l'original). 

Quelques semaines plus tard, après avoir examiné les différentes crypto-monnaies centrées sur la confidentialité, il a déclaré ceci : 

> Après une enquête approfondie, je confirme que MONERO est la meilleure devise de confidentialité. Je recommande donc fortement MONERO à toutes les personnes qui ont besoin de plus de confidentialité. 
> 
> BITMIXER.IO, dans un post de suivi [](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Après une enquête approfondie, je confirme que MONERO est la meilleure devise de confidentialité. Je recommande donc fortement MONERO à toutes les personnes qui ont besoin de plus de confidentialité. 

Après une enquête approfondie, je confirme que MONERO est la meilleure devise de confidentialité. Je recommande donc fortement MONERO à toutes les personnes qui ont besoin de plus de confidentialité. 

BITMIXER.IO, dans un post de suivi [](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Étant donné que toutes les transactions Bitcoin sont visibles sur la blockchain, TOUTES les transactions Bitcoin peuvent être tracées. Un mélangeur Bitcoin peut fortement obscurcir les transactions, ce qui rend beaucoup plus difficile pour quelqu'un de retracer les Bitcoins, mais pas impossible. Au fur et à mesure que la technologie progresse et que les entreprises spécialisées dans le traçage des transactions Bitcoin deviennent plus répandues, les transactions autrefois très obscurcies deviendront relativement facilement traçables : 

  * [Les forces de l'ordre continuent d'investir dans les services de suivi Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [Time.com : les Bitcoins sont plus faciles à suivre que vous ne le pensez ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic : une entreprise spécialisée dans le traçage de Bitcoin pour les forces de l'ordre ](https://www.elliptic.co/)

Une recherche Google révélera des dizaines d'articles comme ceux ci-dessus. Et rappelez-vous, toute transaction qui s'est produite à un moment dans le passé est sur la blockchain et a le potentiel d'être tracée, même si un service de mélange a été utilisé. En fait, l'utilisation d'un service de mélange est susceptible d'attirer l'attention sur ces transactions. 

Tous les Bitcoins ne sont pas égaux et n'ont pas la même valeur. Certains Bitcoins ont été mis sur liste noire et bloqués par plusieurs entités, ce qui rend ces jetons moins précieux que les autres. Si vous recevez des Bitcoins qui ont été utilisés dans le passé à des fins illégales, vos Bitcoins pourraient être mis sur liste noire même si vous n'avez rien à voir avec l'activité illégale. Ou, disons qu'un gouvernement, un employeur ou une autre entité décide de mettre vos Bitcoins sur liste noire à l'avenir, un peu comme ils le font avec le gel ou la confiscation des avoirs. Il n'y aurait rien que vous puissiez faire. Étant donné qu'un mélangeur ne fait que compliquer la traçabilité de vos Bitcoins, cette catégorie a été marquée comme « non fongible ». 

  * Andreas Antonopoulos, un ancien développeur de Bitcoin Core très respecté dans les communautés de Bitcoin et d'autres crypto-monnaies, reconnaît le problème de fongibilité de Bitcoin dans une [vidéo YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Discussion du problème de fongibilité Bitcoin sur [Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Résumé

À notre avis, Monero est le choix évident si vous recherchez une crypto-monnaie privée, sécurisée, intraçable, fongible et décentralisée sans configuration de confiance requise. Tout le reste met votre vie privée et votre sécurité en danger. Mais ne vous contentez pas de prendre notre avis. Faites vos propres recherches et voyez par vous-même. Considérez que Monero est approuvé et utilisé par des entités qui dépendent de la confidentialité et de l'intraçabilité, telles que : 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purism ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) a été fermé en juillet 2017. La [plainte de confiscation fédérale](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) contre AB montre que : 
    * **Monero est la seule crypto-monnaie privée et intraçable :**   
"Au total, les portefeuilles de CAZES et les agents informatiques ont pris le contrôle d'environ 8 800 000 $ en Bitcoin, Ethereum, Moreno [sic] et Zcash, répartis comme suit : 1 605,0503851 Bitcoin, 8 309,271639 Ethereum, 3 691,98 Zcash, _et un quantité inconnue de Monero._ " (bas de la p. 20 et haut de la p. 21, emphase ajoutée) 
    * **Les transactions Bitcoin ne sont pas privées et peuvent être tracées :**   
"Les agents fédéraux ont obtenu les mandats après avoir retracé un certain nombre de transactions en bitcoins provenant d'AlphaBay vers des comptes en monnaie numérique, et finalement des comptes bancaires et d'autres actifs tangibles, détenus par CAZES et son épouse.." (p. 17, lignes 24-26) 

  * **Monero est la seule crypto-monnaie privée et intraçable :**   
"Au total, les portefeuilles de CAZES et les agents informatiques ont pris le contrôle d'environ 8 800 000 $ en Bitcoin, Ethereum, Moreno [sic] et Zcash, répartis comme suit : 1 605,0503851 Bitcoin, 8 309,271639 Ethereum, 3 691,98 Zcash, _et un quantité inconnue de Monero._ " (bas de la p. 20 et haut de la p. 21, emphase ajoutée) 
  * **Les transactions Bitcoin ne sont pas privées et peuvent être tracées :**   
"Les agents fédéraux ont obtenu les mandats après avoir retracé un certain nombre de transactions en bitcoins provenant d'AlphaBay vers des comptes en monnaie numérique, et finalement des comptes bancaires et d'autres actifs tangibles, détenus par CAZES et son épouse.." (p. 17, lignes 24-26) 

LocalMonero ne préconise ni n'encourage aucune activité illégale. 

LocalMonero ne préconise ni n'encourage aucune activité illégale. 

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

  * [Wired Magazine se trompe sur Monero, voici pourquoi](/knowledge/wired-article-debunked)/

  * [Démystification des 15 principaux mythes et inquiétudes au sujet de Monero](/knowledge/monero-myths-debunked)/

  * [Comment Dandelion++ garde les origines des transactions de Monero privées](/knowledge/monero-dandelion)/

  * [Pourquoi Monero est Open Source et décentralisé](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Le minage de Monero : ce qui rend RandomX si spécial](/knowledge/monero-mining-randomx)/

Ressources complémentaires