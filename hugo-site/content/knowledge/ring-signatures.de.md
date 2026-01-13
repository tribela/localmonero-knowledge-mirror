---
title: "Wie Ringsignaturen die Ausgaben von Monero verschleiern"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ist weit und breit im gesamten Kryptoraum als der König der Privacy-Coins bekannt. Während jeder weiß, dass Monero einen guten Datenschutz bietet, verstehen nicht so viele, wie der Datenschutz funktioniert.

Viele andere Privacy-Coins veröffentlichen Vergleichstabellen-Infografiken, die die Namen der Datenschutztechnologie jedes Coins auflisten, und in den meisten Fällen bezeichnen sie die Technologie von Monero als RingCT, aber das ist nur teilweise wahr. Monero hat tatsächlich einen dreigleisigen Ansatz zum Datenschutz. Eine Technologie, um den Empfänger einer Transaktion zu verbergen, eine, um den gesendeten Betrag zu verbergen, und eine, um die verwendeten Outputs zu verbergen, das sind Stealth-Adressen, RingCT bzw. Ringsignaturen.

Dieser dreigleisige Ansatz bedeutet, dass, wenn eine der Technologien kaputt geht, die anderen nicht unbedingt das gleiche Schicksal erleiden. Ringsignaturen sind das schwächste Glied im Datenschutzsystem; das Wort schwach bedeutet hier, dass es am anfälligsten für heuristische Angriffe ist. Nehmen wir uns etwas Zeit, um sie zu erkunden, oder?

Wie oben erwähnt, besteht das Ziel von Ringsignaturen darin, einen in einer Transaktion verwendeten Output zu verschleiern. Machen Sie sich keine Sorgen, wenn die „Input/Output“-Terminologie der Kryptowährung für Sie verwirrend ist. Es ist eigentlich gar nicht so kompliziert. Wenn Sie „Output“ hören, denken Sie einfach an einen Scheck. Eines dieser nicht mehr ganz so verbreiteten Dinge, mit denen die Leute bezahlen. Wie ein Scheck kann es auf einen beliebigen Betrag lauten – 10 $, 32,50 $ usw. – und wird zwischen Transaktionsparteien ausgetauscht. Bei Kryptowährungen erfüllen Outputs diese Funktionen.

Wenn Ihnen jemand 10 Monero zahlt, erhalten Sie einen XMR-Output von 10. Diese Ausgabe hat einen Wert (10) und wird aus der Wallet des Absenders entnommen. Wenn Sie für eine Dienstleistung bezahlen, verlässt ein Schein Ihre physische Brieftasche und wird der Person ausgehändigt, von der Sie kaufen.

Der Output wird verborgen, indem ein Ring (daher der Name) von Täuschungs-Outputs konstruiert wird. Aber diese Täuschungen sind keine „gefälschten“ Outputs. Sie sind reale vergangene Outputs der Blockchain, die nichts mit der gegenwärtigen Transaktion zu tun haben, aber für einen externen Beobachter könnte jeder dieser Outputs genauso wahrscheinlich erscheinen wie die echte. Die Größe des Satzes von Täuschungs-Outputs plus der echten wird als Ringgröße bezeichnet, und diese beträgt derzeit 11 bei Monero. Es gibt also zehn Täuschungs-Outputs und einen echten.

Warum erhöhen wir diese Zahl nicht einfach auf 100 oder sogar 1000? Je mehr desto besser, oder? Nun, aus Sicht des Datenschutzes ja, aber es gibt noch andere Dinge zu beachten. Gehen wir zurück zu einem physikalischen Beispiel, um zu sehen, was ich meine. Wenn Sie einen Ihrer Dollarscheine zwischen zehn Täuschungen verstecken wollten, müssten Sie für jeden Dollar, den Sie ausgeben wollten, ungefähr elf Dollar in Ihrer Brieftasche tragen. Ein echter Dollar und zehn falsche. Das wird schon ziemlich umständlich, wenn man auch nur ein paar Euro ausgeben möchte. Stellen Sie sich nun vor, wir hätten den Täuschbetrag auf 1000 erhöht. Für jeden Dollar, den Sie ausgeben wollten, müssten Sie etwa 1001 Dollar mit sich führen. Sie müssten eine Aktentasche mit sich herumtragen, nur um einen Schokoriegel zu kaufen! Es ist wichtig anzumerken, dass Ringsignaturen nicht ganz so funktionieren, zum Beispiel sind die Täuschungen selbst kein Teil der Signatur, sondern nur Verweise darauf, aber wir hoffen, dass diese Analogie etwas hilfreich sein kann, um die grundlegenden Konzepte darzustellen. < /p>

