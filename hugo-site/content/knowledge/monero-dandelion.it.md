---
title: "Come Dandelion ++ mantiene private le origini delle transazioni di Monero"
slug: "monero-dandelion"
date: "2020-04-28"
image: "/images/dandelion.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Privacy come priorità

Come criptovaluta, Monero potrebbe sembrare molto noioso a occhio nudo. Non ha una grande pretesa di fama come essere un "computer mondiale" o "rivoluzionare l'industria xyz". Sta solo cercando di essere un denaro privato, digitale, fungibile e ogni aggiornamento e nuova tecnologia promuove solo questo fine.   
  
Coloro che ritengono questo obiettivo troppo stretto o poco interessante in genere non comprendono quanto sia difficile ottenere una privacy significativa, soprattutto su un registro aperto permanente come una blockchain. Qualsiasi via per la perdita di metadati è un potenziale per l'erosione della privacy.   
  
Monero prende precauzioni per offuscare i dati della catena, come mittente, destinatario e importi, rispettivamente tramite indirizzi invisibili, firme ad anello e impegni Pedersen. Ciò riduce al minimo le possibilità che un osservatore occasionale deduca informazioni critiche dopo che le transazioni sono già state inviate e fanno ora parte della cronologia registrata. Vi sono, tuttavia, alcuni attacchi che possono essere effettuati nel momento in cui si verifica una transazione che non può essere eseguita in un secondo momento.

## Attacco per rivelare l'indirizzo IP

Questi attacchi ruotano attorno all'identificazione dell'indirizzo IP da cui proviene una transazione. Se si deducono queste informazioni, è possibile che un individuo abbia inviato una transazione Monero. Non è in grado di mostrare a chi e quanto, ma ci sono alcuni casi in cui la conoscenza di qualcuno che usa Monero è sufficiente a causare danni.   
  
La buona notizia è che se queste informazioni non vengono raccolte nel momento in cui viene effettuata la transazione, non possono essere apprese in un secondo momento, poiché gli indirizzi IP non vengono memorizzati sulla blockchain. È anche confortante sapere che è improbabile che si verifichi un simile attacco in natura, poiché, per evitarlo, l'attaccante avrebbe bisogno di una grande maggioranza di nodi sulla rete. Se una persona fosse in grado di controllare questa grande maggioranza, tuttavia, sarebbe in grado di identificare la "direzione" da cui proviene una transazione.   
  
Questo può essere fonte di confusione, quindi spiegheremo alcune informazioni di base qui. Ogni nodo si connette ad altri nodi sulla rete, in modo che possano mantenere la blockchain aggiornata e condividere ciò che sanno con gli altri. Queste connessioni consentono loro di conoscere nuove transazioni, propagarle e inviare le proprie. Poiché un nodo può comunicare ai propri colleghi solo le transazioni di cui sono a conoscenza, è ovvio che il primo nodo che propaga una transazione è il nodo che sta effettivamente inviando Monero.   
  
Se un utente malintenzionato possiede una grande maggioranza di nodi sulla rete, ciascun nodo sentirà una transazione da uno dei suoi peer e, in base alla tempistica in cui ciascun nodo riceve queste informazioni, può dedurre i probabili candidati da dove è iniziata la transazione.   
  
Se questo è ancora confuso, offriamo questo esempio. Supponiamo che entrambi abbiamo un amico comune che si nasconde alla nostra visione. Questo amico chiama ad alta voce. Prima sento la sua chiamata e la sento più forte di te. Da queste informazioni, possiamo sapere che probabilmente sono più vicino al nostro amico di te. Il fatto che tu ascolti il suono in un secondo momento (anche solo di una frazione di secondo) e che il suono sia più debole significa che dovremmo iniziare la nostra ricerca intorno alla mia area, non alla tua.   
  
