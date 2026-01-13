---
title: "Wie Atomic Swaps in Monero funktionieren"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Im Streben nach Dezentralisierung und einem wirklich erlaubnisfreien System sind nur wenige Dinge im Bereich der Kryptowährungen so begehrt wie dezentralisierte Börsen und Atomic Swaps. Seit seiner Gründung hat Monero damit gekämpft, Atomic Swaps zu implementieren, da die Datenschutzfunktionen einzigartige Probleme beim Versuch, ein Protokoll zu entwerfen, verursachen.

Aber lassen Sie uns zunächst einen Schritt zurückgehen. Was sind Atomic Swaps? Ein Atomic Swap ist ein Protokoll, mit dem zwei verschiedene Kryptowährungen auf verschiedenen Blockchains auf vertrauenslose Weise und ohne Vermittler ausgetauscht werden können. Das bedeutet, wenn jemand die Kryptowährung A gegen die Kryptowährung B tauschen möchte, kann er dies ohne eine zentrale oder dezentrale Börse tun. Wie man sich vorstellen kann, erfordert dies beträchtliche Forschung, und die technischen Details, die dies möglich machen, sind ziemlich kompliziert. LocalMonero ist wieder einmal hier, um zu helfen und eine einfache Erklärung für den Normalbürger zu geben.

Betrachten wir zunächst die einfachste Form des Atomic Swaps, wie sie von Bitcoin umgesetzt wird. Wenn jemand Bitcoin gegen einen anderen Coin tauschen möchte, der dieselbe Hash-Time-Lock-Contract-Technologie verwendet, kann er dies auf folgende Weise tun. Alice hat Bitcoin (BTC), möchte aber Litecoin (LTC), und Bob hat LTC, möchte aber BTC. Sie beschließen, einen Atomic Swap durchzuführen, damit jeder den Coin bekommt, den er haben möchte. Alice schickt ihre BTC an eine spezielle Adresse, wobei sie Skripte verwendet, die das Geld sperren, so dass nicht einmal sie darauf zugreifen kann. Man kann sich das so vorstellen, dass Alice ihre BTC in ein Schließfach legt. Wenn das Schließfach hergestellt ist, erhält sie einen Schlüssel und sendet einen Hash dieses Schlüssels an Bob. Nun hat Bob nicht den Schlüssel selbst, sondern nur den Hash, so dass er noch keinen Zugriff auf das Geld hat.

Bob verwendet diesen Hash als Seed, aus dem er seine eigene Lockbox generiert, und schickt seinen LTC dorthin, wo er ebenfalls gesperrt wird. Da der Hash von Alices Schlüssel als Seed verwendet wurde, mit dem Bobs Schließfach erstellt wurde, kann sie mit ihrem Schlüssel den LTC in Bobs Schließfach beanspruchen. Ihr Schlüssel passt! Aber wenn sie ihren Schlüssel benutzt, um das LTC-Schloss zu öffnen, verrät sie ihn an Bob, der ihn dann benutzen kann, um die BTC einzufordern, die sie in ihr Schließfach gelegt hat. Auf diese Weise haben Alice und Bob ohne Zwischenhändler erfolgreich ihre Vermögenswerte ausgetauscht.

Aber es gibt ein kleines Problem. Was passiert, wenn Alice an ihr Schließfach sendet und Bob beschließt, nicht mehr zu traden. Da Alice nun nicht mehr auf ihre BTC zugreifen kann, die sie weggesperrt hat, und Bob seinen Teil der Transaktion nicht abschließen wird, verliert Alice ihr Geld für immer. Glücklicherweise verfügt Bitcoin über eine kleine Technologie namens Rückerstattungstransaktionen, so dass die Skripte nach einer gewissen Zeit, wenn die BTC nicht von Bob eingefordert werden, eine Ausfallsicherung eingebaut haben, bei der die BTC automatisch an Alice zurückgehen. Dies war die Hauptschwierigkeit für Moneros Atomic Swaps. Aufgrund von Moneros [Ring-Signaturen Datenschutz-Technologie](/knowledge/ring-signatures) ist der Absender einer Transaktion immer ungewiss. Wie kann das Protokoll eine Rückzahlungstransaktion durchführen, wenn es selbst nicht weiß, woher die Transaktion kam?

