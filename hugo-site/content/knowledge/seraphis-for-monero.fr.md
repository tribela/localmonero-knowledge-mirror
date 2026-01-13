---
title: "Seraphis : ce qu'il apportera à Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis : une mise à jour de conception modulaire pour les transactions Monero

Cet article décrit [Seraphis](https://github.com/UkoeHB/Seraphis), un ensemble de structures et d'abstractions de protocole de transaction développé par le contributeur à la recherche, sous le pseudonyme de [`koe`](https://github.com/UkoeHB) pour l'écosystème Monero, et avec une analyse de sécurité en cours par un contributeur répondant au pseudonyme de [`coinstudent2048`](https://github.com/coinstudent2048).  
Nous faisons quelques simplifications et omettons certains détails techniques par souci de clarté ; pour cette raison, et parce que la conception de Seraphis est toujours en cours, les lecteurs intéressés doivent se référer à la documentation de Seraphis pour les informations les plus récentes.

## Les transactions dans Monero

Des protocoles comme Bitcoin et Monero, entre autres, reposent sur un modèle de fonctionnement dit « de sortie », où une _sortie_ est une représentation de la valeur qui peut être transférée.  
Les transactions consomment une ou plusieurs sorties contrôlées par un expéditeur et génèrent de nouvelles sorties dirigées vers les destinataires (ou vers l'expéditeur en tant que change) ; la transaction doit être équilibrée en ce que les sorties consommées doivent contenir une valeur totale exactement égale à la valeur des nouvelles sorties (plus des frais de fonctionnement demandés par le réseau).  
Dans de nombreux protocoles comme Bitcoin, la valeur contenue dans une sortie est écrite en clair, tout comme le destinataire.  
De plus, en regardant la blockchain, il est trivial de voir si et quand une sortie a été dépensée (c'est-à-dire si elle a été consommée dans une transaction ultérieure, et quelle transaction l'a dépensée).

En revanche, des protocoles comme Monero introduisent un modèle différent :

  * Les valeurs de sortie sont masquées et non visibles sur la blockchain
  * Les adresses des destinataires sont masquées par l'utilisation d'un protocole d'adressage unique
  * Le fait qu'une sortie ait été dépensée ou non est masqué par l'utilisation de signatures ambiguës

Le résultat est qu'en l'absence d'informations externes, il est difficile de déterminer si une sortie en particulier a été dépensée, quelle est sa valeur et qui en est le destinataire.

Le protocole de transaction Monero actuel s'appelle _RingCT_ et utilise plusieurs briques de construction cryptographiques pour atteindre les objectifs de ce modèle.

  * _Les engagements_ cachent des montants d'une manière mathématiquement utile
  * _Les preuves de portée_ empêchent tout dépassement qui pourrait entraîner une augmentation de la réserve
  * _Les signatures de cercle_ fournissent une ambiguïté de signataire et empêchent les tentatives de double dépense
  * _Les compensations d'engagement_ affirment que les transactions s'équilibrent

Ces briques de construction du modèle global sont soigneusement entrelacées pour créer le protocole RingCT.

Une propriété utile du protocole RingCT est que certaines de ces briques peuvent être modifiées ou mises à jour de manière à conserver le modèle et les propriétés globales intactes, tout en améliorant l'efficacité ou la sécurité. En fait, ces types de mises à jour se sont produites (ou sont prévues) plusieurs fois dans l'histoire de Monero. Les preuves de portée dans le protocole RingCT original étaient volumineuses et lentes ; elles ont ensuite été mises à jour vers un modèle appelé [Bulletproofs](https://eprint.iacr.org/2017/1066) qui a rendu les transactions plus petites et plus rapides avec une meilleure analyse de sécurité, et elles devraient être mises à jour vers un modèle encore plus récent appelé [Bulletproofs+](https://eprint.iacr.org/2020/735) qui propose d'améliorer encore plus l'efficacité. 

Un processus similaire a été suivi avec la brique de construction des signatures de cercle. Dans le protocole d'origine, un modèle appelé [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) était utilisé. Cela a ensuite été mis à jour vers un modèle plus récent appelé [CLSAG](https://eprint.iacr.org/2019/654) qui est plus rapide, entraîne des transactions plus petites et a une meilleure analyse de sécurité. Un modèle de signature de cercle encore plus récent basé sur [Triptych](https://eprint.iacr.org/2020/018) a été proposé, mais il n'a pas été sélectionné pour le déploiement en raison de ses impacts sur les opérations avec multi-signatures.

## Seraphis

Seraphis pousse cette idée un peu plus loin.  
Plutôt que de mettre à jour des briques de construction individuelles du protocole de transaction RingCT existant, il introduit un protocole différent qui peut tirer parti de différentes briques de construction et offrir des fonctionnalités améliorées.

## Briques de construction

Seraphis utilise un ensemble différent de briques de construction cryptographiques pour atteindre ses objectifs de conception.

  * _Les engagements_ cachent toujours des montants
  * _Les preuves de portée_ empêchent toujours tout dépassement qui pourrait entraîner une augmentation de la réserve
  * _Les preuves d'adhésion_ fournissent l'ambiguïté du signataire
  * _Les décalages d'engagement_ affirment toujours l'équilibre
  * _L'autorisation des preuves_ empêche les tentatives de double dépense

Remarquez le changement ici : les signatures de cercle sont remplacées par une combinaison de preuves d'adhésion et de preuves d'autorisation. En gros, les preuves d'adhésion montrent qu'une sortie consommée fait partie d'un ensemble plus large, similaire à ce qui se passe dans RingCT. Mais contrairement à RingCT, les preuves d'adhésion n'impliquent pas du tout la balise de liaison ! Les preuves d'autorisation montrent que la balise de liaison est valide et sont utilisées pour signer la transaction finale.

Étant donné que RingCT intègre la balise de liaison dans la signature ambiguë, les opérations de signature (et de multi-signatures) nécessitent davantage de calculs et il devient plus difficile de créer d'autres fonctionnalités liées aux balises. Mais dans Seraphis, la construction de preuves d'adhésion peut être déléguée en toute sécurité à d'appareils hautement fiables (qui peuvent avoir une puissance de calcul limitée, comme un portefeuille matériel) à un appareil moins fiable, et les opérations de signature (et de multi-signatures) sont beaucoup plus faciles en utilisant la preuve d'autorisation qui est beaucoup plus simple.

Heureusement, certaines des briques de construction requises par Seraphis existent déjà ailleurs et n'ont pas besoin d'être conçues à partir de zéro. Les technologies Bulletproofs et Bulletproofs+ peuvent être utilisées pour les preuves de portée. Des modifications aux systèmes de preuve de type Schnorr peuvent être utilisées pour autoriser des preuves. Et un [système de vérification efficace](https://eprint.iacr.org/2015/643) déjà utilisé comme base pour Triptych, [Lelantus](https://eprint.iacr.org/2019/373) et [Spark](https://eprint.iacr.org/2021/1173)* peut être modifié pour les preuves d'adhésion.

*Cypher Stack reçoit un financement pour le développement de Spark.

## Système d'adressage

Malheureusement, les adresses Monero actuellement utilisées ne sont pas compatibles avec Seraphis. Les utilisateurs devraient générer de nouvelles adresses à partir de leurs clés de portefeuille afin de recevoir du Monero si Seraphis était implémenté. Cependant, ce coût écosystémique s'accompagne de nombreux avantages.

Outre les avantages structurels évoqués ci-dessus, la conception de Seraphis se prête à de nombreuses possibilités de construction d'adresses différentes, chacune s'accompagnant de compromis. Bien que la forme finale de l'adresse qui sera utilsée dans Seraphis est [en cours de décision](https://github.com/monero-project/research-lab/issues/92) (un modèle recevant beaucoup d'attention est appelé [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), nous pouvons décrire certaines fonctionnalités communes et utiles.

Vous savez peut-être que les adresses Monero offrent la fonctionnalité _clé de vue_ , où vous pouvez fournir une clé de vue à un appareil ou à un tiers et lui permettre de surveiller les sorties entrantes à votre nom, mais sans renoncer à votre autorité de dépenser. Ceci est utile pour les portefeuilles, qui peuvent rester à jour tout en gardant votre clé de dépense en toute sécurité. Il est également utile dans les cas où vous souhaitez proposer un accès à une vue externe, comme dans le cas d'un organisme de bienfaisance public offrant de la transparence ou une entreprise dotée d'un service comptable.

L'inconvénient des clés de vue Monero est qu'elles ne fournissent pas un accès complet ou précis à la vue. Il n'est pas possible de détecter de manière fiable quand un portefeuille dépense des fonds, ce qui rend difficile le calcul correct des soldes du portefeuille lorsque la clé de dépense n'est pas disponible. Il n'est pas non plus actuellement possible de détecter les sorties entrantes sans connaître également la valeur contenue dans ces sorties (ce qui signifie que tout tiers chargé de trouver les sorties entrantes saura exactement combien de Monero vous acquérez).

Le système d'adressage de Seraphis peuvent résoudre ce problème. Avec Seraphis, votre adresse est équipée de différentes clés qui peuvent faire différentes choses :

  * Surveillez les sorties entrantes, mais masquez leur valeur
  * Surveillez les sorties entrantes, mais affichez leur valeur
  * Surveillez les sorties sortantes
  * Vous aider à générer des transactions, mais pas à les signer
  * Générer de nouvelles adresses (utile pour les commerçants ou les plateformes d'échanges avec de nombreux clients)

En tant que titulaire de l'adresse, vous décidez du degré d'autorité que vous déléguez à d'autres appareils ou à des tiers.

## Vue d'ensemble

Seraphis est un changement majeur dans l'écosystème Monero. Bien qu'il implique des modifications des adresses et des briques de construction de transaction, sa conception offre une flexibilité et des fonctionnalités utiles qui ne sont pas possibles avec le protocole actuel RingCT. Alors qu'une grande partie du modèle est finalisée et développée dans [une implémentation](https://github.com/UkoeHB/monero/tree/seraphis_lib), le modèle du système d'adressage et l'analyse de la sécurité sont en cours. Seraphis offre une excellente opportunité de faire avancer l'écosystème Monero !

Ressources complémentaires