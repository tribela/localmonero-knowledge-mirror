---
title: "Wie RingCT Monero-Transaktionsbeträge verbirgt"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Die Privatsphäre von Monero hängt nicht von einem einzelnen Mechanismus ab, der, wenn er kaputt geht, die Gesamtheit der Transaktionen aufdecken würde, sondern von drei verschiedenen Technologien, die zusammenarbeiten, um ganzheitliche Privatsphäre zu bieten und gleichzeitig die Schwächen der anderen Teile auszugleichen. Dieser dreigleisige Ansatz besteht aus [Ringsignaturen](/knowledge/ring-signatures), RingCT und [Stealth-Adressen](/knowledge/monero-stealth-addresses). Diese drei Technologien verbergen jeweils den tatsächlichen Output (Sender), Betrag und Empfänger. Heute sprechen wir über RingCT.

RingCT ist wohl das technischste der drei und kann schwer zu verstehen sein, daher werden wir nicht behandeln, wie es genau funktioniert, sondern zeigen, wie es möglich ist, einen Betrag nicht zu kennen und dennoch Dinge darüber zu bestätigen . Und keine Sorge, wir werden wie immer viele Beispiele verwenden.

Lassen Sie uns zuerst untersuchen, warum es wichtig ist, irgendetwas über die Beträge zu überprüfen. Warum können wir sie nicht einfach komplett geheim halten? Die Antwort ist, dass es clevere Möglichkeiten gibt, wie Menschen Geld aus dem Nichts schaffen können, wenn sie die Möglichkeit dazu haben. Wie könnte so etwas funktionieren? Schauen wir uns ein Beispiel an.

Wenn Sie einen Artikel von Ihrem Freund kaufen möchten und er zehn Dollar dafür will, dann beginnen Sie mit zehn Dollar und er beginnt mit null. Nachdem Sie ihm die zehn Dollar gegeben haben, hat er zehn Dollar und Sie haben null. Du hast mit zehn angefangen, und jetzt hat er zehn. Bei dieser Transaktion wurde kein Geld geschaffen oder vernichtet.

Mit Kryptowährungen kann eine clevere Person zehn Dollar für den Artikel geben und statt null Dollar als Wechselgeld zwei Dollar zurückbekommen. Anstatt dass 0 und 10 zu 10 und 0 (oder 10=10) führen, führt jetzt 0 und 10 zu 10 und 2 (oder 10=12). 2 Monero wurden einfach aus dem Nichts erschaffen. Sie können sich vorstellen, dass der Einzelne, wenn er sich das mehrmals antun würde, in kurzer Zeit ein gigantisches Vermögen anhäufen könnte.

Bei Bitcoin und anderen wäre dies leicht zu erkennen. Sie sehen sich die Inputs an, die in eine Transaktion eingehen, und die Outputs, die herauskommen, und stellen sicher, dass das, was gesendet wird, dem entspricht, was empfangen wird. Wenn diese Beträge verschlüsselt und nicht sichtbar waren, hat ein Benutzer keine Möglichkeit zu überprüfen, ob das, was gesendet und was empfangen wird, gleich ist.

In einem Versuch, die Privatsphäre von Bitcoin zu erhöhen, hat Gregory Maxwell Confidential Transactions (CT) entwickelt, eine neue Technologie, die verschlüsselte Beträge ermöglicht und gleichzeitig beweist, dass dabei nichts erstellt oder zerstört wurde. Wie die meisten Datenschutztechnologien hat sie es nicht in Bitcoin geschafft, aber Monero war sehr daran interessiert, sie zu übernehmen. Es gab nur ein Problem. Die bereits implementierte Technologie der Ringsignaturen war mit der vorgeschlagenen Idee nicht kompatibel. Einer der damaligen MRL-Forscher, Shen Noether, modifizierte CT in RingCT, eine Version von CT, die mit Ringsignaturen kompatibel war.

Noch einmal, die Funktionsweise ist recht technisch und in einem Einführungsartikel schwer zu erklären. Für den Kryptographie-Enthusiasten, der es einfach wissen muss, gibt es im Internet viele ausführliche Artikel über das Innenleben von CT. Für den Rest von uns wird dieser Artikel zeigen, wie es möglich sein könnte, die Beträge zu verbergen, aber dennoch zu beweisen, dass nichts erschaffen oder zerstört wurde.

Nehmen wir an, Alice will Bob Geld schicken. Alice sendet 10 XMR an Bob, der 10 XMR erhält. 10 = 10, also ist hier nichts falsch. Aber Alice möchte nicht, dass jemand weiß, wie viel sie sendet. Also schaffen sie und Bob ein gemeinsames Geheimnis. Im Grunde eine Nummer, die nur die beiden kennen. Nehmen wir an, diese Zahl ist 22. Jetzt multipliziert Alice 10 (was sie wirklich sendet) mit 22, um 220 zu erhalten. Dies ist die Zahl, die sie mit dem Netzwerk teilt. 

Die Miner selbst kennen die Geheimnummer nicht. Wenn dies der Fall wäre, könnten sie die angezeigte Zahl durch die Geheimzahl dividieren und den tatsächlichen Betrag erhalten. Aber da sie diese nicht kennen, können sie es nicht. Sie sehen jedoch, dass Bob 220 erhält. 220 gesendet. 220 erhalten. 220 = 220. Auf diese Weise kann das Netzwerk verifizieren, dass kein Monero erstellt oder zerstört wurde, ohne den tatsächlichen Betrag zu kennen, den Alice Bob geschickt hat.

