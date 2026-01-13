---
title: "Monero Mining: Was RandomX so besonders macht"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Am 30. November 2019 hatte Monero seinen halbjährlichen Hard Fork, wobei die am meisten erwartete Änderung ein Wechsel vom alten PoW-Algorithmus Cryptonight zum völlig neuen, intern entwickelten RandomX war. Die Monero-Community glaubt, dass RandomX ein großer Schritt in Richtung egalitäres Mining ist, aber lassen Sie uns tiefer graben, um zu sehen, ob das auch wirklich der Fall ist.

## Zweck

Um beurteilen zu können, ob RandomX eine Verbesserung darstellt, müssen wir zunächst verstehen, was der Zweck des Mining ist. Mining sichert eine Blockchain vor doppelten Ausgaben über Nakamoto Consensus. Die genauen Details, wie dies geschieht, würden den Rahmen dieses Artikels sprengen, aber sie können aus vielen verschiedenen Quellen im Internet gelernt werden. Was zählt, ist, dass die Sicherheit aus Hashes stammt, die von Computern (Minern) generiert werden, die miteinander konkurrieren, um die mathematische Lösung zu finden, die zum Erstellen eines weiteren Blocks erforderlich ist. Dabei fügen sie der Blockchain neue Transaktionen hinzu. Als Gegenleistung für ihre Arbeit (Hashes) werden sie mit neu geprägten Coins entschädigt.   
  
Es gibt eine Reihe von Problemen, die bei diesem Setup auftreten können, und sie erfordern angemessene Anreize, um richtig zu funktionieren, aber wir werden uns auf ein bestimmtes Problem konzentrieren, das auftreten könnte. Wenn Mining ein Wettbewerb sein soll, was passiert, wenn ein Miner einen Vorteil erlangt?

## Hintergrund

Um den Zusammenhang zu verdeutlichen, sollten wir ein wenig über Mining-Hardware sprechen. Miner nutzen Computer, um die Arbeit zu erledigen, aber wir alle wissen, dass nicht jeder Computer gleich gut ist. Einige Computer sind leistungsfähig genug, um KI-Netzwerke oder anspruchsvolle Spiele zu betreiben, während andere selbst mit einfachen Aufgaben Probleme haben. Diese Unterschiede in der Rechenleistung wirken sich auch auf die Hash-Rate aus, also die Geschwindigkeit, mit der nach Blocklösungen gesucht wird.  
  
Aber selbst diese Unterschiede zwischen den Computern verblassen im Vergleich zu den Hash-Raten spezialisierter Hardware, auch bekannt als anwendungsspezifische integrierte Schaltkreise (ASICs), die normale Computer um mehrere Größenordnungen übertreffen.  
  
Nehmen wir uns etwas Zeit, um herauszufinden, was ASICs so leistungsfähig macht. Stellen Sie sich vor, dass alle Computer irgendwo auf einem Spektrum liegen, das von der Fähigkeit, viele Dinge zu tun, aber nichts gut, bis zur Fähigkeit, nur eine Sache zu tun, aber diese sehr gut, reicht. CPUs und ASICs befinden sich an den entgegengesetzten Enden dieses Spektrums.  
  
CPUs, die in allen Standardcomputern enthalten sind, liegen am ersten Ende. Sie können viele Dinge tun, z. B. im Internet surfen, Spiele spielen oder Videos rendern, aber nichts davon besonders gut. Diese Flexibilität geht jedoch auf Kosten der Effizienz.  
  
ASICs stehen am anderen Ende der Skala, wo sie nur eine einzige Aufgabe erfüllen können, dafür aber mit einer unglaublichen Geschwindigkeit. Sie können nur eine einzige mathematische Funktion ausführen, aber da sie alles andere ignorieren können, sind die Leistungsgewinne astronomisch. Diese Effizienz geht jedoch auf Kosten der Flexibilität, d. h. wenn sich die Funktion auch nur geringfügig ändert - z. B. x + y = z wird zu 2x + y = z - dann funktioniert der ASIC nicht mehr.  
  
Nicht jeder besitzt einen ASIC, aber jeder besitzt einen Computer. Dies kann zu einem unfairen Vorteil führen.

## Eine lustige Analogie

