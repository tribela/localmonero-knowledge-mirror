---
title: "Wie Monero Hard-Forks verwendet, um das Netzwerk zu aktualisieren"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Einer der am häufigsten missverstandenen Teile von Moneros Ansatz zum Aufbau einer dezentralisierten, die Privatsphäre wahrenden und sicheren Kryptowährung ist die Rolle, die Hard-Forks (oder Netzwerk-Upgrades) spielen.

In diesem Beitrag gehen wir darauf ein, was Hard-Forks sind, warum sie für Monero wichtig sind und welche Rolle Sie in Zukunft darin spielen können.

## Warum muss Monero das Netzwerk ständig aktualisieren?

Die Monero-Community hat sich verpflichtet, das Projekt im Laufe der Zeit zu wiederholen und zu verbessern, und es scheint, dass sich das Engagement auf zwei Schlüsselaspekte des Ethos der Community reduziert:

  1. Das Monero-Projekt ist letztendlich Software – Code – von Menschen geschrieben. Dies kann dazu führen, dass Fehler behoben, im Laufe der Zeit entdeckte oder erfundene Verbesserungen hinzugefügt, Modernisierungen des Protokolls implementiert oder das Projekt einfach gewartet werden müssen. Dies ähnelt in vielerlei Hinsicht der anderen Software, die Sie verwenden (wie dem Browser, in dem Sie dies lesen!), die ständig aktualisiert werden muss, um neue Funktionen hinzuzufügen und Fehler zu beheben.

  2. Das Monero-Projekt ist ein Datenschutz-Tool, und der Datenschutz ist ein ständig fortschreitendes Wettrüsten. Die Menschen und Gruppen, die nichts lieber tun würden, als der Welt die Privatsphäre (sowohl finanziell als auch persönlich) zu nehmen, verbessern, entwickeln und erfinden ständig neue Wege, um moderne Ansätze zur Wahrung der Privatsphäre, wie sie in Monero verwendet werden, anzugreifen. Da die Feinde der Privatsphäre diese neuen Ansätze finden, muss das Monero-Netzwerk in der Lage sein, sich anzupassen und zu verbessern, um zurückzuschlagen und unser Recht auf finanzielle Privatsphäre zu verteidigen.

Das Monero-Projekt ist letztendlich Software – Code – von Menschen geschrieben. Dies kann dazu führen, dass Fehler behoben, im Laufe der Zeit entdeckte oder erfundene Verbesserungen hinzugefügt, Modernisierungen des Protokolls implementiert oder das Projekt einfach gewartet werden müssen. Dies ähnelt in vielerlei Hinsicht der anderen Software, die Sie verwenden (wie dem Browser, in dem Sie dies lesen!), die ständig aktualisiert werden muss, um neue Funktionen hinzuzufügen und Fehler zu beheben.

Das Monero-Projekt ist ein Datenschutz-Tool, und der Datenschutz ist ein ständig fortschreitendes Wettrüsten. Die Menschen und Gruppen, die nichts lieber tun würden, als der Welt die Privatsphäre (sowohl finanziell als auch persönlich) zu nehmen, verbessern, entwickeln und erfinden ständig neue Wege, um moderne Ansätze zur Wahrung der Privatsphäre, wie sie in Monero verwendet werden, anzugreifen. Da die Feinde der Privatsphäre diese neuen Ansätze finden, muss das Monero-Netzwerk in der Lage sein, sich anzupassen und zu verbessern, um zurückzuschlagen und unser Recht auf finanzielle Privatsphäre zu verteidigen.

## Was ist eine Hard-Fork?

Die Komplexität des Upgrades von Monero wird deutlich, sobald Sie verstehen, wie unterschiedlich das Upgrade einer Kryptowährung ist, anstatt einfach ein Software-Update auf so etwas wie einen Browser zu übertragen.

