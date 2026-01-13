---
title: "View-Tags: Wie ein Byte die Synchronisierungszeiten der Monero-Wallet um über 40 % reduziert"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Eine der häufigsten Beschwerden bei der täglichen Verwendung von Monero ist die Zeit, die es dauern kann, eine Wallet zu synchronisieren, bevor Monero gesendet werden kann. Zum Glück haben Entwickler und Forscher in der Monero-Community einen brillanten Weg gefunden, um die Zeit, die Sie zum Synchronisieren Ihrer Wallet benötigen, um mehr als 40 % zu verkürzen, ohne zusätzliche Blockchain-Aufblähung, Gebühren usw.

Lernen Sie „View-Tags“ kennen, eine Ein-Byte-Ergänzung zu den Daten jeder Transaktion – das kommt beim nächsten Netzwerk-Upgrade zu Monero!

## Warum ist die Wallet-Synchronisierung von Monero langsamer als die von Bitcoin?

Eine der ersten Fragen, die wir beantworten müssen, um die Notwendigkeit einer Lösung wie View Tags besser zu verstehen, ist, warum die Synchronisierung der Wallet von Monero langsamer ist als bei Kryptowährungen wie Bitcoin.

Da in Bitcoin alle Transaktionen nicht privat sind und die ausgegebenen Coins, die Beträge und die beteiligten Adressen auf der Chain offenlegen, können Bitcoin-Wallets einfach nach nicht ausgegebenen Transaktionsausgaben (UTXOs) oder verwendeten Adressen für eine bestimmte Wallet suchen und die Blockchain schnell nach UTXOs scannen, die diesen Adressen gehören, um herauszufinden, welche Coins zu Ihrer Wallet gehören und ausgegeben werden können.

In Monero wird jedoch bei allen Transaktionen die Privatsphäre des Benutzers gewahrt, indem der Absender, der Empfänger und die Beträge, die an jeder Transaktion beteiligt sind, verborgen werden. Diese Privatsphäre ist zwar für den Schutz der Nutzer des Netzwerks unerlässlich, führt aber auch zu einer langsameren Synchronisierung der Wallets. In Monero muss Ihr Wallet jede Transaktionsausgabe (TXO), die im Netzwerk existiert, mit den privaten Schlüsseln Ihres Wallets vergleichen.

Dieser Vergleich beinhaltet eine Menge komplexer Mathematik und Kryptographie, um zu bestätigen, dass eine Ausgabe wirklich Ihnen gehört, da alle Beträge, Adressen und bekannt ausgegebenen Ausgaben (oder Coins) in Monero auf der Chain versteckt sind.

## Was sind View-Tags?

