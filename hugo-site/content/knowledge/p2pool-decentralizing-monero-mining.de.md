---
title: "P2Pool und seine Rolle bei der Dezentralisierung des Monero-Mining"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Eines der Hauptziele des Monero-Projekts ist es, ein faires, dezentralisiertes und sicheres Netzwerk durch neue und innovative Ansätze für das Proof-of-Work (PoW)-Mining zu ermöglichen, die Hauptmethode, mit der Kryptowährungsnetzwerke heute gesichert werden.

Während ein einzigartiger Mining-Algorithmus [wie RandomX](/knowledge/monero-mining-randomx) für dieses Ziel äußerst wichtig ist, da er dazu beiträgt sicherzustellen, dass jeder mit einem Computer einen angemessenen Beitrag zur Sicherheit des Netzwerks leisten kann, löst RandomX die Probleme nicht, die aufgrund von Pool-Mining auftreten können. Pool-Mining ist heute bei weitem die gebräuchlichste Art, Kryptowährungen zu minen, einschließlich Monero, aber zum Glück ändert sich dies durch das Aufkommen von p2pool-Mining schnell.

## Was ist Pool-Mining?

Pool-Mining ist eine Möglichkeit für Miner, die Aufgabe zu teilen, einen Block im Netzwerk zu lösen und dann die Belohnungen gleichmäßig für alle Blöcke zu teilen, die der Pool findet. Während dies immens dazu beiträgt, die Häufigkeit auszugleichen, mit der Miner bezahlt werden, im Vergleich zum Solo-Mining von Monero, ist es nicht ohne ernsthafte Zentralisierungsprobleme.

Wenn jeder Miner Arbeit in den Pool einbringt, gibt er die Kontrolle über jede Arbeit, die er verrichtet und Blöcke, die er findet, an den Pool selbst ab, im Vertrauen darauf, dass der Pool die Belohnungen ehrlich und fair unter allen Minern, basierend auf der Menge von Arbeit, die jeder getan hat, aufteilt. Wenn alles gut geht, sammelt der Pool-Betreiber die Arbeit aller Miner, übermittelt sie an das Netzwerk und teilt die Belohnungen gleichmäßig.

## Was ist das Problem beim Pool-Mining?

Leider beruht dies ausschließlich auf Vertrauen und ermöglicht es dem Poolbetreiber, schändliche Dinge mit der Arbeit der Miner zu tun. Der Pool-Betreiber könnte die geleistete Arbeit nutzen, um das Netzwerk anzugreifen, versuchen, Gelder zu verdoppeln (wenn der Pool groß genug ist) oder einfach die von den Minern geleistete Arbeit verwenden, um sich selbst zu bezahlen, und die Miner niemals angemessen für ihre Arbeit belohnen .

Das größte Risiko für das Netzwerk besteht darin, dass ein Pool (oder mehrere Pools, die zusammenarbeiten) mehr als 51% der Netzwerk-Hashrate unter ihrer Kontrolle haben, da sie dies zum Betrügen und zweimaligen Ausgeben von Geldern verwenden könnten (ein doppelter Output-Angriff) oder versuchen, die Regeln des Netzwerks zu ändern.

## Was ist p2pool?

p2pool ist ein Konzept, das ursprünglich 2011 für das Mining von Bitcoin entwickelt wurde, aber nie eine breite Akzeptanz fand und bei Bitcoin praktisch ungenutzt bleibt. Glücklicherweise verbrachte einer der wichtigsten Entwickler hinter RandomX, SCHernykh, seinen Urlaub damit, Lösungen für einige der Probleme mit der Bitcoin-Implementierung von p2pool zu finden und die gesamte Software von Grund auf neu zu schreiben.

p2pool in Monero ermöglicht Minern eine völlig vertrauenslose Möglichkeit, zusammenzuarbeiten, um Blöcke zu lösen und das Monero-Netzwerk zu sichern, indem spezielle Knotensoftware für p2pool verwendet wird, um die Arbeit zu teilen.

Dies geschieht mit einer neuen Blockchain (einer „Side-Chain“), die die Arbeit jedes Miners, seine Wallet-Adresse und wie viel Monero er verdient hat, aufzeichnet und dann die Belohnung völlig vertrauenslos und dezentral auszahlt. Da diese Side-Chain weit weniger Miner hat, ist es viel einfacher, Blöcke darin zu finden und einzureichen als im Hauptnetzwerk von Monero, was es einfacher für Miner macht, konsistente Auszahlungen zu erhalten, anstatt Monero Solo zu minen.