In Kryptowährungen müssen die Regeln des Netzwerks (Dinge wie Transaktionen aussehen sollten, wie Mining funktioniert und wie jeder Block verifiziert wird) vom Netzwerk vereinbart werden, was als „Konsens“ bezeichnet wird. Wenn eine dieser Regeln geändert oder aktualisiert werden muss, muss sich das Netzwerk auf die neuen Regeln einigen, was zu einer „Hard-Fork“ führt – einer Situation, in der sich das Netzwerk tatsächlich in zwei Chains von Blöcken aufteilt – eine nach den alten Regeln und eine zu den neuen Regeln.

Wenn sich alle in der Community auf die Regeländerungen einigen, wird dies als „nicht umstrittene Hard-Fork“ bezeichnet, und die Kette, die noch die alten Regeln hat, stirbt ab und wird nach der Hard-Fork nicht mehr abgebaut. Dies war bei fast jeder Hard-Fork von Monero der Fall, und die einzige Fortsetzung der alten Regeln waren Projekte, die versuchten, von der Hard-Fork zu profitieren.

Während unstrittige Hard-Forks die einzige Möglichkeit sind, wichtige Aspekte des Monero-Netzwerks richtig zu aktualisieren, haben sie auch einen frustrierenden Nebeneffekt – alte Software, die veröffentlicht wurde, bevor die Hard-Fork geplant war, kann die neue Regeln des Netzwerks nicht verstehen und funktioniert daher nach dem Hard-Fork nicht mehr! Dies kann dazu führen, dass Benutzer denken, dass Gelder verloren sind, denken, dass die Monero-Blockchain gestoppt wurde und Gelder nicht bewegen können, bis sie ihre Wallet aktualisieren.

## Wer entscheidet, wann das Monero-Netzwerk aktualisiert wird und was enthalten ist?

Da es keine zentrale Autorität, keinen CEO oder Präsidenten von Monero gibt, fällt die Arbeit rund um die Entscheidung, wann das Netzwerk aktualisiert werden soll, was aufgenommen werden soll und wie vorzugehen ist, _uns_ zu, diesen Leuten in der Monero-Community, die sich dafür entscheiden, sich zu engagieren und zu interagieren! Dies ist ein äußerst wichtiger Teil eines dezentralisierten Projekts, da die Planung und Entscheidungsfindung für das Projekt letztendlich dezentralisiert und von der Community per Crowdsourcing durchgeführt wird.

Die Planung des Timings und der Funktionen, die in jedem Netzwerk-Upgrade in Monero enthalten sind, erfolgt an zwei Hauptorten:

  1. Auf IRC und Matrix, den am häufigsten verwendeten Chat-Plattformen in der Monero-Community (die miteinander verbunden sind). Diese Plattformen ermöglichen große Gruppenchats und sind der Ort, an dem alle geplanten Monero-Community-Treffen, Entwicklertreffen und Forschungslabortreffen abgehalten werden. Diese Meetings sind die beste Möglichkeit für Sie, der Planung und Diskussion rund um Netzwerk-Upgrades in Monero zuzuhören (oder beizutragen!).

  2. Auf Github, der Hauptkommunikationsplattform für länger laufende Monero-Diskussionen, Planung und Organisation. Die Monero-Community verwendet Github, um Meetings zu organisieren, neue Funktionen und Ideen zu diskutieren und die Planung von Netzwerk-Upgrades zu koordinieren, zusätzlich zum Speichern des Codes für das Monero-Projekt.

Auf IRC und Matrix, den am häufigsten verwendeten Chat-Plattformen in der Monero-Community (die miteinander verbunden sind). Diese Plattformen ermöglichen große Gruppenchats und sind der Ort, an dem alle geplanten Monero-Community-Treffen, Entwicklertreffen und Forschungslabortreffen abgehalten werden. Diese Meetings sind die beste Möglichkeit für Sie, der Planung und Diskussion rund um Netzwerk-Upgrades in Monero zuzuhören (oder beizutragen!).

