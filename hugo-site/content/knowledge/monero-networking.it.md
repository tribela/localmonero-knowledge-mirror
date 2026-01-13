---
title: "Ciò che ogni utente Monero deve sapere quando si tratta di networking"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Non dovrebbe sorprendere nessuno che Monero, e in effetti tutte le criptovalute, gira su Internet. Eppure, anche se questa affermazione sembra basilare e ovvia, molti non considerano le implicazioni di ciò che significa per quanto riguarda la loro privacy. In altre parole, ci sono alcune cose che Monero può e non può proteggere, solo per la natura del funzionamento su Internet. Alcune di queste considerazioni sono semplici inconvenienti, mentre altre sono molto più gravi in uno scenario in cui è richiesta la privacy assoluta. Prendiamoci il tempo per familiarizzare con il modo in cui gli utenti Monero interagiscono tra loro sulla rete e cosa significa per la loro privacy.

Partendo dal lato banale delle cose, se un utente non ha accesso a Internet, non può scaricare nuovi blocchi, propagare transazioni per conto di altri o inviare transazioni per conto proprio. Una cosa interessante da notare è che un utente con un nodo completo, senza accesso a Internet può costruire una transazione offline che può essere inviata in seguito. Questo perché una firma ad anello necessita solo di output dalla blockchain con cui nascondersi. Un breve promemoria su [come funzionano le firme ad anello](/knowledge/ring-signatures), nasconde l'output reale che un utente sta inviando tra una raccolta di output non affiliati scelti dal passato. Se l'utente ha accesso a questi output sotto forma di una blockchain completamente scaricata (nodo completo), può creare la firma ad anello dagli output precedenti e, una volta ripristinata la connettività Internet, propagare la transazione alla rete.

Un utente che sta utilizzando un nodo remoto non può farlo, poiché quando costruisce la propria firma ad anello, contatta il nodo completo remoto per le uscite da includere nella firma ad anello. Nessuna connessione Internet significa che non possono raggiungere questo nodo, quindi non hanno capacità di costruzione di transazioni offline.

Prima di continuare con alcune considerazioni sulla privacy, diamo una breve introduzione su come funziona Internet nel suo complesso. L'intera Internet non è altro che computer che si connettono ad altri computer. Questo è tutto. Il blog che ti piace leggere? Solo alcuni file ospitati sul computer di qualcun altro. Questo sito su cui stai leggendo questo articolo (LocalMonero)? File e codice ospitati su un computer da qualche parte. Anche i grandi siti pazzi funzionano in questo modo. Prendi YouTube per esempio. Solo file video ospitati sui giganteschi sistemi informatici di Google e ti connetti a loro per scaricare il video sul tuo computer in modo da poterlo guardare.

Questi computer possono distinguersi tra loro perché a ogni computer connesso a Internet viene assegnato un numero di identificazione univoco chiamato indirizzo IP. Di solito si tratta di quattro serie di numeri separati da punti, ad esempio: 172.66.35.7. È importante tenerlo presente quando consideriamo il modo in cui le informazioni di Monero vengono spostate su Internet. Monero è una rete peer-to-peer (P2P), il che significa che i computer si connettono direttamente tra loro anziché utilizzare un intermediario. Quindi, quando il nodo completo di un utente sta scaricando un blocco appena scoperto, non lo sta scaricando da un server centrale, ma dai suoi pari. Il rovescio della medaglia è che, poiché gli utenti si connettono tra loro direttamente, conoscono gli indirizzi IP degli altri.

Bene? Qual è il grosso problema? È solo un numero, vero? Non esattamente. Gli stessi indirizzi IP contengono informazioni sull'utente, come il paese di origine e il provider di rete, ma, peggio ancora, i provider di servizi Internet (ISP) conoscono l'indirizzo IP di ogni persona che utilizza i loro servizi. Ciò significa che questi ISP e quelli con cui lavorano possono guardare il traffico Internet di un utente e, utilizzando alcune tattiche intelligenti, scoprire che stanno utilizzando Monero. Ora, prima di spaventarti, prendi nota della dicitura lì. Tutto ciò che questi ficcanaso possono fare è vedere che una persona si sta connettendo ad altri nodi della rete Monero. A causa della tecnologia per la privacy di Monero, non trapelano nient'altro sull'individuo. Non se stanno eseguendo un nodo o se / quando inviano transazioni e se viene inviata una transazione, nessuna delle sue informazioni è nota. Tutto ciò che questi ISP possono vedere è che uno dei loro utenti si sta connettendo alla rete Monero.

Ora, per alcune persone, in alcune località, queste informazioni da sole potrebbero essere sufficienti a causare danni alla reputazione o alla libertà. O forse l'idea che qualcuno invada la tua privacy e ciò che fai su Internet, per qualsiasi motivo, non è accettabile per te. Queste persone sono incoraggiate a connettersi alla rete Monero solo utilizzando VPN, Tor o I2P, che sono tutti servizi che nascondono l'indirizzo IP di un utente agli altri e nascondono ciò che un utente sta facendo dal proprio ISP. Le differenze tra questi servizi esulano dallo scopo di questo articolo, ma ci sono molti articoli di alta qualità scritti sull'argomento, quindi gli utenti interessati sono incoraggiati a studiare!

Per il resto di noi, potremmo pensare che far sapere agli altri che siamo collegati alla rete Monero non è un grosso problema. Dopo tutto, i contenuti effettivi delle nostre transazioni, o se ne stiamo inviando qualcuno, sono nascosti al pubblico, quindi che male c'è? Sebbene questo possa essere vero, gli utenti sono incoraggiati a considerare il fatto che l'attrazione principale delle criptovalute è essere la propria banca. Quando tieni in mano la tua chiave privata e se accade qualcosa, nessuno può aiutarti a recuperare i tuoi fondi persi.

Essere la tua banca significa considerare non solo la tua sicurezza digitale, ma anche la tua sicurezza fisica. Potrebbe benissimo essere che la conoscenza di un individuo che si connette alla rete Monero possa attirare attenzioni indesiderate, non necessariamente da parte di attori su larga scala come gli stati nazionali, ma quelli più piccoli con interessi egoistici, come gli hacker che cercano di guadagnare facilmente. Ci sono davvero innumerevoli storie in tutto lo spazio crittografico di tali scenari che si stanno effettivamente verificando.

Questo articolo non ha lo scopo di allarmare o spaventare, ma piuttosto incoraggiare gli utenti a fare qualche ricerca sui metodi di protezione della navigazione web più adatti a loro. La buona notizia è che queste competenze verranno trasferite anche all'utilizzo generale di Internet, non solo all'utilizzo di Monero, e come tale, nel nostro mondo sempre più connesso a Internet, un utente esperto non può sbagliare accumulando le conoscenze e le competenze adeguate per stare al sicuro ed essere veramente la loro banca.

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

  * [Come RingCT nasconde gli importi delle transazioni Monero](/knowledge/monero-ringct/)

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