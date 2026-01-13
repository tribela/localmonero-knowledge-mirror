---
title: "Wie sich Remote-Knoten auf die Privatsphäre von Monero auswirken"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Einer der größten Vorteile, die Monero gegenüber anderen Kryptowährungen hat, ist der Datenschutz auf der Chain, aber haben Sie sich jemals gefragt, wie sich die Privatsphäre von Monero hält, wenn Sie einen Remote-Knoten verwenden? Wie wäre es, wenn Sie einen „Light Wallet“-Server wie MyMonero verwenden?

In diesem Beitrag werden wir in einige der Details eintauchen, die dahinterstecken, wie Monero auch bei Verwendung eines Remote-Knotens außergewöhnliche On-Chain-Privatsphäre bietet und worauf Sie bei der Verwendung von Remote-Knoten achten müssen.

## Welche Funktion haben Nodes in Monero?

## Welche Funktion haben Nodes in Monero?

Für diejenigen, die mit der Funktionsweise von Monero nicht so vertraut sind: Die Knoten (oder Server) im Monero-Netzwerk können von jedem betrieben werden und ermöglichen es dem Eigentümer des Knotens - oder anderen, mit denen er ihn teilen möchte! - eine Kopie der Blockchain zu synchronisieren und diese Kopie anderen im Netzwerk zur Verfügung zu stellen. Diese Knoten überprüfen auch alle Transaktionen, die im Netzwerk stattfinden, sowie alle Blöcke, die veröffentlicht werden, und stellen sicher, dass sie alle den Regeln folgen, die durch den Konsens festgelegt wurden.

Die andere Funktion, die Knoten in Monero erfüllen, ist die Bereitstellung aller Daten, die Ihre bevorzugte Monero Wallet benötigt, um ordnungsgemäß nach Transaktionen zu suchen, die Ihnen gehören, und um neue Transaktionen durchzuführen. Diese Daten werden von Nodes auf zwei Arten bereitgestellt:

  * Die Daten von jedem Block auf der Blockchain werden von der Wallet angefordert, nach Transaktionen, die Ihnen gehören, gescannt und dann verworfen, sobald sie von der Wallet überprüft wurden. 
    * Dieser Schritt wird dank der [View-Tags](/knowledge/view-tags-reduce-monero-sync-time) bald drastisch verbessert werden.
  * Beim Versenden von Transaktionen stellt der Node, den Sie verwenden, eine Liste möglicher Decoys (oder gefälschter Eingaben) zur Verfügung, die bei der Erstellung der Transaktion zu verwenden sind, um sicherzustellen, dass Sie jedes Mal, wenn Sie Monero ausgeben, eine gute Menge haben, in der Sie sich verstecken können. 
    * Diese Decoys sind ein Teil der [Ringsignaturen](/knowledge/ring-signatures), ein wichtiger Teil von Moneros Ansatz zur Privatsphäre auf der Chain.

  * Dieser Schritt wird dank der [View-Tags](/knowledge/view-tags-reduce-monero-sync-time) bald drastisch verbessert werden.

  * Diese Decoys sind ein Teil der [Ringsignaturen](/knowledge/ring-signatures), ein wichtiger Teil von Moneros Ansatz zur Privatsphäre auf der Chain.

## Was ist die anonymste und sicherste Art, Monero zu verwenden?

## Was ist die anonymste und sicherste Art, Monero zu verwenden?

Trotz der starken On-Chain-Privatsphäre, die Monero bei der Verwendung von Remote-Knoten bietet, ist es am besten, einen eigenen Monero-Knoten zu betreiben, um sicherzustellen, dass Sie eine unverfälschte Kopie der Monero-Blockchain zur Verfügung haben und dass Ihre IP-Adresse gut geschützt ist. Ein weiterer Vorteil eines eigenen Knotens ist, dass Sie einen Beitrag zum Netzwerk leisten können, indem Sie andere Knoten von Ihrem Knoten aus synchronisieren oder sogar andere Nutzer mit ihren Wallets mit Ihrem Knoten verbinden lassen.

