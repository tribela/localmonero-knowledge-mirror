---
title: "Seraphis: Was es für Monero tun wird"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: ein modulares Design-Upgrade für Monero-Transaktionen

Dieser Beitrag beschreibt [Seraphis](https://github.com/UkoeHB/Seraphis), eine Reihe von Transaktionsprotokollstrukturen und -abstraktionen, die von dem pseudonymen Forschungsmitarbeiter [`koe`](https://github.com/UkoeHB) für das Monero-Ökosystem entwickelt wurden und mit laufender Sicherheitsanalyse durch den pseudonymen Mitwirkenden [`coinstudent2048`](https://github.com/coinstudent2048).  
Wir nehmen einige Vereinfachungen vor und lassen bestimmte technische Details aus Gründen der Klarheit weg; Aus diesem Grund und weil das Design von Seraphis noch im Gange ist, sollten interessierte Leser die Seraphis-Dokumentation für die aktuellsten Informationen zurate ziehen.

## Transaktionen in Monero

Protokolle wie Bitcoin und Monero und andere verlassen sich auf ein sogenanntes "Output-Modell" des Betriebs, bei dem ein _Output_ eine Darstellung des Werts ist, der übertragen werden kann.  
Transaktionen verbrauchen eine oder mehrere Outputs, die von einem Sender gesteuert werden, und erzeugen neue Outputs, die an Empfänger gerichtet sind (oder als Wechselgeld zurück an den Sender); Die Transaktion muss dahingehend ausgeglichen sein, dass die verbrauchten Outputs einen Gesamtwert enthalten müssen, der genau dem Wert der neuen Outputs entspricht (zuzüglich einer vom Netzwerk erhobenen Gebühr).  
In vielen Protokollen wie Bitcoin wird der in einem Output enthaltene Wert im Klartext geschrieben, ebenso wie der Empfänger.  
Darüber hinaus ist es durch Betrachten der Blockchain trivial zu sehen, ob und wann ein Output ausgegeben wurde (d. h. ob sie in einer späteren Transaktion verbraucht wurde und welche Transaktion sie ausgegeben hat).

Im Gegensatz dazu führen Protokolle wie Monero ein anderes Design ein:

  * Output-Werte sind versteckt und in der Blockchain nicht sichtbar
  * Empfängeradressen werden durch die Verwendung eines einmaligen Adressierungsprotokolls verborgen
  * Ob ein Output ausgegeben wurde oder nicht, wird durch die Verwendung mehrdeutiger Signaturen verschleiert

Das Ergebnis ist, dass es ohne externe Informationen schwierig ist festzustellen, ob ein bestimmter Output ausgegeben wurde, welchen Wert er hat und wer der Empfänger ist.

Das aktuelle Monero-Transaktionsprotokoll heißt _RingCT_ und verwendet mehrere kryptografische Bausteine, um diese Designziele zu erreichen.

  * _Commitments_ verbergen Beträge auf mathematisch sinnvolle Weise
  * _Reichweitennachweise_ verhindern einen Überlauf, der das Angebot aufblähen könnte
  * _Verknüpfbare Ringsignaturen_ sorgen für Mehrdeutigkeit des Unterzeichners und verhindern doppelte Output-Versuche
  * _Commitment-Offsets_ bestätigen, dass Transaktionen ausgeglichen sind

Diese Bausteine sind sorgfältig miteinander verflochten, um das RingCT-Protokoll aufzubauen.

Eine nützliche Eigenschaft des RingCT-Protokolls ist, dass einige Bausteine so geändert oder aktualisiert werden können, dass das Gesamtdesign und die Eigenschaften intakt bleiben, aber Effizienz- oder Sicherheitsverbesserungen erzielt werden können. Tatsächlich sind diese Art von Upgrades in der Geschichte von Monero mehrmals aufgetreten (oder geplant). Reichweitennachweise im ursprünglichen RingCT-Protokoll waren sperrig und langsam; Sie wurden später auf eine Konstruktion namens [Bulletproofs](https://eprint.iacr.org/2017/1066) aktualisiert, die Transaktionen mit besserer Sicherheitsanalyse kleiner und schneller machte, und sollen für noch größere Effizienzvorteile auf eine neuere Konstruktion namens [Bulletproofs+](https://eprint.iacr.org/2020/735) aktualisiert werden. 

Ein ähnlicher Prozess wurde mit dem verknüpfbaren Ringsignaturbaustein durchgeführt. Im ursprünglichen Protokoll wurde eine Konstruktion namens [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) verwendet. Dies wurde später auf eine neuere Konstruktion namens [CLSAG](https://eprint.iacr.org/2019/654) aktualisiert, die schneller ist, zu kleineren Transaktionen führt und eine bessere Sicherheitsanalyse bietet. Eine noch neuere verknüpfbare Ringsignaturkonstruktion basierend auf [Triptych](https://eprint.iacr.org/2020/018) wurde vorgeschlagen, aber diese wurde wegen ihrer Auswirkungen auf Multisignaturoperationen nicht für den Einsatz ausgewählt.

## Seraphis

Seraphis geht mit dieser Idee noch einen Schritt weiter.  
Anstatt einzelne Bausteine des bestehenden RingCT-Transaktionsprotokolls zu aktualisieren, wird ein anderes Protokoll eingeführt, das verschiedene Bausteine nutzen und eine verbesserte Funktionalität bieten kann.

## Bausteine

Seraphis verwendet eine andere Reihe von kryptografischen Bausteinen, um seine Ziele zu erreichen.

  * _Commitments_ verbergen weiterhin Beträge
  * _Bereichsbeweise_ verhindern nach wie vor Überlauf und Angebotsinflation
  * _Zugehörigkeitsnachweise_ bieten dem Unterzeichner Zweideutigkeit
  * _Commitment-Offsets_ sichern nach wie vor das Gleichgewicht
  * _Berechtigungsnachweise_ verhindern Doppelausgaben

Beachten Sie die Änderung hier: Verknüpfbare Ringsignaturen werden durch eine Kombination aus Zugehörigkeitsnachweisen und Berechtigungsnachweisen ersetzt. Grob gesagt, zeigen Zugehörigkeitsnachweise, dass eine verbrauchte Ausgabe Teil einer größeren Menge ist, ähnlich wie bei RingCT. Aber im Gegensatz zu RingCT ist bei Zugehörigkeitsnachweisen das Linking-Tag überhaupt nicht beteiligt! Autorisierende Beweise zeigen, dass das Linking Tag gültig ist und werden verwendet, um die endgültige Transaktion zu signieren.

Da RingCT das Linking Tag in die mehrdeutige Signatur einbindet, sind Signier- (und Multisignatur-) Operationen rechenintensiver, und es wird schwieriger, andere Tag-bezogene Funktionen zu entwickeln. In Seraphis hingegen kann die Erstellung von Zugehörigkeitsnachweisen von hochgradig vertrauenswürdigen Geräten (die möglicherweise nur über eine begrenzte Rechenleistung verfügen, wie z. B. eine Hardware Wallet) sicher an ein weniger vertrauenswürdiges Gerät delegiert werden, und Signiervorgänge (und Multisignaturvorgänge) sind unter Verwendung des viel einfacheren Autorisierungsnachweises viel einfacher.

Glücklicherweise existieren einige der von Seraphis benötigten Bausteine bereits an anderer Stelle und müssen nicht von Grund auf neu entwickelt werden. Sowohl die Bulletproofs als auch die Bulletproofs+-Konstruktionen können als Bereichsbeweise verwendet werden. Modifikationen an Beweissystemen vom Typ Schnorr können für Autorisierungsbeweise verwendet werden. Und ein effizientes [Beweissystem](https://eprint.iacr.org/2015/643), das bereits als Grundlage für Triptych, [Lelantus](https://eprint.iacr.org/2019/373) und [Spark](https://eprint.iacr.org/2021/1173)* verwendet wurde kann für Mitgliedschaftsbeweise modifiziert werden.

* Cypher Stack erhält Mittel für die Entwicklung von Spark.

## Adressierung

Leider sind derzeit verwendete Monero-Adressen nicht mit Seraphis kompatibel. Benutzer müssten neue Adressen aus ihren Wallet-Schlüsseln generieren, um Monero zu erhalten, wenn Seraphis implementiert wäre. Diese Ökosystemkosten sind jedoch mit einer Vielzahl von Vorteilen verbunden.

Abgesehen von den oben diskutierten strukturellen Vorteilen ist das Seraphis-Design für viele verschiedene Adresskonstruktionsmöglichkeiten zugänglich, von denen jede mit Kompromissen einhergeht. Während die endgültige Adresskonstruktion, die in Seraphis verwendet werden soll, [noch entschieden wird](https://github.com/monero-project/research-lab/issues/92) (ein Schema, das viel Aufmerksamkeit erhält, heißt [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), können wir einige allgemeine und nützliche Funktionen beschreiben.

Sie wissen vielleicht, dass Monero-Adressen eine _Ansichtsschlüssel_ -Funktionalität bieten, bei der Sie einem Gerät oder Dritten einen Ansichtsschlüssel zur Verfügung stellen und ihm erlauben können, in Ihrem Namen nach eingehenden Ausgaben zu suchen, ohne auf Ausgaben zu verzichten Behörde. Dies ist nützlich für Brieftaschen, die auf dem neuesten Stand bleiben können, während Ihr Ausgabenschlüssel sicher verschlossen bleibt. Es ist auch nützlich für Fälle, in denen Sie einen externen Zugriff wünschen, wie z. B. eine öffentliche Wohltätigkeitsorganisation, die Transparenz anbietet, oder ein Unternehmen mit einer Buchhaltungsabteilung.

Der Nachteil von Monero-Ansichtsschlüsseln ist, dass sie keinen vollständigen oder feinkörnigen Ansichtszugriff bieten. Es ist nicht möglich, zuverlässig zu erkennen, wann ein Wallet Geld ausgibt, was es schwierig macht, Wallet-Guthaben richtig zu berechnen, wenn der Ausgabenschlüssel nicht verfügbar ist. Es ist derzeit auch nicht möglich, eingehende Ausgaben zu erkennen, ohne auch den in diesen Ausgaben enthaltenen Wert zu erfahren (was bedeutet, dass alle Drittanbieter, die für die Suche nach eingehenden Ausgaben verantwortlich sind, genau erfahren, wie viel Monero Sie erwerben).

Seraphis-Adressierungskonstruktionen können dieses Problem lösen. Bei Seraphis ist Ihre Adresse mit verschiedenen Schlüsseln ausgestattet, die verschiedene Dinge tun können:

  * Auf eingehende Ausgaben achten, aber deren Wert verbergen
  * Auf eingehende Ausgaben achten, aber deren Wert anzeigen
  * Auf ausgehende Ausgaben achten
  * Ihnen helfen, Transaktionen zu generieren, aber nicht zu signieren
  * Neue Adressen generieren (nützlich für Händler oder Austausch mit vielen Kunden)

Als Adressinhaber können Sie entscheiden, wie viel Befugnis Sie an andere Geräte oder Dritte delegieren.

## Das große Bild

Seraphis ist eine große Veränderung im Monero-Ökosystem. Während es Änderungen an Adressen und Transaktionsbausteinen erfordert, bietet sein Design Flexibilität und nützliche Funktionen, die mit dem heutigen RingCT-Protokoll nicht möglich sind. Während ein Großteil des Designs abgeschlossen ist und zu [einer Implementierung](https://github.com/UkoeHB/monero/tree/seraphis_lib) entwickelt wird, sind das Adressdesign und die Sicherheitsanalyse im Gange. Seraphis bietet eine hervorragende Gelegenheit, das Monero-Ökosystem voranzutreiben!

Weiterlesen