Im Jahr 2017 skizzierte eine kleine Gruppe von Forschern eine andere Methode, mit der Atomic Swaps in Monero funktionieren würden. Nach mehreren Jahren der Verfeinerung stellten die Forscher einen Prozess fertig, mit dem Monero in der Lage wäre, Atomic Swaps mit Bitcoin durchzuführen, auch ohne Rückzahlungstransaktionen.

Wie bei vielen Dingen dieser technischen Komplexität wird unsere Erklärung einige Dinge übermäßig vereinfachen, um die Idee zu vermitteln, aber sie wird dennoch eine solide Vorstellung von den Mechanismen vermitteln, mit denen dieser Prozess funktionieren würde.

Sowohl Alice (die XMR hat und BTC will) als auch Bob (der BTC hat und XMR will) müssen ein Programm herunterladen und ausführen, das den Atomic Swap unterstützt. Dies kann in Wallets, dezentralen Börsen oder speziellen Programmen implementiert sein, aber die Software muss das Atomic Swap-Protokoll ausführen. Im ersten Schritt stellen die Clients von Alice und Bob eine Verbindung zueinander her und erstellen mehrere gemeinsame Geheimnisse und Schlüssel. In diesem Schritt wird eine neue Monero-Adresse erstellt, wobei Alice die eine Hälfte des Schlüssels besitzt und Bob die andere. Allerdings sind dort noch keine Monero drin, es gibt also nichts auszugeben. Eine letzte Anmerkung zu dieser Adresse ist, dass beide den Schlüssel zu dieser Wallet haben, so dass sie beide hineinschauen können, um zu sehen, ob oder wann Monero ankommt.

Im zweiten Schritt schickt Bob seine BTC an eine spezielle Adresse, ähnlich dem Bitcoin Atomic Swaps Protokoll, das wir bereits besprochen haben. Nachdem Alice gesehen hat, dass die BTC an dieser Adresse auf der Blockchain angekommen sind, schickt sie ihre Monero an die Monero-Adresse, für die sie und Bob jeweils eine Hälfte eines Schlüssels besitzen. Bob kann verifizieren, dass die Monero angekommen sind, da er auch den View Key besitzt, und sobald er sieht, dass die Monero sicher in der Wallet sind, schickt er Alice einen Teil des Schlüssels, mit dem sie die Bitcoin abheben kann. Ähnlich wie bei dem anderen Protokoll gibt Alice bei der Abhebung der Bitcoin ihre Hälfte des Monero-Schlüssels an Bob weiter. Jetzt hat Bob beide Hälften, so dass er die Monero einfordern kann, während Alice nur ihre Hälfte hat, so dass sie nicht versuchen kann, sie zu nehmen, bevor er es tut.

Wenn Sie sich das alles angeschaut haben und immer noch ein wenig verwirrt sind, wie Monero das Problem der Rückerstattungstransaktionen umgehen konnte, ist die Antwort ganz einfach. Da Monero selbst keine Rückerstattungstransaktionen hat, sollte der Leser bemerken, dass der Bitcoin (der Rückerstattungstransaktionen hat) zuerst gesendet wird, und erst nachdem er als in der Blockchain verifiziert wurde, wird der Monero gesendet. Auf diese Weise kann Monero die Fähigkeit von Bitcoin nutzen, Rückerstattungstransaktionen zu skripten und sich diese zunutze zu machen, ohne selbst über diese Fähigkeiten verfügen zu müssen.

Der Atomic Swap ist nun abgeschlossen, aber von hier an hat Bob mehrere Möglichkeiten für seine neu erworbenen XMR: Er kann diese Monero Wallet so verwenden, wie sie ist, oder die XMR in eine andere Wallet verschieben, die er bereits besitzt. Bob wird höchstwahrscheinlich die Monero in eine andere Wallet verschieben, da Alice immer noch den View Key hat und hineinsehen kann.

Das Schöne an diesem Protokoll ist, dass es noch recht neu ist und es noch viel Raum für Optimierungen gibt. Es ist auch recht flexibel in seiner Architektur, so dass die Implementierung in anderen Wallets oder dezentralen Börsen einfach sein sollte und sich sauber in deren bestehende Architektur einfügt.

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