Die Täuschungen auf der Blockchain funktionieren ähnlich. Jede hinzugefügte Täuschung erhöht die Zeit und die Überprüfungskosten der Transaktion. Jeder Knoten muss die gesamte Ringsignatur für jede Transaktion herunterladen, und jede Ringsignatur enthält den tatsächlichen Output sowie die Täuschungen. Nicht nur das, es muss auch die Mathematik verifizieren, dass mindestens einer dieser Outputs echt ist, und die mathematische Verifizierungszeit erhöht sich auch mit jeder Täuschung. Das bedeutet, dass wir einen Mittelweg finden müssen, bei dem die Ringgröße groß genug ist, um den tatsächlichen Output auch gegen viele heuristische Angriffe angemessen zu verschleiern, aber klein genug, um die Blockchain nicht massiv wachsen zu lassen. Es reicht nicht aus, eine beliebige Zahl auszuwählen oder einfach die Ringgröße zu erhöhen, wenn wir die Signatur verkleinern (wie bei CLSAG). Die Monero-Community möchte konkrete, mathematische Beweise dafür, welche Ringgröße die besten Kompromisse bietet. Eine Nummer zu klein, und die Privatsphäre ist nicht stark genug gegen heuristische Angriffe. Zu groß, und wir profitieren möglicherweise nur geringfügig von der Datenschutzseite und leiden unnötigerweise in Bezug auf die Skalierung.

Eine letzte Sache, die zu erwähnen ist. Einige Monero-Literatur vereinfacht und sagt, dass Ringsignaturen den Absender verbergen, aber das ist nicht ganz richtig, und der Unterschied ist nicht nur pedantisch. Der Unterschied zwischen dem Absender (einem Menschen) und einem Output (einem "Geldschein") ist groß, wenn es um die Wahrung der Privatsphäre geht. Während ein Output Verbindungen zu einem Absender haben kann, ist ein Output selbst nicht gleich einem Absender. Selbst wenn eine Ringsignatur gebrochen werden sollte, ist sie nicht unbedingt mit der Identität einer Person verknüpft, und sowohl der Betrag als auch der Empfänger sind immer noch verborgen, wodurch der Schaden für die Privatsphäre aller Parteien minimiert wird.

Das soll nicht heißen, dass eine defekte Ringsignatur unbedeutend ist. Alle durchgesickerten Metadaten sind schlecht und haben das Potenzial, mehr Informationen preiszugeben, als wir denken, insbesondere wenn sie in Verbindung mit anderen Metadaten verwendet werden. Daher tun wir unser Bestes, um sicherzustellen, dass die gewählte Ringgröße eine akademische Strenge hinter der Entscheidung hat, andere Metadatenlecks minimiert werden und die Benutzererfahrung standardmäßig auf die bestmöglichen Aktionen zurückgreift.

Aber wenn Sie die Wahrscheinlichkeit einer gebrochenen Signatur immer noch beunruhigt, nun, es gibt einige unglaubliche Neuigkeiten am Horizont. Die nächste Generation von Datenschutzprotokollen, an denen gearbeitet wird, wie Triptych, Arcturus und Lelantus, haben wirklich nette Fähigkeiten. In diesen Protokollen skaliert die Größe logarithmisch, nicht linear, wenn die Ringgröße zunimmt. Das bedeutet, dass wir 100 Täuschungen unterbringen können, aber der verwendete Platz ist näher an der Ringgröße 10 in der alten Technologie. Das ist ein ziemlicher Unterschied und wird den Datenschutz rundum erheblich verbessern.

Im Katz-und-Maus-Spiel des Datenschutzes führt Monero kontinuierlich Innovationen ein, um der Kurve immer einen Schritt voraus zu sein und den bestmöglichen Datenschutz für alle zu gewährleisten.

