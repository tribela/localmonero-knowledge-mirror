---
title: "Monero-Outputs erklärt"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero verwendet wie andere Kryptowährungen Outputs als Mittel zur Abrechnung von Geldern. Viele Krypto-versierte Benutzer haben diesen Begriff wahrscheinlich schon einmal gehört, aber nicht jeder versteht, was sie bedeuten und wie sie funktionieren. Wie in unserem [Ringsignaturen-Artikel](/knowledge/ring-signatures) untersucht, sind Outputs die tatsächliche Einheit, die auf der Blockchain zwischen Transaktionsparteien ausgetauscht wird. Ähnlich wie ein Dollarschein, aber der Betrag hat keinen festen Nennwert.

Wenn Sie 16 Dollar für einen Job bekommen, erhalten Sie vielleicht einen Ein-Dollar-Schein, einen Fünf-Dollar-Schein und einen Zehn-Dollar-Schein. Sie haben 16 $, aber Sie haben auch drei verschiedene Scheine in Ihrer Brieftasche. Wenn Sie jemandem 6 Dollar zahlen wollten, könnten Sie den 5- und den 1-Schein verwenden, aber wenn Sie jemandem 8 Dollar zahlen wollten, könnten Sie nur die 10 Dollar verwenden und 2 Dollar als Wechselgeld zurückbekommen. Wenn Sie schließlich jemandem 14 Dollar zahlen wollten, müssten Sie alle drei Scheine verwenden und würden 2 Dollar als Wechselgeld zurückbekommen, aber wenn Sie alle drei Scheine übergeben, haben Sie für einen Moment kein Geld in Ihrer Brieftasche, bis Sie das Wechselgeld zurück bekommen.

Monero funktioniert ähnlich. Angenommen, Sie betreiben ein Geschäft und tätigen drei Verkäufe mit drei verschiedenen Artikeln. Sie erhalten möglicherweise 1,5 XMR, 2,25 XMR und 5,25 XMR für insgesamt 9 XMR, aber Sie haben auch drei verschiedene Outputs in Ihrer Brieftasche mit den zuvor genannten Nennwerten. Genau wie bei den Dollars möchten Sie vielleicht jemandem 3 XMR zahlen. Sie könnten nur die 5,25-XMR-Ausgabe verwenden und 2,25 XMR als Wechselgeld zurückerhalten, oder Sie könnten die 1,5- und 2,25-XMR-Ausgaben kombinieren und 0,75 XMR als Wechselgeld zurückerhalten.

Aber sobald Sie die Transaktion senden, werden die von Ihnen verwendeten Outputs in einen "gesperrten" Zustand versetzt, was bedeutet, dass sie unzugänglich sind, bis Sie das Wechselgeld zurückerhalten. Das Protokoll entsperrt das Geld (d. h. gibt Ihnen das Wechselgeld zurück) nach 10 Bestätigungen oder etwa 20 Minuten. So wie Sie das Geld nach der Übergabe der Dollarscheine aus Ihrer Brieftasche nicht erneut verwenden können, bis Sie das Wechselgeld von der Kasse zurückerhalten, ist Ihr Monero unzugänglich, bis Sie das Wechselgeld zurückerhalten.

Lassen Sie uns zu dem Beispiel zurückkehren, in dem 3 XMR an jemanden gesendet werden, und Sie verwenden die 5,25-XMR-Ausgabe. Jetzt, während Sie darauf warten, dass Sie 1,75 XMR als Wechselgeld zurückbekommen, können Sie es nicht verwenden. Dieses 1.75 XMR ist für Sie nicht zugänglich. Aber Sie können immer noch die 1,5 XMR- und 2,25 XMR-Ausgänge verwenden, da diese nicht ausgegeben wurden. Um auf das Dollar-Beispiel zurückzukommen: Wenn Sie jemandem 8 $ bezahlt haben, wie im vorherigen Beispiel, könnten Sie die 2 $, die Sie als Wechselgeld erwarten, nicht verwenden, bis Sie sie erhalten, aber in diesem Beispiel haben Sie immer noch einen unbenutzten 10-Dollar-Schein in Ihrer Brieftasche. Dies kann immer noch verwendet werden, um alles zu kaufen, was Sie wollen, während Sie auf das Wechselgeld warten. Dasselbe gilt für Monero.

