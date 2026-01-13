---
title: "Wired Magazine on väärässä Monerosta, tässä miksi"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sekä yksityisyyden että kryptovaluuttojen alalla väärää tietoa on usein runsaasti. Meillä on [artikkeli, joka hahmottelee viisitoista yleistä virheellistä tai vanhentunutta oletusta Monerosta](/knowledge/monero-myths-debunked), mutta haluamme käyttää aikaa käsitelläksemme yhtä tiettyä artikkelia, jota Monero-skeptikot usein lainaavat ja levittävät.

Wired julkaisi [artikkelin](https://www.wired.com/story/monero-privacy/) 27\. maaliskuuta 2018, joka kirjoitettiin vastauksena eri tutkijoiden julkaisemaan toiseen tuoreeseen julkaisuun, jonka otsikko on "An Empirical Analysis of Traceability in the Monero Blockchain”.

Vaikka lehden ovat kirjoittaneet henkilöt, joilla oli selvä eturistiriita (lue: he ovat Zcashin neuvonantajia ja heillä on osuus siitä), Monero-yhteisö otti paperin vastaan kohtalaisen hyvin, koska se vahvistaa asioita, jotka yhteisö on jo tiennyt, ja niistä on kirjoitettu omissa Monero Research Lab -papereissa ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) ja [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), joista aikaisempi julkaistiin neljä vuotta sitten. Wiredin julkaisuun liittyi kuitenkin myös useita turhautumisia, pääasiassa eturistiriidan takia ja siksi, että asiat olivat jo tiedossa, niistä keskusteltiin ja joissain tapauksissa ne korjattiin, sekä Moneron tuolloisten yksityisyystakuut luonnehdittiin törkeästi. Yhteisö kommentoi työn esipainosta, ja monet heidän suosituksista päätyivät lopulliseen paperiin.

Mutta mitä tarkalleen luonnehdittiin törkeästi? Se, että Monerolla ei ollut lehdessä käsiteltyjä puutteita yli vuoteen. Ennen vuotta 2017 tehdyt liiketoimet olivat todellakin haavoittuvia tietynlaiselle tietosuojavuodolle, mutta julkaisuhetkellä Monero oli käsitellyt suurimman osan huolenaiheista. Ollakseen oikeudenmukainen tekijöitä kohtaan, he keskustelevat Moneron korjaustoimenpiteistä pienessä määrin, mutta eivät tarpeeksi vaikuttamaan negatiiviseen vaikutukseen, joka artikkelilla oli tuolloin kryptovaluuttamediassa.

Vaikka voimme tarkastella kyseistä Wired-artikkelia aikakautena ja kuinka totta se oli tuolloin. Se tosiasia, että sitä jaetaan edelleen tänään perusteena sille, miksi Moneron tietosuojatakuut ovat heikkoja, oikein kutsuu analysoimaan artikkelia. Otamme mielellämme tämän kutsun vastaan.

Lyhyen lukemisen perusteella artikkelista löytyy useita sensaatiomaisia lauseita, kuten "Tulosten ei pitäisi huolestuttaa vain ihmisiä, jotka yrittävät salaa käyttää Moneroa" ja koko artikkelin sävy, jossa tutkimusta esitetään "uutena" julkaisun perusteella. Itse akateeminen paperi esittää suosituksia, kuten varoituksen Monero-käyttäjille mahdollisesta anonymiteetin vaarantumisesta, vaikka nämä keskustelut ovat olleet käynnissä jo vuodesta 2014 ja yhteisön mielipide oli, ettei Moneroa pitäisi ostaa ja että se oli hyvin kokeellinen.

Mutta entä itse kritiikki? Tosiasia on, että monet Moneroon yksityisyyskolikkona liittyvät ongelmat eivät joko enää koske Moneroa tai jakavat huolenaiheet tietosuojakolikoiden kanssa lohkoketjupohjaisten kryptovaluuttojen luokkana. Aloitetaan näiden käsitteleminen.

Yksi Moneron useimmin lainatuista kritiikeistä on se, että lohkoketjun pysyvyyden ja muuttumattomuuden vuoksi, tulevan teknologian mahdollisesti rikkoessa lohkoketjun, kaikki Moneron aiemmat liiketoimet paljastuisivat. Toisin sanoen yksityisyytesi olisi tikittävä kello.

