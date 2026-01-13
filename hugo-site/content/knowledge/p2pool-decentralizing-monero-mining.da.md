---
title: "P2Pool og Dets rolle i Decentralisering Monero Minedrift"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Et af kernemålene i Monero-projektet er at muliggøre et retfærdigt, decentraliseret og sikkert netværk gennem nye og innovative tilgange til proof-of-work (PoW) mining, den vigtigste måde, hvorpå kryptovaluta-netværk er sikret i dag.

Mens en unik minealgoritme [som RandomX](/knowledge/monero-mining-randomx) er ekstremt vigtig for dette mål, da den hjælper for at sikre, at alle med en computer kan bidrage med et rimeligt beløb til sikkerheden på netværket, løser RandomX ikke de problemer, der kan opstå på grund af pool-mining. Pool-mining er langt den mest almindelige måde at mine kryptovalutaer på i dag, inklusive Monero, men heldigvis ændrer fremkomsten af p2pool-mining det hurtigt.

## Hvad er pool minedrift?

Pool-mining er en måde for minearbejdere at dele opgaven med at forsøge at løse en blok på netværket og derefter dele belønningerne ligeligt for alle blokke, som puljen finder. Selvom dette hjælper enormt med at udjævne den frekvens, hvormed minearbejdere bliver betalt i forhold til minedrift af Monero alene, er det ikke uden alvorlige centraliseringsproblemer.

Da hver minearbejder bidrager med arbejde til puljen, opgiver de kontrollen over alt arbejde, de udfører, og blokerer, som de finder til selve puljen, i tillid til, at puljen ærligt og retfærdigt vil dele belønningen mellem alle minearbejdere baseret på mængden af arbejde hver især har udført. Hvis alt går vel, indsamler pooloperatøren arbejdet fra alle minearbejdere, sender det til netværket og deler belønningerne ligeligt.

## Hvad er den problem med pool mining?

Desværre er dette helt afhængigt af tillid og giver pooloperatøren mulighed for at gøre uhyggelige ting med det arbejde, der udføres af minearbejdere. Pooloperatøren kunne bruge det arbejde, der udføres til at angribe netværket, forsøge at dobbeltbruge midler (hvis puljen er stor nok), eller blot bruge det arbejde, der udføres af minearbejderne til at betale sig selv og aldrig belønne minearbejdere ordentligt for deres arbejde .

Den største risiko for netværket er, at en pulje (eller flere puljer arbejder sammen) har mere end 51 % af netværkets hashrate under deres kontrol, da de kunne bruge dette til at snyde og bruge penge to gange (et dobbeltforbrug) angreb) eller forsøg på at ændre reglerne for netværket.

## Hvad er p2pool?

p2pool er et koncept, der oprindeligt blev skabt til at udvinde Bitcoin tilbage i 2011, men som aldrig har været udbredt og forbliver praktisk talt ubrugt på Bitcoin. Heldigvis brugte en af nøgleudviklerne bag RandomX, SChernykh, sin ferie på at finde på løsninger på nogle af problemerne med Bitcoin-implementeringen af p2pool og omskrive al softwaren fra bunden.

p2pool i Monero giver mulighed for en fuldstændig tillidsfri måde for minearbejdere at arbejde sammen om at løse blokke og sikre Monero-netværket ved at bruge speciel nodesoftware til p2pool for at dele arbejdet.

Dette gøres ved hjælp af en ny blockchain (en "sidekæde"), der registrerer det arbejde, hver minearbejder udfører, deres pungadresse, og hvor meget Monero de har tjent, og derefter udbetaler belønningen i en trust -mindre og decentraliseret måde. Da denne sidekæde har langt færre minearbejdere, er det meget nemmere at finde og indsende blokke på den end på det primære Monero-netværk, hvilket gør det lettere for minearbejdere at få ensartede udbetalinger i forhold til at minedrift Monero alene.

## Hvordan løser p2pool problemerne med pool mining?

I p2pool er der ingen centraliseret pulje, centraliseret puljeoperatør eller enkelt person, der holder på midler og fordeler udbetalinger. Alt det arbejde, der i fællesskab udføres af dem, der miner via p2pool, kontrolleres af p2pool blockchain og andre nodeoperatører for at sikre, at det er legitimt, og alle minearbejdere udbetales i henhold til det arbejde, de har udført, umiddelbart når en blok er fundet direkte fra belønningerne i den fundne blok.

Når minearbejdere vælger at bruge p2pool i stedet for en centraliseret pool, fjerner de al magt og tillid fra pooloperatørerne og sikrer, at deres arbejde bidrager til netværkets bedste og til deres egne belønninger, reducerer risikoen for netværksangreb, misbrug af deres arbejde eller tyveri af belønninger, som de skylder.

Dette hjælper ikke kun dem med at beskytte deres egne interesser, det reducerer også risikoen for, at centraliserede puljer kan udgøre for Monero-netværket som helhed. p2pool-brug hjælper også enormt med at reducere risikoen for, at nationalstater eller regulatorer kan udgøre for netværkets sundhed, da der ikke er nogen centraliserede pooloperatører at presse, ingen geografisk koncentration af pools at læne sig op af, eller noget andet let prespunkt. for dem at bruge mod Monero.

## Hvad er den ulemperne?

Heldigvis er p2pool i Monero blevet veldesignet og velbygget og fungerer ekstremt godt! Den største ulempe ved p2pool-mining er dog, at hver minearbejder, der ønsker at bruge p2pool, skal køre deres egen Monero-node, hvilket medfører, at processen med at komme i gang bliver en smule mere involveret. Denne node bruges dog derefter til at beregne al den information, der er nødvendig for at bygge og kontrollere blokke, og sikrer, at minearbejderen har fuldstændig kontrol over deres arbejde, der udføres. Noden kan også fungere som en ekstern node for minearbejdernes egen tegnebog, bidrager til netværket og meget mere.

Den anden væsentlige forskel fra centraliseret minedrift er, at små minearbejdere, der bruger p2pool, vil have lidt mere "varians", eller tid mellem udbetalinger, end en stor centraliseret pulje - men det er _ekstremt_ vigtigt at bemærke, at dette ikke vil føre til at tjene mindre Monero over tid! p2pool vil være lige så rentabelt for selv små minearbejdere over tid som centraliserede puljer. Noget af denne afvigelse opvejes også af, at p2pool oprindeligt har 0 % gebyrer, da der ikke er nogen centraliseret pooloperatør til at betale for deres tjenester!

## Hvordan kan jeg få startede?

På grund af det fremragende design af Monero's p2pool-implementering og de mange mennesker i samfundet, der har brugt tid på at hjælpe med at forenkle processen med minedrift via p2pool, bliver det heldigvis nemmere at komme i gang med tiden. Der er flere måder at komme i gang med mining med p2pool, men da de tekniske detaljer er uden for rammerne af denne artikel, er du velkommen til at springe ind på et link nedenfor afhængigt af dit operativsystem:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Hvordan kan jeg lære mere?

Hvis dette har vakt din nysgerrighed omkring p2pool-mining, så tag et kig nedenfor for nogle yderligere links og forklaringer om p2pool, hvordan det virker, og hvad det betyder for Monero:

  * [Den officielle Github til p2pool](https://github.com/SChernykh/p2pool)
  * [The officielle dokumenter om brug af p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool er nu live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, en "blokudforsker" af slagsen til p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Om hans udvikling af P2Pool en decentraliseret XMR-minepulje](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Yderligere læsning