Die Täuschungen auf der Blockchain funktionieren ähnlich. Jede hinzugefügte Täuschung erhöht die Zeit und die Überprüfungskosten der Transaktion. Jeder Knoten muss die gesamte Ringsignatur für jede Transaktion herunterladen, und jede Ringsignatur enthält den tatsächlichen Output sowie die Täuschungen. Nicht nur das, es muss auch die Mathematik verifizieren, dass mindestens einer dieser Outputs echt ist, und die mathematische Verifizierungszeit erhöht sich auch mit jeder Täuschung. Das bedeutet, dass wir einen Mittelweg finden müssen, bei dem die Ringgröße groß genug ist, um den tatsächlichen Output auch gegen viele heuristische Angriffe angemessen zu verschleiern, aber klein genug, um die Blockchain nicht massiv wachsen zu lassen. Es reicht nicht aus, eine beliebige Zahl auszuwählen oder einfach die Ringgröße zu erhöhen, wenn wir die Signatur verkleinern (wie bei CLSAG). Die Monero-Community möchte konkrete, mathematische Beweise dafür, welche Ringgröße die besten Kompromisse bietet. Eine Nummer zu klein, und die Privatsphäre ist nicht stark genug gegen heuristische Angriffe. Zu groß, und wir profitieren möglicherweise nur geringfügig von der Datenschutzseite und leiden unnötigerweise in Bezug auf die Skalierung.

Eine letzte Sache, die zu erwähnen ist. Einige Monero-Literatur vereinfacht und sagt, dass Ringsignaturen den Absender verbergen, aber das ist nicht ganz richtig, und der Unterschied ist nicht nur pedantisch. Der Unterschied zwischen dem Absender (einem Menschen) und einem Output (einem "Geldschein") ist groß, wenn es um die Wahrung der Privatsphäre geht. Während ein Output Verbindungen zu einem Absender haben kann, ist ein Output selbst nicht gleich einem Absender. Selbst wenn eine Ringsignatur gebrochen werden sollte, ist sie nicht unbedingt mit der Identität einer Person verknüpft, und sowohl der Betrag als auch der Empfänger sind immer noch verborgen, wodurch der Schaden für die Privatsphäre aller Parteien minimiert wird.

Das soll nicht heißen, dass eine defekte Ringsignatur unbedeutend ist. Alle durchgesickerten Metadaten sind schlecht und haben das Potenzial, mehr Informationen preiszugeben, als wir denken, insbesondere wenn sie in Verbindung mit anderen Metadaten verwendet werden. Daher tun wir unser Bestes, um sicherzustellen, dass die gewählte Ringgröße eine akademische Strenge hinter der Entscheidung hat, andere Metadatenlecks minimiert werden und die Benutzererfahrung standardmäßig auf die bestmöglichen Aktionen zurückgreift.

Aber wenn Sie die Wahrscheinlichkeit einer gebrochenen Signatur immer noch beunruhigt, nun, es gibt einige unglaubliche Neuigkeiten am Horizont. Die nächste Generation von Datenschutzprotokollen, an denen gearbeitet wird, wie Triptych, Arcturus und Lelantus, haben wirklich nette Fähigkeiten. In diesen Protokollen skaliert die Größe logarithmisch, nicht linear, wenn die Ringgröße zunimmt. Das bedeutet, dass wir 100 Täuschungen unterbringen können, aber der verwendete Platz ist näher an der Ringgröße 10 in der alten Technologie. Das ist ein ziemlicher Unterschied und wird den Datenschutz rundum erheblich verbessern.

Im Katz-und-Maus-Spiel des Datenschutzes führt Monero kontinuierlich Innovationen ein, um der Kurve immer einen Schritt voraus zu sein und den bestmöglichen Datenschutz für alle zu gewährleisten.

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

  * [Wie Monero Stealth-Adressen Ihre Identität schützen](/knowledge/monero-stealth-addresses/)

  * [Wie Monero-Subadressen die Identitätsverknüpfung verhindern](/knowledge/monero-subaddresses/)

  * [Monero-Outputs erklärt](/knowledge/monero-outputs/)

  * [Monero Best Practices für Anfänger](/knowledge/monero-best-practices/)

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