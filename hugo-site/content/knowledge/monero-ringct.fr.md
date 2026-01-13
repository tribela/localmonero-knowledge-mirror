---
title: "Comment RingCT masque les montants des transactions Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
La confidentialité de Monero ne dépend pas d'un seul mécanisme qui, s'il était cassé, révélerait l'intégralité des transactions, mais plutôt de trois technologies différentes qui fonctionnent de concert pour fournir une confidentialité globale, tout en compensant les faiblesses des autres parties. Cette approche à trois volets consiste en [les signatures de cercle](/knowledge/ring-signatures), RingCT et [les adresses furtives](/knowledge/monero-stealth-addresses). Ces trois technologies masquent respectivement la sortie réelle (expéditeur), le montant et le récepteur. Aujourd'hui, nous allons parler de RingCT.

RingCT est sans doute la plus technique des trois, et peut être difficile à comprendre, donc nous n'expliquerons pas comment cela fonctionne exactement, mais plutôt comment il est possible de ne pas connaître un montant et de confirmer des informations à ce sujet . Et ne vous inquiétez pas, nous utiliserons de nombreux exemples comme toujours.

D'abord, explorons pourquoi il est important de vérifier tout ce qui concerne les montants. Pourquoi ne pouvons-nous pas les garder complètement secrets ? La réponse est qu'il existe des moyens intelligents permettant aux gens de créer de l'argent à partir de rien si on leur en donne l'occasion. Comment quelque chose comme ça pourrait-il fonctionner ? Prenons un exemple.

Si vous voulez acheter un article à votre ami et qu'il en veut dix euros, vous commencez avec dix euros et il commence avec zéro. Après que vous lui ayez donné les dix euros, il a dix euros et vous avez zéro. Vous avez commencé avec dix, et maintenant il en a dix. Aucun argent n'a été créé ou détruit dans cette transaction.

Avec les crypto-monnaies, un individu intelligent peut donner dix euros pour l'article et au lieu de recevoir zéro euro en change, il peut recevoir deux euros en retour. Au lieu de 0 et 10 menant à 10 et 0 (ou 10 = 10), c'est maintenant 0 et 10 menant à 10 et 2 (ou 10 = 12). Deux euros viennent d'être créés à partir de rien. Vous pouvez imaginer que si l'individu faisait cela plusieurs fois, il pourrait amasser une fortune gigantesque en peu de temps.

Avec Bitcoin et d'autres, ce serait facile à voir. Vous regardez les entrées et les sorties d'une transaction et vous assurez que ce qui est envoyé est égal à ce qui est reçu. Si ces montants ont été cryptés et non visibles, l'utilisateur n'a aucun moyen de vérifier que le montant qui est envoyé est le même que celui qui est reçu.

Pour tenter d'augmenter la confidentialité de Bitcoin, Gregory Maxwell a créé les transactions confidentielles (CT), une nouvelle technologie qui permettrait des montants cryptés, tout en prouvant que rien n'a été créé ou détruit au cours du processus. Comme pour la plupart des technologies de confidentialité, elle n'a pas été intégrée à Bitcoin, mais Monero tenait à l'adopter. Il y avait juste un problème. La technologie déjà mise en œuvre des signatures de cercle était incompatible avec l'idée proposée. Ainsi, l'un des chercheurs du MRL à l'époque, Shen Noether, a modifié CT en RingCT, une version de CT compatible avec les signatures de cercle.

Encore une fois, le fonctionnement est assez technique et serait difficile à expliquer dans un article d'introduction. Pour les amateurs de cryptographie qui veulent tout savoir, il existe de nombreux articles détaillés sur Internet concernant les rouages de la technologie CT. Pour le reste d'entre nous, cet article montrera comment il pourrait être possible de cacher les montants, mais prouvera toujours que rien n'a été créé ou détruit.

Imaginons qu'Alice veuille envoyer de l'argent à Bob. Alice enverra 10 XMR à Bob, qui recevra 10 XMR. 10 = 10 donc tout va bien ici. Mais Alice ne veut pas que quiconque sache combien elle envoie. Alors elle et Bob créent un secret partagé. En gros un numéro que seuls eux deux connaissent. Disons que ce nombre est 22. Maintenant, Alice multiplie 10 (ce qu'elle envoie réellement) par 22 pour obtenir 220. C'est le nombre qu'elle partage avec le réseau.

Les mineurs eux-mêmes ne connaissent pas le numéro secret. S'ils le connaissaient, ils pourraient diviser le nombre qui leur est indiqué par le nombre secret et obtenir le montant réel envoyé. Mais comme ils ne le connaissent pas, ils ne peuvent pas. Ils voient cependant que Bob recevra 220. 220 envoyés. 220 reçus. 220 = 220. De cette manière, le réseau peut vérifier qu'aucun Monero n'a été créé ou détruit, le tout sans connaître le montant réel qu'Alice a envoyé à Bob.

Puisque Bob connaît le numéro secret partagé, lorsqu'il reçoit l'argent, il divise simplement par 22 pour obtenir le montant réel qu'Alice a envoyé, 10. Alice et Bob savent tous les deux combien a été envoyé et combien a été reçu, tout en donnant à tout le monde un faux montant.

Encore une fois, ce n'est pas la façon exacte dont fonctionne CT, mais cela donne une idée de la façon dont quelque chose comme ça pourrait être possible. La vraie manière implique des choses comme les engagements de Pedersen, deux montants envoyés (un montant crypté au destinataire et un montant d'engagement au réseau), et … oui, il est déjà facile de voir comment on pourrait se perdre dans tout ça.

Une chose à noter cependant, c'est que si RingCT cache le montant échangé entre deux parties dans une transaction, il ne cache pas deux autres types de montants.

Le premier concerne les transactions « coinbase ». Si ce terme ne vous est pas familier, cela signifie essentiellement la récompense que les mineurs obtiennent pour avoir trouvé le bloc suivant. Ce montant n'est pas caché. Tout le monde peut voir combien le protocole a récompensé un mineur pour son service. De cette façon, le montant actuel de Monero existant peut être connu en additionnant toutes les transactions « coinbase ». Leur somme sera égale au total de Monero actuel en circulation.

Le deuxième montant non masqué correspond aux frais payés aux mineurs lorsqu'un utilisateur envoie une transaction. Les frais doivent être clairs pour que les mineurs sachent à qui donner la priorité. Cela peut être une source de compromission de confidentialité, si par exemple une personne utilisait un montant fixe pour les frais de mineur à chaque fois qu'il envoyait une transaction (par exemple 0,12345), ce qui permettrait alors de pouvoir potentiellement lier ses transactions.

En dehors de ces cas, RingCT cache les montants de Monero depuis 2017, et notre confidentialité collective en est d'autant plus forte.

Ressources complémentaires