---
title: "Hvordan Monero Stealth Adresser Beskyt Din Identitet"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har implementeret en trestrenget tilgang til privatliv. Disse teknologier er [ringsignaturer](/knowledge/ring-signatures), som skjuler det sande output (afsender), RingCT, som skjuler beløbene, og stealth-adresser, som skjuler modtageren. I dag vil vi diskutere den sidste af disse nævnte teknologier: stealth-adresser.

Der er mange grunde til, at en person måske ønsker at skjule, hvem de sender til. Vi må aldrig lade nogen forsøge at overbevise os om, at alle eksempler på dette er ubehagelig adfærd. Ting som at sende til et upopulært politisk parti, donere til velgørende organisationer eller støtte dem, som kulturen anser for "aflyst", er alle eksempler på, hvor man måske ønsker at skjule deres forbrugsadfærd af frygt for konsekvenser, men de er af helt legitime natur.

På en gennemsigtig blockchain er de adresser, man sender deres transaktioner til, synlige for alle. Det er vigtigt at overveje, at hvis minearbejdere selv er uenige i, hvor pengene går hen, kan de vælge ikke at mine dem i en blok, hvilket effektivt censurerer denne transaktion på en tilsyneladende censurresistent platform. Den eneste måde at gøre denne, ganske vist usandsynlige, censur ikke mulig er, hvis minearbejdere ikke kan skelne mellem transaktioner, fordi alle on-chain metadata er skjult på forskellige måder. Noget som Monero er kendt for.

Monero løser dette problem med gennemsigtige adresser ved at implementere stealth-adresser, en teknologi, der faktisk oprindeligt blev lavet til Bitcoin i 2011 af Bitcoin Talk-forumbrugeren ByteCoin (relationen til Bytecoin, som senere ville integrere stealth-adresser, er ukendt). Den nuværende form for stealth-adresser har dog adskillige forbedringer i forhold til den oprindelige idé. Men lad os først tale om nøgler for at se, hvordan de virker.

Det er svært at være i cryptocurrency-området og ikke høre om nøgler. Sætninger som 'sikkerhedskopier din private nøgle' er almindelige, men når en gennemsnitlig Joe hører ordene "offentlig nøgle" og "privat nøgle", bliver de bange og tror, det vil være for teknisk og forvirrende at forstå. Men bare rolig. Vi tager det langsomt og bruger masser af eksempler.

De to slags nøgler, der bruges i kryptovalutaer, er som nævnt offentlige og private. Disse to nøgler kommer normalt i et par, hvilket betyder, at en bestemt offentlig og privat nøgle er knyttet til hinanden. Faktisk er den offentlige nøgle normalt afledt af den private, hvilket betyder, at hvis du kender den private nøgle, kan din tegnebog lave nogle smarte regnestykker og finde den korrekte offentlige nøgle hver gang.

Nu, som navnene antyder, kan den offentlige nøgle være offentlig uden konsekvenser. Normalt er det en del af adressen, som du deler for at modtage penge i din kryptovaluta-pung. Også efter sin navnebror er den private nøgle en, der ikke bør deles. Det er den ting, der giver dig mulighed for at underskrive og bruge en transaktion, så hvis den bliver stjålet eller delt, så kan den modbydelige tredjepart bruge dine penge, normalt til sig selv.

En let analogi til dette ville være en hængelås og den nødvendige nøgle for at låse den op. Den åbne hængelås kan frit deles, og faktisk kan alt låses op med denne hængelås, men kun personen med nøglen kan åbne alt, hvad hængelåsen er lukket på. Hængelåsen kan kopieres og deles, nøglen skal ikke være det.

Disse nøgler er normalt fjernet fra brugeren, så du ser dem aldrig rigtigt. I Monero fremstår de slet ikke som en skræmmende alfanumerisk streng. I Monero kender den almindelige bruger den private nøgle som deres frø. Frøet (som du bør skrive ned, hvis du ikke har), er faktisk kun en privat nøgle, der kan læses af mennesker. 

Ser du? Ikke så skræmmende alligevel. Tilbage til stealth-adresser.

Som tidligere nævnt blev stealth-adresser ikke oprindeligt lavet til Monero, men Bitcoin. Som med de fleste nye ideer havde denne første iteration problemer. Det næste forsøg kom, da CryptoNote blev skabt af Nicholas van Saberhagan til Bytecoin, forløberen for Monero ([se vores historie om Monero og Bytecoin her](/knowledge/monero-history)), og selvom det var en klar forbedring i forhold til originalen, havde selv den nogle subtile fejl.

Til sidst opstod en sidste iteration fra en udvikler til en anden nu nedlagt privatlivs-cryptocurrency, som løste de udestående privatlivs- og sikkerhedsproblemer med ideen. Dette kom til sidst ind i Monero, og er det, der bruges i dag.

Selvom disse privatlivs- og sikkerhedsproblemer blev løst, tilføjede stealth-adresser i sig selv en anden slags særpræg til blockchain-teknologier, en der ikke eksisterede før. Behovet for at scanne. Da modtageradresser ikke vises offentligt på blockchain, ved modtageren aldrig, om en given transaktion er deres, så de skal scanne alle indgående transaktioner med deres private nøgle for at se, om den er deres.

Med gennemsigtighedsmønter er det eneste, de skal gøre, at tjekke, om en transaktion er detsender til din adresse. Et nemt ja eller nej spørgsmål. Men med stealth-adresser kan hver transaktion potentielt være en, der sendes til dig, så du skal prøve at låse hver enkelt op med din private nøgle for at se, om den åbner.

Dette er et ekstra trin, som Bitcoin og dets derivater ikke har, og det laver den indledende tegnebogsopsætning sammen med synkronisering af en tegnebog, når du ikke har åbnet den i et stykke tid, meget længere end Bitcoin. Afvejningen er dog nødvendig for at låse op for de privatlivsgarantier, den har. Det skal bemærkes, at i modsætning til det svageste punkt i privatlivets trifecta, er ringsignaturer, stealth-adresser ikke modtagelige for heuristik. Den er afhængig af afprøvet og ægte elliptisk kurvekryptografi, som hele internettet er afhængig af, så at bryde den ville betyde en ende på computersikkerhed generelt, ikke kun Monero.

Yderligere læsning