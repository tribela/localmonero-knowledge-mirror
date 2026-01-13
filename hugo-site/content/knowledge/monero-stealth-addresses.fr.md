---
title: "Comment les adresses furtives de Monero protègent votre identité"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero a mis en place une approche à trois volets en matière de confidentialité. Ces technologies sont les [les signatures de cercle](/knowledge/ring-signatures), qui masquent la véritable sortie (expéditeur), RingCT qui masque les montants, et les adresses furtives, qui masquent le récepteur. Aujourd'hui, nous discuterons de la dernière de ces technologies mentionnées : les adresses furtives.

Il existe de nombreuses raisons pour lesquelles un individu peut vouloir cacher à qui il envoie de l'argent. Nous ne devons jamais laisser quiconque essayer de nous convaincre que tous les exemples de ceci sont des comportements peu recommandables. Des choses comme envoyer un soutien à un parti politique impopulaire, faire un don à des œuvres caritatives ou soutenir ceux que la culture considère comme « annulés » (les personnes ignorées, dans la « cancel culture ») sont tous des exemples de cas où l'on pourrait vouloir cacher ses habitudes de dépenses par crainte de répercussions, mais qui sont parfaitement légitimes par nature.

Sur une blockchain transparente, les adresses où l'on envoie ses transactions sont visibles de tous. Il est important de considérer que si les mineurs eux-mêmes ne sont pas d'accord avec la destination de l'argent, ils peuvent choisir de ne pas l'inclure dans un bloc, censurant ainsi cette transaction sur une plateforme apparemment résistante à la censure. La seule façon de rendre cette censure, certes improbable, impossible est si les mineurs ne peuvent pas faire la distinction entre les transactions, car toutes les métadonnées en chaîne sont masquées par divers moyens. Quelque chose pour lequel Monero est connu.

Monero résout ce problème d'adresses transparentes en implémentant des adresses furtives, une technologie qui a en fait été initialement conçue pour Bitcoin en 2011 par l'utilisateur du forum Bitcoin Talk ByteCoin (la relation avec Bytecoin, qui intégrera plus tard des adresses furtives, est inconnue). La forme actuelle des adresses furtives présente cependant plusieurs améliorations par rapport à l'idée initiale. Mais d'abord, afin de voir comment elles fonctionnent, parlons des clés.

Il est difficile d'être dans le domaine des crypto-monnaies et de ne pas entendre parler des clés. Des expressions telles que « sauvegarder votre clé privée » sont courantes, mais lorsqu'un utilisateur moyen entend les mots « clé publique » et « clé privée », il a peur et pense que ce sera trop technique et déroutant à comprendre. Mais ne vous inquiétez pas. Nous allons y aller lentement et utiliser de nombreux exemples.

Les deux types de clés utilisées dans les crypto-monnaies sont, comme nous venons de le mentionner, les clés publiques et privées. Ces deux clés viennent généralement par paire, ce qui signifie qu'une clé publique et une clé privée particulières sont liées l'une à l'autre. En fait, la clé publique est généralement dérivée de la clé privée, ce qui signifie que si vous connaissez la clé privée, votre portefeuille peut faire des calculs nécessaires et trouver la bonne clé publique à chaque fois.

Maintenant, comme les noms l'indiquent, la clé publique peut être publique sans conséquence. Habituellement, c'est une partie de l'adresse que vous partagez pour recevoir de l'argent dans votre portefeuille de crypto-monnaie. Suivant également son homonyme, la clé privée est celle qui ne doit pas être partagée. C'est la chose qui vous permet de signer et de dépenser une transaction, donc si elle est volée ou partagée, alors un tiers malveillant peut dépenser votre argent, généralement pour lui-même.

Une analogie simple serait un cadenas et la clé nécessaire pour le déverrouiller. Le cadenas ouvert peut être partagé librement, et en effet tout peut être verrouillé avec ce cadenas, mais seule la personne avec la clé peut ouvrir tout ce sur quoi le cadenas est fermé. Le cadenas peut être copié et partagé, la clé ne doit pas l'être.

Ces clés sont généralement masquées de l'utilisateur, de sorte que vous ne les voyez jamais vraiment. Dans Monero, elles n'apparaissent pas du tout comme une chaîne alphanumérique effrayante. Dans Monero, l'utilisateur lambda connaît la clé privée sous la forme d'une phrase mnémonique. Cette phrase (que vous devriez écrire si vous ne l'avez pas fait) n'est en fait qu'une clé privée lisible par l'homme. 

Vous voyez ? Pas si effrayant finalement. Retour maintenant aux adresses furtives.

Comme mentionné précédemment, les adresses furtives n'étaient pas conçues à l'origine pour Monero, mais pour Bitcoin. Comme pour la plupart des idées naissantes, cette première itération avait des problèmes. La tentative suivante est survenue lorsque CryptoNote a été créé par Nicholas van Saberhagan pour Bytecoin, le précurseur de Monero ([voir notre histoire de Monero et Bytecoin ici](/knowledge/monero-history)), et bien qu'il s'agisse d'une nette amélioration par rapport à l'original, même elle avait quelques défauts subtils.

Finalement, une dernière itération est née d'un développeur pour une autre crypto-monnaie de confidentialité, aujourd'hui disparue, qui a résolu les problèmes de confidentialité et de sécurité en suspens avec l'idée. Cela a finalement fait son chemin dans Monero, et c'est ce qui est utilisé aujourd'hui.

Bien que ces problèmes de confidentialité et de sécurité aient été résolus, les adresses furtives elles-mêmes ont ajouté un autre type de bizarrerie aux technologies de blockchain, une qui n'existait pas auparavant. Le besoin de « scanner ». Étant donné que les adresses de réception ne sont pas affichées publiquement sur la blockchain, le destinataire ne sait jamais si une transaction donnée lui appartient, il doit donc analyser toutes les transactions entrantes avec sa clé privée pour voir si c'est la leur ; ce c'est l'opération de « scanner ».

Avec les crypto-monnaies transparentes, tout ce qu'elles ont à faire est de vérifier si une transaction est envoyée à votre adresse. Une question facilement et rapidement répondue par oui ou non. Mais avec les adresses furtives, chaque transaction pourrait potentiellement être celle qui vous est envoyée, vous devez donc essayer de déverrouiller chacune avec votre clé privée pour voir si elle s'ouvre.

C'est une étape supplémentaire que Bitcoin et ses dérivés n'ont pas, et fait que la configuration initiale du portefeuille, ainsi que la synchronisation d'un portefeuille lorsque vous ne l'avez pas ouvert depuis un certain temps, prennent beaucoup plus longtemps que Bitcoin. Le compromis est cependant nécessaire pour asssurer les garanties de confidentialité dont Monero dispose. Il convient de noter que, contrairement au point le plus faible du trio de des briques pour l'obtention de la confidentialité, les signatures de cercle, les adresses furtives ne sont pas sensibles à l'heuristique. Elles s'appuient sur une cryptographie à courbe elliptique éprouvée, sur laquelle tout Internet s'appuie, donc la briser signifierait la fin de la sécurité informatique en général, pas seulement de Monero.

Ressources complémentaires