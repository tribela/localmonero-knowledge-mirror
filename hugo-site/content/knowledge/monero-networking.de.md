---
title: "Was jeder Monero-Benutzer wissen muss, wenn es ums Networking geht"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Es sollte niemanden überraschen, dass Monero, und tatsächlich alle Kryptowährungen, im Internet laufen. Und doch, obwohl diese Aussage grundlegend und offensichtlich erscheint, berücksichtigen viele nicht die Auswirkungen dessen, was dies in Bezug auf ihre Privatsphäre bedeutet. Mit anderen Worten, es gibt einige Dinge, vor denen Monero schützen kann und vor denen nicht, nur weil es von Natur aus im Internet läuft. Einige dieser Überlegungen sind lediglich Unannehmlichkeiten, während andere in einem Szenario, in dem absolute Privatsphäre erforderlich ist, viel schwerwiegender sind. Nehmen wir uns die Zeit, uns damit vertraut zu machen, wie Monero-Benutzer im Netzwerk miteinander interagieren und was dies für ihre Privatsphäre bedeutet.

Beginnend mit der trivialen Seite der Dinge, wenn ein Benutzer keinen Zugang zum Internet hat, kann er keine neuen Blöcke herunterladen, Transaktionen im Namen anderer verbreiten oder eigene Transaktionen senden. Interessant ist, dass ein Benutzer mit einem vollständigen Knoten ohne Internetzugang offline eine Transaktion erstellen kann, die später gesendet werden kann. Dies liegt daran, dass eine Ringsignatur nur Ausgaben aus der Blockchain benötigt, um sich zu verstecken. Eine kurze Erinnerung daran, [wie Ringsignaturen funktionieren](/knowledge/ring-signatures), sie verbergen den tatsächlichen Output, den ein Benutzer sendet, unter einer Sammlung nicht verbundener Outputs, die aus der Vergangenheit ausgewählt wurden. Wenn der Benutzer Zugriff auf diese Outputs in Form einer vollständig heruntergeladenen Blockchain (vollständiger Knoten) hat, kann er die Ringsignatur aus den vergangenen Ausgaben erstellen und, sobald die Internetverbindung wiederhergestellt ist, die Transaktion an das Netzwerk weitergeben.

Ein Benutzer, der einen entfernten Knoten verwendet, kann dies nicht tun, da er beim Erstellen seiner Ringsignatur den entfernten vollständigen Knoten kontaktiert, um Outputs zu erhalten, die in die Ringsignatur aufgenommen werden sollen. Kein Internet bedeutet, dass sie diesen Knoten nicht erreichen können, also haben sie keine Offline-Transaktionskonstruktionsfunktionen.

Bevor wir mit einigen Überlegungen zum Datenschutz fortfahren, lassen Sie uns eine kurze Einführung in die Funktionsweise des Internets als Ganzes geben. Das gesamte Internet ist nichts anderes als Computer, die sich mit anderen Computern verbinden. Das ist es. Der Blog, den Sie gerne lesen? Nur einige Dateien, die auf dem Computer einer anderen Person gehostet werden. Diese Website, auf der Sie diesen Artikel lesen (LocalMonero)? Dateien und Code, die irgendwo auf einem Computer gehostet werden. Sogar verrückt große Seiten funktionieren auf diese Weise. Nehmen Sie zum Beispiel YouTube. Nur Videodateien, die auf den gigantischen Computersystemen von Google gehostet werden, und Sie stellen eine Verbindung her, um das Video auf Ihren eigenen Computer herunterzuladen, damit Sie es ansehen können.

Diese Computer können sich voneinander unterscheiden, da jeder mit dem Internet verbundene Computer eine eindeutige Identifikationsnummer erhält, die als IP-Adresse bezeichnet wird. Dies sind normalerweise vier durch Punkte getrennte Zahlengruppen, zum Beispiel: 172.66.35.7. Es ist wichtig, dies im Hinterkopf zu behalten, wenn wir darüber nachdenken, wie Monero-Informationen im Internet übertragen werden. Monero ist ein Peer-to-Peer-Netzwerk (P2P), was bedeutet, dass sich Computer direkt miteinander verbinden, anstatt einen Vermittler zu verwenden. Wenn also der Full Node eines Benutzers einen neu entdeckten Block herunterlädt, lädt er ihn nicht von einem zentralen Server herunter, sondern von seinen Kollegen. Der Nachteil dabei ist, dass die Benutzer, da sie sich direkt miteinander verbinden, die IP-Adressen der anderen kennen.