Dies ist oft ein Punkt der Verwirrung für neue Monero-Benutzer. Oft hat ein Benutzer nur einen Output in seiner Wallet, die er von einer Börse oder einem Freund erhalten hat. Nehmen wir an, diese Ausgabe ist 20 XMR. Sie haben keine anderen Outputs in ihrer Brieftasche. Sie wollen jetzt eine Spende an zwei ihrer Lieblings-Wohltätigkeitsorganisationen machen. Sie senden 5 XMR an die erste Wohltätigkeitsorganisation und sind dann verwirrt, weil sie, obwohl sie 15 XMR übrig haben sollten, nicht sofort die nächste Spende an die zweite Wohltätigkeitsorganisation senden können. Wie Sie vielleicht erraten haben, liegt dies daran, dass die 15 XMR gesperrt sind. Es kann nicht ausgegeben werden, bis es als Wechselgeld zurückgegeben wird (10 Bestätigungen oder etwa 20 Minuten). Nachdem ihre Gelder freigeschaltet sind, können sie ihre zweite Spende senden.

Um den Punkt noch einmal zu wiederholen, sie hätten dieses Problem nicht gehabt, wenn sie stattdessen mehrere Ausgänge gehabt hätten, wie z. B. zwei 10 XMR-Outputs oder ähnliches. Sie könnten beide Spenden direkt nacheinander senden, da die erste Spende einen der 10 XMR-Ausgänge verwenden würde (und 10 Bestätigungen abwarten würde, um 5 XMR als Wechselgeld zurück zu erhalten), und die zweite Spende den anderen 10 XMR-Output verwenden würde.

Einige Kryptowährungs-Wallets haben eine Funktion namens „Output Management“, die einem Benutzer einfach anzeigt, welche Outputs er derzeit hat (zusätzlich zu seiner Gesamtsumme), und es ihm ermöglicht, auszuwählen, welche er verwenden möchte, wenn er seine Kryptowährung ausgibt.

Ab sofort führt die Monero-GUI die Output-Auswahl für Benutzer automatisch durch, da Benutzer, die ihre eigenen Outputs auswählen, oft zu Verwirrung oder in einigen Fällen zu Beeinträchtigungen der Privatsphäre führen. Es befinden sich jedoch Wallets im Aufbau, wie z. B. das neue Feather-Wallet-Projekt, das diese Output-Management-Funktionen enthalten wird.

Wir haben viel über den Sendeteil gesprochen, aber auf der Empfängerseite passiert etwas Faszinierendes. Um auf unser Beispiel zurückzukommen, in dem Sie 3 XMR an jemanden senden und Ihre 1,5 XMR- und 2,25 XMR-Outputs in der Transaktion verwenden (während Sie 0,75 XMR als Wechselgeld erwarten), erhält der Empfänger NICHT zwei Outputs von 1,5 XMR und 2,25 XMR. Sie erhalten stattdessen EINEN 3 XMR-Output.

Im Hintergrund kombiniert das Protokoll alle Outputs, die zum Ausgeben verwendet werden, und gibt dem Empfänger einen Output des bezahlten Betrags und sendet einen Wechselgeld-Output zurück an den Sender. Der Sender erhält also auch einen Output als Wechselgeld zurück, unabhängig davon, ob er zwei, drei oder zehn Outputs zum Senden der Transaktion verwendet hat.

Wir hoffen, dass dies einige Verwirrung über die Outputs und die Funktionsweise der internen Abrechnung des Protokolls sowie das allgemeine Problem der Verwirrung bei gesperrten Geldern beseitigt hat. In einem anderen Artikel werden wir uns mit der Verwaltung Ihrer Outputs befassen, um die Wahrscheinlichkeit zu minimieren, dass Sie auf freigeschaltete Gelder warten müssen, bevor Sie zukünftige Transaktionen senden.

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