Emme voi korostaa tätä tarpeeksi. Kirjaimellisesti jokaisessa tietosuojakolikossa, joka käyttää lohkoketjun menetelmiä hämärtämiseen ja yksityisyyteen on tämä puute, ja silti sitä käytetään usein vain Moneroa vastaan (ironista kyllä, monta kertaa yksityisyyskolikoiden kilpailussa, joilla on kaikilla sama ongelma), ja sitä käytetään myös tässä artikkelissa Moneroa vastaan. Vastaus tähän kritiikkiin saattaa olla yllättävää joillekin, mutta Monero voi itse asiassa olla vähemmän haavoittuvainen kuin muut yksityisyyden kolikot, koska sillä on monitahoinen lähestymistapa yksityisyyteen.

Monero piilottaa ulostulot(lähettäjät), summat ja vastaanottajat kolmen eri tekniikan avulla joita ovat: sormusallekirjoitukset, RingCT ja salatut osoitteet. Näistä sormusallekirjoitukset ovat heikoimpia ja herkimpiä sekä nykypäivän heuristiikalle että teoreettisille, tulevaisuuden yksityisyyttä rikkoville tekniikoille. Tämä on ollut Monero-yhteisön tiedossa jo vuosia ja käynnissä on aktiivista tutkimusta sormusallekirjoitusjärjestelmän parantamiseksi tai korvaamiseksi kokonaan.

Vaikka sormusallekirjoitus hajoaisi kokonaan, vain todellinen ulostulo paljastetaan. EI lähettäjää, vaan ulostulo. Ulostulon yhdistäminen identiteetin kanssa ei ole mahdotonta, mutta se vaatisi enemmän metatietoja ja resursseja. Yhdessä sen tosiasian kanssa, että RingCT:tä ja salattua osoitetta EI paljasteta, vaikutus pienenee entisestään.

On huomattava, että Wired-artikkeli käsittelee yllä olevia tietoja kevyesti osiossa, jossa he ottivat yhteyttä Riccardo 'fluffypony' Spagniin kommentoidakseen, mutta sille annettu aika on lyhyt ja näyttää melkein käsien heilautukselta. Ymmärryksen puute on erityisen ilmeistä, kun yritetään keskustella näistä asioista ihmisten kanssa, jotka jakavat artikkelin tahtomattaan nykypäivänä.

Toinen kritiikki, jota on paljon vaikeampi käsitellä, liittyy siihen miten ulkomaailma näkee Moneron ja miten se liittyy siihen, miten Moneroa ympäröivä yhteisö näkee kolikon. Tästä esimerkkinä lukijoiden ei tarvitse katsoa pidemmälle kuin itse artikkelin otsikko: "Pimeän verkon suosikkivaluutta on vähemmän jäljittämätön kuin miltä se näyttää."

Jokainen henkilö, joka viettää paljon aikaa Monero-yhteisössä voi todistaa, että yhteisö näkee paljon vaivaa osoittaakseen, kuinka vaikeaa todellista yksityisyyttä on saavuttaa, jopa markkinointi- tai adoptiopyrkimysten kustannuksella. Jos yhteisö tarjoaa runsaasti resursseja keskustella kolikosta ja sen puutteista tarkasti, jossain vaiheessa tietämättömyys muuttuu käyttäjän syyksi, joka luulee, että kolikko on kaikki mitä he tarvitsevat ollakseen 100% yksityisiä.

Tässä vaiheessa pitäisi olla selvää, että Monero-yhteisö suhtautuu vakavasti sekä yksityisyytensä että rehellisyytensä sen heikkouksista ja myöhemmistä parannuksista. Kyseisen artikkelin kaltaiset artikkelit kaipaavat täysin tätä Moneron innovaatiohenkeä. Se vertaa Moneroa muiden kryptovaluuttojen joukkoon, jotka esittävät suurenmoisia väitteitä, jotka ajattelevat vain voittoa ja kouluttamattomien sijoittajien saalistamista.

Todellisuus ei voisi olla toisenlainen. Monero on erittäin tietoinen heikkouksistaan, pyrkii jatkamaan rakentamista parantaakseen niitä, kiristääkseen löystyneitä liitoksia ja saavuttaakseen todellisen, mutta erittäin vaikean tavoitteen antaa maailmalle yksityinen, vaihdettavissa oleva kryptovaluutta, jota kaikki voivat käyttää. Tehdä se reilulla, hajautetulla ja yhteisölähtöisellä tavalla. Ehkä on aika luopua sensaatioista ja artikkelien jakamisesta keinona levittää tavaraa ja mainostaa kilpailijoita. Ehkä on aika kertoa toinen tarina.

Lue lisää