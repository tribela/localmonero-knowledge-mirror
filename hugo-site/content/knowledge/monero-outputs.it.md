---
title: "Spiegazione dei risultati di Monero"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, come altre criptovalute, utilizza gli output come mezzo per contabilizzare i fondi. Molti utenti esperti di criptovaluta hanno probabilmente sentito questo termine prima, ma non tutti capiscono cosa intendono e come funzionano. Come esplorato nel nostro [articolo sulle firme ad anello](/knowledge/ring-signatures), gli output sono l'unità effettiva scambiata sulla blockchain tra le parti che effettuano transazioni. Simile a una banconota da un dollaro, ma l'importo non è in una denominazione fissa.

Se vieni pagato $ 16 per un lavoro, potresti ricevere una banconota da un dollaro, una banconota da cinque dollari e una banconota da dieci dollari. Hai $ 16, ma hai anche tre diverse banconote nel tuo portafoglio. Se volessi pagare a qualcuno 6 dollari, potresti usare il 5 e il conto 1, ma se volessi pagare a qualcuno $ 8 potresti usare solo $ 10 e ricevere $ 2 in cambio. Infine, se volessi pagare $ 14 a qualcuno dovresti usare tutte e tre le banconote e riceveresti $ 2 in cambio, ma per un momento, quando consegni tutte e tre le banconote, non hai soldi nel tuo portafoglio finché non ottieni il cambiare indietro.

Monero funziona in modo simile. Supponiamo che tu gestisca un negozio e effettui tre vendite su tre articoli diversi. Potresti ricevere 1.5 XMR, 2.25 XMR e 5.25 XMR per un totale di 9 XMR, ma hai anche tre diverse uscite nel tuo portafoglio delle denominazioni indicate in precedenza. Proprio come con i dollari, potresti voler pagare a qualcuno 3 XMR. È possibile utilizzare solo l'uscita XMR 5,25 e ricevere di nuovo 2.25 XMR in cambio, oppure è possibile combinare le uscite XMR 1,5 e 2,25 e ottenere 0,75 XMR in cambio.

Ma, non appena invii la transazione, gli output che usi vengono messi in uno stato "bloccato", il che significa che sono inaccessibili finché non ricevi la modifica. Il protocollo sblocca i fondi (ovvero ti restituisce la modifica) dopo 10 conferme o circa 20 minuti. Proprio come una volta che hai consegnato le banconote in dollari dal tuo portafoglio, non puoi riutilizzare il denaro finché non ricevi il resto dalla cassa, il tuo Monero è inaccessibile finché non ricevi il resto.

Torniamo all'esempio dell'invio di 3 XMR a qualcuno e utilizzi l'uscita 5.25 XMR. Ora, mentre aspetti che l'1,75 XMR torni in cambio, non puoi usarlo. Questo 1,75 XMR è inaccessibile per te. Ma puoi comunque utilizzare le uscite 1.5 XMR e 2.25 XMR, poiché non sono state spese. Tornando all'esempio del dollaro, se pagassi a qualcuno $ 8, come nell'esempio precedente, non saresti in grado di utilizzare i $ 2 che ti aspetti in cambio fino a quando non ti viene dato, ma in questo esempio, hai ancora un Banconota da $ 10 non utilizzata nel tuo portafoglio. Questo può ancora essere utilizzato per acquistare quello che vuoi mentre aspetti il cambiamento. Lo stesso con Monero.

Questo è spesso un punto di confusione per i nuovi utenti Monero. Spesso, un utente può avere solo un output nel proprio portafoglio, ricevuto da uno scambio o da un amico. Diciamo che questo output è 20 XMR. Non hanno altre uscite nel loro portafoglio. Ora vogliono fare una donazione a due dei loro enti di beneficenza preferiti. Mandano 5 XMR al primo ente di beneficenza e poi sono confusi perché, anche se dovrebbero avere 15 XMR rimasti, non possono inviare immediatamente la donazione successiva al secondo ente di beneficenza. Come avrai intuito, questo perché il 15 XMR è bloccato. Non può essere speso finché non viene restituito come resto (10 conferme o circa 20 minuti). Una volta sbloccati i fondi, potranno inviare la seconda donazione.

Giusto per ribadire il punto, non avrebbero avuto questo problema se avessero invece avuto più uscite, come due uscite 10 XMR o simili. Sarebbero in grado di inviare entrambe le donazioni una dopo l'altra, perché la prima donazione userebbe una delle 10 uscite XMR (e attenderebbe 10 conferme per ricevere 5 XMR in cambio), e la seconda donazione userebbe le altre 10 XMR produzione.

Alcuni portafogli di criptovaluta hanno una funzione chiamata "gestione dell'output", che mostra semplicemente a un utente quali output ha attualmente (oltre alla loro somma totale) e gli consente di scegliere quali desidera utilizzare quando spende la loro criptovaluta.

A partire da ora, la GUI di Monero seleziona automaticamente gli output per gli utenti, poiché gli utenti che selezionano i propri output spesso creano confusione o, in alcuni casi, danneggiano la privacy. Ci sono portafogli in costruzione tuttavia, come il nuovo progetto di portafoglio Feather, che conterrà queste funzionalità di gestione dell'output.

Abbiamo parlato molto della parte di invio, ma accade qualcosa di affascinante all'estremità ricevente. Tornando al nostro esempio di invio di 3 XMR a qualcuno e utilizzando le tue uscite 1.5 XMR e 2.25 XMR nella transazione (aspettandoti 0,75 XMR in cambio), il ricevitore NON riceve due uscite di 1.5 XMR e 2.25 XMR. Ricevono invece ONE 3 XMR output.

In background, il protocollo combina tutti gli output utilizzati per la spesa e fornisce al destinatario un output dell'importo pagato e invia un output di modifica al mittente. Quindi il mittente riceverà anche un output come resto, indipendentemente dal fatto che abbia utilizzato due, tre o dieci output per inviare la transazione.

Ci auguriamo che questo abbia chiarito un po 'di confusione sugli output e su come funziona la contabilità interna del protocollo, così come l'utente comune deve affrontare problemi di confusione quando incontra fondi bloccati. In un altro articolo esploreremo la gestione dei tuoi output in modo da ridurre al minimo la possibilità di dover attendere i fondi sbloccati prima di inviare transazioni future.

Ulteriori letture