---
title: "Come Monero ha risolto il problema delle dimensioni del blocco che affligge Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Nota:** Si consiglia vivamente al lettore di leggere i nostri articoli ["Perché Monero ha un'emissione di coda"](/knowledge/monero-tail-emission) e ["Monero Mining: What Makes RandomX così speciale”](/knowledge/monero-mining-randomx). Questo articolo si basa sui concetti qui presentati._

Ogni volta che le persone discutono dei problemi con la blockchain, una delle prime parole a comparire sarà "dimensionamento". Non è un segreto che le blockchain non si adattino bene, ma la maggior parte delle persone non sa perché.

La verità è che il ridimensionamento è in realtà un termine generico che copre due diverse categorie: supporto del protocollo e supporto tecnologico in un dato momento. In questo articolo concentreremo la nostra attenzione su uno: il supporto del protocollo è fondamentalmente una misura di quante transazioni il protocollo può gestire in un dato momento.

Bitcoin ha un limite alla dimensione del blocco, il che significa che una volta incluse un numero sufficiente di transazioni in un blocco, eventuali transazioni aggiuntive dovranno attendere in linea per il blocco successivo. Un’analogia utile potrebbe essere pensare a un treno. Un treno si ferma alla stazione e quelli in fila entrano. Una volta che il treno è pieno, chiunque sia rimasto fuori dovrà aspettare il successivo.

Bitcoin utilizza le commissioni per determinare chi entra o meno nel blocco. Tornando all'analogia del treno, si può immaginare che un potenziale passeggero, che sta per essere lasciato indietro, offra al macchinista cinque dollari per dargli un posto. Altri passeggeri seguono l'esempio e alla fine scoppia una guerra di offerte per vedere chi ottiene quali posti. Spetta all'autista decidere se vuole onorare la politica "primo arrivato, primo servito", ma è nel suo miglior interesse finanziario massimizzare il suo reddito accettando a bordo i migliori offerenti.

In questa analogia, i minatori sono i macchinisti. Possono includere qualunque transazione vogliano nel blocco, ma generalmente sceglieranno quelle che hanno le commissioni pagate più alte.

In alternativa, se i blocchi non sono molto pieni, le persone non hanno alcun incentivo a pagare tariffe elevate perché ci sono molti posti liberi da riservare.

Al culmine del boom delle criptovalute del 2017, Bitcoin è stato inondato di transazioni e le commissioni sono salite alle stelle per coloro che volevano essere inclusi nel blocco successivo, o in qualsiasi blocco del prossimo futuro. Coloro che non erano disposti a pagare commissioni elevate hanno visto le loro transazioni rinviate per ore, giorni o addirittura eliminate del tutto dalla coda.

Questa è stata una visione straziante di come se la sarebbe cavata Bitcoin se si fosse verificata la tanto citata "adozione di massa". Se Bitcoin dovesse essere utilizzato dalle masse, le cose andrebbero ancora peggio che nel 2017, e Bitcoin sarebbe inaccessibile a chiunque tranne che ai ricchi, semplicemente perché il throughput è piccolo a causa della dimensione fissa dei blocchi, facendo sì che il mercato delle commissioni prenda il sopravvento. .

Monero lo aveva previsto e voleva fare qualcosa di diverso. Quindi gli sviluppatori di Monero hanno implementato una dimensione di blocco dinamica.

Fondamentalmente, Monero ha anche un limite massimo alle dimensioni dei blocchi, ma è un limite morbido. Quando la fila delle transazioni in attesa diventa troppo lunga, i minatori possono aumentare la dimensione dei blocchi. Con la nostra analogia con il treno, puoi immaginare di aggiungere più vagoni ferroviari per accogliere i passeggeri in più. Dopo che la coda è vuota, i blocchi ritornano alla loro dimensione originale da ora in poi.

Se sembra un'idea interessante, sembra ragionevole chiedersi perché Monero è l'unica criptovaluta ad averlo implementato. Perché non aggiungerlo su Bitcoin in modo da porre fine ai problemi di throughput?