Nun? Was ist die große Sache? Es ist nur eine Zahl, richtig? Nicht genau. IP-Adressen selbst enthalten Informationen über den Benutzer, wie z. B. das Herkunftsland und den Netzwerkanbieter, aber noch schlimmer, Internet Service Provider (ISPs) kennen die IP-Adresse jeder Person, die ihre Dienste nutzt. Dies bedeutet, dass diese ISPs und diejenigen, mit denen sie zusammenarbeiten, den Internetverkehr eines Benutzers beobachten und mithilfe einiger cleverer Taktiken feststellen können, dass sie Monero verwenden. Nun, bevor Sie Angst bekommen, beachten Sie die Formulierung dort. Alles, was diese Schnüffler tun können, ist zu sehen, dass sich eine Person mit anderen Knoten im Monero-Netzwerk verbindet. Aufgrund der Datenschutztechnologie von Monero wird nichts anderes über die Person durchsickern gelassen. Nicht, ob sie einen Knoten betreiben oder nicht, oder ob/wann sie Transaktionen senden, und wenn eine Transaktion gesendet wird, ist keine ihrer Informationen bekannt. Alles, was diese ISPs sehen können, ist, dass sich einer ihrer Benutzer mit dem Monero-Netzwerk verbindet.

Nun, für manche Menschen an einigen Orten können diese Informationen allein ausreichen, um den Ruf oder die Freiheit zu schädigen. Oder vielleicht ist die Vorstellung, dass jemand in Ihre Privatsphäre eindringt und was Sie im Internet tun, aus irgendeinem Grund für Sie nicht akzeptabel. Diese Personen werden ermutigt, sich nur über VPNs, Tor oder I2P mit dem Monero-Netzwerk zu verbinden, allesamt Dienste, die die IP-Adresse eines Benutzers vor anderen verbergen und verstecken, was ein Benutzer vor seinem ISP tut. Die Unterschiede zwischen diesen Diensten würden den Rahmen dieses Artikels sprengen, aber es gibt viele qualitativ hochwertige Artikel zu diesem Thema, daher werden besorgte Benutzer ermutigt, sich zu informieren!

Für den Rest von uns denken wir vielleicht, dass es keine große Sache ist, wenn andere wissen, dass wir mit dem Monero-Netzwerk verbunden sind. Schließlich werden die tatsächlichen Inhalte unserer Transaktionen, oder wenn wir überhaupt welche versenden, der Öffentlichkeit verborgen, also was ist der Schaden? Dies mag zwar zutreffen, Benutzer werden jedoch ermutigt, die Tatsache zu berücksichtigen, dass die Hauptattraktion von Kryptowährungen ihre eigene Bank ist. Wenn Sie Ihre privaten Keys besitzen und etwas damit passiert, kann Ihnen niemand helfen, Ihr verlorenes Geld zurückzuerhalten.

Ihre eigene Bank zu sein bedeutet, nicht nur Ihre digitale Sicherheit, sondern auch Ihre physische Sicherheit zu berücksichtigen. Es könnte sehr gut sein, dass das Wissen einer Person, die sich mit dem Monero-Netzwerk verbindet, unerwünschte Aufmerksamkeit erregen kann, nicht unbedingt von großen Akteuren wie Nationalstaaten, sondern von kleineren mit egoistischen Interessen, wie Hackern, die auf leichtes Geld aus sind. Es gibt in der Tat unzählige Geschichten im Krypto-Raum, dass solche Szenarien tatsächlich stattfinden.

Dieser Artikel soll keine Angst machen oder abschrecken, sondern die Benutzer dazu ermutigen, zu recherchieren, welche Methoden zum Schutz beim Surfen im Internet für sie geeignet sind. Die gute Nachricht ist, dass diese Fähigkeiten auch auf die allgemeine Internetnutzung übertragen werden, nicht nur auf die Monero-Nutzung, und daher kann ein versierter Benutzer in unserer zunehmend mit dem Internet verbundenen Welt nichts falsch machen, wenn er die richtigen Kenntnisse und Fähigkeiten ansammelt, um sicher zu bleiben und wirklich seine eigene Bank zu sein.

Weiterlesen

  * [Wie Monero auf einzigartige Weise Kreislaufwirtschaften ermöglicht](/knowledge/monero-circular-economies/)

  * [Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Warum (und wie!) Sie Ihre eigenen Keys halten sollten](/knowledge/hold-your-keys/)

  * [Zu Monero beitragen](/knowledge/contributing-to-monero/)

  * [Wie sich Remote-Knoten auf die Privatsphäre von Monero auswirken](/knowledge/remote-nodes-privacy/)

  * [Wie Monero Hard-Forks verwendet, um das Netzwerk zu aktualisieren](/knowledge/network-upgrades/)

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