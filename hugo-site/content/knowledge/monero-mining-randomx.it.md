---
title: "Monero Mining: cosa rende RandomX così speciale"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Il 30 novembre 2019, Monero ha avuto il suo hard fork semestrale, con il cambiamento più atteso che è stato il passaggio dal vecchio algoritmo PoW, cryptonight, a quello completamente nuovo, sviluppato internamente, RandomX. La comunità Monero ritiene che RandomX sia un grande passo verso il mining egualitario, ma approfondiamo per vedere se è così.

## Scopo

Per valutare se RandomX è un miglioramento, dobbiamo prima capire qual è lo scopo del mining. L'estrazione mineraria protegge una blockchain dalle doppie spese tramite il consenso di Nakamoto. Le complessità esatte di come lo fanno vanno oltre lo scopo di questo articolo, ma possono essere apprese da molte fonti diverse su Internet. Ciò che conta è che la sicurezza provenga da hash generati da computer (minatori), in concorrenza tra loro per trovare la soluzione matematica necessaria per creare un altro blocco. Mentre lo fanno, aggiungono nuove transazioni alla blockchain. In cambio del loro lavoro (hash) vengono compensati con monete coniate di recente.   
  
Ci sono una serie di problemi che possono verificarsi con questa configurazione e richiedono incentivi adeguati per funzionare correttamente, ma ci concentreremo su un particolare problema che potrebbe sorgere. Se l'estrazione mineraria dovrebbe essere una competizione, cosa succede quando un minatore ottiene un vantaggio?

## sfondo

Per contesto, parliamo un po’ dell’hardware di mining. I minatori utilizzano i computer per svolgere il lavoro, ma sappiamo tutti che non tutti i computer sono uguali. Alcuni computer sono abbastanza potenti da gestire reti di intelligenza artificiale o giochi intensivi, mentre altri hanno difficoltà anche con compiti semplici. Queste differenze nella potenza di calcolo influiscono anche sull’hash rate, ovvero la velocità con cui cercano soluzioni a blocchi.   
  
Ma anche queste differenze tra computer impallidiscono in confronto ai tassi di hash dell'hardware specializzato, altrimenti noto come circuiti integrati specifici per l'applicazione (ASIC), che surclassano i normali computer di diversi ordini di grandezza.  
  
Prendiamoci un po' di tempo per esplorare ciò che rende gli ASIC così potenti. Immaginate che tutti i computer rientrino in uno spettro che va dall'essere in grado di fare molte cose, ma niente bene, al fare solo una cosa, ma farla molto bene. CPU e ASIC si trovano agli estremi opposti di questo spettro.  
  
Le CPU presenti in tutti i computer standard si trovano al primo posto. Possono fare molte cose, come navigare sul Web, giocare o eseguire il rendering di video, ma non ne fanno nessuna particolarmente bene. Ma questa flessibilità va a scapito dell'efficienza.  
  
Gli ASIC sono dall'altra parte, dove possono fare solo una cosa, ma lo fanno a una velocità incredibile. Possono eseguire solo una funzione matematica, ma poiché possono ignorare tutto il resto, i miglioramenti in termini di prestazioni sono astronomici. Questa efficienza, tuttavia, va a scapito della flessibilità, quindi se la funzione cambia anche leggermente – un esempio è x + y = z cambia in 2x + y = z – allora l'ASIC cesserà di funzionare del tutto.   
  
Non tutti possiedono un ASIC, ma tutti possiedono un computer. Ciò può portare ad un vantaggio ingiusto.

## Un'analogia divertente

Se questo è ancora confuso, forse la seguente analogia aiuterà. Immagina una lotteria in cui vengono assegnati mille dollari ogni ora e questa lotteria ti consente di stampare i tuoi biglietti! Inizi a stampare tutti i biglietti che puoi sulla tua stampante di casa, che può stampare un biglietto al secondo. Dopo aver sottratto i costi di elettricità e inchiostro, vedi che puoi ancora realizzare un profitto, anche se vinci la lotteria solo una volta ogni poche settimane.  
  
Nel tempo, si espande l'operazione fino a quando non si dispone di un'intera sala dedicata alle stampanti. 20 in tutto. Va tutto bene ... fino a un fatidico giorno.  
  
C'è una grande novità. Qualcuno ha inventato un nuovo tipo di stampante. Può solo stampare i biglietti della lotteria. Non è possibile stampare immagini o documenti di ufficio o eseguire la stampa fronte-retro. Solo biglietti della lotteria. Ma può stamparli al ritmo di 1000 biglietti al secondo. Guardi nella tua piccola sala stampanti. 20 stampanti. Hai bisogno di altre 980 stampanti solo per stare al passo con UNA di queste stampanti mostruose, e se qualcuno ne ha due ...?  
  
Purtroppo esci dal gioco della lotteria perché non puoi più giustificare i costi di elettricità e inchiostro.  
  
Ma aspetta! Un paio di settimane ci sono altre notizie! Il design del biglietto è cambiato. Ora i numeri, che erano in cima, ora sono in fondo. Le nuove stampanti per mostri sono così rigide da non poterlo fare. Potevano solo realizzare il disegno precedente. Non passa molto tempo prima che tu stia di nuovo felicemente stampando. Almeno fino a quando qualcuno non realizzerà una nuova stampante monster per il nuovo design.

## RandomX