## Wie löst p2pool die Probleme des Pool Mining?

In p2pool gibt es keinen zentralisierten Pool, keinen zentralisierten Poolbetreiber oder eine einzelne Person, die Gelder verwaltet und Auszahlungen verteilt. Die gesamte Arbeit, die von denjenigen, die über p2pool schürfen, gemeinsam erledigt wird, wird von der p2pool-Blockchain und anderen Node-Betreibern überprüft, um sicherzustellen, dass sie legitim ist, und alle Miner werden entsprechend ihrer geleisteten Arbeit sofort ausgezahlt, wenn ein Block gefunden wird, direkt mit der Belohnungen in diesem gefundenen Block.

Wenn Miner sich entscheiden, p2pool anstelle eines zentralisierten Pools zu verwenden, entziehen sie den Poolbetreibern jegliche Macht und Vertrauen und stellen sicher, dass ihre Arbeit zum Wohl des Netzwerks und zu ihren eigenen Belohnungen beiträgt, das Risiko von Netzwerkangriffen und Missbrauch verringern oder Diebstahl von Vergütungen aus Arbeit, die ihnen geschuldet werden.

Das hilft ihnen nicht nur, ihre eigenen Interessen zu schützen, es reduziert auch das Risiko, das zentralisierte Pools für das gesamte Monero-Netzwerk darstellen können. Die Nutzung von p2pool trägt auch immens dazu bei, das Risiko zu verringern, das Nationalstaaten oder Aufsichtsbehörden für die Gesundheit des Netzwerks darstellen könnten, da es keine zentralisierten Poolbetreiber gibt, die unter Druck stehen, keine geografische Konzentration von Pools, auf die man sich stützen kann, oder andere einfache Druckpunkte damit sie gegen Monero eingesetzt werden können.

## Was sind die Nachteile?

Glücklicherweise wurde p2pool in Monero gut entworfen und gebaut und funktioniert extrem gut! Der Hauptnachteil des p2pool-Minings besteht jedoch darin, dass jeder Miner, der p2pool verwenden möchte, seinen eigenen Monero-Knoten betreiben muss, wodurch der Einstiegsprozess etwas komplizierter wird. Dieser Knoten wird dann jedoch verwendet, um alle Informationen zu berechnen, die zum Erstellen und Überprüfen von Blöcken erforderlich sind, und stellt sicher, dass der Miner die vollständige Kontrolle über seine Arbeit hat. Der Knoten kann auch als Remote-Knoten für die eigene Wallet des Miners fungieren, zum Netzwerk beitragen und vieles mehr.

Der andere Hauptunterschied zum zentralisierten Mining besteht darin, dass kleine Miner, die p2pool verwenden, etwas mehr "Varianz" oder Zeit zwischen den Auszahlungen haben als ein großer, zentralisierter Pool -- aber es'ist _extrem_ wichtig zu beachten, dass dies nicht dazu führt, dass Sie im Laufe der Zeit weniger Monero verdienen! p2pool wird im Laufe der Zeit auch für kleine Miner genauso profitabel sein wie zentralisierte Pools. Ein Teil dieser Abweichung wird auch dadurch ausgeglichen, dass p2pool nativ 0 % Gebühren hat, da es keinen zentralisierten Poolbetreiber gibt, der für seine Dienste bezahlt werden muss!

## Wie kann ich anfangen?

Dank des hervorragenden Designs der p2pool-Implementierung in Monero' und der vielen Menschen in der Community, die Zeit investiert haben, um den Prozess des Mining über p2pool zu vereinfachen, wird der Einstieg mit der Zeit einfacher. Es gibt mehrere Möglichkeiten, mit dem Mining mit p2pool zu beginnen, aber da die technischen Details den Rahmen dieses Artikels sprengen würden, können Sie je nach Betriebssystem einfach auf einen der folgenden Links gehen:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Wie kann ich mehr erfahren?

Wenn dies Ihre Neugier auf p2pool-Mining geweckt hat, werfen Sie einen Blick auf einige zusätzliche Links und Erklärungen zu p2pool, wie es funktioniert und was es für Monero bedeutet:

  * [Der offizielle Github für p2pool](https://github.com/SChernykh/p2pool)
  * [Die offiziellen Dokumente zur Verwendung von p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool ist jetzt live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, eine Art "Block-Explorer" für p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Über seine Entwicklung von P2Pool, einem dezentralisierten XMR-Mining-Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Weiterlesen