---
title: "Kaip Monero Stealth Addresses apsaugo jūsų tapatybę"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero įdiegė trijų dalių privatumo požiūrį. Šios technologijos yra [ skambėjimo parašai ](/knowledge/ring-signatures), kurie paslepia tikrąją išvestį (siuntėją), RingCT, kuris paslepia sumas, ir slapti adresai, kurie paslepia imtuvą. Šiandien aptarsime paskutinę iš šių paminėtų technologijų: slaptus adresus.

Yra daugybė priežasčių, kodėl asmuo gali norėti paslėpti, kam siunčia. Niekada neturime leisti niekam bandyti įtikinti, kad visi to pavyzdžiai yra nemalonus elgesys. Tokie dalykai, kaip siuntimas į nepopuliarią politinę partiją, aukojimas labdaros organizacijoms ar tų, kurias kultūra laiko „atšauktomis“, yra pavyzdžiai, kai gali norėti nuslėpti savo išlaidų elgesį, baiminantis pasekmių, tačiau jie yra visiškai teisėti.[X840X ] 

Skaidrioje blokų grandinėje adresai, kuriais siunčiamos operacijos, yra matomi visiems. Svarbu atsižvelgti į tai, kad jei patys kalnakasiai nesutinka su tuo, kur nukeliauja pinigai, jie gali nuspręsti jų nekasti į bloką, efektyviai cenzūruodami šį sandorį iš pažiūros cenzūrai atsparioje platformoje. Vienintelis būdas padaryti šią, tiesa, mažai tikėtina, cenzūrą neįmanomą, yra, jei kalnakasiai negali atskirti operacijų, nes visi grandinės metaduomenys yra užtemdomi įvairiomis priemonėmis. Kažkas, dėl ko Monero yra žinomas.

Monero išsprendžia šią skaidrių adresų problemą įdiegdamas slaptus adresus – technologiją, kurią iš pradžių Bitcoin Talk forumo naudotojas ByteCoin 2011 m. sukūrė (ryšys su Bytecoin, kuris vėliau integruos slaptus adresus, nežinomas). Tačiau dabartinė slaptų adresų forma turi keletą patobulinimų, palyginti su pradine idėja. Bet pirmiausia, norėdami pamatyti, kaip jie veikia, pakalbėkime apie raktus.

Sunku būti kriptovaliutų erdvėje ir negirdėti apie raktus. Tokios frazės kaip „sukurkite atsarginę privataus rakto kopiją“ yra dažnos, tačiau vidutinis Džo išgirdęs žodžius „viešasis raktas“ ir „privatus raktas“ išsigąsta ir mano, kad tai bus per daug techniška ir painu, kad suprastų. Bet nesijaudink. Elgsimės lėtai ir naudosime daugybę pavyzdžių.

Dviejų tipų kriptovaliutose naudojami raktai, kaip ką tik minėta, yra viešieji ir privatūs. Šie du raktai paprastai būna poroje, o tai reiškia, kad tam tikras viešasis ir privatusis raktas yra susieti vienas su kitu. Tiesą sakant, paprastai viešasis raktas yra išvedamas iš privataus rakto, o tai reiškia, kad jei žinote privatųjį raktą, jūsų piniginė gali atlikti dailius skaičiavimus ir kiekvieną kartą sugalvoti tinkamą viešąjį raktą.

Dabar, kaip rodo pavadinimai, viešasis raktas gali būti viešas be pasekmių. Paprastai tai yra adreso dalis, kurią bendrinate norėdami gauti pinigų į savo kriptovaliutų piniginę. Be to, privatus raktas yra toks, kurio nereikėtų bendrinti. Tai yra dalykas, leidžiantis pasirašyti ir išleisti operaciją, taigi, jei ji pavogta arba dalijamasi, niekšiška trečioji šalis gali išleisti jūsų pinigus, dažniausiai sau.

Paprasta analogija būtų pakabinama spyna ir jai atrakinti reikalingas raktas. Atidaryta pakabinama spyna gali būti laisvai dalijamasi, ir iš tikrųjų su šia spyna galima užrakinti bet ką, tačiau tik raktą turintis žmogus gali atidaryti viską, kas yra užrakinta. Pakabinamą spyną galima kopijuoti ir dalytis, rakto neturi būti.

Šie klavišai paprastai yra abstrahuojami nuo vartotojo, todėl niekada jų nematysite. Monero jie visai nerodomi kaip baisi raidinė ir skaitmeninė eilutė. Monero dažnas vartotojas žino privatųjį raktą kaip savo pradą. Sėkla (kurią turėtumėte užsirašyti, jei to nepadarėte) iš tikrųjų yra tik žmogaus skaitomas privatus raktas. 

Matote? Ne taip jau baisu. Atgal į slaptus adresus.

Kaip minėta anksčiau, slapti adresai iš pradžių buvo sukurti ne Monero, o Bitcoin. Tačiau, kaip ir daugumos naujų idėjų atveju, ši pirmoji iteracija turėjo problemų. Kitas bandymas įvyko, kai Nicholasas van Saberhaganas sukūrė CryptoNote, skirtą Bytecoin, Monero pirmtakui ([žr. mūsų Monero ir Bytecoin istoriją čia](/knowledge/monero-history)), ir nors tai buvo neabejotinas patobulinimas, palyginti su originalu, net jis turėjo kai kurie subtilūs trūkumai.

Galų gale, kitos jau nebeegzistuojančios privatumo kriptovaliutos kūrėjas sukūrė paskutinę iteraciją, kuri išsprendė iškilusias privatumo ir saugumo problemas, susijusias su idėja. Tai galiausiai pateko į Monero ir yra tai, kas naudojama šiandien.

Nors šios privatumo ir saugumo problemos buvo išspręstos, patys slapti adresai suteikė blokų grandinės technologijoms kitokio pobūdžio keistumo, kurio anksčiau nebuvo. Poreikis nuskaityti. Kadangi gavimo adresai nėra viešai rodomi blokų grandinėje, gavėjas niekada nežino, ar kokia nors operacija yra jo, todėl jis turi nuskaityti visas gaunamas operacijas naudodamas savo privatų raktą, kad pamatytų, ar tai jų.

Naudojant skaidrias monetas, tereikia patikrinti, ar operacija siunčiama jūsų adresu. Lengvas taip arba ne klausimas. Tačiau naudojant slaptus adresus, kiekviena operacija gali būti siunčiama jums, todėl turite pabandyti atrakinti kiekvieną iš jų privačiu raktu, kad pamatytumėte, ar jis atsidaro.

Tai yra papildomas veiksmas, kurio Bitcoin ir jo išvestiniai produktai neturi. Jis atlieka pradinę piniginės sąranką ir sinchronizuoja piniginę, kai jos neatidarėte kurį laiką, daug ilgiau nei Bitcoin. Tačiau kompromisas yra būtinas norint atrakinti privatumo garantijas. Reikėtų pažymėti, kad, skirtingai nei silpniausia privatumo trifecta vieta, skambučio parašai, slapti adresai nėra jautrūs euristikai. Ji remiasi išbandyta ir tikra elipsinės kreivės kriptografija, kuria remiasi visas internetas, todėl jos sulaužymas reikštų galą kompiuterių saugumui apskritai, o ne tik Monero.

Papildoma literatūra