---
title: "Wie Monero Stealth-Adressen Ihre Identität schützen"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero hat einen dreistufigen Ansatz zum Schutz der Privatsphäre implementiert. Diese Technologien sind [Ringsignaturen](/knowledge/ring-signatures), die den wahren Ausgang (Absender) verbergen, RingCT, das die Beträge verbirgt, und Stealth-Adressen, die den Empfänger verbergen. Heute werden wir uns mit der letzten der genannten Technologien befassen: Stealth-Adressen.

Es gibt viele Gründe, warum eine Person verbergen möchte, an wen sie sendet. Wir dürfen uns nicht einreden lassen, dass es sich bei allen Beispielen dieser Art um unerwünschte Verhaltensweisen handelt. Dinge wie das Senden an eine unpopuläre politische Partei, das Spenden an Wohltätigkeitsorganisationen oder das Unterstützen von Personen, die von der Kultur als "gestrichen" angesehen werden, sind alles Beispiele dafür, dass man sein Ausgabeverhalten aus Angst vor Konsequenzen verbergen möchte, aber sie sind völlig legitim.

Auf einer transparenten Blockchain sind die Adressen, an die man seine Transaktionen sendet, für alle sichtbar. Es ist wichtig zu bedenken, dass Miner, die nicht damit einverstanden sind, wohin das Geld fließt, sich dafür entscheiden können, es nicht zu einem Block zu machen, wodurch diese Transaktion auf einer scheinbar zensurresistenten Plattform effektiv zensiert wird. Die einzige Möglichkeit, diese zugegebenermaßen unwahrscheinliche Zensur zu verhindern, besteht darin, dass die Miner nicht zwischen den Transaktionen unterscheiden können, weil alle Metadaten auf der Kette durch verschiedene Mittel verschleiert werden. Etwas, wofür Monero bekannt ist.

Monero löst das Problem der transparenten Adressen durch die Implementierung von Stealth-Adressen, einer Technologie, die 2011 von dem Bitcoin-Talk-Forumsnutzer ByteCoin für Bitcoin entwickelt wurde (die Beziehung zu Bytecoin, das später Stealth-Adressen integrieren sollte, ist unbekannt). Die aktuelle Form von Stealth-Adressen hat jedoch einige Verbesserungen gegenüber der ursprünglichen Idee. Aber um zu sehen, wie sie funktionieren, sollten wir zunächst über Schlüssel sprechen.

Es ist schwer, im Bereich der Kryptowährungen zu sein und nicht von Schlüsseln zu hören. Sätze wie "Sichern Sie Ihren privaten Schlüssel" sind üblich, aber wenn der Durchschnittsbürger die Worte "öffentlicher Schlüssel" und "privater Schlüssel" hört, bekommt er Angst und denkt, dass es zu technisch und verwirrend ist, um es zu verstehen. Aber keine Sorge. Wir werden es langsam angehen und viele Beispiele verwenden.

Die beiden Arten von Schlüsseln, die bei Kryptowährungen verwendet werden, sind, wie bereits erwähnt, öffentlich und privat. Diese beiden Schlüssel werden in der Regel paarweise verwendet, was bedeutet, dass ein bestimmter öffentlicher und privater Schlüssel miteinander verbunden sind. Der öffentliche Schlüssel wird in der Regel vom privaten Schlüssel abgeleitet, d. h., wenn Sie den privaten Schlüssel kennen, kann Ihre Wallet einige raffinierte Berechnungen anstellen und jedes Mal den richtigen öffentlichen Schlüssel ermitteln.

Wie die Namen schon andeuten, kann der öffentliche Schlüssel ohne Folgen öffentlich sein. Normalerweise ist er ein Teil der Adresse, die Sie freigeben, um Geld in Ihre Kryptowährungs-Wallet zu erhalten. Der private Schlüssel ist ebenfalls ein Schlüssel, der nicht weitergegeben werden sollte. Wenn er also gestohlen oder weitergegeben wird, kann die heimtückische dritte Partei Ihr Geld ausgeben, in der Regel für sich selbst.

