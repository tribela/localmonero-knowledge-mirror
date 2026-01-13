---
title: "In che modo i sottoindirizzo Monero impediscono il collegamento di identità"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ha sempre trovato modi innovativi per risolvere difficili problemi di privacy. Spesso queste innovazioni portano ad altre innovazioni, e talvolta queste tecnologie risultanti possono essere utilizzate anche per casi d'uso non considerati in precedenza. Da nessuna parte questo è esemplificato più che nel caso della tecnologia di sottoindirizzo di Monero.

Considera un ipotetico problema di privacy, in cui l'utilizzo di un indirizzo su più piattaforme da persone apparentemente non correlate può portare al collegamento e alla deanonimizzazione di tali persone. In parole povere, se tu fossi una persona di nome Billy Joe Bob e vendessi mele per Bitcoin, potresti pubblicare il tuo indirizzo Bitcoin in un luogo pubblico affinché i clienti ti paghino. Diciamo che l'indirizzo inizia con la stringa alfanumerica 7XybV3 ... Ma mettendo da parte l'evidente rischio per la privacy che chiunque possa controllare il tuo saldo Bitcoin e vedere quanto hai venduto, c'è un secondo, non spesso parlato di rischio per la privacy. Supponiamo che tu fossi anche un hacker clandestino con il nome di l33tz0r. Fai il lavoro di denuncia, raccontando a una popolazione ignara della corruzione del governo, ed è imperativo che tu mantenga segreta la tua identità. Accetti donazioni di Bitcoin per il tuo lavoro e pubblichi l'indirizzo su un forum pubblico. È lo stesso indirizzo a cui accetti denaro dai tuoi clienti Apple. Il 7XybV3 ... uno.

Un semplice, ma devastante attacco di deanonimizzazione consiste nell'utilizzare un motore di ricerca su Internet per cercare il tuo indirizzo Bitcoin. Inserendo l'indirizzo di 7XybV3 ... nel motore si ottengono due risultati diversi. Il business delle mele e l33tz0r. Questo è sufficiente per collegare le due identità e deanonimizzare l33tz0r, con conseguenze potenzialmente spaventose dai poteri forti.

È importante notare che questo attacco è possibile ANCHE con Monero. Anche se Monero nasconde la maggior parte dei dati on-chain, questo attacco non ne utilizza nessuno. Utilizza solo l'indirizzo, che deve essere condiviso per ricevere il pagamento. Pubblicamente in caso di donazioni anonime. Questo è un potenziale modo in cui gli utenti Monero possono danneggiare involontariamente la loro privacy ed è anche un esempio di come, anche se Monero è di alto livello per quanto riguarda la conservazione della privacy, non è a prova di proiettile.

Il modo usuale per aggirare questo problema era possedere più portafogli. Con diversi indirizzi pubblicati per ogni identità (o caso d'uso), non possono essere collegati. Ma questa privacy vale solo se l'utente non le confonde mai. La pubblicazione accidentale di un indirizzo errato avrebbe gli stessi effetti di collegamento. Inoltre, il seed di ogni indirizzo deve essere mantenuto al sicuro, aumentando il lavoro di infosec necessario con ogni nuovo wallet realizzato.

La soluzione di Monero erano gli indirizzi secondari. La possibilità di creare un numero assolutamente enorme di indirizzi sotto l'indirizzo principale, utilizzandolo come una sorta di seme. Ogni sottoindirizzo generato può accettare Monero e tutto va allo stesso portafoglio. Utilizzando questo metodo, il numero di identità che possono essere utilizzate con un indirizzo è enorme, mantenendo al minimo il lavoro di infosec. Questi indirizzi non sono nemmeno collegabili matematicamente, quindi a meno che l'utente non gridi la loro connessione al mondo, un osservatore esterno avrà grandi difficoltà a collegarli.

Ma un altro caso d'uso interessante è emerso dai sottoindirizzo; come opzione sostitutiva degli ID di pagamento universalmente odiati.

Gli ID pagamento erano un modo per i commercianti di identificare quale cliente aveva inviato quale pagamento. Poiché le informazioni di Monero sono oscurate sulla catena, il destinatario di una transazione non è in grado di vedere quale indirizzo l'ha inviata. Ciò significa che se ci sono articoli con prezzi simili e più ordini, può diventare impossibile identificare chi ha inviato cosa. Gli ID pagamento sono una stringa univoca e casuale generata dal commerciante e fornita al cliente. Il cliente lo aggiunge come campo separato quando invia la transazione. Questa stringa casuale viene inserita sulla blockchain come parte della transazione e in questo modo il commerciante è in grado di identificare e ordinare le transazioni in entrata.

Questo metodo era difettoso in diversi modi. In primo luogo, sminuisce l'uniformità dei dati on-chain. Metadati aggiuntivi e univoci possono far distinguere alcune transazioni dalla massa, consentendo così un'analisi euristica. Ciò è particolarmente vero quando questi metadati non vengono applicati come obbligatori per tutti. Renderlo obbligatorio per tutti aggiungerebbe spazio inutile alla blockchain e non è stato perseguito. Inoltre, se un ID pagamento fosse mai riutilizzato per qualsiasi motivo, sarebbe banale collegare due transazioni come connesse. Ciò si verificava in genere con i depositi in borsa e chiunque poteva facilmente collegare le transazioni sia come deposito su uno scambio, sia da un particolare individuo.

In secondo luogo, da una prospettiva UX, gli ID di pagamento creano un secondo passaggio a cui non sono abituati gli utenti di criptovaluta provenienti da altre monete e, se vengono dimenticati, provoca un enorme mal di testa al commerciante che deve identificare queste transazioni con altri mezzi . Questo in genere veniva fatto parlando direttamente con ogni cliente che aveva dimenticato di inserire l'ID pagamento e confermando altre informazioni identificative che solo loro potevano conoscere, come una combinazione di importo, data di invio e ID transazione.

Questo passaggio aggiuntivo è stato ignorato da molti ed è arrivato al punto in cui alcuni scambi hanno iniziato ad addebitare denaro ai clienti se i loro soldi dovevano essere recuperati manualmente a causa della dimenticanza di un ID di pagamento. Altri stringevano i denti e mangiavano i costi di supporto extra, ma nessuno ne era contento.

C'era una soluzione a questo, indirizzi integrati, che univano l'indirizzo e l'ID pagamento in un'unica stringa, quindi non poteva essere dimenticato, ma l'adozione era piuttosto debole, nonostante i vantaggi che i commercianti avrebbero ricevuto dall'inclusione.

In un'interessante svolta degli eventi, sono entrati dei sottoindirizzo per salvare la situazione. La capacità di generare grandi quantità di sottoindirizzo per indirizzo principale e di identificare quali transazioni sono entrate in quali sottoindirizzo, ha permesso ai commercianti di sbarazzarsi degli ID di pagamento in modo elegante, adottando la tecnologia Monero di nuova generazione. Da allora, la maggior parte degli scambi e degli strumenti mercantili sono passati agli indirizzi secondari come metodo principale di identificazione delle transazioni.

Ciò che era iniziato come una soluzione a un problema di privacy si è trasformato in qualcosa di molto di più, che ha risolto un importante problema di UX per commercianti e clienti. L'innovazione genera più innovazione, che spesso può portare a vittorie inaspettate per tutti. Monero lo ha visto più e più volte e si impegna a innovare ciò che è possibile sulla blockchain. Chissà quali altre cose possiamo sbloccare insieme?

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