---
title: "Wie Monero das Blockgrößenproblem löste, das Bitcoin plagt"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Hinweis:** Es wird dringend empfohlen, dass der Leser unsere Artikel [ „Warum Monero eine Tail-Emission hat“ ](/knowledge/monero-tail-emission) und [ „Monero Mining: Was RandomX so besonders macht“ ](/knowledge/monero-mining-randomx). Dieser Artikel baut auf den dort vorgestellten Konzepten auf._

Wann immer Menschen die Probleme mit Blockchain diskutieren, ist eines der ersten Worte, die auftauchen, "Skalierung". Es ist kein Geheimnis, dass sich Blockchains nicht gut skalieren lassen, aber die meisten Leute wissen nicht, warum.

Die Wahrheit ist, dass Skalierung eigentlich ein Oberbegriff ist, der zwei verschiedene Kategorien abdeckt: Protokollunterstützung und technologische Unterstützung zu einem bestimmten Zeitpunkt. In diesem Artikel werden wir uns auf eine davon konzentrieren: Protokollunterstützung ist im Grunde ein Maß dafür, wie viele Transaktionen das Protokoll zu einem bestimmten Zeitpunkt verarbeiten kann.

Bitcoin hat ein Blockgrößenlimit, was bedeutet, dass, sobald genügend Transaktionen in einem Block enthalten sind, alle weiteren Transaktionen auf den nächsten Block warten müssen. Eine hilfreiche Analogie wäre, sich einen Zug vorzustellen. Ein Zug fährt in den Bahnhof ein, und die Wartenden steigen ein. Sobald der Zug voll ist, muss jeder, der draußen bleibt, auf den nächsten warten.

Bitcoin verwendet Gebühren, um zu bestimmen, wer in den Block kommt oder nicht. Um auf die Analogie mit dem Zug zurückzukommen, kann man sich vorstellen, dass ein potenzieller Fahrgast, der im Begriff ist, zurückgelassen zu werden, dem Lokführer fünf Dollar bietet, damit er einen Sitzplatz bekommt. Andere Fahrgäste folgen diesem Beispiel, und schließlich kommt es zu einem Bieterkrieg, wer welche Plätze bekommt. Es liegt im Ermessen des Lokführers, ob er sich an das Windhundverfahren halten will, aber es liegt in seinem finanziellen Interesse, seine Einnahmen zu maximieren, indem er die Höchstbietenden an Bord nimmt.

In dieser Analogie sind die Miner die Zugführer. Sie können jede beliebige Transaktion in den Block aufnehmen, werden aber in der Regel diejenigen auswählen, für die sie die höchsten Gebühren zahlen.

Wenn die Blöcke jedoch nicht sehr voll sind, haben die Leute keinen Anreiz, hohe Gebühren zu zahlen, weil es noch viele freie Plätze gibt.

Auf dem Höhepunkt des Kryptowährungsbooms 2017 wurde Bitcoin mit Transaktionen überflutet, und die Gebühren für diejenigen, die in den nächsten Block aufgenommen werden wollten, schossen in die Höhe, ebenso wie für jeden zukünftigen Block. Diejenigen, die nicht bereit waren, hohe Gebühren zu zahlen, mussten mit ansehen, wie ihre Transaktionen um Stunden oder Tage verschoben wurden oder sogar ganz aus der Warteschlange fielen.

Dies war ein erschütternder Einblick, wie es Bitcoin ergehen würde, wenn die oft erwähnte "Massenakzeptanz" eintreten würde. Wenn Bitcoin von der breiten Masse genutzt würde, wäre es noch schlimmer als 2017, und Bitcoin wäre für jeden außer den Wohlhabenden unzugänglich, einfach weil der Durchsatz aufgrund einer festen Blockgröße gering ist, was dazu führt, dass der Gebührenmarkt die Oberhand gewinnt.

Monero hat dies vorausgesehen und wollte etwas anders machen. Also implementierten die Monero-Entwickler eine dynamische Blockgröße.

