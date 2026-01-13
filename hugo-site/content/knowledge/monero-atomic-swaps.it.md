---
title: "Come funzioneranno gli Atomic Swap in Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nel perseguimento del decentramento e di un sistema veramente senza autorizzazione, poche cose sono tanto ambite nello spazio delle criptovalute quanto gli scambi decentralizzati e gli scambi atomici. Fin dal suo inizio, Monero ha lottato per implementare gli atomic swap, poiché le funzionalità di privacy creano problemi unici quando si cerca di progettare un protocollo.

Ma prima torniamo indietro. Cosa sono gli atomic swap? Uno scambio atomico è un protocollo mediante il quale due diverse criptovalute, su diverse blockchain, possono essere scambiate in modo trustless senza intermediari. Ciò significa che se qualcuno volesse scambiare la criptovaluta A con la criptovaluta B, sarebbe in grado di farlo senza uno scambio, centralizzato o decentralizzato. Come si potrebbe immaginare, questo richiede una notevole ricerca e tutti i dettagli tecnici che lo rendono possibile diventano piuttosto complicati. Ancora una volta, LocalMonero è qui per aiutare e dare una semplice spiegazione alla persona comune.

Per iniziare, consideriamo la forma più semplice di atomic swap, implementata da Bitcoin. Se qualcuno desidera scambiare Bitcoin con un'altra moneta che utilizza la stessa tecnologia del contratto di blocco dell'ora di hash, può farlo nel modo seguente. Alice ha Bitcoin (BTC), ma vuole Litecoin (LTC) e Bob ha LTC, ma vuole BTC. Decidono di fare uno scambio atomico in modo che ognuno riceva la moneta che desidera. Alice invia il suo BTC a un indirizzo speciale, utilizzando script che bloccano i fondi in modo che nemmeno lei possa accedervi. Puoi pensarlo come se Alice mettesse il suo BTC in una cassetta di sicurezza. Quando viene creato il lockbox, ottiene una chiave e invia un hash di questa chiave a Bob. Ora Bob non ha la chiave stessa, solo l'hash, quindi non può ancora accedere ai fondi.

Bob utilizza questo hash come seme da cui genera il proprio lockbox e invia lì il suo LTC, dove è anche bloccato. Poiché l'hash della chiave di Alice è stato utilizzato come seme con cui è stato creato il lockbox di Bob, può usare la sua chiave per rivendicare l'LTC nel lockbox di Bob. La sua chiave si adatta! Ma, usando la magia matematica vudù, quando usa la sua chiave per aprire il lucchetto LTC, rivela la chiave a Bob, che può quindi usarla per richiedere il BTC che ha messo nel suo armadietto. In questo modo, senza intermediari, Alice e Bob si sono scambiati con successo i loro beni.

Ma c'è un piccolo problema. E se Alice lo manda al suo armadietto e Bob decide che non vuole più fare scambi. Ora, poiché Alice non può accedere al suo BTC che ha bloccato e Bob non completerà la sua parte della transazione, Alice perde i suoi soldi per sempre. Bene, fortunatamente, Bitcoin ha una piccola tecnologia chiamata transazioni di rimborso, quindi dopo un periodo di tempo, se il BTC non viene rivendicato da Bob, gli script hanno un sistema di sicurezza integrato, in cui il BTC tornerà automaticamente ad Alice. Questo è stato lo speedbump principale per l'implementazione degli atomic swap di Monero. A causa della [tecnologia per la privacy delle firme ad anello](/knowledge/ring-signatures)di Monero, il mittente di una transazione è sempre incerto. Come può il protocollo eseguire una transazione di rimborso se anche non sa da dove proviene la transazione?

Nel 2017, un piccolo gruppo di ricercatori ha delineato un metodo diverso con cui gli scambi atomici avrebbero funzionato in Monero. Dopo diversi anni di perfezionamento, i ricercatori hanno finalizzato un processo mediante il quale Monero sarebbe stata in grado di fare atomic swap con Bitcoin, anche senza transazioni di rimborso.

Come per molte cose di questo livello di complessità tecnica, la nostra spiegazione semplificherà eccessivamente alcune cose per trasmettere l'idea, ma darà comunque un'idea solida dei meccanismi con cui questo processo funzionerebbe.

Sia Alice (che ha XMR e vuole BTC) che Bob (che ha BTC e vuole XMR) devono scaricare ed eseguire un programma che supporti lo scambio atomico. Questo può essere implementato in portafogli, scambi decentralizzati o programmi speciali e specifici, ma il software deve eseguire il protocollo di scambio atomico. Nella prima fase, i client di Alice e Bob si connettono tra loro e creano diversi segreti e chiavi condivisi. In questo passaggio, viene creato un nuovo indirizzo Monero, con Alice che ha una metà della chiave e Bob che ha l'altra. Nessun Monero è ancora lì, quindi non c'è niente da spendere. Un'ultima cosa da notare su questo indirizzo è che entrambi hanno la chiave di visualizzazione per questo portafoglio, quindi possono entrambi sbirciare dentro per vedere se o quando arriva Monero.

Nella seconda fase, Bob invia il suo BTC a un indirizzo speciale, simile al protocollo di scambio atomico di Bitcoin di cui abbiamo già parlato. Dopo che Alice vede il BTC arrivare a questo indirizzo sulla blockchain, invia il suo Monero all'indirizzo Monero a cui lei e Bob hanno entrambi metà della chiave. Bob può verificare che il Monero sia arrivato poiché ha anche la chiave di visualizzazione, e una volta che vede il Monero è al sicuro nel portafoglio, invia ad Alice un pezzo di una chiave che le permetterà di ritirare il Bitcoin. Simile all'altro protocollo, il processo di rivendicazione del Bitcoin rivela a Bob la sua metà della chiave Monero. Ora Bob ha entrambe le metà, quindi può rivendicare il Monero, mentre Alice ha solo la sua metà, quindi non può provare a prenderlo prima di lui.

Quindi, se hai esaminato tutto questo e sei ancora un po 'confuso su come Monero sia stata in grado di aggirare il problema delle transazioni di rimborso, la risposta è abbastanza semplice. Poiché Monero stesso non ha transazioni di rimborso, il lettore dovrebbe notare che il Bitcoin (che ha transazioni di rimborso) viene inviato per primo, e solo dopo che è stato verificato come essere sulla blockchain viene inviato Monero. Ciò consente a Monero di utilizzare la capacità di Bitcoin di eseguire script nelle transazioni di rimborso e di trarne vantaggio, senza la necessità di avere queste funzionalità stesse.

Lo scambio atomico è ora completo, ma da qui Bob ha un paio di opzioni per il suo XMR appena rivendicato. Può usare questo portafoglio Monero così com'è o spostare l'XMR su un altro portafoglio che già possiede. Molto probabilmente Bob sposterà il Monero su un altro portafoglio, perché Alice ha ancora la chiave di visualizzazione e può vedere all'interno.

La bellezza di questo protocollo è che è ancora abbastanza nuovo e c'è molto spazio per le ottimizzazioni. È anche abbastanza flessibile nella sua architettura, quindi l'implementazione in altri portafogli o scambi decentralizzati dovrebbe essere semplice e adattarsi perfettamente alla loro architettura esistente.

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

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx)/

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better)/

Ulteriori letture