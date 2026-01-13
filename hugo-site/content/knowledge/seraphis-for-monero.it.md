---
title: "Seraphis: Cosa farà per Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: un aggiornamento del design modulare per le transazioni di Monero

Questo post descrive [Seraphis](https://github.com/UkoeHB/Seraphis), un insieme di strutture e astrazioni del protocollo delle transazioni sviluppato da un collaboratore di ricerca pseudonimo [`koe`](https://github.com/UkoeHB) per l'ecosistema Monero, e con un'analisi di sicurezza in corso da parte dello pseudonimo [`coinstudent2048`](https://github.com/coinstudent2048).  
Facciamo alcune semplificazioni e omettiamo alcuni dettagli tecnici per motivi di chiarezza; per questo motivo, e perché la progettazione di Seraphis è ancora in corso, i lettori interessati dovrebbero fare riferimento alla documentazione di Seraphis per le informazioni più aggiornate.

## Transazioni in Monero

Protocolli come Bitcoin e Monero e altri si basano su un cosiddetto "modello di output" di funzionamento, dove un _output_ è una rappresentazione di valore che può essere trasferito.  
Le transazioni consumano uno o più output controllati da un mittente, e generano nuovi output diretti ai destinatari (o indietro al mittente come cambiamento); la transazione deve bilanciare in quanto gli output consumati devono contenere un valore totale esattamente uguale al valore dei nuovi output (più una tassa imposta dalla rete).  
In molti protocolli come Bitcoin, il valore contenuto in un output è scritto in chiaro, così come il destinatario.  
Inoltre, guardando la blockchain, è banale vedere se e quando un output è stato speso (cioè, se è stato consumato in una transazione successiva, e quale transazione lo ha speso).

Al contrario, protocolli come Monero introducono un design diverso:

  * I valori di uscita sono nascosti e non visibili sulla blockchain
  * Gli indirizzi dei destinatari sono nascosti dall'uso di un protocollo di indirizzamento una tantum
  * Se un output è stato speso o meno è oscurato dall'uso di firme ambigue

Il risultato è che, in assenza di informazioni esterne, è difficile determinare se un dato output è stato speso, qual è il suo valore e chi è il suo destinatario.

L'attuale protocollo di transazione di Monero è chiamato _RingCT_ e utilizza diversi blocchi crittografici per raggiungere questi obiettivi di progettazione.

  * _Impegni_ nascondono somme in un modo matematicamente utile
  * _Range proofs_ impediscono l'overflow che potrebbe gonfiare l'offerta
  * _Le firme ad anello collegabili_ forniscono ambiguità al firmatario e prevengono i tentativi di doppia spesa
  * _Le compensazioni di impegno_ affermano che le transazioni bilanciano

Questi blocchi sono accuratamente intrecciati per costruire il protocollo RingCT.

Un'utile proprietà del protocollo RingCT è che alcuni blocchi possono essere cambiati o aggiornati in modo da mantenere intatto il design e le proprietà generali, ma che possono fornire miglioramenti di efficienza o sicurezza. Infatti, questo tipo di aggiornamenti si sono verificati (o sono previsti) diverse volte nella storia di Monero. Le prove di portata nel protocollo RingCT originale erano ingombranti e lente; sono state successivamente aggiornate ad una costruzione chiamata [Bulletproofs](https://eprint.iacr.org/2017/1066) che ha reso le transazioni più piccole e veloci con una migliore analisi di sicurezza, e si prevede di aggiornarle con una costruzione più recente chiamata [Bulletproofs+](https://eprint.iacr.org/2020/735) per benefici di efficienza ancora maggiori.

Un processo simile è stato subito con il blocco di costruzione della firma ad anello collegabile. Nel protocollo originale, una costruzione chiamata [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) . Questa è stata successivamente aggiornata ad una costruzione più recente chiamata [CLSAG](https://eprint.iacr.org/2019/654) che è più veloce, risulta in transazioni più piccole e ha una migliore analisi di sicurezza. Una costruzione di firma ad anello ancora più recente, basata su [Triptych](https://eprint.iacr.org/2020/018) è stata proposta, ma non è stata scelta per l'implementazione a causa del suo impatto sulle operazioni con più firme.

## Seraphis

Seraphis fa un ulteriore passo avanti con questa idea.  
Anziché aggiornare i singoli elementi costitutivi del protocollo di transazione RingCT esistente, introduce un protocollo diverso che può trarre vantaggio da diversi elementi costitutivi e offrire funzionalità migliorate.

## Blocchi di costruzione

Seraphis utilizza un diverso insieme di blocchi di costruzione crittografici per raggiungere i suoi obiettivi di progettazione.

  * _Gli impegni_ nascondono ancora gli importi
  * _Le prove di intervallo_ impediscono ancora l'overflow e l'inflazione dell'offerta
  * _Le prove di appartenenza_ forniscono ambiguità al firmatario
  * _Le compensazioni di impegno_ affermano ancora l'equilibrio
  * _Autorizzare le prove_ prevenire i tentativi di doppia spesa

Notate il cambiamento qui: le firme ad anello collegabili sono sostituite da una combinazione di prove di appartenenza e prove di autorizzazione. In parole povere, le prove di appartenenza mostrano che un'uscita consumata fa parte di un insieme più grande, in modo simile a quanto accade in RingCT. Ma a differenza di RingCT, le prove di appartenenza non coinvolgono affatto il tag di collegamento! Le prove di autorizzazione mostrano che il tag di collegamento è valido e sono usate per firmare la transazione finale.

Poiché RingCT inserisce il tag di collegamento nella firma ambigua, le operazioni di firma (e multisignature) sono più impegnative dal punto di vista computazionale, e diventa più difficile costruire altre funzionalità relative ai tag. Ma in Seraphis, la costruzione delle prove di appartenenza può essere tranquillamente delegata da dispositivi altamente fidati (che possono avere una potenza di calcolo limitata, come un portafoglio hardware) a un dispositivo meno fidato, e le operazioni di firma (e multisignature) sono molto più semplici utilizzando la prova di autorizzazione molto più semplice.

Fortunatamente, alcuni dei blocchi di costruzione richiesti da Seraphis esistono già altrove, e non hanno bisogno di essere progettati da zero. Sia le costruzioni Bulletproofs che Bulletproofs+ possono essere usate come prove di range. Le modifiche ai sistemi di prova di tipo Schnorr possono essere usate per autorizzare le prove. E un efficiente sistema dimostrativo [](https://eprint.iacr.org/2015/643) usato già come base per Triptych, [Lelantus](https://eprint.iacr.org/2019/373)e [Spark](https://eprint.iacr.org/2021/1173)* può essere modificato per le prove di appartenenza.

* Cypher Stack riceve finanziamenti per lo sviluppo di Spark.

## Affrontare

Sfortunatamente, gli indirizzi Monero attualmente in uso non sono compatibili con Seraphis. Gli utenti avrebbero bisogno di generare nuovi indirizzi dalle chiavi dei loro portafogli per ricevere Monero se Seraphis fosse implementato. Tuttavia, questo costo di ecosistema è accompagnato da una serie di vantaggi.

A parte i benefici strutturali discussi sopra, il design di Seraphis è adatto a diverse possibilità di costruzione degli indirizzi, ognuna delle quali ha dei compromessi. Mentre la costruzione finale dell'indirizzo da usare in Seraphis è [ancora in fase di decisione](https://github.com/monero-project/research-lab/issues/92) (uno schema che sta ricevendo molta attenzione è chiamato [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), possiamo descrivere alcune caratteristiche comuni e utili.

Potresti sapere che gli indirizzi Monero offrono _la funzionalità view key_ , dove puoi fornire una view key a un dispositivo o a una terza parte e permettergli di guardare le uscite in entrata per tuo conto, ma senza rinunciare all'autorità di spesa. Questo è utile per i portafogli, che possono rimanere aggiornati mantenendo la chiave di spesa al sicuro. È anche utile per i casi in cui si desidera l'accesso di vista esterno, come un ente di beneficenza pubblico che offre trasparenza o una società con un reparto di contabilità.

L'aspetto negativo delle chiavi di vista Monero è che non forniscono un accesso completo o a grana fine alla vista. Non è possibile rilevare in modo affidabile quando un portafoglio spende fondi, il che rende difficile calcolare correttamente i bilanci del portafoglio quando la chiave di spesa non è disponibile. Al momento non è nemmeno possibile rilevare le uscite in entrata senza conoscere anche il valore contenuto in tali uscite (il che significa che qualsiasi terza parte responsabile di trovare le uscite in entrata apprenderà esattamente quanto Monero si sta acquisendo).

Le costruzioni di indirizzamento di Seraphis possono risolvere questo problema. Con Seraphis, il tuo indirizzo è dotato di diversi tasti che possono fare cose diverse:

  * Osservare le uscite in arrivo, ma nascondere il loro valore
  * Guarda le uscite in arrivo, ma mostra il loro valore
  * Controlla le uscite in uscita
  * Aiuta a generare transazioni, ma non le firma
  * Generare nuovi indirizzi (utile per rivenditori o scambi con molti clienti)

Come titolare dell'indirizzo, puoi decidere quanta autorità delegare ad altri dispositivi o a terzi.

## Il quadro generale

Seraphis è un cambiamento importante per l'ecosistema Monero. Anche se comporta modifiche agli indirizzi e ai blocchi di costruzione delle transazioni, il suo design offre flessibilità e funzionalità utili che non sono possibili con l'attuale protocollo RingCT. Mentre gran parte del design è stato finalizzato e sviluppato in [un'implementazione](https://github.com/UkoeHB/monero/tree/seraphis_lib), il design degli indirizzi e l'analisi della sicurezza sono in corso. Seraphis offre un'eccellente opportunità per spingere in avanti l'ecosistema Monero!

Ulteriori letture