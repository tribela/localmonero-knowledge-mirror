---
title: "In che modo CLSAG migliorerà l'efficienza di Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Come protocollo, Monero è attualmente in costante stato di innovazione. Utilizzando la ricerca in soluzioni sia on-chain che off-chain, la comunità Monero cerca aree da migliorare per rendere Monero più privato, più scalabile e più accessibile a tutti. Una delle innovazioni più recenti è la sostituzione del sistema di firma ad anello collegabile, MLSAG, con un CLSAG sostitutivo drop-in, che sta per Concise Linkable Spontaneous Anonymous Group.

A livello di superficie, l'implementazione di CLSAG ridurrà le transazioni 2 input, 2 output più comuni del 25%. Vedremo anche una riduzione del 10% nei tempi di verifica.

Ma cos'è esattamente CLSAG? Cosa fa e in cosa differisce dalla vecchia versione, MLSAG? Dedichiamo un minuto a ricordare a noi stessi perché e come delle firme ad anello in modo da poter meglio comprendere questo concetto. Le firme ad anello consentono input non interattivi e indistinguibili da testimone mediante l'uso di set di anonimato selezionati dal firmatario di output precedenti. In parole povere, consente a un utente di nascondere i propri output utilizzati in una transazione insieme a output non correlati, e può fare tutto questo senza la necessità che nessun altro partecipi. Tutto ciò che serve è una copia della blockchain. Ognuno di questi output sembra per lo più ugualmente probabile che sia quello reale inviato, nascondendo in tal modo metadati sul mittente.

Questo genera un po 'di problemi, comunque. E se un utente dovesse costruire una firma ad anello con tutte le uscite esca? Come si potrebbe sapere che il mittente sconosciuto non ha l'autorità di inviare nessuno di loro? Questo utente sarebbe in grado di spendere soldi falsi? La risposta è no. La firma dell'anello include un metodo per dimostrare che almeno una delle uscite è di proprietà del mittente sconosciuto, senza rivelare quale sia. In effetti, sia CLSAG che MLSAG (d'ora in poi noti come SAG) sono la parte della firma dell'anello che lo dimostra. È interessante notare che, allo stesso tempo, dimostra che l'importo della transazione, sebbene nascosto dietro le transazioni riservate (RingCT), si bilancia. Che i SAG dimostrino due cose, che un output è di proprietà di qualcuno sul ring e che la transazione si bilancia, è importante e in realtà dove risiedono le dimensioni e i risparmi di verifica. Se questo sta diventando confuso, non preoccuparti, presto arriveremo a un'analogia divertente e di facile comprensione.

Il vecchio schema di firma, MLSAG (Multonered Linkable Spontaneous Anonymous Group) dimostra le due cose sopra menzionate in una firma ad anello, ma ognuna le fa separatamente. L'uso di calcoli separati per le chiavi di firma e impegno implica operazioni più lente. Un computer moderno può eseguire questi calcoli in pochi millisecondi, il che non sembra molto, e in effetti per una transazione non lo è. Ma quando consideriamo il semplice numero di transazioni sulla blockchain Monero e che un nodo che si sincronizza da zero dovrà scaricare e verificare ognuna di esse, i byte e i millisecondi iniziano ad accumularsi rapidamente.

CLSAG combina le matematiche necessarie per dimostrarle entrambe in una, così come le calcola entrambe in una volta, e lo fa in modo sicuro. Cosa significa questo in modo sicuro? Bene, per chiarire questo, e speriamo che abbia più senso il tutto, esploriamo questa divertente analogia promessa.

Diciamo che devi andare sia al negozio di alimentari che al negozio di ferramenta, per raccogliere due cose diverse: cibo e prodotti chimici per la pulizia tossici. Non vuoi che si mescolino, come se ci fosse un incidente, le sostanze chimiche si riverseranno sul cibo, rendendole immangiabili. Decidi di essere super sicuro e guidare da casa tua alla drogheria, comprare il cibo e poi tornare a casa tua. Solo dopo aver scaricato il cibo torni in macchina, guidi al negozio di ferramenta e torni a casa tua con i prodotti chimici. Hai effettuato due viaggi separati per garantire la sicurezza di tutti gli acquisti. Sebbene sia davvero sicuro, è inefficiente. Questo rappresenta MLSAG, dove sono memorizzati due diversi set di matematica e due diversi "viaggi" sono fatti per calcolarli.

Decidi di volere un modo più rapido per farlo, tuttavia. È troppo tempo sprecato. Sicuramente farlo una o due volte non ti ruberà la vita, ma dovendo farlo più e più volte, le ore iniziano a sommarsi. Inizi a chiederti se invece puoi fare un viaggio. Da casa tua, dal negozio di alimentari, al negozio di ferramenta e da casa. Non puoi semplicemente lanciare tutto a casaccio nella tua macchina. Non è sicuro. Invece, si designano diversi punti nella tua auto per cose diverse e assicurati che tutto si adatti perfettamente al suo posto. In tal modo, sei in grado di fare un viaggio sicuro in entrambi i negozi e tenere le cose lontane l'una dall'altra. Questo rappresenta CLSAG. Ora c'è un solo set di matematica memorizzato in questa transazione per provare queste due cose, ed è fatto in modo da non interferire tra loro. È ancora necessario effettuare un viaggio, ma il numero di questi è stato ridotto drasticamente.

Tutto questo sembra abbastanza eccitante. È possibile trovare altre scorciatoie o altri modi per risparmiare tempo e spazio? La risposta è sì e no. Secondo gli attuali ricercatori dell'MRL, è probabile che non sia possibile modificare ulteriormente le costruzioni di tipo SAG per dimensioni o velocità migliori; tuttavia altre costruzioni come Arcturus, Omniring, RCT3 o Triptych producono vantaggi di ridimensionamento e verifica delle dimensioni molto migliori utilizzando diversi metodi matematici. Tuttavia, ciascuno di questi approcci di prossima generazione ai protocolli ambigui firmatari presenta i propri compromessi nei dettagli di implementazione e sono oggetto di ricerche e indagini attive.

Dopotutto, Monero è sempre innovativo.

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

  * [Perché Monero ha un'emissione di coda](/knowledge/monero-tail-emission)/

  * [La storia di Monero](/knowledge/monero-history)/

  * [Wired Magazine ha sbagliato su Monero, ecco perché](/knowledge/wired-article-debunked)/

  * [Top 15 Miti e preoccupazioni Monero debunked](/knowledge/monero-myths-debunked)/

  * [Come Dandelion ++ mantiene private le origini delle transazioni di Monero](/knowledge/monero-dandelion)/

  * [Perché Monero è open source e decentralizzato](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx)/

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better)/

Ulteriori letture