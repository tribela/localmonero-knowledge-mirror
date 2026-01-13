---
title: "Firme ad anello di Monero vs CoinJoin come in Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Man mano che gli strumenti di privacy di Bitcoin hanno guadagnato più attenzione e utilizzo, sono stati sottoposti a un maggiore controllo normativo. Questo esame ha portato a un [recente annuncio](https://twitter.com/wasabiwallet/status/1503091503207432193) da uno strumento di privacy Bitcoin, Wasabi Wallet, che inizierà a censurare e rifiutare gli input in entrata ai mix che ritengono illeciti o contro i loro ToS, e pagherà una società di analisi della catena per "controllare" i partecipanti ai mix in entrata.

L'uso delle transazioni CoinJoin per offuscare la fonte dei fondi in Bitcoin è stato il nucleo della privacy di Bitcoin per molti anni, e i problemi e i rischi inerenti al suo uso sono alcuni dei problemi principali che le firme ad anello di Monero correggono e prevengono.

In questo post del blog ci immergeremo brevemente in un confronto tra CoinJoin e le firme ad anello, così come il motivo per cui l'approccio adottato in Monero porta ad una maggiore resistenza alla censura, maggiore privacy e meno problemi per gli utenti.

## Cos'è una transazione CoinJoin?

## Cos'è una transazione CoinJoin?

Poiché tutte le transazioni sono completamente trasparenti in Bitcoin - rivelando il mittente, il destinatario e gli importi - gli utenti devono prendere misure extra per preservare la loro privacy dai precedenti mittenti e dai futuri destinatari dei loro fondi o rischiare la censura, la sorveglianza o il furto di fondi tramite violenza fisica.

La migliore soluzione oggi per la privacy su Bitcoin è uno strumento chiamato ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/)dove 2 o più utenti lavorano insieme (di solito attraverso un coordinatore centralizzato) per creare una transazione speciale che rende difficile per gli osservatori esterni collegare gli ingressi con le uscite. Ogni partecipante comunica per costruire insieme la transazione senza cedere la custodia dei propri fondi, e riceve alla fine un output la cui storia precedente è ora poco chiara (o offuscata) agli osservatori esterni.

Questo rompe la storia di specifici UTXO, permettendo agli utenti di Bitcoin di ottenere un po' di segretezza in avanti durante le transazioni. Tuttavia, CoinJoin (come implementato in Wasabi Wallet e Samourai Wallet, i due strumenti CoinJoin più utilizzati per Bitcoin) ha alcuni svantaggi principali:

  * Poiché le transazioni CoinJoin sono completamente opt-in e richiedono una partecipazione attiva, ogni partecipante mostra necessariamente che cerca una maggiore privacy rispetto a quella degli utenti "normali" di Bitcoin, potenzialmente individuandoli e causando problemi a spendere fondi in molti scambi o entità regolamentate. Ogni utente non può negare di aver partecipato a una transazione CoinJoin.
  * Al fine di trovare altri con cui CoinJoin, la maggior parte degli approcci a CoinJoin (compreso Wasabi Wallet) utilizzano un coordinatore centralizzato che collega i partecipanti e li aiuta a comunicare e costruire una corretta transazione CoinJoin. Questo coordinatore centralizzato non ha mai la custodia dei fondi dell'utente, ma ottiene un'ampia visione delle transazioni che coordina, può censurare gli input in entrata (come nel caso di Wasabi Wallet), e può essere costretto a raccogliere o condividere informazioni sui partecipanti CoinJoin.
  * Gli utenti con grandi quantità di fondi da CoinJoin possono spesso dover aspettare ore (o anche giorni!) per trovare abbastanza partecipanti con cui CoinJoin, portando a grandi ritardi dal momento in cui un utente riceve i fondi a quando può spenderli privatamente.
  * La privacy fornita da una transazione CoinJoin si degrada nel tempo man mano che altri partecipanti spendono i fondi o collegano le loro uscite alla loro identità attraverso scambi KYC, commercianti che richiedono l'ID, ecc. Questo significa che gli utenti idealmente mantengono i loro fondi costantemente in movimento nelle transazioni CoinJoin per mantenere il loro set di anonimato ("folla in cui nascondersi") il più fresco possibile.
  * Nella maggior parte degli approcci a CoinJoin, i partecipanti devono usare un UTXO di dimensione fissa (cioè 0,1 BTC) per rendere più difficile collegare gli ingressi e le uscite delle transazioni CoinJoin. Questo porta a commissioni più elevate (più transazioni separate necessarie per un grande input), più "cambiamento tossico" (fondi che non sono spendibili senza gravi rischi per la privacy), e può impedire agli utenti più piccoli di essere in grado di mescolare affatto se non hanno il saldo minimo richiesto.

