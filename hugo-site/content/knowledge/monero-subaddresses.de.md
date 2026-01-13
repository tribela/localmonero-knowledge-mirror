---
title: "Wie Monero-Subadressen die Identitätsverknüpfung verhindern"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero hat schon immer innovative Wege gefunden, um schwierige Datenschutzprobleme zu lösen. Oftmals führen diese Innovationen zu weiteren Innovationen und manchmal können diese daraus resultierenden Technologien sogar für Anwendungsfälle genutzt werden, die zuvor nicht in Betracht gezogen wurden. Nirgendwo wird dies deutlicher als im Fall von Moneros Subadressen-Technologie.

Stellen Sie sich ein hypothetisches Datenschutzproblem vor, bei dem die Nutzung einer Adresse auf mehreren Plattformen durch scheinbar nicht miteinander verbundene Personen zu einer Verknüpfung und Deanonymisierung dieser Personen führen kann. Einfach ausgedrückt: Wenn Sie eine Person namens Billy Joe Bob wären und Äpfel für Bitcoin verkaufen, könnten Sie Ihre Bitcoin-Adresse an einem öffentlichen Ort veröffentlichen, damit Kunden Sie bezahlen können. Sagen wir, die Adresse beginnt mit der alphanumerischen Zeichenfolge 7XybV3... Aber abgesehen von dem offensichtlichen Risiko für die Privatsphäre, dass jeder Ihr Bitcoin-Guthaben überprüfen und sehen kann, wie viel Sie verkauft haben, gibt es noch ein zweites, nicht so oft erwähntes Risiko für die Privatsphäre. Nehmen wir an, Sie wären auch ein Untergrund-Hacker mit dem Namen l33tz0r. Sie arbeiten als Whistleblower, der die ahnungslose Bevölkerung über die Korruption der Regierung aufklärt, und es ist unbedingt notwendig, dass Sie Ihre Identität geheim halten. Sie nehmen Bitcoin-Spenden für Ihre Arbeit an und veröffentlichen die Adresse in einem öffentlichen Forum. Es ist dieselbe Adresse, unter der Sie auch Geld von Ihren Apfelkunden annehmen. Die mit 7XybV3....

Ein einfacher, aber verheerender Deanonymisierungsangriff wäre es, eine Internetsuchmaschine zu benutzen, um nach Ihrer Bitcoin-Adresse zu suchen. Gibt man die Adresse von 7XybV3... in die Suchmaschine ein, erhält man zwei verschiedene Ergebnisse. Das Apfelgeschäft und l33tz0r. Das reicht aus, um die beiden Identitäten miteinander zu verknüpfen und l33tz0r zu deanonymisieren, was möglicherweise beängstigende Folgen für die Machthaber hat.

Es ist wichtig zu wissen, dass dieser Angriff auch mit Monero möglich ist. Obwohl Monero die meisten On-Chain-Daten verbirgt, werden bei diesem Angriff keine Daten verwendet. Es wird nur die Adresse verwendet, die mitgeteilt werden muss, um eine Zahlung zu erhalten. Im Falle von anonymen Spenden ist dies öffentlich. Dies ist ein möglicher Weg, auf dem Monero-Benutzer unwissentlich ihre Privatsphäre verletzen können, und ist auch ein Beispiel dafür, dass Monero, obwohl es in Bezug auf die Wahrung der Privatsphäre erstklassig ist, nicht kugelsicher ist.

Der übliche Weg, dieses Problem zu umgehen, war der Besitz mehrerer Wallets. Da für jede Identität (oder jeden Anwendungsfall) unterschiedliche Adressen angegeben werden, können sie nicht miteinander verknüpft werden. Dieser Schutz gilt jedoch nur, wenn der Nutzer die Adressen nicht verwechselt. Würde er versehentlich die falsche Adresse angeben, hätte dies die gleichen Auswirkungen auf die Verknüpfung. Außerdem muss der Seed jeder Adresse sicher aufbewahrt werden, was den Aufwand für die Sicherheit bei jeder neuen Wallet erhöht.

Die Lösung von Monero waren Subadressen. Die Fähigkeit, eine absolut riesige Anzahl von Adressen unterhalb der Hauptadresse zu erstellen und diese als eine Art Seed zu verwenden. Jede generierte Subadresse kann Monero akzeptieren, und alle gehen an dieselbe Wallet. Mit dieser Methode ist die Anzahl der Identitäten, die unter einer Adresse betrieben werden können, riesig, während der Aufwand für die Datensicherheit minimal ist. Diese Adressen sind auch mathematisch nicht verknüpfbar, so dass ein außenstehender Beobachter große Schwierigkeiten haben wird, sie zu verknüpfen, es sei denn, der Nutzer schreit seine Verbindung in die Welt hinaus.