Im Grunde hat Monero auch eine Obergrenze für die Blockgröße, aber es ist eine weiche Obergrenze. Wenn die Schlange der wartenden Transaktionen zu lang wird, können die Miner die Größe der Blöcke erhöhen. Mit unserer Zug-Analogie können Sie sich vorstellen, mehr Waggons hinzuzufügen, um die zusätzlichen Passagiere aufzunehmen. Wenn die Warteschlange leer ist, schrumpfen die Blöcke wieder auf ihre ursprüngliche Größe zurück.

Wenn dies eine nette Idee zu sein scheint, ist die Frage berechtigt, warum Monero die einzige Kryptowährung ist, die dies implementiert hat. Warum nicht auch bei Bitcoin, um den Durchsatzproblemen ein Ende zu setzen?

Leider ist dies nicht möglich. Dafür gibt es mehrere Gründe, und wir werden unser Bestes tun, um sie zu erklären.

Es ist immer im besten Interesse der Miner, große Blöcke zu haben. Mit großen Blöcken können sie mehr Transaktionen unterbringen und mehr Geld mit den Gebühren und den Blockprämien verdienen. Dies kann zu Spam-Angriffen führen, bei denen jemand viele kleine Transaktionen mit geringen Gebühren sendet, um die Kette aufzublähen. Die Miner würden einfach die Blockgröße erhöhen und sie alle einschließen, denn Geld ist Geld, egal wie klein es ist. Dies würde zu konstant großen Blöcken mit wenig wirtschaftlichem Nutzen führen. Bitcoin löst dieses Problem, indem es die Blockgröße künstlich einschränkt und dadurch einen Gebührenmarkt schafft. Spam-Angreifer müssten die anderen Nutzer mit Gebühren übertreffen, und das ist nicht mehr billig. Aber das bedeutet, dass die Blöcke voll werden und einige Transaktionen warten, wie oben erwähnt.

Wie kann Monero also dynamische Blockgrößen haben und gleichzeitig Spam-Angriffe vermeiden? Die Antwort ist einfach, aber clever. Es wird ein Malus auf die Blockbelohnung eingeführt, wenn ein Block größer als normal ist. Wenn ein Miner die Blockgröße erhöhen möchte, ist die Belohnung, die er für das Finden dieses Blocks erhält, geringer als die, die er sonst erhalten würde. Er wird die Blockgröße also nur dann erhöhen, wenn die von den Nutzern gezahlten Transaktionsgebühren den verlorenen Teil der Blockbelohnung aufwiegen. Wenn der Miner beispielsweise 0,5 XMR verlieren würde, wenn er die Blockgröße erhöht, und die Summe der gezahlten Transaktionsgebühren 0,4 XMR betragen würde, dann gäbe es einen Nettoverlust von 0,1 XMR, wenn er die Größe erhöhen würde, also würde er es nicht tun. Umgekehrt, wenn sich die gesamten Transaktionsgebühren auf 0,7 XMR summieren würden, dann gäbe es einen Nettogewinn von 0,2 XMR, obwohl sie die 0,5 XMR aus der Blockbelohnung verlieren, also wird der Miner die Größe erhöhen.

Diese dynamischen Blöcke ermöglichen es dem Netzwerk, organisch zu wachsen, ohne die Blockgröße künstlich einzuschränken, um einen erzwungenen Gebührenmarkt zu schaffen, und gleichzeitig Spam-Angriffe zu vermeiden. Es gibt noch einige weitere Blickwinkel, aus denen wir diese Idee betrachten können, und weitere Gründe, warum es nicht möglich wäre, Bitcoin hinzuzufügen, aber für den Moment hoffen wir, dass der Leser ein Verständnis dafür hat, wie Monero einige der Probleme in Bitcoin und seinen Derivaten umgeht und wie es plant, seinen Durchsatz in der Zukunft zu skalieren.

Weiterlesen