---
title: "Come i nodi remoti impattano sulla privacy di Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Uno dei maggiori vantaggi che Monero ha rispetto alle altre criptovalute è la sua privacy sulla catena, ma ti sei mai chiesto come la privacy di Monero regge quando usi un nodo remoto? E se usi un server "portafoglio leggero" come MyMonero?

In questo post ci immergeremo in alcuni dei dettagli di come Monero fornisce un'eccezionale privacy sulla catena anche quando si usa un nodo remoto, così come a cosa fare attenzione quando si usano i nodi remoti.

## Che funzione hanno i nodi in Monero?

## Che funzione hanno i nodi in Monero?

Per chi ha meno dimestichezza con il funzionamento di Monero, i nodi (o server) nella rete Monero possono essere eseguiti da chiunque e consentire al proprietario del nodo, o ad altre persone con cui scelgono di condividerlo! – per sincronizzare una copia della blockchain e fornire quella copia ad altri sulla rete. Questi nodi verificano anche tutte le transazioni che avvengono sulla rete, così come tutti i blocchi che vengono pubblicati e assicurano che tutti seguano le regole stabilite dal consenso.

L'altra funzione che i nodi svolgono in Monero è un modo per fornire tutti i dati necessari al tuo portafoglio Monero preferito per controllare correttamente le transazioni che ti appartengono ed effettuare nuove transazioni. Questi dati vengono forniti dai nodi in due modi:

  * I dati di ogni blocco sulla blockchain vengono richiesti dal portafoglio, scansionati per le transazioni che ti appartengono e quindi scartati una volta controllati dal portafoglio. 
    * Questo passaggio sarà presto notevolmente migliorato, grazie ai [tag di visualizzazione](/knowledge/view-tags-reduce-monero-sync-time).
  * Quando invii transazioni, il nodo che utilizzi fornisce un elenco di possibili esche (o input falsi) da utilizzare durante la creazione della transazione, assicurandoti di avere una buona folla in cui nasconderti ogni volta spendi Monero. 
    * Queste esche fanno parte delle [firme ad anello](/knowledge/ring-signatures), un pezzo importante dell'approccio di Monero alla privacy sulla catena.

  * Questo passaggio sarà presto notevolmente migliorato, grazie ai [tag di visualizzazione](/knowledge/view-tags-reduce-monero-sync-time).

  * Queste esche fanno parte delle [firme ad anello](/knowledge/ring-signatures), un pezzo importante dell'approccio di Monero alla privacy sulla catena.

## Qual è il modo più privato e sicuro di usare Monero?

## Qual è il modo più privato e sicuro di usare Monero?

La cosa migliore da fare, anche con la forte privacy on-chain fornita da Monero quando si utilizzano nodi remoti, è eseguire il proprio nodo Monero per assicurarsi di avere a portata di mano una copia originale della blockchain Monero e che il proprio indirizzo IP è ben protetto. L'altro vantaggio quando si esegue il proprio nodo è che si può contribuire alla rete, consentendo ad altri nodi di sincronizzarsi dal proprio nodo o anche consentendo ad altri utenti di connettersi al proprio nodo con i loro portafogli.