Auf Github, der Hauptkommunikationsplattform für länger laufende Monero-Diskussionen, Planung und Organisation. Die Monero-Community verwendet Github, um Meetings zu organisieren, neue Funktionen und Ideen zu diskutieren und die Planung von Netzwerk-Upgrades zu koordinieren, zusätzlich zum Speichern des Codes für das Monero-Projekt.

Wenn Sie eine wichtige Idee für ein Netzwerk-Upgrade haben, einen Ansatz nicht mögen oder Bedenken hinsichtlich des Zeitpunkts eines Upgrades haben, ist es wichtig, dass Sie sich zu Wort melden und Ihren Fall der Community klar präsentieren!

## Wie kann ich bei Netzwerk-Upgrades helfen?

Da Upgrades des Monero-Netzwerks zusammen mit Software-Updates eine Community-Koordination und -Genehmigung erfordern, ist es äußerst wichtig, dass sich so viele Menschen wie möglich an der Planung, dem Testen und dem Kommunikationsprozess von Netzwerk-Upgrades beteiligen.

Hier sind ein paar einfache Möglichkeiten, wie Sie helfen können, die Dinge rund um ein Netzwerk-Upgrade zu glätten:

  1. Nehmen Sie an den Planungstreffen teil, [die auf Github](https://github.com/monero-project/meta/issues) gepostet werden, hören Sie zu und tragen Sie bei, wenn Sie etwas Relevantes anzusprechen haben.
  2. Teilen Sie die Details zum Zeitpunkt des Netzwerk-Upgrades (nachdem Sie sich entschieden haben!) mit Ihrer bevorzugten Börse, Wallet oder Ihrem bevorzugten Mining-Pool. Es kann schwierig sein, alle Monero-Benutzer ordnungsgemäß über ein Upgrade zu informieren, daher ist es wichtig, dass wir alle helfen, wo wir können, um die Nachricht zu verbreiten.
  3. Testen Sie die Software vor dem Netzwerk-Upgrade. Vor dem Netzwerk-Upgrade wird sowohl im Testnet als auch im Stagenet ein Aufruf an die Tester gesendet, um sicherzustellen, dass jeder Aspekt des Upgrades ordnungsgemäß geplant und in der Software implementiert wurde. Je mehr Leute sich engagieren und die neuen Versionen gründlich testen, desto wahrscheinlicher wird das Netzwerk-Upgrade reibungslos verlaufen!
  4. Sobald Releases veröffentlicht werden, die mit dem Netzwerk-Upgrade kompatibel sind, stellen Sie sicher, dass Sie sofort ein Upgrade durchführen! Je mehr Leute aktualisiert und bereit für das Netzwerk-Upgrade sind, desto reibungsloser wird das Netzwerk damit umgehen und desto weniger Kopfschmerzen werden die Benutzer haben.

## Was kann ich beim nächsten Monero-Netzwerk-Upgrade erwarten?

Obwohl es noch kein in Stein gemeißeltes Datum gibt, wird es bald ein Netzwerk-Upgrade geben, um einige wichtige Upgrades und Funktionen in Monero zu implementieren:

  1. Eine Erhöhung der Ringgröße von 11 auf 16, wodurch der Basis-Anonymitätssatz (sprich: plausible Leugnung oder Basis-Datenschutz) jeder Transaktion im Netzwerk erhöht wird
  2. [Tags anzeigen, eine hervorragende Möglichkeit, die Synchronisierungszeiten der Wallet um 30–40% zu reduzieren](/knowledge/view-tags-reduce-monero-sync-time/)
  3. Gebührenänderungen, Verbesserung der Sicherheit und Widerstandsfähigkeit des Netzwerks gegenüber schnellen Änderungen auf dem Gebührenmarkt oder Angriffen durch böswillige Entitäten
  4. [Bulletproofs+, eine weitere Verbesserung der Effizienz von Monero-Transaktionen](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Diese Änderungen werden einen großen Beitrag zur Erhöhung der Privatsphäre, Effizienz und Sicherheit des Netzwerks leisten und gleichzeitig den Weg für [Seraphis](/knowledge/seraphis-for-monero/) ebnen, das Transaktionsprotokoll der nächsten Generation für Monero.

## Wie kann ich mehr erfahren?

Das Thema Hard-Forks und Netzwerk-Upgrades ist weitreichend und es gibt eine lange und geschichtsträchtige Geschichte von ihnen in Monero, also vergewissern Sie sich, dass Sie sich einige der folgenden Links ansehen, wenn Sie mehr über den Verlauf erfahren möchten, über den Prozess oder laufende Planung für das bevorstehende Netzwerk-Upgrade!

  * [Monero v15 Hard-Fork-Planung](https://github.com/monero-project/meta/issues/630)
  * [Geplante Software-Upgrades (in Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Ein Hinweis zu geplanten Protokoll-Upgrades](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Weiterlesen

  * [Wie Monero auf einzigartige Weise Kreislaufwirtschaften ermöglicht](/knowledge/monero-circular-economies/)

  * [Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Warum (und wie!) Sie Ihre eigenen Keys halten sollten](/knowledge/hold-your-keys/)

  * [Zu Monero beitragen](/knowledge/contributing-to-monero/)

  * [Wie sich Remote-Knoten auf die Privatsphäre von Monero auswirken](/knowledge/remote-nodes-privacy/)

  * [View-Tags: Wie ein Byte die Synchronisierungszeiten der Monero-Wallet um über 40 % reduziert](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool und seine Rolle bei der Dezentralisierung des Monero-Mining](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Was es für Monero tun wird](/knowledge/seraphis-for-monero/)

  * [Ist die Umwandlung von Bitcoin in Monero genauso privat wie der direkte Kauf von Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [Warum Monero im Gegensatz zu Zcash ein vertrauensloses Setup verwendet](/knowledge/monero-trustless-setup/)

  * [Warum Monero ein besserer Wertspeicher ist als Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Wie Monero die Netzwerkeffekte von Bitcoin überwinden kann](/knowledge/network-effect/)

  * [Warum Monero die kritischste Community hat](/knowledge/critical-thinking/)

  * [Betrügereien, auf die Sie bei der Verwendung von Monero achten sollten](/knowledge/monero-scams/)

  * [Wie Atomic Swaps in Monero funktionieren](/knowledge/monero-atomic-swaps/)

  * [Was jeder Monero-Benutzer wissen muss, wenn es ums Networking geht](/knowledge/monero-networking/)

  * [Wie RingCT Monero-Transaktionsbeträge verbirgt](/knowledge/monero-ringct/)

  * [Wie Monero Stealth-Adressen Ihre Identität schützen](/knowledge/monero-stealth-addresses/)

  * [Wie Monero-Subadressen die Identitätsverknüpfung verhindern](/knowledge/monero-subaddresses/)

  * [Monero-Outputs erklärt](/knowledge/monero-outputs/)

  * [Monero Best Practices für Anfänger](/knowledge/monero-best-practices/)

  * [Wie Ringsignaturen die Ausgaben von Monero verschleiern](/knowledge/ring-signatures/)

  * [Wie Monero das Blockgrößenproblem löste, das Bitcoin plagt](/knowledge/dynamic-block-size/)

  * [Wie CLSAG die Effizienz von Monero verbessern wird](/knowledge/what-is-clsag/)

  * [Warum Monero eine Tail-Emission hat](/knowledge/monero-tail-emission/)

  * [Eine kurze Geschichte von Monero](/knowledge/monero-history/)

  * [Das Wired Magazine hat Unrecht mit Monero, hier ist der Grund](/knowledge/wired-article-debunked/)

  * [Die 15 wichtigsten Monero-Mythen und -Bedenken widerlegt](/knowledge/monero-myths-debunked/)

  * [Wie Dandelion++ die Transaktionsursprünge von Monero geheim hält](/knowledge/monero-dandelion/)

  * [Warum Monero Open Source und dezentralisiert ist](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Was RandomX so besonders macht](/knowledge/monero-mining-randomx/)

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better/)