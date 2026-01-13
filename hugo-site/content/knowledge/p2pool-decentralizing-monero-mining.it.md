---
title: "P2Pool e il suo ruolo nella decentralizzazione del mining di Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Uno degli obiettivi principali del progetto Monero è quello di abilitare una rete equa, decentralizzata e sicura attraverso approcci nuovi e innovativi al mining proof-of-work (PoW), il modo principale in cui le reti di criptovalute sono protette oggi.

Mentre un algoritmo di mining unico [come RandomX](/knowledge/monero-mining-randomx) è estremamente importante per questo scopo, poiché aiuta a garantire che chiunque abbia un computer possa contribuire in modo equo alla sicurezza della rete, RandomX non risolve i problemi che possono verificarsi a causa del pool mining. Il pool mining è di gran lunga il modo più comune per estrarre criptovalute oggi, compreso Monero, ma fortunatamente l'emergere del p2pool mining sta rapidamente cambiando la situazione.

## Cos'è il pool mining?

Il pool mining è un modo per i minatori di condividere il compito di tentare di risolvere un blocco sulla rete e quindi condividere le ricompense in modo uniforme per tutti i blocchi che il pool trova. Sebbene questo aiuti immensamente a uniformare la frequenza con cui i minatori vengono pagati rispetto al solo mining di Monero, non mancano seri problemi di centralizzazione.

Man mano che ogni minatore contribuisce con il lavoro al pool, rinuncia al controllo di qualsiasi lavoro svolto e blocca quello che trova nel pool stesso, confidando che il pool condividerà onestamente e equamente i premi tra tutti i minatori in base alla quantità di lavoro che ciascuno ha svolto. Se tutto va bene, l'operatore del pool raccoglie il lavoro da tutti i minatori, lo invia alla rete e condivide equamente le ricompense.

## Qual è il problema del pool mining?

Sfortunatamente, questo si basa interamente sulla fiducia e permette all'operatore del pool di fare cose nefaste con il lavoro svolto dai minatori. L'operatore del pool potrebbe usare il lavoro svolto per attaccare la rete, tentare di raddoppiare i fondi (se il pool è abbastanza grande), o semplicemente usare il lavoro svolto dai minatori per pagarsi e non ricompensare mai adeguatamente i minatori per il loro lavoro.

Il più grande rischio per la rete è quello di un pool (o più pool che lavorano insieme) che hanno più del 51% dell'hashrate della rete sotto il loro controllo, in quanto potrebbero usarlo per barare e spendere i fondi due volte (un attacco double-spend) o tentare di cambiare le regole della rete.

## Cos'è p2pool?

p2pool è un concetto che è stato originariamente creato per il mining di Bitcoin nel 2011, ma non ha mai visto un'ampia adozione e rimane praticamente inutilizzato su Bitcoin. Fortunatamente, uno degli sviluppatori chiave dietro RandomX, SChernykh, ha trascorso le sue vacanze trovando soluzioni ad alcuni dei problemi con l'implementazione Bitcoin di p2pool e riscrivendo tutto il software da zero.

p2pool in Monero permette un modo completamente privo di fiducia per i minatori di lavorare insieme per risolvere i blocchi e proteggere la rete Monero utilizzando un software speciale per i nodi p2pool al fine di condividere il lavoro.

Questo viene fatto usando una nuova blockchain (una "side-chain") che tiene un registro del lavoro che ogni minatore esegue, il suo indirizzo di portafoglio, e quanti Monero ha guadagnato, e poi paga la ricompensa in un modo decentralizzato e senza fiducia. Poiché questa catena secondaria ha molti meno minatori, è molto più facile trovare e inviare blocchi su di essa che sulla rete principale di Monero, rendendo più facile per i minatori ottenere pagamenti consistenti rispetto al solo mining di Monero.

## Come fa p2pool a risolvere i problemi del pool mining?

In p2pool, non c'è un pool centralizzato, un operatore di pool centralizzato, o una singola persona che tiene i fondi e distribuisce i pagamenti. Tutto il lavoro fatto collettivamente da coloro che fanno mining tramite p2pool è controllato dalla blockchain di p2pool e dagli altri operatori dei nodi per assicurarsi che sia legittimo, e tutti i minatori sono pagati in base al lavoro che hanno fatto immediatamente quando viene trovato un blocco direttamente dalle ricompense in quel blocco trovato.

Quando i minatori scelgono di usare p2pool invece di un pool centralizzato, rimuovono tutto il potere e la fiducia dagli operatori del pool e assicurano che il loro lavoro contribuisca al bene della rete e alle proprie ricompense, riducono il rischio di attacchi alla rete, l'uso improprio del loro lavoro o il furto delle ricompense che gli sono dovute.

Non solo questo li aiuta a proteggere i propri interessi, ma riduce il rischio che i pool centralizzati possono rappresentare per la rete Monero nel suo complesso. L'uso di p2pool aiuta anche immensamente a ridurre il rischio che gli Stati nazionali o le autorità di regolamentazione potrebbero rappresentare per la salute della rete, in quanto non ci sono operatori di pool centralizzati da mettere sotto pressione, nessuna concentrazione geografica di pool su cui appoggiarsi, o qualsiasi altro facile punto di pressione da utilizzare contro Monero.

## Quali sono gli svantaggi?

Fortunatamente p2pool in Monero è stato ben progettato e ben costruito, e funziona estremamente bene! Tuttavia, lo svantaggio principale del p2pool mining è che ogni minatore che vuole usare p2pool deve gestire il proprio nodo Monero, rendendo il processo di inizio un po' più complesso. Tuttavia, questo nodo è poi usato per calcolare tutte le informazioni necessarie per la costruzione e il controllo dei blocchi, e assicura che il minatore abbia il controllo completo del lavoro che sta facendo. Il nodo può anche funzionare come un nodo remoto per il portafoglio del minatore, contribuisce alla rete e molto altro.

L'altra differenza chiave rispetto al mining centralizzato è che i piccoli minatori che usano p2pool avranno un po' più "varianza", o tempo tra i pagamenti, rispetto ad un grande pool centralizzato - ma è's _estremamente_ importante notare che questo non porterà a guadagnare meno Monero nel tempo! p2pool sarà altrettanto redditizio per i piccoli minatori nel tempo quanto i pool centralizzati. Parte di questa variazione è anche compensata dal fatto che p2pool ha nativamente 0% di commissioni, dato che non c'è nessun operatore di pool centralizzato da pagare per i suoi servizi!

## Come posso iniziare?

Per fortuna, grazie all'eccellente progettazione dell'implementazione di p2pool di Monero'e alle molte persone nella community che hanno dedicato del tempo per aiutare a semplificare il processo di mining tramite p2pool, iniziare sta diventando più semplice nel tempo. Esistono diversi modi per iniziare a fare mining con p2pool, ma poiché i dettagli tecnici esulano dallo scopo di questo articolo, sentiti libero di accedere a un link di seguito a seconda del tuo sistema operativo:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Come posso saperne di più?

Se questo ha stuzzicato la tua curiosità sul p2pool mining, dai un'occhiata qui sotto per alcuni link aggiuntivi e spiegazioni su p2pool, come funziona e cosa significa per Monero:

  * [Il Github ufficiale di p2pool](https://github.com/SChernykh/p2pool)
  * [La documentazione ufficiale sull'uso di p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool è ora attivo](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, un "esploratore di blocchi" di sorta per p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Sul suo sviluppo di P2Pool un pool di estrazione XMR decentralizzato](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Ulteriori letture