Eine einfache Analogie dazu wäre ein Vorhängeschloss und der Schlüssel, der zum Aufschließen benötigt wird. Das geöffnete Vorhängeschloss kann frei weitergegeben werden, und tatsächlich kann alles mit diesem Vorhängeschloss verschlossen werden, aber nur die Person, die den Schlüssel hat, kann alles öffnen, was mit dem Vorhängeschloss verschlossen ist. Das Vorhängeschloss kann kopiert und weitergegeben werden, der Schlüssel sollte es nicht.

Diese Schlüssel werden normalerweise vom Benutzer abstrahiert, so dass man sie nie wirklich sieht. In Monero erscheinen sie nicht als eine unheimliche alphanumerische Zeichenkette. In Monero kennt der normale Benutzer den privaten Schlüssel als Seed. Der Seed (den Sie sich aufschreiben sollten, falls Sie es noch nicht getan haben), ist eigentlich nur ein für Menschen lesbarer privater Schlüssel.

Sehen Sie? Also doch nicht so beängstigend. Zurück zu Stealth-Adressen.

Wie bereits erwähnt, wurden Stealth-Adressen ursprünglich nicht für Monero, sondern für Bitcoin entwickelt. Wie bei den meisten jungen Ideen gab es auch bei dieser ersten Version Probleme. Der nächste Versuch war CryptoNote, das von Nicholas van Saberhagan für Bytecoin, den Vorläufer von Monero, entwickelt wurde ([siehe unsere Geschichte von Monero und Bytecoin hier](/knowledge/monero-history)) und obwohl es eine deutliche Verbesserung gegenüber dem Original darstellte, hatte auch es einige kleine Mängel.

Schließlich wurde eine letzte Iteration von einem Entwickler für eine andere, inzwischen nicht mehr existierende Kryptowährung entwickelt, die die noch bestehenden Datenschutz- und Sicherheitsprobleme mit der Idee beseitigte. Dies fand schließlich seinen Weg in Monero und wird heute verwendet.

Obwohl diese Datenschutz- und Sicherheitsprobleme gelöst wurden, fügten die Stealth-Adressen selbst der Blockchain-Technologie eine andere Art von Eigenart hinzu, eine, die es vorher nicht gab. Die Notwendigkeit zu scannen. Da die Empfängeradressen nicht öffentlich auf der Blockchain angezeigt werden, weiß der Empfänger nie, ob eine bestimmte Transaktion von ihm stammt, so dass er jede eingehende Transaktion mit seinem privaten Schlüssel scannen muss, um zu sehen, ob sie von ihm stammt.

Bei transparenten Coins müssen sie nur prüfen, ob eine Transaktion an Ihre Adresse geht. Eine einfache Ja-oder-Nein-Frage. Bei Stealth-Adressen hingegen könnte jede Transaktion an Sie gesendet werden, so dass Sie versuchen müssen, jede Transaktion mit Ihrem privaten Schlüssel zu entsperren, um zu sehen, ob sie geöffnet wird.

Dies ist ein zusätzlicher Schritt, den Bitcoin und seine Derivate nicht haben, und macht die anfängliche Einrichtung der Wallet, zusammen mit der Synchronisierung einer Wallet, wenn man sie eine Weile nicht geöffnet hat, viel länger als Bitcoin. Der Kompromiss ist jedoch notwendig, um die Datenschutzgarantien freizuschalten, die es gibt. Es sei darauf hingewiesen, dass Stealth-Adressen, anders als der schwächste Punkt des Datenschutz-Dreigestirns, die Ringsignaturen, nicht anfällig für Heuristiken sind. Sie beruht auf der bewährten elliptischen Kurvenkryptographie, auf die sich das gesamte Internet verlässt, so dass ihr Bruch das Ende der Computersicherheit im Allgemeinen bedeuten würde, nicht nur für Monero.

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

  * [Was jeder Monero-Benutzer wissen muss, wenn es ums Networking geht](/knowledge/monero-networking/)

  * [Wie RingCT Monero-Transaktionsbeträge verbirgt](/knowledge/monero-ringct/)

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