Trotzdem bietet Monero bei der Verwendung eines Remote-Knotens immer noch hervorragende Privatsphäre. Wenn Sie daran interessiert sind, Ihren eigenen Monero-Knoten zu betreiben, finden Sie hier eine leicht verständliche Anleitung dazu:

  * [Einen Monero-Knoten ausführen](https://sethforprivacy.com/guides/run-a-monero-node/)

## Was kann ein Remote-Knoten über mich erfahren?

## Was kann ein Remote-Knoten über mich erfahren?

Bei der Verwendung eines entfernten Knotens gibt es einige wichtige Informationen, die einem entfernten Knoten offengelegt werden, und einige wichtige Möglichkeiten, wie dieser Knoten Sie angreifen, Sie an der Durchführung von Transaktionen hindern kann und mehr.

Das erste, was ein entfernter Knotenpunkt über Sie erfahren kann, ist Ihre öffentliche IP-Adresse. Obwohl diese hoffentlich über ein VPN oder Tor verborgen ist, könnte der entfernte Knoten Ihre öffentliche IP-Adresse mit der Transaktion in Verbindung bringen, was ihm hilft, den Ort, von dem aus Sie die Transaktion durchführen, einzugrenzen. Der entfernte Knoten kann auch den letzten Block, den Ihre Wallet synchronisiert hat, in Erfahrung bringen und damit versuchen, Rückschlüsse auf Sie zu ziehen, z. B. wann Sie Monero normalerweise verwenden und wann Sie zuletzt Monero ausgegeben haben. Dies gilt insbesondere dann, wenn Sie immer von der gleichen IP-Adresse kommen (z.B. von zu Hause). Die letzte wichtige Sache, die ein entfernter Knoten über Sie erfahren kann, sind grundlegende Informationen über die Transaktionen, die Sie über ihn senden. Dies sind zwar die offensichtlichsten Daten, die der Betreiber des entfernten Knotens über Sie erhält, aber es ist wichtig zu verstehen, dass diese Informationen dazu verwendet werden können, den Absender der Transaktion ausfindig zu machen, wenn diese Informationen mit anderen Off-Chain-Daten kombiniert werden. Dies kann besonders gefährlich sein, wenn der Remote-Node von einer böswilligen Entität, einem Blockchain-Analyseunternehmen oder einem repressiven Nationalstaat betrieben wird.

Ein entfernter Knoten kann auch versuchen, Ihnen Probleme zu bereiten, indem er Blöcke vor Ihnen versteckt und Ihre Wallet glauben lässt, dass sie synchronisiert wurde, obwohl dies nicht der Fall ist. Dies kann dazu führen, dass Sie denken, Ihr Geld sei verloren gegangen, oder dass Sie kein Geld ausgeben können, bis Sie sich mit einem anderen Knoten verbinden. Der letzte wichtige Punkt, den ein entfernter Knoten tun könnte, ist, Ihre Wallet mit einer manipulierten Liste von Köderblöcken zu füttern. Dies kann dazu führen, dass Ihre Wallet entweder gar keine Transaktionen mehr durchführen kann (so dass Sie kein Geld mehr ausgeben können), oder dass der entfernte Knoten versucht, Decoys bereitzustellen, von denen er weiß, dass sie ausgegeben wurden, um die Anonymität zu verringern, die Sie bei jeder Transaktion erhalten.

## Welche Datenschutzgarantien gibt es noch bei der Verwendung eines Remote-Knotens?

## Welche Datenschutzgarantien gibt es noch bei der Verwendung eines Remote-Knotens?

Auch wenn dieser Artikel Sie vielleicht ein wenig erschreckt hat, ist es wichtig zu wissen, dass die von Monero gebotene Privatsphäre auch bei der Verwendung eines entfernten Knotens ausgezeichnet ist und jede andere Kryptowährung bei dieser Verwendung weit übertrifft. Sie profitieren immer noch von der starken On-Chain-Privatsphäre, die Monero bietet, da der Remote-Node niemals den wahren Input (welche Coins Sie ausgeben), die Menge der in der Transaktion ausgegebenen Monero oder die Adresse des Empfängers der Transaktion kennt. Außenstehende Beobachter können auch nicht die wahre Eingabe, den Betrag oder die beteiligten Adressen sehen (unabhängig davon, welche Art von Knoten Sie verwenden!), wodurch sichergestellt wird, dass außerhalb des entfernten Knotens sogar Ihre IP-Adresse, Wallet-Synchronisierungsinformationen und Transaktionen starke Datenschutzgarantien haben.

Der entfernte Knoten hat auch niemals Zugriff auf die vorherigen Transaktionen, die Sie gesendet oder erhalten haben, oder auf die Menge an Monero, die sich derzeit in Ihrer Wallet befindet, und verliert jeden Einblick in Ihre Transaktionen, sobald Sie beginnen, einen anderen Knoten zu verwenden. Es werden keine privaten Schlüssel (weder Ausgaben- noch Einsichtsschlüssel) an den entfernten Knoten weitergegeben, so dass Ihre Wallet privat, sicher und benutzbar bleibt. Unabhängig vom entfernten Knotenpunkt sind Sie auch nie dem Risiko ausgesetzt, Monero zu verlieren oder gestohlen zu werden, da der Knotenpunkt die Empfängeradresse nicht bearbeiten kann, keinen Zugriff auf die privaten Schlüssel Ihrer Wallet hat und Ihre Monero in keiner Weise beschlagnahmen kann.

## Was hat es mit „Light Wallets“ wie MyMonero auf sich?

## Was hat es mit „Light Wallets“ wie MyMonero auf sich?

Das Thema liegt zwar etwas außerhalb des Rahmens dieses Artikels, aber ich wollte eine einzigartige Art von Wallet in Monero ansprechen - Light Wallets. Der Name Light-Wallet kommt daher, dass Ihre Wallet (auf Ihrem Telefon oder Computer) keine Blockchain-Synchronisation durchführen muss, was die Erfahrung schneller und flüssiger macht.

Solche Wallets haben jedoch einen großen Nachteil in Bezug auf die Privatsphäre: Ihre Wallet sendet den privaten View Key an den von Ihnen verwendeten Remote Server (wie die Standardeinstellung in MyMonero), wodurch der Remote Server vollen Einblick in alle erhaltenen Gelder seit der Erstellung Ihrer Wallet erhält (und bis Sie die Wallet oder Seed nicht mehr verwenden). Dies reduziert die Privatsphäre, die Sie vom Node-Betreiber erhalten, drastisch und sollte mit Vorsicht genossen werden.

Glücklicherweise arbeitet die Monero-Gemeinschaft an der Verbesserung der Software, mit der Sie Ihren eigenen Light-Wallet-Server (LWS) hosten können, der Ihnen eine schnelle Synchronisation ermöglicht, ohne dass Sie Ihre privaten View-Keys einem Drittanbieter anvertrauen müssen - da Sie die Software ausführen, mit der Ihre Wallet die privaten View-Keys sendet!

Weitere Informationen über den Light Wallet Server finden Sie im folgenden Github Repository:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Wie kann ich mehr erfahren?

## Wie kann ich mehr erfahren?

Wenn Sie neugierig sind und Knoten in Monero besser verstehen und sich mit der Verwendung eines Remote-Knotens oder dem Betrieb Ihres eigenen befassen möchten, finden Sie unter den folgenden Links großartige Einstiegsmöglichkeiten:

  * [Monero World, eine Liste der von der Gemeinschaft betriebenen Remote Nodes, die verwendet werden können](https://moneroworld.com/#nodes)
  * [Monero-Knoten, betrieben von Seth For Privacy, dem Autor dieses Artikels](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, eine Liste von Remote-Knoten mit häufig überprüftem Status< /a>](https://monero.fail/)
  * [Verbindung herstellen zu einem Remote-Knoten innerhalb der GUI-Brieftasche](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia – Remote Knoten](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Weiterlesen

  * [Wie Monero auf einzigartige Weise Kreislaufwirtschaften ermöglicht](/knowledge/monero-circular-economies)/

  * [Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Warum (und wie!) Sie Ihre eigenen Keys halten sollten](/knowledge/hold-your-keys)/

  * [Zu Monero beitragen](/knowledge/contributing-to-monero)/

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

  * [Monero Mining: Was RandomX so besonders macht](/knowledge/monero-mining-randomx)/

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better)/

Weiterlesen