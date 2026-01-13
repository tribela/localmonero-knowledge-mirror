---
title: "Moneros Ringsignaturen vs. CoinJoin wie bei Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
In dem Maße, in dem die Bitcoin-Datenschutz-Tools an Aufmerksamkeit und Nutzung gewonnen haben, sind sie auch stärker ins Visier der Behörden geraten. Diese Prüfung hat zu einer [kürzlichen Ankündigung](https://twitter.com/wasabiwallet/status/1503091503207432193) eines Bitcoin-Privatsphäre-Tools, Wasabi Wallet, geführt, dass sie beginnen werden, eingehende Eingaben zu Mixen zu zensieren und zurückzuweisen, die sie als illegal oder gegen ihre ToS erachten, und eine Blockchain-Analysefirma bezahlen werden, um eingehende Mix-Teilnehmer zu "überprüfen".

Die Verwendung von CoinJoin-Transaktionen, um die Herkunft von Geldern in Bitcoin zu verschleiern, ist seit vielen Jahren das Herzstück der Bitcoin-Privatsphäre, und die Probleme und Risiken, die damit verbunden sind, sind einige der Hauptprobleme, die Moneros Ringsignaturen korrigieren und verhindern.

In diesem Blogbeitrag werden wir kurz einen Vergleich zwischen CoinJoin und Ringsignaturen anstellen und erläutern, warum der Ansatz von Monero zu mehr Zensurresistenz, mehr Privatsphäre und weniger Ärger für die Nutzer führt.

## Was ist eine CoinJoin-Transaktion?

Da alle Transaktionen bei Bitcoin völlig transparent sind - Absender, Empfänger und Beträge werden offengelegt - müssen die Nutzer zusätzliche Maßnahmen ergreifen, um ihre Privatsphäre vor früheren Absendern und zukünftigen Empfängern ihrer Gelder zu schützen, oder sie riskieren Zensur, Überwachung oder den Diebstahl von Geldern durch physische Gewalt.

Die derzeit beste Lösung für den Schutz der Privatsphäre bei Bitcoin ist ein Tool namens [„CoinJoin“](https://bitcoiner.guide/qna/coinjoin/), bei dem zwei oder mehr Nutzer zusammenarbeiten (in der Regel über einen zentralen Koordinator), um eine spezielle Transaktion zu erstellen, die es Beobachtern von außen erschwert, die Eingaben mit den Ausgaben zu verbinden. Jeder Teilnehmer kommuniziert, um die Transaktion gemeinsam zu erstellen, ohne die Verfügungsgewalt über seine Gelder abzugeben, und erhält am Ende eine Ausgabe, deren Vorgeschichte für Außenstehende nun unklar (oder verschleiert) ist.

Dies unterbricht die Historie bestimmter UTXOs und ermöglicht es Bitcoin-Nutzern, ein gewisses Maß an Geheimhaltung bei Transaktionen zu erreichen. CoinJoin (wie es in Wasabi Wallet und Samourai Wallet, den beiden meistgenutzten CoinJoin-Tools für Bitcoin, implementiert ist) hat jedoch ein paar große Nachteile:

  * Da CoinJoin-Transaktionen vollständig auf freiwilliger Basis erfolgen und eine aktive Teilnahme erfordern, zeigt jeder Teilnehmer zwangsläufig, dass er eine größere Privatsphäre als "normale" Bitcoin-Nutzer anstrebt, was dazu führen kann, dass er auffällt und Probleme beim Ausgeben von Geldern bei vielen regulierten Börsen oder Einrichtungen verursacht. Jeder Nutzer kann nicht leugnen, dass er an einer CoinJoin-Transaktion teilgenommen hat.
  * Um andere CoinJoin-Teilnehmer zu finden, verwenden die meisten CoinJoin-Ansätze (einschließlich Wasabi Wallet) einen zentralen Koordinator, der die Teilnehmer miteinander verbindet und ihnen hilft, zu kommunizieren und eine ordnungsgemäße CoinJoin-Transaktion aufzubauen. Dieser zentralisierte Koordinator hat nie die Verfügungsgewalt über die Gelder der Nutzer, erhält aber einen umfassenden Einblick in die Transaktionen, die er koordiniert, kann eingehende Eingaben zensieren (wie im Fall von Wasabi Wallet) und kann unter Druck gesetzt werden, Informationen über CoinJoin-Teilnehmer zu sammeln oder weiterzugeben.
  * Nutzer mit großen Geldbeträgen, die CoinJoin nutzen wollen, müssen oft Stunden (oder sogar Tage!) warten, um genügend Teilnehmer für CoinJoin zu finden, was zu großen Verzögerungen zwischen dem Zeitpunkt, an dem ein Nutzer Geld erhält, und dem Zeitpunkt, an dem er es privat ausgeben kann, führt.
  * Die Privatsphäre, die eine CoinJoin-Transaktion bietet, nimmt mit der Zeit ab, wenn andere Teilnehmer Gelder ausgeben oder ihre Ausgaben mit ihrer Identität über KYC-Börsen, Händler, die eine ID verlangen, usw. verknüpfen. Das bedeutet, dass die Nutzer idealerweise ihre Gelder ständig in CoinJoin-Transaktionen umwandeln, um ihre Anonymität ("crowd to hide in") so frisch wie möglich zu halten.
  * Bei den meisten CoinJoin-Ansätzen müssen die Teilnehmer eine feste UTXO-Größe (d.h. 0,1 BTC) verwenden, um die Verbindung zwischen Ein- und Ausgängen von CoinJoin-Transaktionen zu erschweren. Dies führt zu höheren Gebühren (mehr separate Transaktionen sind für einen großen Input erforderlich), mehr "toxischem Kleingeld" (Gelder, die nicht ohne ernsthafte Risiken für die Privatsphäre ausgegeben werden können) und kann kleinere Nutzer davon abhalten, überhaupt zu mischen, wenn sie nicht über das erforderliche Mindestguthaben verfügen.

## Wie lösen Ringsignaturen diese Probleme?

Da [wir uns in der Vergangenheit eingehend mit dem Thema Ringsignaturen beschäftigt haben](/knowledge/ring-signatures), werde ich in diesem Blog-Beitrag nicht näher auf die technischen Aspekte ihrer Funktionsweise eingehen. Stattdessen werden wir uns ansehen, wie die in Monero verwendeten Ansätze die oben diskutierten Probleme mit CoinJoin lösen.

> CoinJoin ist Opt-in und erfordert die Teilnahme

Moneros Ringsignaturen sind ein zentrales Merkmal des Datenschutzprotokolls, und _jede_ Transaktion im Netzwerk verwendet sie. Das bedeutet, dass die Transaktionen eines Benutzers nicht dadurch auffallen, dass er mehr Privatsphäre sucht als "normale" Monero-Benutzer, und dass alle Benutzer plausibel abstreiten können, dass sie in einer bestimmten Transaktion Geld ausgegeben haben. Da ein Nutzer, der Geld ausgibt, sich nicht mit den Lockvogel-Eingaben in einer Transaktion koordiniert oder daran teilnimmt, können die Nutzer, die Eingaben besitzen, die zufällig als Lockvogel ausgewählt wurden, ehrlich sagen, dass sie nicht an dieser Transaktion teilgenommen haben, was ihre Privatsphäre stärkt.

> Verwendung eines zentralisierten Koordinators

Da Moneros Ringsignaturen völlig unkoordiniert sind und nur den wahren Geldgeber benötigen, um die Transaktion zu erstellen, gibt es keinen Bedarf für einen zentralen Koordinator in Monero. Dies stellt sicher, dass _niemand_ Niemand kann Ihnen den Zugang zur Privatsphäre in Monero verwehren, und es gibt keine zentralisierte Instanz, die unter Druck gesetzt werden kann, keine einfachen Sybil-Angriffe auf die Liquidität, etc. Solange Sie für Ihre Transaktion die richtigen Gebühren zahlen, erhalten Sie unzensierten Zugang zu Privatsphäre, Sicherheit und Anonymität in Monero.

> CoinJoin erfordert Liquidität

Die "Liquidität", die jedem zur Verfügung steht, der Monero ausgibt, um sie als Lockvogel zu verwenden, ist immer die Gesamtmenge der Ausgänge auf der Kette, so dass es nie einen Mangel an Lockvögeln gibt, in denen man sich mit Monero verstecken kann. Jemand, der Monero ausgeben möchte, kann dies ~20 Minuten nach Erhalt des Geldes tun und muss keine zusätzlichen Schritte durchführen, um eine starke Privatsphäre in Monero zu erhalten.

> CoinJoin Privatsphäre verschlechtert sich mit der Zeit

Da die Ausgaben von Monero dem Netzwerk nie bekannt sind, ist die Privatsphäre, die durch Ringsignaturen gewährleistet wird, viel weniger anfällig für eine Verschlechterung im Laufe der Zeit. Ein Benutzer muss nicht ständig Ausgaben in Monero tätigen, und außer unter extrem seltenen Umständen verliert er im Laufe der Zeit keine Privatsphäre.

Wenn ein Benutzer jedoch die mit einer Ausgabe verwendeten Köder "auffrischen" möchte, kann er die Mittel einfach an sich selbst zurücksenden und sie ~20 Minuten später wie gewohnt ausgeben.

> CoinJoin erfordert normalerweise Eingaben mit fester Größe

Da Beträge in jeder Transaktion versteckt werden mit [" Confidential Transactions"](/knowledge/monero-ringct) (ein Teil von "RingCT"), können die in einer bestimmten Transaktion verwendeten Köder eine beliebige Größe haben. Es gibt keinen Grund, sich über betragsbasierte Heuristiken in Monero Gedanken zu machen, und so sind Transaktionen viel einfacher zu erstellen und können Decoys von jedem Zeitpunkt und in jeder Höhe auf der Monero-Blockchain nutzen.

## Wie kann ich mehr erfahren?

Wenn Sie neugierig geworden sind und Ring-Signaturen oder CoinJoin-Transaktionen besser verstehen möchten, finden Sie unter den folgenden Links gute Einstiegsmöglichkeiten:

  * [Wie Ringsignaturen die Ausgaben von Monero verschleiern](/knowledge/ring-signatures)
  * [Ringsignatur - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin-Fragen und Antworten](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin-Übersicht](https://6102bitcoin.com/coinjoin-overview/)

Weiterlesen