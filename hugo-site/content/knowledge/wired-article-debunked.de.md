---
title: "Das Wired Magazine hat Unrecht mit Monero, hier ist der Grund"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sowohl im Datenschutz- als auch im Kryptowährungsbereich sind Fehlinformationen oft weit verbreitet. Wir haben [einen Artikel, der fünfzehn häufig falsche oder veraltete Annahmen über Monero skizziert](/knowledge/monero-myths-debunked), aber wir möchten uns die Zeit nehmen, einen bestimmten Artikel anzusprechen, der oft von Monero-Skeptikern zitiert und verbreitet wird.

Die Wired-Publikation veröffentlichte [einen Artikel](https://www.wired.com/story/monero-privacy/) am 27. März 2018, der seinerseits als Antwort auf ein anderes druckfrisches Paper geschrieben wurde, das von verschiedenen Wissenschaftlern mit dem Titel „Eine empirische Analyse der Rückverfolgbarkeit in der Monero Blockchain“.

Obwohl das Papier von Personen mit klarem Interessenkonflikt mitverfasst wurde (sprich: sie sind Berater von Zcash und haben eine Beteiligung an Zcash), wurde das Papier von der Monero-Community mäßig gut aufgenommen, da es Dinge bestätigt, die der Community bereits bekannt sind und darüber in ihren eigenen Monero Research Lab-Papieren ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) und [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) geschrieben, von denen das früheste vier Jahre zuvor veröffentlicht wurde. Es gab jedoch auch einige Frustrationen, vor allem der Interessenkonflikt, die Tatsache, dass die Probleme bereits bekannt waren, diskutiert und – in einigen Fällen – behoben wurden, und die grobe Fehlcharakterisierung der damaligen Datenschutzgarantien von Monero. Die Community hat den Preprint der Arbeit kommentiert, und viele ihrer Empfehlungen haben es bis zum endgültigen Paper geschafft.

Aber was genau wurde falsch charakterisiert? Die Tatsache, dass Monero die in dem Paper diskutierten Mängel seit über einem Jahr nicht mehr hatte. Transaktionen vor 2017 waren in der Tat anfällig für eine Form von Datenschutzlecks, aber zum Zeitpunkt der Veröffentlichung hatte Monero die meisten Bedenken ausgeräumt. Um den Autoren gegenüber fair zu sein, diskutieren sie die Abhilfemaßnahmen von Monero in geringem Maße, aber nicht genug, um die Auswirkungen zu beeinflussen, die sie auf den Medienzyklus der Kryptowährung zu dieser Zeit hatten. Daher der Wired-Artikel.

Obwohl wir den fraglichen Wired-Artikel als historischen Artikel untersuchen können und wie wahr oder unwahr er damals war, lädt die Tatsache, dass er noch heute als Begründung dafür geteilt wird, warum Moneros Datenschutzgarantien schwach sind, tatsächlich zu einer Analyse ein wie sich das Stück in der Gegenwart behauptet. Diese Einladung nehmen wir gerne an.

Ein schnelles Lesen des Artikels zeigt mehrere sensationelle Zeilen, wie „[Die Ergebnisse] sollten nicht nur jeden beunruhigen, der versucht, Monero heute heimlich auszugeben“ und der gesamte Ton des Artikels, der die Forschung als „neu“ postuliert, basiert weitgehend auf der Veröffentlichung. Das wissenschaftliche Paper selbst enthält Empfehlungen wie die Warnung von Monero-Benutzern vor der möglichen Gefährdung ihrer Anonymität, obwohl diese Diskussionen nicht nur seit 2014 geführt wurden, sondern der Schlachtruf der Community darin bestand, dass die Menschen Monero nicht kaufen sollten und es noch sehr experimentell war.

Aber was ist mit der Kritik selbst? Die Realität ist, dass viele Probleme mit Monero als Privacy Coin entweder nicht mehr auf Monero zutreffen oder gemeinsame Bedenken mit Privacy Coins als einer Kategorie Blockchain-basierter Kryptowährungen haben. Beginnen wir damit, diese anzusprechen.

Einer der am häufigsten zitierten Kritikpunkte an Monero ist, dass aufgrund der Permanenz und Unveränderlichkeit der Blockchain alle vergangenen Transaktionen von Monero offengelegt würden, wenn eine zukünftige Technologie die Privatsphäre durchbrechen würde. Mit anderen Worten, Ihre Privatsphäre hat eine tickende Uhr.

Wir können das nicht genug betonen. Buchstäblich jeder Privacy-Coin, die On-Chain-Methoden zur Verschleierung und Privatsphäre einsetzt, hat diesen Fehler, und dennoch wird sie oft gegen Monero verwendet (ironischerweise oft von konkurrierenden Privacy-Coins mit demselben Problem) und wird auch in diesem Artikel verwendet. Die Reaktion auf diese Kritik mag für einige überraschend sein, aber Monero ist möglicherweise weniger anfällig als andere Privacy-Coins, da es einen mehrgleisigen Ansatz zum Datenschutz verfolgt.