Wenn das immer noch verwirrend ist, hilft vielleicht die folgende Analogie. Stellen Sie sich eine Lotterie vor, bei der jede Stunde 1000 Dollar vergeben werden, und diese Lotterie ermöglicht es Ihnen, Ihre eigenen Lose auszudrucken! Sie beginnen damit, so viele Tickets wie möglich auf Ihrem Heimdrucker zu drucken, der ein Ticket pro Sekunde drucken kann. Nach Abzug der Strom- und Tintenkosten sehen Sie, dass Sie immer noch Gewinn machen können, selbst wenn Sie nur alle paar Wochen einmal im Lotto gewinnen.  
  
Im Laufe der Zeit erweitern Sie Ihren Betrieb, bis Sie einen ganzen Raum für Drucker haben. 20 insgesamt. Alles ist gut ... bis zu einem schicksalhaften Tag.   
  
Es gibt große Neuigkeiten. Jemand hat eine neue Art von Drucker erfunden. Er kann nur Lottoscheine drucken. Er kann keine Bilder, Office-Dokumente oder doppelseitig drucken. Nur Lottoscheine. Aber er kann sie mit einer Geschwindigkeit von 1000 Tickets pro Sekunde drucken. Sie schauen in Ihr kleines Druckerzimmer. 20 Drucker. Sie brauchen 980 weitere Drucker, nur um mit EINEM dieser Monsterdrucker Schritt zu halten, und wenn jemand zwei hat …?  
  
Sie steigen leider aus dem Lotteriespiel aus, da Sie die Strom- und Tintenkosten nicht mehr rechtfertigen können.  
  
Aber warten Sie! Ein paar Wochen später gibt es weitere Neuigkeiten! Das Design des Tickets hat sich geändert. Jetzt sind die Zahlen, die früher oben waren, jetzt unten. Die neuen Monsterdrucker sind so unflexibel, dass sie das nicht können. Sie konnten nur das vorherige Design herstellen. Es dauert nicht lange, bis Sie wieder glücklich drucken. Zumindest bis jemand einen neuen Monsterdrucker für das neue Design herstellt.

## RandomX

Wie passt RandomX in all das hinein? Es versucht, den Vorteil von ASICs auszugleichen, indem es die Herstellung von ASICs sehr schwierig macht. Dies geschieht, indem Miner aufgefordert werden, zufälligen Code zu erstellen und auszuführen, anstatt auf der Grundlage eines Algorithmus zu hashen.  
  
Es mag verwirrend sein, wie das tatsächlich hilft, also kehren wir zu unserer Druckeranalogie zurück. Erinnerst du dich, was passiert ist, als sich das Design geändert hat? Die alten Monsterdrucker werden jede Nacht obsolet, und neue mussten mit Blick auf das neue Design entwickelt werden. Was würde passieren, wenn jeder neue Lotteriegewinnschein für jeden neuen Jackpot einen neuen Designstandard einhalten müsste?   
  
Das Erstellen eines neuen Monsterdruckers würde unglaublich schwierig werden. Sie können nicht mehr nur mit einem Ticketdesign planen. Da das Design zufällig ist, müssten die Hersteller von Monsterdruckern Farbfunktionen, Möglichkeiten zum Drucken verschiedener Schriftzüge und Ränder und Formen und mehr hinzufügen. Kurz gesagt, die Maschine, die sie schließlich erfanden, wäre ein normaler Standarddrucker. Genau wie alle anderen auch.  
  
Indem wir diese Zufälligkeit einfach in das Ticketdesign implementiert haben, haben wir den großen Vorteil, der durch spezialisierte Hardware erzielt wird, erheblich reduziert. RandomX macht dasselbe, aber mit Mining.  
  
Auf diese Weise werden die Vorteile einiger weniger wohlhabender Personen minimiert, als würden sie in die Entwicklung von „ASICs“ für das Mining von RandomX investieren und tatsächlich nur stärkere, bessere CPUs erfinden, was der ganzen Welt zugute kommt.  
  
Damit ist der kleine Kerl mit seinen 20 Ticketdruckern wieder im Spiel. Er hat es vielleicht immer noch schwerer, da diese wohlhabenden Personen immer noch mehr Drucker kaufen können als er, aber zumindest ist er jetzt nicht nur von einer Maschine um Größenordnungen übertroffen. Er ist auf seine kleine Art konkurrenzfähig.  
  
Da wir wissen, dass selbst der kleine Kerl beim Monero-Mining wettbewerbsfähig sein kann, ermutigen wir jeden, es auszuprobieren, entweder in der Monero-GUI-Wallet, die Solo-Mining unterstützt, oder durch das Herunterladen von Community-unterstützter Software. Es ist einfach, wettbewerbsfähig und offen für alle.

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

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better)/