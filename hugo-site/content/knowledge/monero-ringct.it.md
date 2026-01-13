---
title: "Come RingCT nasconde gli importi delle transazioni Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
La privacy di Monero non dipende da un singolo meccanismo che, se rotto, rivelerebbe la totalità delle transazioni, ma piuttosto da tre diverse tecnologie che lavorano in tandem per fornire privacy olistica compensando i punti deboli delle altre parti. Questo approccio a tre poli è costituito da firme ad anello, RingCT e indirizzi invisibili. Queste tre tecnologie nascondono rispettivamente l'output reale (mittente), l'importo e il destinatario. Oggi parleremo di RingCT.

RingCT è probabilmente il più tecnico dei tre e può essere difficile da capire, quindi non spiegheremo come funziona esattamente, ma piuttosto mostreremo come è possibile non conoscere una quantità e comunque confermare le cose al riguardo . E non preoccuparti, useremo molti esempi come sempre.

Innanzitutto, esploriamo perché è importante verificare qualcosa sugli importi. Perché non possiamo semplicemente tenerli completamente segreti? La risposta è che ci sono modi intelligenti con cui le persone possono creare denaro dal nulla se ne hanno l'opportunità. Come potrebbe funzionare qualcosa di simile? Vediamo un esempio.

Se desideri acquistare un oggetto dal tuo amico e lui vuole dieci dollari per questo, inizi con dieci dollari e lui inizia con zero. Dopo che gli hai dato i dieci dollari, lui ha dieci dollari e tu zero. Hai iniziato con dieci, e ora ne ha dieci. Nessun denaro è stato creato o distrutto in questa transazione.

Con le criptovalute, un individuo intelligente può dare dieci dollari per l'articolo e invece di ricevere zero dollari in resto, può ricevere indietro due dollari. Invece di 0 e 10 che portano a 10 e 0 (o 10 = 10), ora è 0 e 10 porta a 10 e 2 (o 10 = 12). Two Monero è stato appena creato dal nulla. Puoi immaginare che se l'individuo facesse questo a se stesso più volte, sarebbe in grado di accumulare una fortuna gigantesca in breve tempo.

Con Bitcoin e altri, questo sarebbe facile da vedere. Osservi gli input che entrano in una transazione e gli output che escono e assicurati che ciò che viene inviato sia uguale a ciò che viene ricevuto. Se questi importi fossero crittografati e non visibili, un utente non ha modo di verificare che ciò che viene inviato e ciò che viene ricevuto sia lo stesso.

Nel tentativo di aumentare la privacy di Bitcoin, Gregory Maxwell ha creato Confidential Transactions (CT), una nuova tecnologia che consentirebbe importi crittografati, dimostrando che nulla è stato creato o distrutto nel processo. Come con la maggior parte delle tecnologie per la privacy, non è entrata in Bitcoin, ma Monero desiderava adottarla. C'era solo un problema. La tecnologia già implementata delle firme ad anello era incompatibile con l'idea proposta. Quindi, uno dei ricercatori di MRL dell'epoca, Shen Noether, modificò CT in RingCT, una versione di CT compatibile con le firme degli anelli.

Ancora una volta, il modo in cui funziona è piuttosto tecnico e sarebbe difficile da spiegare in un articolo introduttivo. Per gli appassionati di crittografia che semplicemente devono saperlo, ci sono molti articoli approfonditi scritti su Internet sul funzionamento interno della TC. Per il resto di noi, questo articolo mostrerà come potrebbe essere possibile nascondere gli importi, ma comunque dimostrare che nulla è stato creato o distrutto.

Supponiamo che Alice volesse inviare denaro a Bob. Alice invierà 10 XMR a Bob, che riceverà 10 XMR. 10 = 10 quindi non c'è niente di sbagliato qui. Ma Alice non vuole che nessuno sappia quanto sta inviando. Quindi lei e Bob creano un segreto condiviso. Fondamentalmente un numero che solo loro due conoscono. Supponiamo che il numero sia 22. Ora, Alice moltiplica 10 (ciò che sta realmente inviando) per 22 per ottenere 220. Questo è il numero che condivide con la rete.

I minatori stessi non conoscono il numero segreto. Se lo facessero, potrebbero dividere il numero che viene mostrato dal numero segreto e ottenere l'importo reale inviato. Ma dal momento che non lo fanno, non possono. Tuttavia, vedono che Bob ne riceverà 220. 220 inviato. 220 ricevuti. 220 = 220. In questo modo, la rete può verificare che nessun Monero sia stato creato o distrutto, il tutto senza conoscere l'effettivo importo che Alice ha inviato a Bob.