Da Bob die gemeinsame Geheimzahl kennt, dividiert er, wenn er das Geld erhält, einfach durch 22, um den tatsächlichen Betrag zu erhalten, den Alice gesendet hat, 10. Alice und Bob wissen beide, wie viel gesendet und wie viel empfangen wurde allen anderen wird eine falsche Nummer gegeben.

Noch einmal, das ist nicht die eigentliche Funktionsweise von CT, aber es gibt eine Vorstellung davon, wie so etwas möglich sein könnte. Der wahre Weg beinhaltet Dinge wie Pedersen-Zusagen, zwei gesendete Beträge (ein verschlüsselter Betrag an den Empfänger und ein zugesagter Betrag an das Netzwerk) und … ja, es ist bereits leicht zu sehen, wie man sich in all dem verlieren kann. 

Eine Sache, die jedoch zu beachten ist, ist, dass RingCT zwar den zwischen zwei Parteien in einer Transaktion getätigten Betrag verbirgt, aber nicht zwei andere Zahlengruppen.

Das erste sind die Coinbase-Transaktionen. Wenn Ihnen dieser Begriff nicht geläufig ist, bedeutet er im Grunde die Belohnung, die Miner für das Finden des nächsten Blocks erhalten. Diese Nummer ist nicht versteckt. Jeder kann sehen, wie viel das Protokoll einem Miner für seinen Dienst verliehen hat. Auf diese Weise kann die aktuelle Menge an vorhandenem Monero ermittelt werden, indem alle Coinbase-Transaktionen addiert werden. Ihre Summe entspricht dem aktuell im Umlauf befindlichen Monero.

Die zweite nicht versteckte Zahl ist die Gebühr, die an die Miner gezahlt wird, wenn ein Benutzer eine Transaktion sendet. Die Gebühren müssen klar sein, damit die Miner wissen, wen sie priorisieren müssen. Auf diese Weise können Benutzer jedoch ihre Privatsphäre verletzen, als ob jemand jedes Mal, wenn er eine Transaktion sendet (wie 0,12345), eine einzigartige Miner-Gebühr verwendet, dann können seine Transaktionen verknüpft werden.

Abgesehen von diesen Fällen versteckt RingCT seit 2017 Monero-Beträge und unsere kollektive Privatsphäre ist umso stärker.

Weiterlesen

  * [Wie Monero auf einzigartige Weise Kreislaufwirtschaften ermöglicht](/knowledge/monero-circular-economies)/

  * [Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Warum (und wie!) Sie Ihre eigenen Keys halten sollten](/knowledge/hold-your-keys)/

  * [Zu Monero beitragen](/knowledge/contributing-to-monero)/

  * [Wie sich Remote-Knoten auf die Privatsphäre von Monero auswirken](/knowledge/remote-nodes-privacy)/

  * [Wie Monero Hard-Forks verwendet, um das Netzwerk zu aktualisieren](/knowledge/network-upgrades)/

  * [View-Tags: Wie ein Byte die Synchronisierungszeiten der Monero-Wallet um über 40 % reduziert](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool und seine Rolle bei der Dezentralisierung des Monero-Mining](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Was es für Monero tun wird](/knowledge/seraphis-for-monero)/

  * [Ist die Umwandlung von Bitcoin in Monero genauso privat wie der direkte Kauf von Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [Warum Monero im Gegensatz zu Zcash ein vertrauensloses Setup verwendet](/knowledge/monero-trustless-setup)/

  * [Warum Monero ein besserer Wertspeicher ist als Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Wie Monero die Netzwerkeffekte von Bitcoin überwinden kann](/knowledge/network-effect)/

  * [Warum Monero die kritischste Community hat](/knowledge/critical-thinking)/

  * [Betrügereien, auf die Sie bei der Verwendung von Monero achten sollten](/knowledge/monero-scams)/

  * [Wie Atomic Swaps in Monero funktionieren](/knowledge/monero-atomic-swaps)/

  * [Was jeder Monero-Benutzer wissen muss, wenn es ums Networking geht](/knowledge/monero-networking)/

  * [Wie Monero Stealth-Adressen Ihre Identität schützen](/knowledge/monero-stealth-addresses)/

  * [Wie Monero-Subadressen die Identitätsverknüpfung verhindern](/knowledge/monero-subaddresses)/

  * [Monero-Outputs erklärt](/knowledge/monero-outputs)/

  * [Monero Best Practices für Anfänger](/knowledge/monero-best-practices)/

  * [Wie Ringsignaturen die Ausgaben von Monero verschleiern](/knowledge/ring-signatures)/

  * [Wie Monero das Blockgrößenproblem löste, das Bitcoin plagt](/knowledge/dynamic-block-size)/

  * [Wie CLSAG die Effizienz von Monero verbessern wird](/knowledge/what-is-clsag)/

  * [Warum Monero eine Tail-Emission hat](/knowledge/monero-tail-emission)/

  * [Eine kurze Geschichte von Monero](/knowledge/monero-history)/

  * [Das Wired Magazine hat Unrecht mit Monero, hier ist der Grund](/knowledge/wired-article-debunked)/

  * [Die 15 wichtigsten Monero-Mythen und -Bedenken widerlegt](/knowledge/monero-myths-debunked)/

  * [Wie Dandelion++ die Transaktionsursprünge von Monero geheim hält](/knowledge/monero-dandelion)/

  * [Warum Monero Open Source und dezentralisiert ist](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: Was RandomX so besonders macht](/knowledge/monero-mining-randomx)/

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better)/

Weiterlesen