Purtroppo questo non è possibile. Esistono diversi motivi e faremo del nostro meglio per spiegarli.

È sempre nell'interesse del minatore avere blocchi di grandi dimensioni. Con blocchi di grandi dimensioni possono adattarsi a più transazioni e guadagnare di più dalle commissioni, nonché dai premi dei blocchi. Ciò può potenzialmente portare ad attacchi di spam, in cui qualcuno invia molte piccole transazioni, con piccole commissioni, per gonfiare la catena. I minatori aumenterebbero semplicemente la dimensione dei blocchi includendoli tutti perché il denaro è denaro, non importa quanto piccolo. Ciò porterebbe a blocchi costantemente grandi con scarsi vantaggi economici. Bitcoin risolve questo problema limitando artificialmente la dimensione del blocco, generando così un mercato delle commissioni. Gli aggressori di spam dovrebbero pagare più degli altri utenti in commissioni, e questo non è più economico. Ma questo significa che i blocchi si riempiono lasciando alcune transazioni in attesa come menzionato sopra.

Allora come può Monero avere dimensioni di blocco dinamiche ed evitare attacchi di spam? La risposta è semplice, ma intelligente. Viene introdotta una penalità sulla ricompensa del blocco quando un blocco è più grande del normale. Se un minatore desidera aumentare la dimensione del blocco, la ricompensa che otterrà trovando quel blocco sarà inferiore a quella che riceverebbe altrimenti. Quindi aumenteranno la dimensione del blocco solo quando le commissioni di transazione pagate dagli utenti supereranno la parte persa della ricompensa del blocco. Ad esempio, se il minatore perdesse 0,5 XMR aumentando la dimensione del blocco e la somma delle commissioni di transazione pagate fosse 0,4 XMR, allora ci sarebbe una perdita netta di 0,1 XMR se aumentasse la dimensione, quindi non farebbero non farlo. Al contrario, se le commissioni di transazione totali ammontassero a 0,7 XMR, allora ci sarebbe un guadagno netto di 0,2 XMR, anche se perdono 0,5 XMR dalla penalità di ricompensa del blocco, quindi il minatore aumenterà le dimensioni.

Questi blocchi dinamici consentono alla rete di crescere organicamente, senza limitare artificialmente la dimensione del blocco per creare un mercato a tariffa forzata, evitando comunque attacchi di spam. Ci sono molti altri punti di vista da cui possiamo vedere questa idea, e più ragioni per cui non sarebbe possibile aggiungerla a Bitcoin, ma per ora, speriamo che il lettore abbia una comprensione di come Monero elude molti dei problemi di Bitcoin e Bitcoin. i suoi derivati e come prevede di ampliare la propria produttività in futuro.

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

  * [Come RingCT nasconde gli importi delle transazioni Monero](/knowledge/monero-ringct/)

  * [In che modo gli indirizzi Monero Stealth proteggono la tua identità](/knowledge/monero-stealth-addresses/)

  * [In che modo i sottoindirizzo Monero impediscono il collegamento di identità](/knowledge/monero-subaddresses/)

  * [Spiegazione dei risultati di Monero](/knowledge/monero-outputs/)

  * [Migliori pratiche Monero per principianti](/knowledge/monero-best-practices/)

  * [Come le firme ad anello oscurano i risultati di Monero](/knowledge/ring-signatures/)

  * [In che modo CLSAG migliorerà l'efficienza di Monero](/knowledge/what-is-clsag/)

  * [Perché Monero ha un'emissione di coda](/knowledge/monero-tail-emission/)

  * [La storia di Monero](/knowledge/monero-history/)

  * [Wired Magazine ha sbagliato su Monero, ecco perché](/knowledge/wired-article-debunked/)

  * [Top 15 Miti e preoccupazioni Monero debunked](/knowledge/monero-myths-debunked/)

  * [Come Dandelion ++ mantiene private le origini delle transazioni di Monero](/knowledge/monero-dandelion/)

  * [Perché Monero è open source e decentralizzato](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx/)

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better/)