Dove si inserisce RandomX in tutto questo? Cerca di uniformare il vantaggio degli ASIC rendendo gli ASIC molto difficili da realizzare. Lo fa richiedendo ai minatori di creare ed eseguire codice casuale al posto dell'hash basato su un algoritmo.  
  
Potrebbe confondere il fatto che questo in realtà aiuti qualsiasi cosa, quindi torniamo all'analogia con la nostra stampante. Ricordi cosa è successo quando il design è cambiato? Le vecchie stampanti mostruose diventano obsolete ogni notte e bisognava svilupparne di nuove pensando al nuovo design. Cosa accadrebbe se ogni nuovo biglietto premio della lotteria dovesse aderire a un nuovo standard di progettazione per ogni nuovo jackpot?   
  
La creazione di una nuova stampante mostro diventerebbe incredibilmente difficile. Non puoi più pianificare un solo biglietto. Poiché il design è casuale, i produttori di stampanti mostruose dovrebbero aggiungere capacità di colore, modi per stampare caratteri e bordi e forme diversi e altro ancora. In breve, la macchina che hanno finito per inventare sarebbe una normale stampante standard. Proprio come hanno fatto tutti gli altri.  
  
Semplicemente implementando questa casualità nella progettazione dei biglietti, abbiamo sostanzialmente ridotto il grande vantaggio ottenuto dall'hardware specializzato. RandomX fa lo stesso, ma con il mining.  
  
In questo modo, i vantaggi ottenuti da poche persone benestanti selezionate sono ridotti al minimo, come se investissero nella creazione di "ASIC" per il mining di RandomX, in realtà inventerebbero semplicemente CPU più forti e migliori, a beneficio del mondo in generale.  
  
Ciò significa che il ragazzino con le sue 20 stampanti di biglietti è tornato in gioco. Potrebbe ancora avere un momento più difficile poiché questi individui ricchi possono ancora acquistare più stampanti di lui, ma almeno ora non è surclassato da ordini di grandezza semplicemente da una macchina. È competitivo nel suo piccolo.  
  
Sapendo che anche il ragazzino può essere competitivo nel mining di Monero, incoraggiamo tutti a provarlo, sia nel portafoglio GUI di Monero, che supporta il mining in solitario, sia scaricando software gestito dalla community. È facile, competitivo e aperto a tutti.

Ulteriori letture

  * [Come Monero abilita in modo unico le economie circolari](/knowledge/monero-circular-economies)/

  * [Firme ad anello di Monero vs CoinJoin come in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Perché (e come!) dovresti tenere le tue chiavi](/knowledge/hold-your-keys)/

  * [Contribuire a Monero](/knowledge/contributing-to-monero)/

  * [Come i nodi remoti impattano sulla privacy di Monero](/knowledge/remote-nodes-privacy)/

  * [Come Monero usa gli hard-forks per aggiornare la rete](/knowledge/network-upgrades)/

  * [Visualizza i tag: Come un byte ridurrà i tempi di sincronizzazione del portafoglio Monero del 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool e il suo ruolo nella decentralizzazione del mining di Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Cosa farà per Monero](/knowledge/seraphis-for-monero)/

  * [Convertire Bitcoin in Monero è altrettanto privato che comprare Monero direttamente?](/knowledge/most-private-way-to-buy-monero)/

  * [Perché Monero usa una configurazione senza fiducia a differenza di Zcash](/knowledge/monero-trustless-setup)/

  * [Perché Monero è un migliore deposito di valore rispetto a Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Come Monero può superare gli effetti di rete di Bitcoin](/knowledge/network-effect)/

  * [Perché Monero ha la comunità di pensiero più critico](/knowledge/critical-thinking)/

  * [Truffe a cui prestare attenzione quando si utilizza Monero](/knowledge/monero-scams)/

  * [Come funzioneranno gli Atomic Swap in Monero](/knowledge/monero-atomic-swaps)/

  * [Ciò che ogni utente Monero deve sapere quando si tratta di networking](/knowledge/monero-networking)/

  * [Come RingCT nasconde gli importi delle transazioni Monero](/knowledge/monero-ringct)/

  * [In che modo gli indirizzi Monero Stealth proteggono la tua identità](/knowledge/monero-stealth-addresses)/

  * [In che modo i sottoindirizzo Monero impediscono il collegamento di identità](/knowledge/monero-subaddresses)/

  * [Spiegazione dei risultati di Monero](/knowledge/monero-outputs)/

  * [Migliori pratiche Monero per principianti](/knowledge/monero-best-practices)/

  * [Come le firme ad anello oscurano i risultati di Monero](/knowledge/ring-signatures)/

  * [Come Monero ha risolto il problema delle dimensioni del blocco che affligge Bitcoin](/knowledge/dynamic-block-size)/

  * [In che modo CLSAG migliorerà l'efficienza di Monero](/knowledge/what-is-clsag)/

  * [Perché Monero ha un'emissione di coda](/knowledge/monero-tail-emission)/

  * [La storia di Monero](/knowledge/monero-history)/

  * [Wired Magazine ha sbagliato su Monero, ecco perché](/knowledge/wired-article-debunked)/

  * [Top 15 Miti e preoccupazioni Monero debunked](/knowledge/monero-myths-debunked)/

  * [Come Dandelion ++ mantiene private le origini delle transazioni di Monero](/knowledge/monero-dandelion)/

  * [Perché Monero è open source e decentralizzato](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better)/