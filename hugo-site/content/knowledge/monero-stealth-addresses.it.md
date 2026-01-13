---
title: "In che modo gli indirizzi Monero Stealth proteggono la tua identità"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero ha implementato un approccio alla privacy su tre fronti. Queste tecnologie sono [firme ad anello](/knowledge/ring-signatures), che nascondono il vero output (mittente), RingCT che nasconde gli importi e indirizzi invisibili, che nasconde il destinatario. Oggi discuteremo dell'ultima di queste tecnologie menzionate: indirizzi stealth.

Ci sono molti motivi per cui una persona potrebbe voler nascondere a chi sta inviando. Non dobbiamo mai permettere a nessuno di provare a convincerci che tutti gli esempi di ciò sono comportamenti sgradevoli. Cose come inviare a un partito politico impopolare, donare a enti di beneficenza o sostenere quelli che la cultura ritiene 'cancellati' sono tutti esempi di dove si potrebbe voler nascondere i propri comportamenti di spesa per timore di ripercussioni, ma sono di natura perfettamente legittima.

Su una blockchain trasparente, gli indirizzi a cui si inviano le transazioni sono visibili a tutti. È importante considerare che se i minatori stessi non sono d'accordo con dove sta andando il denaro, possono scegliere di non estrarlo in un blocco, censurando efficacemente questa transazione su una piattaforma apparentemente resistente alla censura. L'unico modo per rendere questa censura, certamente improbabile, non possibile è se i minatori non sono in grado di distinguere tra le transazioni perché tutti i metadati on-chain sono oscurati con vari mezzi. Qualcosa per cui Monero è noto.

Monero risolve questo problema di indirizzi trasparenti implementando indirizzi stealth, una tecnologia che in realtà è stata inizialmente realizzata per Bitcoin nel 2011 dall'utente del forum Bitcoin Talk ByteCoin (la relazione con Bytecoin, che in seguito avrebbe integrato indirizzi stealth, è sconosciuta). L'attuale forma di indirizzi invisibili ha tuttavia diversi miglioramenti rispetto all'idea iniziale. Ma prima, per vedere come funzionano, parliamo di chiavi.

È difficile essere nel campo delle criptovalute e non sentire parlare di chiavi. Frasi come "esegui il backup della tua chiave privata" sono comuni, ma quando un Joe medio sente le parole "chiave pubblica" e "chiave privata" si spaventa e pensa che sarà troppo tecnico e confuso per essere compreso. Ma non preoccuparti. Lo prenderemo lentamente e useremo molti esempi.

I due tipi di chiavi utilizzate nelle criptovalute sono, come appena accennato, pubbliche e private. Queste due chiavi di solito vengono fornite in coppia, il che significa che una particolare chiave pubblica e privata sono collegate l'una all'altra. In effetti, di solito la chiave pubblica deriva da quella privata, il che significa che se conosci la chiave privata, il tuo portafoglio può fare dei calcoli ingegnosi e trovare la chiave pubblica corretta ogni volta.

Ora, come implicano i nomi, la chiave pubblica può essere pubblica senza conseguenze. Di solito è una parte dell'indirizzo che condividi per ricevere denaro nel tuo portafoglio di criptovaluta. Anche a seguito del suo omonimo, la chiave privata è quella che non dovrebbe essere condivisa. È la cosa che ti consente di firmare e spendere una transazione, quindi se viene rubata o condivisa, la terza parte vile può spendere i tuoi soldi, di solito per se stessa.

Una facile analogia con questo sarebbe un lucchetto e la chiave necessaria per aprirlo. Il lucchetto aperto può essere condiviso liberamente, e infatti tutto può essere bloccato con questo lucchetto, ma solo la persona con la chiave è in grado di aprire qualsiasi cosa il lucchetto sia chiuso. Il lucchetto può essere copiato e condiviso, la chiave non dovrebbe esserlo.

Queste chiavi sono solitamente astratte dall'utente, quindi non le vedi mai veramente. In Monero, non appaiono affatto come una stringa alfanumerica spaventosa. In Monero, l'utente comune conosce la chiave privata come seme. Il seme (che dovresti scrivere se non l'hai fatto), è in realtà solo una chiave privata leggibile dall'uomo. 

Vedi? Non così spaventoso, dopo tutto. Torna a indirizzi nascosti.

Come accennato prima, gli indirizzi stealth non erano originariamente creati per Monero, ma per Bitcoin. Come con la maggior parte delle idee alle prime armi, però, questa prima iterazione ha avuto problemi. Il tentativo successivo è stato quando CryptoNote è stato creato da Nicholas van Saberhagan per Bytecoin, il precursore di Monero ([vedi la nostra storia di Monero e Bytecoin qui](/knowledge/monero-history)), e sebbene fosse un netto miglioramento rispetto all'originale, anche se aveva alcuni sottili difetti.

Alla fine, un'ultima iterazione è nata da uno sviluppatore per un'altra criptovaluta per la privacy ormai defunta, che ha risolto i problemi di privacy e sicurezza in sospeso con l'idea. Questo alla fine si è fatto strada in Monero, ed è quello che viene utilizzato oggi.

Sebbene questi problemi di privacy e sicurezza siano stati risolti, gli stessi indirizzi stealth hanno aggiunto un diverso tipo di stranezza alle tecnologie blockchain, che prima non esisteva. La necessità di eseguire la scansione. Poiché gli indirizzi di ricezione non vengono visualizzati pubblicamente sulla blockchain, il destinatario non sa mai se una determinata transazione è sua, quindi deve scansionare ogni transazione in entrata con la sua chiave privata per vedere se è la sua.

Con le monete trasparenti, tutto ciò che devono fare è controllare se una transazione viene inviata al tuo indirizzo. Una semplice domanda sì o no. Ma con indirizzi nascosti, ogni transazione potrebbe potenzialmente essere una che ti viene inviata, quindi devi provare a sbloccare ciascuna con la tua chiave privata per vedere se si apre.

Questo è un passaggio in più che Bitcoin e i suoi derivati non hanno e rende la configurazione iniziale del portafoglio, insieme alla sincronizzazione di un portafoglio quando non lo apri da un po ', molto più a lungo di Bitcoin. Il compromesso è necessario, tuttavia, per sbloccare le garanzie di privacy che ha. Va notato che, a differenza del punto più debole della tripla privacy, le firme ad anello, gli indirizzi stealth non sono suscettibili di euristica. Si basa su una vera e collaudata crittografia a curva ellittica, su cui si basa l'intera Internet, quindi interromperla significherebbe la fine della sicurezza informatica in generale, non solo Monero.

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