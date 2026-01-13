---
title: "Wie CLSAG die Effizienz von Monero verbessern wird"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Als Protokoll befindet sich Monero derzeit in einem ständigen Stadium der Innovation. Die Monero-Gemeinschaft forscht sowohl an On-Chain- als auch an Off-Chain-Lösungen und sucht nach Bereichen, die verbessert werden können, um Monero privater, skalierbarer und für alle zugänglicher zu machen. Eine der jüngsten Innovationen ist der Ersatz des verlinkbaren Ringsignaturschemas, MLSAG, durch ein Drop-in-Ersatzverfahren CLSAG, das für Concise Linkable Spontaneous Anonymous Group steht.

Oberflächlich betrachtet wird die Implementierung von CLSAG die häufigsten Transaktionen mit 2 Eingängen und 2 Ausgängen um 25 % reduzieren. Außerdem wird die Verifizierungszeit um 10 % verkürzt.

Aber was genau ist CLSAG? Was bewirkt es, und wie unterscheidet es sich von der alten Version MLSAG? Nehmen wir uns eine Minute Zeit, um uns an das Warum und Wie von Ringsignaturen zu erinnern, damit wir dieses Konzept besser verstehen können. Ringsignaturen ermöglichen nicht-interaktive, von Zeugen nicht unterscheidbare Eingaben durch die Verwendung von vom Unterzeichner ausgewählten Anonymitätssätzen früherer Ausgaben. Für den Laien bedeutet dies, dass ein Benutzer seine in einer Transaktion verwendeten Ausgaben zusammen mit nicht verwandten Ausgaben verbergen kann, und zwar ohne dass jemand anderes daran teilnehmen muss. Alles, was man braucht, ist eine Kopie der Blockchain. Jeder dieser Outputs scheint mit gleicher Wahrscheinlichkeit der tatsächliche zu sein, der gesendet wird, wodurch Metadaten über den Absender verborgen werden.

Daraus ergibt sich jedoch ein kleines Problem. Was wäre, wenn ein Benutzer eine Ringsignatur mit allen Täuschungsausgängen konstruieren würde? Woher würde jemand wissen, dass der unbekannte Absender nicht befugt ist, eine dieser Nachrichten zu versenden? Wäre dieser Benutzer in der Lage, gefälschtes Geld auszugeben? Die Antwort ist nein. Die Ringsignatur enthält eine Methode, um zu beweisen, dass mindestens einer der Ausgänge dem unbekannten Absender gehört, ohne zu verraten, welcher es ist. In der Tat sind sowohl CLSAG als auch MLSAG (im Folgenden als SAGs bezeichnet) der Teil der Ringsignatur, der dies beweist. Interessanterweise beweist sie gleichzeitig, dass der Betrag der Transaktion, obwohl er hinter vertraulichen Transaktionen (RingCT) verborgen ist, ausgeglichen ist. Dass die SAGs zwei Dinge beweisen, nämlich dass eine Ausgabe jemandem im Ring gehört und dass die Transaktion ausgeglichen ist, ist wichtig und liegt in der Tat an den Einsparungen bei Größe und Überprüfung. Wenn dies verwirrend ist, keine Sorge, wir werden bald zu einer lustigen und leicht verständlichen Analogie kommen.

Das alte Signaturschema MLSAG (Multilayered Linkable Spontaneous Anonymous Group) beweist die beiden oben genannten Dinge in einer Ringsignatur, aber es macht jedes separat. Die Verwendung von separaten Berechnungen für die Unterschrift und den Commitment-Schlüssel bedeutet langsamere Operationen. Ein moderner Computer kann diese Berechnungen in wenigen Millisekunden durchführen, was nicht viel zu sein scheint, und für eine Transaktion ist es das auch nicht. Wenn wir jedoch die schiere Anzahl der Transaktionen auf der Monero-Blockchain berücksichtigen und bedenken, dass ein Knoten, der von Grund auf neu synchronisiert wird, jede einzelne von ihnen herunterladen und verifizieren muss, beginnen sich die Bytes und Millisekunden schnell zu stapeln.

CLSAG kombiniert die Mathematik, die notwendig ist, um beides zu beweisen, und berechnet beides auf einmal, und zwar auf sichere Weise. Was heißt hier sicher? Nun, um das zu klären und dem Ganzen hoffentlich mehr Sinn zu geben, lassen Sie uns die versprochene lustige Analogie untersuchen.