Um die Synchronisierungszeit für Monero-Wallets zu verkürzen, [hat ein Forscher namens UkoeHB einen neuen Ansatz entwickelt](https://github.com/monero-project/research-lab/issues/73): Er fügt jeder Transaktion ein 1-Byte-"Tag" hinzu, das ein gemeinsames Geheimnis enthält, das nur dem Sender und dem Empfänger der Transaktion bekannt ist.

Dieses gemeinsame Geheimnis wird vom Absender anhand der vom Empfänger angegebenen Adresse generiert und erfordert keine aktive Mitarbeit von Absender und Empfänger. Das erste Byte (oder Zeichen) dieses gemeinsamen Geheimnisses wird dann den Daten der Transaktion hinzugefügt, wenn diese im Monero-Netzwerk veröffentlicht wird.

Wenn einer der Teilnehmer an dieser Transaktion seine Wallet anschließend mit der Monero-Blockchain synchronisieren möchte, muss die Wallet nicht mehr alle komplexen mathematischen und kryptografischen Operationen für jeden einzelnen TXO im Netzwerk durchführen, sondern kann nur noch nach diesem 1-Byte-Feld in jeder Transaktion suchen und die zeitaufwändige Verifizierung nur für Transaktionen durchführen, die dieses Tag haben - 1/256 TXOs im Netzwerk, um genau zu sein!

Dieses Tag verrät Außenstehenden keine Informationen über die Transaktion, fügt nur 1 Byte (eine vernachlässigbare Menge) zur Transaktionsgröße hinzu und ermöglicht es uns dennoch, die Synchronisierungszeiten um mehr als 40 % zu reduzieren, indem wir die erforderlichen komplexen Verifizierungen einsparen!

## View-Tags: ein vereinfachtes Beispiel

Stellen Sie sich vor, Sie haben 4.096 Kisten in einem Raum, von denen nur 5 Kisten Ihnen gehören. Die Schachteln sind alle von außen nicht zu unterscheiden, und der einzige Weg, um festzustellen, ob eine Schachtel für Sie bestimmt ist, besteht darin, sie zu öffnen und eine zeitaufwändige mathematische Aufgabe zu lösen, die darin aufgeschrieben ist, um sicherzustellen, dass sie Ihnen gehört.

Stellen Sie sich nun vor, Sie entscheiden sich dafür, dass die Person, die Ihnen diese 5 Boxen schickt, einen speziellen Code mit Ihrer Adresse generiert und dann nur das erste Zeichen dieses generierten Codes auf der Außenseite jeder Box anbringt, die an Sie gesendet wird. Alle anderen machen dasselbe für ihre Schachteln (um sicherzustellen, dass alle Schachteln immer noch nicht zu unterscheiden sind), aber jetzt können Sie einfach auf den Ein-Zeichen-Code auf der Außenseite der Schachtel schauen und nur die Schachteln öffnen, auf denen dieses Zeichen steht.

Während andere Kästchen mit Ihrem Code übereinstimmen, sogar solche, die Ihnen nicht gehören, müssen Sie jetzt nur noch 16 (1/256 Kästchen!) anstelle von 4.096 Kästchen öffnen, um eine mathematische Aufgabe zu lösen. 

Jetzt öffnen Sie diese 16 Kisten, lösen die Matheaufgaben und behalten die 5 Kisten aus dieser Gruppe, die Ihnen tatsächlich gehören!

## Wann werden View-Tags in Monero verfügbar sein?

View-Tags sind eine der Funktionen, die derzeit für die Aufnahme in das [kommende Netzwerk-Upgrade](https://github.com/monero-project/meta/issues/630) geplant sind, und sollten irgendwann in diesem Frühjahr veröffentlicht werden. Die Community [ hat 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (zum Zeitpunkt des Schreibens) zusammengelegt, um Anreize für die Entwicklung und Implementierung von View-Tags zu schaffen, und als Ergebnis daraus wurde der Großteil der Arbeit zur Aufnahme von View-Tags in die Monero-Codebasis bereits von j-berman in Zusammenarbeit mit Gutachtern und Entwicklern fertiggestellt.

Sobald View-Tags vom Netzwerk erzwungen werden, profitieren alle Transaktionen, die nach dem Netzwerk-Upgrade gesendet werden, von der drastisch verbesserten Wallet-Synchronisierungszeit. Sie müssen nichts Besonderes tun, um mit der Verwendung von View-Tags zu beginnen, Ihre bevorzugte Wallet für Monero wird sie nach dem Netzwerk-Upgrade einfach automatisch verwenden!

## Wie kann ich mehr erfahren?

Wenn dies Ihre Neugier auf View-Tags geweckt hat, sehen Sie sich unten einige zusätzliche Links an, die sich ausführlich mit dem Thema befassen:

  * [Reduzieren Sie die Scanzeiten mit 1 Byte pro Ausgabe „View-Tags“](https://github.com/monero-project/research-lab/issues/73)
  * [Fügen Sie View-Tags zu Outputs hinzu, um die Zeit zum Scannen von Wallets zu verkürzen](https://github.com/monero-project/monero/pull/8061)

Weiterlesen

  * [Wie Monero auf einzigartige Weise Kreislaufwirtschaften ermöglicht](/knowledge/monero-circular-economies/)

  * [Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Warum (und wie!) Sie Ihre eigenen Keys halten sollten](/knowledge/hold-your-keys/)

  * [Zu Monero beitragen](/knowledge/contributing-to-monero/)

  * [Wie sich Remote-Knoten auf die Privatsphäre von Monero auswirken](/knowledge/remote-nodes-privacy/)

  * [Wie Monero Hard-Forks verwendet, um das Netzwerk zu aktualisieren](/knowledge/network-upgrades/)

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