---
title: "Hvordan Monero-underadresser forhindrer identitetskobling"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero har alltid funnet innovative måter å løse vanskelige personvernproblemer på. Ofte fører disse innovasjonene til andre innovasjoner, og noen ganger kan disse resulterende teknologiene til og med brukes til bruksområder som ikke tidligere er vurdert. Ingen steder er dette eksemplifisert mer enn i tilfellet med Moneros subadresseteknologi.

Vurder et hypotetisk personvernproblem, der bruk av én adresse på tvers av flere plattformer fra tilsynelatende ikke-relaterte mennesker kan føre til kobling og deanonymisering av nevnte folk. Enkelt sagt, hvis du var en person som het Billy Joe Bob og du solgte epler for Bitcoin, kan du legge ut Bitcoin-adressen din på et offentlig sted slik at kundene kan betale deg. La oss si at adressen starter med den alfanumeriske strengen 7XybV3... Men ser vi bort fra den åpenbare personvernrisikoen ved at noen kan sjekke Bitcoin-saldoen din og se hvor mye du har solgt, er det en annen, ikke ofte snakket om personvernrisiko. La oss si at du også var en underjordisk hacker som heter l33tz0r. Du utfører varslingsarbeid, forteller en intetanende befolkning om korrupsjon fra myndighetene, og det er viktig at du holder identiteten din hemmelig. Du godtar Bitcoin-donasjoner for arbeidet ditt, og legger ut adressen på et offentlig forum. Det er samme adresse som du tar imot penger fra apple-kundene dine. 7XybV3... en.

Et enkelt, men ødeleggende deanonymiseringsangrep ville være å bruke en søkemotor på Internett for å søke etter Bitcoin-adressen din. Å sette adressen til 7XybV3... i motoren gir to forskjellige resultater. Apple-virksomheten, og l33tz0r. Dette er nok til å koble sammen de to identitetene og deanonymisere l33tz0r, med potensielt skumle konsekvenser fra maktene som er.

Det er viktig å merke seg at dette angrepet OGSÅ er mulig med Monero. Selv om Monero skjuler de fleste data på kjeden, bruker ikke dette angrepet noen. Den bruker kun adressen, som må deles for å motta betaling. Offentlig ved anonyme donasjoner. Dette er en mulig måte Monero-brukere uforvarende kan skade privatlivet sitt på, og er også et eksempel på hvordan, selv om Monero er på topp med hensyn til oppbevaring av personvern, er den ikke skuddsikker.

Den vanlige måten å omgå dette problemet på var å eie flere lommebøker. Med forskjellige adresser lagt ut for hver identitet (eller usecase), kan de ikke kobles sammen. Men dette personvernet gjelder bare hvis brukeren aldri blander dem sammen. Å legge ut feil adresse ved et uhell vil ha samme koblingseffekter. I tillegg må frøet til hver adresse holdes sikkert, noe som øker informasjonsarbeidet som er nødvendig med hver ny lommebok som lages.

Moneros løsning var underadresser. Muligheten til å lage et helt enormt antall adresser under hovedadressen, ved å bruke den som et slags frø. Hver generert underadresse kan godta Monero, og alt går til samme lommebok. Ved å bruke denne metoden er antallet identiteter som kan opereres under én adresse enormt samtidig som infosec-arbeidet holdes på et minimum. Disse adressene er heller ikke matematisk koblingsbare, så med mindre brukeren roper sin forbindelse til verden, vil en utenforstående observatør ha store problemer med å koble dem.

Men en annen interessant usecase dukket opp fra underadresser; som et erstatningsalternativ for de universelt hatede betalings-ID-ene.

Betalings-ID-er var en måte for selgere å identifisere hvilken kunde som sendte hvilken betaling. Siden Monero-informasjon er skjult på kjeden, kan ikke mottakeren av en transaksjon se hvilken adresse som sendte den. Dette betyr at hvis det er varer med samme pris og flere bestillinger, kan det bli umulig å identifisere hvem som sendte hva. Betalings-IDer er en unik, tilfeldig streng generert av selgeren og gitt til kunden. Kunden legger dette til som et eget felt ved sending av transaksjonen. Denne tilfeldige strengen plasseres på blokkjeden som en del av transaksjonen, og på denne måten kan selgeren identifisere og sortere gjennom innkommende transaksjoner.

Denne metoden var feil på flere måter. For det første forringer det enhetligheten til data i kjeden. Ytterligere, unike metadata kan få noen transaksjoner til å skille seg fra mengden, og dermed tillate heuristisk analyse. Dette gjelder spesielt når disse metadataene ikke håndheves som obligatoriske for alle. Å gjøre dette obligatorisk for alle ville imidlertid legge til unødvendig plass til blokkjeden, og ble ikke fulgt opp. I tillegg, hvis en betalings-ID noen gang ble gjenbrukt av en eller annen grunn, ville det være trivielt å koble to transaksjoner som koblet. Dette skjedde vanligvis med bytteinnskudd, og hvem som helst kunne enkelt koble transaksjoner som både innskudd på en børs og fra en bestemt person.

For det andre, fra et UX-perspektiv, skaper betalings-ID-er et andre trinn som kryptovalutabrukere som kommer fra andre mynter ikke er vant til, og hvis de blir glemt, forårsaker det en massiv hodepine for selgeren som må identifisere disse transaksjonene på andre måter . Dette ble vanligvis gjort ved å snakke direkte med hver kunde som glemte å angi betalings-ID og bekrefte annen identifiserende informasjon som bare de kunne vite, for eksempel en kombinasjon av beløp, dato sendt og transaksjons-ID.

Dette ekstra trinnet ble savnet av mange, og det kom til det punktet at noen børser begynte å belaste kunder hvis pengene deres måtte hentes manuelt fordi de glemte en betalings-ID. Andre biter tennene sammen og spiste de ekstra støttekostnadene, men ingen var glade for det.

Det var én løsning på dette, integrerte adresser, som slo sammen adressen og betalings-IDen til én streng, så den kunne ikke glemmes, men adopsjonen var ganske svak, til tross for fordelene selgere ville ha fått ved å inkludere den. 

I en interessant vending kom underadresser inn for å redde dagen. Muligheten til å generere store mengder subadresser per hovedadresse, og identifisere hvilke transaksjoner som kom inn i hvilke subadresser, gjorde at selgere kunne kvitte seg med betalings-IDer på en elegant måte, samtidig som de tok i bruk neste generasjon Monero-teknologi. Siden den gang har de fleste børser og selgerverktøy byttet til underadresser som den primære måten for transaksjonsidentifikasjon.

Det som startet som en løsning for et personvernproblem, ble til noe mye mer, som løste et stort UX-problem for både selgere og kunder. Innovasjon avler mer innovasjon, som ofte kan snøballe til uventede gevinster for alle. Monero har sett dette gang på gang, og legger ned stor innsats i å innovere hva som er mulig på blokkjeden. Hvem vet hvilke andre ting vi kan låse opp sammen?

Videre lesning