Detto questo, Monero fornisce comunque un'eccellente privacy quando si utilizza un nodo remoto. Se sei interessato a eseguire il tuo nodo Monero, ecco una guida facile da seguire per farlo:

  * [Esegui un nodo Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Cosa può imparare di me un nodo remoto?

## Cosa può imparare di me un nodo remoto?

Quando si usa un nodo remoto, ci sono alcune informazioni chiave che vengono esposte a un nodo remoto e un paio di modi chiave in cui quel nodo può attaccarvi, impedirvi di fare transazioni e altro.

La prima cosa che un nodo remoto può imparare su di te è il tuo indirizzo IP pubblico. Anche se si spera che questo sia nascosto tramite una VPN o Tor, il nodo remoto potrebbe associare il tuo indirizzo IP pubblico alla transazione, aiutandolo a restringere il campo da dove stai effettuando la transazione. Il nodo remoto può anche imparare l'ultimo blocco che il tuo portafoglio ha sincronizzato e usarlo per provare a fare congetture educate su di te, come quando usi normalmente Monero e quando hai speso Monero l'ultima volta. Questo è particolarmente vero se vieni sempre dallo stesso indirizzo IP (come la tua casa). L'ultima cosa chiave che un nodo remoto può imparare su di te sono le informazioni di base sulle transazioni che invii attraverso di esso. Mentre questi possono essere i dati più ovvi che l'operatore del nodo remoto ottiene su di te, è importante capire che questo potrebbe essere usato per aiutare a rintracciare il mittente della transazione quando si combinano queste informazioni con altri dati fuori dalla catena. Questo può essere particolarmente pericoloso se il nodo remoto è gestito da un'entità maligna, una società di analisi della blockchain o uno stato nazionale oppressivo.

Un nodo remoto può anche tentare di causarti problemi nascondendoti dei blocchi, facendo credere al tuo portafoglio di essere stato sincronizzato quando non lo era. Questo può farti pensare che i fondi siano persi o impedirti di spendere i fondi fino a quando non ti connetti ad un altro nodo. L'ultima cosa chiave che un nodo remoto potrebbe fare è alimentare il tuo portafoglio con una lista manipolata di esche. Questo potrebbe far sì che il tuo portafoglio non riesca completamente a costruire transazioni (rendendoti incapace di spendere fondi), o potrebbe permettere al nodo remoto di provare a fornire esche che sa essere state spese per ridurre l'anonimato che ricevi in ogni transazione.

## Quali garanzie di privacy esistono ancora quando si usa un nodo remoto?

## Quali garanzie di privacy esistono ancora quando si usa un nodo remoto?

Anche se questo articolo può averti spaventato un po', è importante rendersi conto che la privacy fornita da Monero è eccellente anche quando si utilizza un nodo remoto, e supera di gran lunga qualsiasi altra criptovaluta quando viene utilizzata in questo modo. Ottieni ancora la forte privacy on-chain fornita da Monero, poiché il nodo remoto non conosce mai il vero input (quali monete stai spendendo), la quantità di Monero spesa nella transazione, o l'indirizzo del destinatario della transazione. Anche gli osservatori esterni non possono vedere il vero input, l'importo o gli indirizzi coinvolti (non importa quale tipo di nodo scegli di usare!), assicurando che al di fuori del nodo remoto anche il tuo indirizzo IP, le informazioni di sincronizzazione del portafoglio e le transazioni hanno forti garanzie di privacy.

Il nodo remoto inoltre non ha mai accesso alle transazioni precedenti che hai inviato o ricevuto o la quantità di Monero attualmente nel tuo portafoglio, e perde tutta la visibilità sulle tue transazioni nel momento in cui inizi a usare un altro nodo. Nessuna chiave privata (sia di spesa che di visualizzazione) viene mai fornita al nodo remoto, e quindi il tuo portafoglio rimane privato, sicuro e utilizzabile. Non importa il nodo remoto, non sei mai a rischio di perdere Monero o di averlo rubato, poiché il nodo non può modificare l'indirizzo del destinatario, non ha mai accesso alle chiavi private del tuo portafoglio e non può confiscare il tuo Monero in alcun modo.

## Che ne dite di "portafogli leggeri" come MyMonero?

## Che ne dite di "portafogli leggeri" come MyMonero?

Anche se l'argomento è un po' fuori dallo scopo di questo articolo, ho voluto affrontare un tipo unico di portafoglio in Monero - i portafogli leggeri. Il nome light wallet deriva dal fatto che il tuo portafoglio (sul tuo telefono o computer) non deve eseguire alcuna sincronizzazione della blockchain, rendendo l'esperienza più veloce e fluida.

Tuttavia, portafogli come questo hanno un grave compromesso sulla privacy per ora - il tuo portafoglio invia la chiave di visualizzazione privata al server remoto che usi (come il default in MyMonero), dando al server remoto piena visibilità su tutti i fondi ricevuti dalla creazione del tuo portafoglio (e fino a quando non smetti di usare quel portafoglio o seme). Questo riduce drasticamente la privacy che ricevi dall'operatore del nodo, e dovrebbe essere affrontato con cautela.

Fortunatamente, la comunità Monero sta lavorando per migliorare il software che puoi usare per ospitare il tuo light wallet server (LWS), che ti permetterà di avere una sincronizzazione veloce senza fidarti di una terza parte con le tue chiavi private di visualizzazione - dato che eseguirai il software dove il tuo portafoglio invia le chiavi private di visualizzazione!

Per saperne di più sul light wallet server personalizzato, vedi il seguente repository Github:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Come posso saperne di più?

## Come posso saperne di più?

Se sei curioso e ti piacerebbe capire meglio i nodi di Monero e cercare di utilizzare un nodo remoto o eseguire il tuo, guarda i link qui sotto per i posti migliori per iniziare:

  * [Monero World, un elenco di nodi remoti gestiti dalla comunità che possono essere utilizzati](https://moneroworld.com/#nodes)
  * [Nodi Monero gestiti da Seth For Privacy, l'autore di questo articolo](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, una lista di nodi remoti con stato controllato frequentemente](https://monero.fail/)
  * [Come connettersi a un nodo remoto all'interno del portafoglio GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Nodo remoto](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Ulteriori letture

  * [Come Monero abilita in modo unico le economie circolari](/knowledge/monero-circular-economies)/

  * [Firme ad anello di Monero vs CoinJoin come in Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Perché (e come!) dovresti tenere le tue chiavi](/knowledge/hold-your-keys)/

  * [Contribuire a Monero](/knowledge/contributing-to-monero)/

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