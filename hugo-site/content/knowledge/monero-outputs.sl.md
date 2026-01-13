---
title: "Pojasnjeni Monero Izhodi (Outputs)"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, tako kot druge kriptovalute, uporablja rezultate kot sredstvo za obračunavanje sredstev. Mnogi uporabniki, ki poznajo kriptovalute, so verjetno že slišali za ta izraz, vendar vsi ne razumejo, kaj pomenijo in kako delujejo. Kot je raziskano v našem [članku o podpisih obročev ](/knowledge/ring-signatures), so izhodi dejanske enote, izmenjane v verigi blokov med pogodbenimi strankami. Podobno dolarskemu bankovcu, vendar znesek ni v fiksnem apoenu.

Če za delo prejmete plačilo 16 dolarjev, boste morda prejeli bankovec za en dolar, bankovec za pet dolarjev in bankovec za deset dolarjev. Imate 16 dolarjev, vendar imate v denarnici tudi tri različne bankovce. Če bi nekomu želeli plačati 6 dolarjev, bi lahko uporabili bankovca za 5 in 1, če pa bi nekomu želeli plačati 8 dolarjev, bi lahko uporabili samo 10 dolarjev in prejeli 2 dolarja nazaj v drobižu. Nazadnje, če bi nekomu želeli plačati 14 dolarjev, bi morali uporabiti vse tri bankovce in bi prejeli 2 dolarja nazaj v drobižu, a za trenutek, ko izročite vse tri bankovce, nimate denarja v denarnici, dokler ne dobite spremeni nazaj.

Monero deluje podobno. Recimo, da imate trgovino in trikrat prodate tri različne artikle. Morda boste prejeli 1,5 XMR, 2,25 XMR in 5,25 XMR za skupno 9 XMR, vendar imate v svoji denarnici tudi tri različne izhode prej navedenih apoenov. Tako kot pri dolarjih boste morda želeli nekomu plačati 3 XMR. Uporabite lahko samo izhod 5,25 XMR in prejmete 2,25 XMR nazaj kot drobiž ali pa združite izhoda 1,5 in 2,25 XMR in dobite 0,75 XMR nazaj kot drobiž.

Toda takoj, ko pošljete transakcijo, so izhodi, ki jih uporabljate, postavljeni v "zaklenjeno" stanje, kar pomeni, da so nedostopni, dokler ne prejmete nazaj spremembe. Protokol odklene sredstva (tj. vrne vam drobiž) po 10 potrditvah ali približno 20 minutah. Tako kot ko enkrat izročite dolarske bankovce iz denarnice, denarja ne morete več uporabiti, dokler ne prejmete drobiža od blagajne, je vaš Monero nedostopen, dokler ne prejmete nazaj drobiža.

Vrnimo se k primeru pošiljanja 3 XMR nekomu, vi pa uporabite izhod 5,25 XMR. Zdaj, ko čakate na 1,75 XMR nazaj v menjavi, ga ne morete uporabiti. Ta 1.75 XMR vam je nedostopen. Še vedno pa lahko uporabljate izhode 1,5 XMR in 2,25 XMR, saj ti niso bili porabljeni. Če se vrnemo k primeru z dolarji, če bi nekomu plačali 8 dolarjev, kot v prejšnjem primeru, ne bi mogli uporabiti 2 dolarjev, ki jih pričakujete nazaj v drobižu, dokler vam jih ne dajo, toda v tem primeru imate še vedno Bankovec za 10 $, ki je neuporabljen v vaši denarnici. To lahko še vedno uporabite za nakup, kar želite, medtem ko čakate na spremembo. Enako z Monero.

To je pogosto zmeda za nove uporabnike Monera. Pogosto ima uporabnik v svoji denarnici samo en izhod, ki ga je prejel od borze ali prijatelja. Recimo, da je ta izhod 20 XMR. V svoji denarnici nimajo drugih izhodov. Zdaj želita donirati dvema svojima najljubšima dobrodelnima organizacijama. Pošljejo 5 XMR prvi dobrodelni organizaciji, nato pa so zmedeni, ker, čeprav bi jim moralo ostati 15 XMR, ne morejo takoj poslati naslednje donacije drugi dobrodelni organizaciji. Kot ste morda uganili, je to zato, ker je 15 XMR zaklenjen. Ni ga mogoče porabiti, dokler ni vrnjen kot drobiž (10 potrditev ali približno 20 minut). Ko bodo njihova sredstva odklenjena, bodo lahko poslali svojo drugo donacijo.

Če samo ponovim, te težave ne bi imeli, če bi namesto tega imeli več izhodov, na primer dva izhoda 10 XMR ali podobno. Obe donaciji bi lahko poslali eno za drugo, ker bi prva donacija uporabila enega od 10 izhodov XMR (in počakala 10 potrditev, da bi prejela 5 XMR nazaj v spremembi), druga donacija pa bi uporabila ostalih 10 XMR. izhod.

Nekatere denarnice za kriptovalute imajo funkcijo, imenovano 'upravljanje izhodov', ki uporabniku preprosto prikaže, katere izhode trenutno ima (poleg njihove skupne vsote), in mu omogoča, da izbere, katere želi uporabiti, ko porabi njihova kriptovaluta.

Od zdaj GUI Monero samodejno izbira izhode za uporabnike, saj uporabniki, ki izbirajo lastne izhode, pogosto povzročajo zmedo ali v nekaterih primerih škodijo zasebnosti. Vendar pa so v izdelavi denarnice, kot je nov projekt denarnice Feather, ki bo vseboval te funkcije za upravljanje izhoda.

Veliko smo govorili o delu pošiljanja, vendar se na prejemnem koncu zgodi nekaj fascinantnega. Če se vrnemo k našemu primeru pošiljanja 3 XMR nekomu in uporabi vaših izhodov 1,5 XMR in 2,25 XMR v transakciji (medtem ko pričakujemo 0,75 XMR v spremembi), prejemnik NE prejme dveh izhodov 1,5 XMR in 2,25 XMR. Namesto tega prejmejo EN 3 izhod XMR.

V ozadju protokol združuje vse izhode, ki se uporabljajo za porabo, in daje prejemniku en izhod plačanega zneska ter pošlje en izhod spremembe nazaj pošiljatelju. Tako bo tudi pošiljatelj prejel en izhod nazaj kot drobiž, ne glede na to, ali je za pošiljanje transakcije uporabil dva, tri ali deset izhodov.

Upamo, da je to razjasnilo nekaj zmede glede rezultatov in delovanja notranjega računovodstva protokola, pa tudi običajnega uporabnika, ki se sooča s težavo zmede, ko naleti na zaklenjena sredstva. V drugem članku bomo raziskali upravljanje vaših rezultatov, da bi čim bolj zmanjšali možnost čakanja na odklenjena sredstva pred pošiljanjem prihodnjih transakcij.

Nadaljnje branje