Monero verbirgt Outputs (Absender), Beträge und Empfänger durch drei verschiedene Technologien, Ringsignaturen, RingCT bzw. Stealth-Adressen. Von diesen sind Ringsignaturen die schwächsten und am anfälligsten sowohl für moderne Heuristiken als auch für theoretische, zukünftige, die Privatsphäre verletzende Technologien. Dies ist der Monero-Community seit Jahren bekannt, und es wird aktiv daran geforscht, das Ringsignaturschema zu verbessern oder vollständig zu ersetzen.

Aber selbst wenn die Ringsignatur vollständig gebrochen wäre, würde nur der wahre Output enthüllt werden. NICHT der Absender (wie im Einzelnen), sondern der Output. Ein Output mit einer Identität zu koppeln ist nicht unmöglich, würde aber mehr Metadaten und Ressourcen erfordern. In Verbindung mit der Tatsache, dass RingCT und die Stealth-Adresse NICHT preisgegeben würden, wird die Wirkung noch weiter verringert.

Es sollte beachtet werden, dass der Wired-Artikel die obigen Informationen in dem Teil, in dem sie Riccardo 'fluffypony' Spagni um einen Kommentar baten, kurz diskutierten, aber die dafür gegebene Zeit ist zu kurz und sie scheinen die entscheidenden Informationen fast wegzuwinken. Der Mangel an Verständnis wird besonders deutlich, wenn man versucht, diese Dinge mit Leuten zu diskutieren, die den Artikel in der heutigen Zeit wohl oder übel teilen.

Eine andere Kritik, die viel schwieriger zu behandeln ist, betrifft die Sichtweise der Außenwelt auf Monero und wie dies damit zusammenhängt, wie die Community um Monero den Coin sieht. Als Beispiel hierfür müssen die Leser nicht weiter als bis zum Titel des Artikels selbst suchen: „The Dark Web’s Favorite Currency Is Less Untraceable Than It Seems“.

Jede Person, die viel Zeit in der Monero-Community verbringt, kann bezeugen, dass die Monero-Community große Anstrengungen unternimmt, um zu zeigen, wie schwer echte Privatsphäre zu erreichen ist, selbst auf Kosten von Marketing- oder Adoptionsbemühungen. Wenn die Community reichlich Ressourcen bereitstellt, um den Coin und dessen Mängel genau zu diskutieren, wird die Unwissenheit irgendwann zum Fehler des Benutzers, der glaubt, dass der Coin alles ist, was er braucht, um 100 % anonym zu sein.

An diesem Punkt sollte offensichtlich sein, dass die Monero-Community sowohl ihre Privatsphäre als auch ihre Ehrlichkeit bezüglich der darin enthaltenen Schwächen und nachfolgenden Verbesserungen ernst nimmt. Artikel, wie der fragliche, verfehlen diesen Innovationsgeist von Monero völlig. Es vergleicht Monero mit den Scharen anderer Kryptowährungen, die grandiose Behauptungen aufstellen, nur an Profit denken und ungebildete Möchtegern-Investoren ausbeuten.

Die Realität könnte unterschiedlicher nicht sein. Monero ist sich seiner Schwächen sehr bewusst, versucht weiter zu bauen, um sie zu verbessern, lockere Verbindungen zu straffen und das sehr reale, aber sehr harte Ziel zu erreichen, der Welt eine private, fungible Kryptowährung zu geben, die von allen genutzt werden kann, und tun dies alles auf eine faire, dezentralisierte und gemeinschaftsgesteuerte Weise. Vielleicht ist es an der Zeit, die Sensation und das Teilen von Artikeln beiseite zu lassen, um "Bags zu shillen" und Konkurrenten zu fördern. Vielleicht ist es an der Zeit, eine andere Geschichte zu erzählen.

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

  * [Wie Ringsignaturen die Ausgaben von Monero verschleiern](/knowledge/ring-signatures/)

  * [Wie Monero das Blockgrößenproblem löste, das Bitcoin plagt](/knowledge/dynamic-block-size/)

  * [Wie CLSAG die Effizienz von Monero verbessern wird](/knowledge/what-is-clsag/)

  * [Warum Monero eine Tail-Emission hat](/knowledge/monero-tail-emission/)

  * [Eine kurze Geschichte von Monero](/knowledge/monero-history/)

  * [Die 15 wichtigsten Monero-Mythen und -Bedenken widerlegt](/knowledge/monero-myths-debunked/)

  * [Wie Dandelion++ die Transaktionsursprünge von Monero geheim hält](/knowledge/monero-dandelion/)

  * [Warum Monero Open Source und dezentralisiert ist](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Was RandomX so besonders macht](/knowledge/monero-mining-randomx/)

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better/)