## Come fanno le firme ad anello a risolvere questi problemi?

## Come fanno le firme ad anello a risolvere questi problemi?

Come [abbiamo esaminato a fondo cosa sono le firme ad anello negli ultimi](/knowledge/ring-signatures), non entrerò in grandi dettagli sugli aspetti tecnici di come funzionano in questo post del blog. Invece, vedremo come gli approcci adottati in Monero risolvono i problemi con CoinJoin discussi sopra.

> CoinJoin è opt-in e richiede la partecipazione

CoinJoin è opt-in e richiede la partecipazione

le firme ad anello di Monero sono una caratteristica fondamentale del protocollo di privacy e _ogni transazione_ sulla rete le utilizza. Ciò significa che nessuna transazione dell'utente si distingue per la ricerca di una maggiore privacy rispetto ai "normali" utenti Monero e tutti gli utenti ottengono una negazione plausibile che hanno speso fondi in una determinata transazione. Poiché un utente che spende fondi non si coordina o non partecipa con gli input esca in una transazione, quegli utenti che possiedono input che vengono selezionati come esca possono onestamente dire che non stavano partecipando a quella transazione, rafforzando la loro privacy.

> Uso di un coordinatore centralizzato

Uso di un coordinatore centralizzato

Poiché le firme ad anello di Monero sono completamente non coordinate e richiedono solo il vero spender di fondi per creare la transazione, non è necessario un coordinatore centralizzato in Monero. Ciò garantisce che _nessuno_ possa negarti l'accesso alla privacy in Monero, e non esiste un'entità centralizzata che possa essere messa sotto pressione, nessun facile attacco Sybil alla liquidità, ecc. Finché la tua transazione paga le commissioni appropriate, ottieni un accesso non censurabile alla privacy, alla sicurezza e all'anonimato in Monero.

> CoinJoin richiede liquidità

CoinJoin richiede liquidità

La "liquidità" disponibile per chiunque spenda Monero da utilizzare come esca è sempre l'insieme totale di output on-chain, quindi non c'è mai carenza di esche per nascondersi con Monero. Qualcuno che cerca di spendere Monero può farlo ~ 20 minuti dopo aver ricevuto fondi e non ha bisogno di eseguire ulteriori passaggi per ottenere una forte privacy in Monero.

> la privacy di CoinJoin degrada nel tempo

la privacy di CoinJoin degrada nel tempo

Poiché gli output di Monero non sono mai noti e spesi dalla rete, la privacy fornita dalle firme ad anello è molto meno suscettibile al degrado nel tempo. Un utente non ha bisogno di sfornare costantemente output in Monero e, al di fuori di circostanze estremamente rare, non perde privacy con il passare del tempo.

Se un utente vuole "aggiornare" le esche utilizzate con un output, tuttavia, può semplicemente inviare i fondi a se stesso ed essere in grado di spenderli ~ 20 minuti dopo come al solito.

> CoinJoin di solito richiede input di dimensioni fisse

CoinJoin di solito richiede input di dimensioni fisse

Poiché gli importi sono nascosti in ogni transazione utilizzando [](/knowledge/monero-ringct) "Transazioni riservate" (una parte di "RingCT"), le esche utilizzate in una determinata transazione possono essere di qualsiasi dimensione. Non c'è motivo di doversi preoccupare dell'euristica basata sulla quantità in Monero, e quindi le transazioni sono molto più semplici da costruire e possono sfruttare le esche da qualsiasi momento e di qualsiasi importo sulla blockchain di Monero.

## Come posso saperne di più?

## Come posso saperne di più?

Se sei curioso e vuoi capire meglio le firme ad anello o le transazioni CoinJoin, guarda i link qui sotto per i posti migliori per iniziare:

  * [Come le firme ad anello oscurano gli output di Monero](/knowledge/ring-signatures)
  * [Firma ad anello - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Panoramica su CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Ulteriori letture

  * [Come Monero abilita in modo unico le economie circolari](/knowledge/monero-circular-economies)/

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

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx)/

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better)/

Ulteriori letture