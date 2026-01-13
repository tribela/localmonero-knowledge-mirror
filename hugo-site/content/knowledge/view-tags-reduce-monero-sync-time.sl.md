---
title: "Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ena najpogostejših pritožb pri vsakodnevni uporabi Monera je čas, ki ga lahko traja, da sinhronizirate denarnico, preden lahko pošljete Monero. K sreči so razvijalci in raziskovalci v skupnosti Monero našli sijajen način za zmanjšanje časa, ki ga potrebujete za sinhronizacijo denarnice, za 40 %+ brez dodatnih stroškov verige blokov, provizij itd. 

Vnesite "ogled oznak", enobajtni dodatek k podatkom vsake transakcije – prihaja v Monero pri naslednji nadgradnji omrežja!

## Zakaj je sinhronizacija Monero denarnice počasnejša od sinhronizacije denarnice Bitcoin?

Eno od prvih vprašanj na katero moramo odgovoriti, da bi bolje razumeli potrebo po rešitvi, kot so oznake za ogled, je, zakaj je sinhronizacija denarnice Monero počasnejša od kriptovalut, kot je Bitcoin.

Ker v Bitcoinu vse transakcije niso zasebne in razkrivajo porabljene kovance, zneske in vključene naslove v verigi, lahko denarnice Bitcoin preprosto poiščejo morebitne neporabljene izhode transakcij (UTXO) ali uporabljene naslove za dano denarnico. , hitro skeniranje verige blokov samo za UTXO, ki so v lasti teh naslovov, da ugotovi, kateri kovanci pripadajo vaši denarnici in jih je mogoče porabiti.

V Monero pa vse transakcije ohranjajo zasebnost uporabnika tako, da skrijejo pošiljatelja, prejemnika in zneske, vključene v posamezno transakcijo. Ta zasebnost, ki je ključna za zaščito uporabnikov omrežja, uvaja tudi počasnejšo sinhronizacijo denarnice. V Monero mora vaša denarnica primerjati vsak izhod transakcije (TXO), ki obstaja v omrežju, z zasebnimi ključi vaše denarnice.

Ta primerjava vključuje veliko zapletene matematike in kriptografije za potrditev, da je rezultat resnično vaš, saj so vsi zneski, naslovi in znano porabljeni rezultati (ali kovanci) skriti v verigi v Monero.

## Kaj so oznake pogleda?

Da bi zmanjšal čas sinhronizacije za Monero denarnice, [je raziskovalec UkoeHB iznašel nov pristop](https://github.com/monero-project/research-lab/issues/73) – dodajte 1-bajtno "oznako" vsaki transakciji z uporabo skupne skrivnosti, ki je znana samo pošiljatelju in prejemniku te transakcije.

To skupno skrivnost ustvari pošiljatelj z uporabo naslova, ki mu ga je posredoval prejemnik, in ne zahteva nobenega aktivnega sodelovanja pošiljatelja in prejemnika. Prvi bajt (ali znak) te skupne skrivnosti se nato doda k podatkom transakcije, ko jo objavite v omrežju Monero.

Ko želi eden od udeležencev te transakcije pozneje sinhronizirati svojo denarnico z Monero blockchainom, namesto da bi moral izvesti vso zapleteno matematiko in kriptografijo za vsak TXO v omrežju, lahko denarnica zdaj samo preveri, ali to 1-bajtno polje v vsaki transakciji in šele nato opravite zamudno preverjanje transakcij, ki imajo to oznako – 1/256 TXO v omrežju, če smo natančni! 

Ta oznaka ne razkrije nobenih informacij o transakciji zunanjim gledalcem, doda le 1 bajt (zanemarljivo količino) velikosti transakcije, vendar nam omogoča, da skrajšamo čase sinhronizacije za 40 %+ z zmanjšanjem zapletenih preverjanj potrebno!

## Ogled oznak: poenostavljen primer

Predstavljajte si, da imate v sobi 4096 škatel, od katerih vam pripada samo 5 škatel. Vse škatle so od zunaj popolnoma nerazločljive in edini način, da ugotovite, ali je škatla za vas, je, da jo odprete in rešite zamudno matematično nalogo, zapisano v njej, da zagotovite, da je vaša. 

Zdaj pa si predstavljajte, da se odločite, da oseba, ki vam pošlje teh 5 škatel, ustvari posebno kodo z uporabo vašega naslova in nato na zunanjo stran vsake škatle, ki vam je poslana, vnese samo prvi znak te generirane kode. Vsi ostali naredijo isto za svoje škatle (da zagotovijo, da so vse škatle še vedno nerazločljive), zdaj pa lahko preprosto pogledate kodo z enim znakom na zunanji strani škatle in odprete samo tiste škatle, ki imajo ta znak. 

Medtem ko se bodo druge škatle ujemale z vašo kodo, tudi tiste, ki niso v vaši lasti, je število škatel, ki jih morate odpreti in rešiti matematično nalogo, zdaj le 16 (1/256 škatel!) namesto vseh 4096. 

Zdaj odprite teh 16 škatel, rešite matematične probleme in obdržite 5 škatel, ki vam dejansko pripadajo iz te skupine!

## Kdaj bodo oznake za ogled na voljo v Moneru?

Oznake za ogled so ena od funkcij, ki so trenutno načrtovane za vključitev v [prihajajočo nadgradnjo omrežja](https://github.com/monero-project/meta/issues/630) in bi morale biti izdane to pomlad. Skupnost [je zbrala 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (v času pisanja), da bi spodbudila razvoj in implementacijo oznak za oglede, zato je bila velika večina dela za vključitev oznak za oglede v osnovo kode Monero že opravljena. dokončal j-berman v sodelovanju z recenzenti in raziskovalci.

Ko bo omrežje uveljavilo oznake za ogled, bodo vse transakcije, poslane po nadgradnji omrežja, imele koristi od drastično izboljšanega časa sinhronizacije denarnice. Ne bo vam treba narediti nič posebnega, da začnete uporabljati oznake za ogled, vaša najljubša denarnica za Monero jih bo preprosto začela uporabljati po samodejni nadgradnji omrežja! 

## Kako lahko izvem več?

Če je to vzbudilo vašo radovednost glede oznak pogleda, si spodaj oglejte nekaj dodatnih povezav, ki se poglobijo v temo: 

  * [Zmanjšajte čas skeniranja z 'oznako pogleda' 1-bajt ](https://github.com/monero-project/research-lab/issues/73)
  * [Dodajte oznake pogleda izhodom, da skrajšate čas skeniranja denarnice](https://github.com/monero-project/monero/pull/8061)

Nadaljnje branje