Nehmen wir an, Sie müssen sowohl in den Lebensmittelladen als auch in den Baumarkt gehen, um zwei verschiedene Dinge zu besorgen: Lebensmittel und giftige Reinigungschemikalien. Sie wollen nicht, dass sich die beiden Dinge vermischen, denn wenn es zu einem Unfall kommt, werden die Chemikalien auf die Lebensmittel verschüttet und diese ungenießbar. Du beschließt, auf Nummer sicher zu gehen, und fährst von deinem Haus zum Lebensmittelgeschäft, kaufst die Lebensmittel und fährst dann zurück zu deinem Haus. Erst nachdem du die Lebensmittel abgeladen hast, steigst du wieder ins Auto, fährst zum Baumarkt und mit den Chemikalien zurück zu deinem Haus. Sie haben zwei getrennte Fahrten unternommen, um die Sicherheit aller Einkäufe zu gewährleisten. Das ist zwar sicher, aber ineffizient. Es handelt sich um MLSAG, bei dem zwei verschiedene mathematische Sätze gespeichert und zwei verschiedene "Fahrten" unternommen werden, um sie zu berechnen.

Sie entscheiden sich jedoch für einen schnelleren Weg, dies zu tun. Das ist zu viel verschwendete Zeit. Sicher, ein- oder zweimal zu rechnen, wird Ihnen nicht das Leben rauben, aber wenn Sie das immer wieder tun müssen, summieren sich die Stunden. Man beginnt sich zu fragen, ob man nicht stattdessen eine Fahrt machen kann. Von Ihrem Haus zum Lebensmittelladen, zum Baumarkt und wieder nach Hause. Du kannst nicht einfach losfahren und alles wahllos in dein Auto werfen. Das ist nicht sicher. Stattdessen kennzeichnen Sie verschiedene Plätze in Ihrem Auto für verschiedene Dinge und sorgen dafür, dass alles ordentlich an seinen Platz passt. Auf diese Weise können Sie beide Läden auf einmal anfahren und die Dinge voneinander fernhalten. Das ist CLSAG. In dieser Transaktion ist nur noch ein Satz Mathematik gespeichert, um diese beiden Dinge zu beweisen, und zwar so, dass sie sich nicht gegenseitig behindern. Eine Reise muss immer noch gemacht werden, aber Sie haben die Anzahl der Reisen drastisch reduziert.

Das klingt alles sehr spannend. Ist es möglich, dass wir andere Abkürzungen oder andere Wege finden, um Zeit und Platz zu sparen? Die Antwort lautet ja und nein. Nach Ansicht der MRL-Forscher ist es wahrscheinlich nicht möglich, die SAG-Konstruktionen weiter zu modifizieren, um die Größe oder die Geschwindigkeit zu verbessern. Andere Konstruktionen wie Arcturus, Omniring, RCT3 oder Triptych bieten jedoch eine viel bessere Größenskalierung und Verifikationsvorteile, indem sie andere mathematische Methoden verwenden. Jeder dieser "Next-Gen"-Ansätze für eindeutige Protokolle bringt jedoch seine eigenen Kompromisse bei den Implementierungsdetails mit sich und wird derzeit aktiv erforscht und untersucht.

Schließlich ist Monero immer innovativ.

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

  * [Warum Monero eine Tail-Emission hat](/knowledge/monero-tail-emission/)

  * [Eine kurze Geschichte von Monero](/knowledge/monero-history/)

  * [Das Wired Magazine hat Unrecht mit Monero, hier ist der Grund](/knowledge/wired-article-debunked/)

  * [Die 15 wichtigsten Monero-Mythen und -Bedenken widerlegt](/knowledge/monero-myths-debunked/)

  * [Wie Dandelion++ die Transaktionsursprünge von Monero geheim hält](/knowledge/monero-dandelion/)

  * [Warum Monero Open Source und dezentralisiert ist](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: Was RandomX so besonders macht](/knowledge/monero-mining-randomx/)

  * [Warum Monero besser ist als Dash, Zcash, Zcoin (sogar mit Lelantus), Grin und Bitcoin-Mixer wie Wasabi (Aktualisiert Mai 2020)](/knowledge/why-monero-is-better/)