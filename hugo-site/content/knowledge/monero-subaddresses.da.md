---
title: "Hvordan Monero Underadresser Forebyg Identitet Linking"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har altid fundet innovative måder at løse vanskelige privatlivsproblemer på. Ofte fører disse innovationer til andre innovationer, og nogle gange kan disse resulterende teknologier endda bruges til usecases, der ikke tidligere er overvejet. Ingen steder er dette eksemplificeret mere end i tilfældet med Moneros underadresseteknologi.

Overvej et hypotetisk privatlivsproblem, hvor brug af én adresse på tværs af flere platforme fra tilsyneladende ubeslægtede personer kan føre til sammenkædning og deanonymisering af nævnte folk. Forenklet sagt, hvis du var en person ved navn Billy Joe Bob, og du solgte æbler for Bitcoin, kan du måske sende din Bitcoin-adresse på et offentligt sted, så kunderne kan betale dig. Lad os sige, at adressen starter med den alfanumeriske streng 7XybV3... Men hvis man ser bort fra den åbenlyse privatlivsrisiko, at nogen kan tjekke din Bitcoin-saldo og se, hvor meget du har solgt, er der en anden, ikke ofte talt om privatlivsrisiko. Lad os sige, at du også var en underjordisk hacker under navnet l33tz0r. Du laver fløjteblæsningsarbejde, fortæller en intetanende befolkning om regeringskorruption, og det er bydende nødvendigt, at du holder din identitet hemmelig. Du accepterer Bitcoin-donationer til dit arbejde og lægger adressen på et offentligt forum. Det er den samme adresse, som du tager imod penge fra dine apple-kunder. 7XybV3... en.

Et simpelt, men ødelæggende deanonymiseringsangreb ville være at bruge en internetsøgemaskine til at søge efter din Bitcoin-adresse. At sætte adressen på 7XybV3... i motoren giver to forskellige resultater. Æbleforretningen, og l33tz0r. Dette er nok til at forbinde de to identiteter og deanonymisere l33tz0r, med potentielt skræmmende konsekvenser fra magthaverne.

Det er vigtigt at bemærke, at dette angreb OGSÅ er muligt med Monero. Selvom Monero skjuler de fleste on-chain data, bruger dette angreb ikke nogen. Den bruger kun adressen, som skal deles for at kunne modtage betaling. Offentligt i tilfælde af anonyme donationer. Dette er en potentiel måde, hvorpå Monero-brugere uforvarende kan skade deres privatliv, og det også et eksempel på, hvordan, selvom Monero er top-tier med hensyn til bevarelse af privatlivets fred, er det ikke skudsikkert.

Den sædvanlige måde at omgå dette problem på var at eje flere tegnebøger. Med forskellige adresser opslået for hver identitet (eller usecase), kan de ikke linkes. Men dette privatliv gælder kun, hvis brugeren aldrig blander dem sammen. Hvis du ved et uheld skriver den forkerte adresse, vil det have de samme koblingseffekter. Desuden skal frøet af hver adresse holdes sikkert, hvilket øger det nødvendige infosec-arbejde med hver ny tegnebog, der laves.

Moneros løsning var underadresser. Evnen til at oprette et helt enormt antal adresser under hovedadressen ved at bruge det som en slags frø. Hver genereret underadresse kan acceptere Monero, og det hele går til den samme tegnebog. Ved at bruge denne metode er antallet af identiteter, der kan betjenes under én adresse, enormt, samtidig med at infosec-arbejdet holdes på et minimum. Disse adresser er heller ikke matematisk linkbare, så medmindre brugeren råber deres forbindelse til verden, vil en ekstern observatør have meget svært ved at forbinde dem.

Men en anden interessant usecase dukkede op fra underadresser; som en erstatningsmulighed for de universelt hadede betalings-id'er.

Betalings-id'er var en måde for sælgere at identificere, hvilken kunde der sendte hvilken betaling. Da Monero-information er skjult på kæden, er modtageren af en transaktion ikke i stand til at se, hvilken adresse der har sendt den. Det betyder, at hvis der er varer til samme pris og flere ordrer, kan det blive umuligt at identificere, hvem der har sendt hvad. Betalings-id'er er en unik, tilfældig streng, der genereres af forhandleren og gives til kunden. Kunden tilføjer dette som et separat felt ved afsendelse af transaktionen. Denne tilfældige streng placeres på blockchainen som en del af transaktionen, og på denne måde er købmanden i stand til at identificere og sortere i indgående transaktioner.

Denne metode var mangelfuld på flere måder. For det første forringer det ensartetheden af on-chain data. Yderligere, unikke metadata kan få nogle transaktioner til at skille sig ud fra mængden og derved tillade heuristisk analyse. Dette gælder især, når disse metadata ikke håndhæves som obligatoriske for alle. At gøre dette obligatorisk for alle ville dog tilføje unødvendig plads til blockchain, og det blev ikke forfulgt. Ligeledes, hvis et betalings-id nogensinde blev genbrugt af en eller anden grund, ville det være trivielt at forbinde to transaktioner som forbundet. Dette skete typisk med udvekslingsindskud, og enhver kunne nemt forbinde transaktioner som både værende en indbetaling på en børs og fra en bestemt person.

For det andet, fra et UX-perspektiv, skaber betalings-id'er et andet trin, som kryptovalutabrugere, der kommer fra andre mønter, ikke er vant til, og hvis de bliver glemt, forårsager det en massiv hovedpine for den handlende, som skal identificere disse transaktioner på andre måder . Dette blev typisk gjort ved at tale direkte med hver skikder glemte at angive betalings-id'et og bekræfte andre identificerende oplysninger, som kun de kunne kende, såsom en kombination af beløbet, afsendelsesdatoen og transaktions-id'et.

Dette ekstra trin blev savnet af mange, og det nåede til det punkt, hvor nogle børser begyndte at opkræve penge til kunder, hvis deres penge skulle hentes manuelt på grund af at have glemt et betalings-id. Andre bider tænder sammen og spiste de ekstra supportomkostninger, men ingen var glade for det.

Der var én løsning på dette, integrerede adresser, som slog adressen og betalings-id'et sammen i én streng, så det kunne ikke glemmes, men adoptionen var ret svag, på trods af de fordele, købmænd ville have fået ved at inkludere det. 

I en interessant begivenhed kom der underadresser ind for at redde dagen. Evnen til at generere store mængder af underadresser pr. hovedadresse og identificere, hvilke transaktioner der kom ind i hvilke underadresser, gjorde det muligt for købmænd at slippe af med betalings-id'er på en elegant måde, mens de tog den næste generation af Monero-teknologi. Siden da er de fleste børser og købmandsværktøjer skiftet til underadresser som den primære måde til transaktionsidentifikation.

Det, der startede som en løsning på et privatlivsproblem, blev til noget meget mere, som løste et stort UX-problem for både handlende og kunder. Innovation afføder mere innovation, som ofte kan snebolde sig ind i uventede gevinster for alle. Monero har set dette gang på gang, og lægger stor vægt på at forny, hvad der er muligt på blockchain. Hvem ved, hvilke andre ting vi kan låse op sammen?

Yderligere læsning