Dato che Bob conosce il numero segreto condiviso, quando riceve il denaro, divide semplicemente per 22 per ottenere l'importo reale che Alice ha inviato, 10. Alice e Bob sanno entrambi quanto è stato inviato e quanto è stato ricevuto, il tutto mentre a tutti gli altri viene assegnato un numero falso.

Ancora una volta, questo non è il modo effettivo in cui funziona la TC, ma dà un'idea di come potrebbe essere possibile qualcosa di simile. Il vero modo coinvolge cose come gli impegni di Pedersen, due importi inviati (un importo crittografato al destinatario e un importo di impegno alla rete), e ... sì, è già facile vedere come ci si possa perdere in tutto questo.

Una cosa da notare, tuttavia, è che mentre RingCT nasconde l'importo negoziato tra due parti in una transazione, non nasconde altre due serie di numeri.

Il primo sono le transazioni coinbase. Se questo termine non ti è familiare, significa fondamentalmente la ricompensa che i minatori ottengono per aver trovato il blocco successivo. Questo numero non è nascosto. Chiunque può vedere quanto il protocollo ha assegnato a un minatore per il suo servizio. In questo modo, la quantità attuale di Monero esistente può essere conosciuta sommando tutte le transazioni coinbase. La loro somma sarà pari all'attuale Monero in circolazione.

Il secondo numero non nascosto è la commissione pagata ai miner quando un utente invia una transazione. Le tariffe devono essere chiare in modo che i minatori possano sapere a chi dare la priorità. Questo è un modo in cui gli utenti possono danneggiare la loro privacy, tuttavia, come se qualcuno utilizzasse una commissione univoca del minatore ogni volta che invia una transazione (come 0,12345), le loro transazioni possono essere collegate.

Oltre a questi casi, RingCT nasconde gli importi Monero dal 2017 e la nostra privacy collettiva è tanto più forte per questo.

Ulteriori letture

  * [Come Monero abilita in modo unico le economie circolari](/knowledge/monero-circular-economies/)

  * [Firme ad anello di Monero vs CoinJoin come in Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Perché (e come!) dovresti tenere le tue chiavi](/knowledge/hold-your-keys/)

  * [Contribuire a Monero](/knowledge/contributing-to-monero/)

  * [Come i nodi remoti impattano sulla privacy di Monero](/knowledge/remote-nodes-privacy/)

  * [Come Monero usa gli hard-forks per aggiornare la rete](/knowledge/network-upgrades/)

  * [Visualizza i tag: Come un byte ridurrà i tempi di sincronizzazione del portafoglio Monero del 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool e il suo ruolo nella decentralizzazione del mining di Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Cosa farà per Monero](/knowledge/seraphis-for-monero/)

  * [Convertire Bitcoin in Monero è altrettanto privato che comprare Monero direttamente?](/knowledge/most-private-way-to-buy-monero/)

  * [Perché Monero usa una configurazione senza fiducia a differenza di Zcash](/knowledge/monero-trustless-setup/)

  * [Perché Monero è un migliore deposito di valore rispetto a Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Come Monero può superare gli effetti di rete di Bitcoin](/knowledge/network-effect/)

  * [Perché Monero ha la comunità di pensiero più critico](/knowledge/critical-thinking/)

  * [Truffe a cui prestare attenzione quando si utilizza Monero](/knowledge/monero-scams/)

  * [Come funzioneranno gli Atomic Swap in Monero](/knowledge/monero-atomic-swaps/)

  * [Ciò che ogni utente Monero deve sapere quando si tratta di networking](/knowledge/monero-networking/)

  * [In che modo gli indirizzi Monero Stealth proteggono la tua identità](/knowledge/monero-stealth-addresses/)

  * [In che modo i sottoindirizzo Monero impediscono il collegamento di identità](/knowledge/monero-subaddresses/)

  * [Spiegazione dei risultati di Monero](/knowledge/monero-outputs/)

  * [Migliori pratiche Monero per principianti](/knowledge/monero-best-practices/)

  * [Come le firme ad anello oscurano i risultati di Monero](/knowledge/ring-signatures/)

  * [Come Monero ha risolto il problema delle dimensioni del blocco che affligge Bitcoin](/knowledge/dynamic-block-size/)

  * [In che modo CLSAG migliorerà l'efficienza di Monero](/knowledge/what-is-clsag/)

  * [Perché Monero ha un'emissione di coda](/knowledge/monero-tail-emission/)

  * [La storia di Monero](/knowledge/monero-history/)

  * [Wired Magazine ha sbagliato su Monero, ecco perché](/knowledge/wired-article-debunked/)

  * [Top 15 Miti e preoccupazioni Monero debunked](/knowledge/monero-myths-debunked/)

  * [Come Dandelion ++ mantiene private le origini delle transazioni di Monero](/knowledge/monero-dandelion/)

  * [Perché Monero è open source e decentralizzato](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx/)

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better/)