Se un utente malintenzionato è in grado di indovinare con successo quali dei loro peer hanno inviato la transazione, poiché hanno l'indirizzo IP che è collegato al loro nodo e inoltrato a loro, possono essere certi dell'indirizzo IP che lo ha inviato. Si tratta di informazioni potenti, poiché gli indirizzi IP contengono informazioni sul paese e sul provider di servizi Internet (ISP) dell'utente e l'ISP stesso sa quale utente è collegato a quale indirizzo IP esatto, deanonimizzando efficacemente l'utente Monero.

## Le mitigazioni

Una possibile soluzione per questo attacco è l'utilizzo di una rete overlay come Tor o I2P. Questo fa sì che anche se un utente malintenzionato può dedurre un indirizzo IP di origine, probabilmente non è quello che ha effettuato la transazione, ma piuttosto il outproxy (I2P) o il nodo di uscita (Tor) della rete di overlay. Questa non è una soluzione onnicomprensiva, poiché reti sovrapposte, VPN e software simile sono vietati in molti paesi e aspettarsi che tutti utilizzino, sincronizzino e propagino su queste reti non è realistico. Deve esserci una soluzione che non richiede l'utilizzo di software e reti esterni; uno che è disponibile per la persona comune.   
  
Questa soluzione è Dandelion ++ (DPP), che è un protocollo aggiornato alla proposta Dandelion originale per Bitcoin. In questo protocollo, ci sono due fasi, la fase dello stelo e la fase di fluff; entrambi dovrebbero rappresentare la forma di un dente di leone.   
  
Nella fase radice, ogni pochi minuti, il nodo mittente sceglie casualmente due peer da tutti i nodi a cui è connesso. Quando il nodo mittente invia una transazione, per conto proprio o semplicemente inoltrando la transazione da un altro nodo nella fase radice, sceglie casualmente uno di questi due peer selezionati e vi invia la transazione.   
  
La fase di fluff è quando un nodo riceve una transazione e la trasmette a ogni connessione in uscita, piuttosto che solo a una scelta a caso, ciò consente una vera propagazione della transazione. Ogni pochi minuti un nodo si definisce come uno che si propagherà casualmente o tramite fluff via casualmente, quindi una fase radice può essere piuttosto lunga se ogni nodo di connessione si definisce come nodo radice, ma una volta che la transazione raggiunge la fase fluff, rimane lì.   
  
Ciò significa che un utente malintenzionato non sarà più in grado di ascoltare semplicemente la direzione di una transazione, perché prima che fosse propagato a tutti, ha subito la fase radice e il nodo di origine della fase fluff non è il nodo da cui la transazione ha avuto origine e non è noto quanti salti siano stati sottoposti alla transazione.   
  
Naturalmente, combinando le soluzioni di cui sopra (DPP più una rete overlay) fornirà garanzie ancora più forti di privacy e protezione contro la tracciabilità IP. Va anche notato che DPP non difende da un'altra forma di attacco di tracciabilità della rete che può essere fatto con gli ISP, ma questo va oltre lo scopo di questo articolo.   
  
Dandelion ++ è impostato per essere attivo sulla rete Monero ed essere utilizzato per impostazione predefinita sul client di riferimento, nella versione 0.16. Questa piccola modifica mitigherà ulteriormente gli attacchi possibili sulla rete Monero ed esemplifica il motivo per cui Monero guida il pacchetto in pratiche tecnologie di privacy applicate.

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

  * [In che modo CLSAG migliorerà l'efficienza di Monero](/knowledge/what-is-clsag)/

  * [Perché Monero ha un'emissione di coda](/knowledge/monero-tail-emission)/

  * [La storia di Monero](/knowledge/monero-history)/

  * [Wired Magazine ha sbagliato su Monero, ecco perché](/knowledge/wired-article-debunked)/

  * [Top 15 Miti e preoccupazioni Monero debunked](/knowledge/monero-myths-debunked)/

  * [Perché Monero è open source e decentralizzato](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Mining: cosa rende RandomX così speciale](/knowledge/monero-mining-randomx)/

  * [Perché Monero è meglio di Dash, Zcash, Zcoin (anche con Lelantus), Grin e Bitcoin Mixer come Wasabi (Aggiornato a maggio 2020)](/knowledge/why-monero-is-better)/