Aber es gibt noch einen weiteren interessanten Anwendungsfall für Subadressen: als Ersatz für die allseits verhassten Zahlungsverkehrs-IDs.

Mit Hilfe von Zahlungs-IDs konnten Händler feststellen, welcher Kunde welche Zahlung getätigt hat. Da die Monero-Informationen auf der Kette verschleiert werden, kann der Empfänger einer Transaktion nicht sehen, von welcher Adresse sie gesendet wurde. Das bedeutet, dass es bei Artikeln mit ähnlichem Preis und mehreren Bestellungen unmöglich sein kann, den Absender zu identifizieren. Die Zahlungs-IDs sind eine eindeutige, zufällige Zeichenfolge, die vom Händler generiert und dem Kunden mitgeteilt wird. Der Kunde fügt sie beim Absenden der Transaktion in ein separates Feld ein. Diese zufällige Zeichenfolge wird als Teil der Transaktion in der Blockchain gespeichert, und auf diese Weise kann der Händler eingehende Transaktionen identifizieren und sortieren.

Diese Methode war in mehrfacher Hinsicht mangelhaft. Erstens beeinträchtigt sie die Einheitlichkeit der Daten auf der Blockchain. Zusätzliche, eindeutige Metadaten können einige Transaktionen aus der Masse herausheben und so eine heuristische Analyse ermöglichen. Dies gilt insbesondere dann, wenn diese Metadaten nicht für alle verbindlich vorgeschrieben sind. Dies für alle verpflichtend zu machen, würde jedoch unnötig Platz in der Blockchain schaffen und wurde daher nicht weiter verfolgt. Sollte eine Zahlungs-ID aus irgendeinem Grund wiederverwendet werden, wäre es zudem trivial, zwei Transaktionen als miteinander verbunden zu kennzeichnen. Dies ist typischerweise bei Einzahlungen an einer Börse der Fall, und jeder könnte problemlos Transaktionen als Einzahlungen an einer Börse und von einer bestimmten Person verknüpfen.

Zweitens, aus einer UX-Perspektive, schaffen Zahlungs-IDs einen zweiten Schritt, an den Kryptowährungsnutzer, die von anderen Coins kommen, nicht gewöhnt sind, und wenn sie vergessen werden, verursacht dies dem Händler, der diese Transaktionen mit anderen Mitteln identifizieren muss, massive Kopfschmerzen. Dies geschah in der Regel, indem man direkt mit jedem Kunden sprach, der die Zahlungs-ID vergessen hatte, und andere Identifizierungsinformationen bestätigte, die nur er kennen konnte, wie z. B. eine Kombination aus dem Betrag, dem Sendedatum und der Transaktions-ID.

Dieser zusätzliche Schritt wurde von vielen versäumt, und es ging so weit, dass einige Börsen anfingen, den Kunden Geld in Rechnung zu stellen, wenn ihr Geld manuell zurückgeholt werden musste, weil sie eine Zahlungs-ID vergessen hatten. Andere bissen die Zähne zusammen und nahmen die zusätzlichen Supportkosten in Kauf, aber niemand war darüber glücklich.

Es gab eine Lösung für dieses Problem, nämlich integrierte Adressen, bei denen die Adresse und die Zahlungs-ID in einer Zeichenkette zusammengeführt wurden, so dass sie nicht vergessen werden konnte, aber die Akzeptanz war ziemlich gering, trotz der Vorteile, die sich für die Händler daraus ergeben hätten.

Eine interessante Entwicklung war die Einführung von Subadressen, die den Tag retteten. Die Fähigkeit, große Mengen an Subadressen pro Hauptadresse zu generieren und zu identifizieren, welche Transaktionen in welche Subadressen flossen, ermöglichte es Händlern, sich auf elegante Weise von Zahlungs-IDs zu befreien und gleichzeitig die nächste Generation der Monero-Technologie einzuführen. Seitdem haben die meisten Börsen und Händler-Tools auf Subadressen als primäre Methode zur Identifizierung von Transaktionen umgestellt.

Was als Lösung für ein Datenschutzproblem begann, wurde zu etwas viel Größerem, das ein wichtiges UX-Problem für Händler und Kunden gleichermaßen löste. Innovation zieht weitere Innovationen nach sich, die oft zu unerwarteten Gewinnen für alle führen können. Monero hat dies immer wieder erlebt und setzt große Anstrengungen in die Innovation dessen, was auf der Blockchain möglich ist. Wer weiß, was wir gemeinsam noch alles auf die Beine stellen können?

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

  * [Wie RingCT Monero-Transaktionsbeträge verbirgt](/knowledge/monero-ringct)/

  * [Wie Monero Stealth-Adressen Ihre Identität schützen](/knowledge/monero-stealth-addresses)/

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