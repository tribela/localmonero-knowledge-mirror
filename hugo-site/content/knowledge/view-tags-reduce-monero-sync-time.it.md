---
title: "Visualizza i tag: Come un byte ridurrà i tempi di sincronizzazione del portafoglio Monero del 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Una delle lamentele più comuni riguardo all'uso quotidiano di Monero è il tempo che ci può volere per sincronizzare un portafoglio prima di essere in grado di inviare Monero. Fortunatamente, gli sviluppatori e i ricercatori della comunità Monero hanno trovato un modo brillante per ridurre il tempo necessario per sincronizzare il tuo portafoglio del 40% e oltre, senza alcun blocco aggiuntivo, tasse, ecc.

Inserisci i "tag di visualizzazione", un'aggiunta di un byte ai dati di ogni transazione - in arrivo su Monero nel prossimo aggiornamento della rete!

## Perché la sincronizzazione del portafoglio di Monero è più lenta di quella di Bitcoin?

Una delle prime domande a cui dobbiamo rispondere per capire meglio la necessità di una soluzione come i tag view è perché la sincronizzazione del portafoglio di Monero è più lenta delle criptovalute come Bitcoin.

In Bitcoin, poiché tutte le transazioni non sono private e rivelano le monete che vengono spese, gli importi e gli indirizzi coinvolti sulla catena, i portafogli Bitcoin possono semplicemente cercare qualsiasi uscita di transazione non spesa (UTXOs) o indirizzi usati per un dato portafoglio, scansionando rapidamente la blockchain per solo UTXOs posseduti da quegli indirizzi per capire quali monete appartengono al tuo portafoglio e possono essere spese.

In Monero, tuttavia, tutte le transazioni preservano la privacy dell'utente nascondendo il mittente, il destinatario e gli importi coinvolti in ogni transazione. Questa privacy, sebbene sia vitale per proteggere gli utenti della rete, introduce anche una sincronizzazione del portafoglio più lenta. In Monero, il tuo portafoglio deve confrontare ogni uscita di transazione (TXO) che esiste sulla rete con le chiavi private del tuo portafoglio.

Questo confronto comporta un sacco di matematica complessa e crittografia per convalidare che un output è veramente tuo, dal momento che tutti gli importi, gli indirizzi, e gli output (o monete) spesi conosciuti sono nascosti sulla catena in Monero.

## Cosa sono i tag di visualizzazione?

Come un modo per aiutare a ridurre il tempo di sincronizzazione per i portafogli Monero, [un ricercatore chiamato UkoeHB ha proposto un nuovo approccio](https://github.com/monero-project/research-lab/issues/73) \- aggiungere un "tag" di 1 byte ad ogni transazione utilizzando un segreto condiviso noto solo al mittente e al destinatario di quella transazione.

Questo segreto condiviso è generato dal mittente utilizzando l'indirizzo fornito dal destinatario, e non richiede alcuna collaborazione attiva da parte del mittente e del destinatario. Il primo byte (o carattere) di questo segreto condiviso viene aggiunto ai dati della transazione quando viene pubblicata sulla rete Monero.

Quando uno dei partecipanti a quella transazione vuole sincronizzare il proprio portafoglio con la blockchain di Monero, invece di dover eseguire tutta la complessa matematica e crittografia per ogni singolo TXO sulla rete, il portafoglio può ora semplicemente controllare quel campo di 1 byte in ogni transazione e solo allora eseguire la verifica che richiede tempo sulle transazioni che hanno quel tag - 1/256 TXO sulla rete, per essere precisi!

Questo tag non rivela alcuna informazione sulla transazione agli osservatori esterni, aggiunge solo 1 byte (una quantità trascurabile) alle dimensioni della transazione, e tuttavia ci permette di ridurre i tempi di sincronizzazione del 40%+ riducendo le complesse verifiche necessarie!

## Visualizza i tag: un esempio semplificato

Immagina di avere 4096 scatole in una stanza, di cui solo 5 scatole ti appartengono. Le scatole sono tutte del tutto indistinguibili dall'esterno e l'unico modo per sapere se una scatola fa per te è aprirla e risolvere un problema di matematica che richiede tempo e annotato all'interno per assicurarti che sia tuo.

Ora, immagina di decidere che la persona che ti ha inviato quelle 5 caselle generi un codice speciale usando il tuo indirizzo, e poi metta solo il primo carattere di quel codice generato all'esterno di ogni casella che ti viene inviata. Tutti gli altri fanno la stessa cosa per le loro scatole (per garantire che tutte le scatole siano ancora indistinguibili), ma ora puoi semplicemente guardare il codice di un carattere all'esterno della scatola e aprire solo quelle scatole che hanno quel carattere su di esse.

Mentre altre caselle corrisponderanno al tuo codice, anche alcune che non sono di tua proprietà, il numero di caselle che devi aprire e risolvere un problema di matematica ora è solo 16 (1/256 caselle!) invece di tutti 4.096.

Ora apri quelle 16 caselle, risolvi i problemi di matematica e mantieni le 5 caselle che effettivamente ti appartengono di quel gruppo!

## Quando saranno disponibili i tag di visualizzazione in Monero?

I tag di visualizzazione sono una delle caratteristiche attualmente previste per l'inclusione nel [prossimo aggiornamento della rete](https://github.com/monero-project/meta/issues/630)e dovrebbe essere rilasciata in primavera. La comunità [ha raccolto 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (al momento della scrittura) per incentivare lo sviluppo e l'implementazione dei view tag, e di conseguenza la maggior parte del lavoro per includere i view tag nel codice base di Monero è già stato completato da j-berman in collaborazione con revisori e ricercatori.

Una volta che le etichette di visualizzazione saranno applicate dalla rete, tutte le transazioni inviate dopo l'aggiornamento della rete beneficeranno del tempo di sincronizzazione del portafoglio drasticamente migliorato. Non avrai bisogno di fare nulla di speciale per iniziare a usare i view tag, il tuo portafoglio preferito per Monero inizierà semplicemente a usarli dopo l'aggiornamento della rete automaticamente!

## Come posso saperne di più?

Se questo ha stuzzicato la vostra curiosità sui tag di visualizzazione, date un'occhiata qui sotto per alcuni link aggiuntivi che approfondiscono l'argomento:

  * [Ridurre i tempi di scansione con "view tag" da 1 byte per uscita](https://github.com/monero-project/research-lab/issues/73)
  * [Aggiungere tag di visualizzazione alle uscite per ridurre il tempo di scansione del portafoglio](https://github.com/monero-project/monero/pull/8061)

Ulteriori letture