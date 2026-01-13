---
title: "Kaip žiedo parašai užgožia Monero išvestis"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero kriptovaliutų erdvėje žinomas kaip privatumo monetų karalius. Nors visi žino, kad Monero užtikrina gerą privatumą, ne tiek daug supranta, kaip privatumas veikia.

Daugelyje kitų privatumo monetų skelbiamos palyginimo diagramos infografikos, kuriose pateikiami kiekvienos monetos privatumo technologijos pavadinimai, o daugumoje Monero technologija žymima kaip RingCT, tačiau tai tiesa tik iš dalies. Monero iš tikrųjų turi trijų aspektų požiūrį į privatumą. Viena technologija, skirta paslėpti operacijos gavėją, kita, skirta paslėpti išsiųstą sumą, ir kita naudojama išvestis. Tai yra atitinkamai slapti adresai, skambėjimo CT ir skambėjimo parašai.

Šis trijų krypčių požiūris reiškia, kad sugedus vienai iš technologijų, kitų nebūtinai ištiks toks pat likimas. Žiediniai parašai yra silpniausia privatumo schemos grandis; žodis silpnas čia reiškia labiausiai jautrius euristiniams išpuoliams. Skirkime šiek tiek laiko juos ištirti, ar ne?

Kaip minėta pirmiau, skambėjimo parašų tikslas yra uždengti operacijos metu naudojamą išvestį. Jei kriptovaliutos „įvesties / išvesties“ terminologija jums kelia painiavą, nesijaudinkite. Iš tikrųjų tai nėra taip sudėtinga. Kai išgirsite žodį „išvestis“, tiesiog pagalvokite, kad patikrintumėte. Vienas iš tų dalykų, nebėra toks įprastas, kuriuo žmonės moka atsiskaityti. Kaip čekis, jis gali būti pažymėtas bet kokia suma – 10 USD, 32,50 USD ir tt ir yra keičiamas tarp sandorio šalių. Kriptovaliutų išvestis atlieka šias funkcijas.

Kai kas nors jums sumoka 10 Monero, gaunate 10 XMR išvestį. Ši išvestis turi reikšmę (10) ir yra paimama iš siuntėjo piniginės, lygiai taip pat, kai mokate už paslaugą, sąskaita paliekama jūsų fizinėje piniginėje ir perduodama asmeniui, iš kurio perkate.

Išvestis slepiama sukuriant jauko išėjimų žiedą (taigi ir pavadinimą). Tačiau šie masalai nėra „netikra“ produkcija. Tai yra tikri ankstesni blokų grandinės išėjimai, neturintys nieko bendra su dabartine operacija, tačiau išoriniam stebėtojui kiekvienas iš šių išėjimų gali atrodyti taip pat tikėtinas, kaip ir tikrasis. Jauko išėjimų rinkinio dydis, plius tikrasis, vadinamas žiedo dydžiu, o šiuo metu Monero yra vienuolika. Taigi yra dešimt jaukų išėjimų ir vienas tikras.

Kodėl tiesiog nepadidinus šio skaičiaus iki 100 ar net 1000? Kuo daugiau, tuo geriau, tiesa? Na, žvelgiant iš privatumo perspektyvos, taip, tačiau reikia atsižvelgti į kitus dalykus. Grįžkime prie fizinio pavyzdžio, kad suprastume, ką turiu omenyje. Jei norite paslėpti vieną iš savo dolerio kupiūrų tarp dešimties jaukų, už kiekvieną norimą išleisti dolerį piniginėje turėsite neštis maždaug vienuolika dolerių. Vienas tikras doleris ir dešimt netikrų. Tai jau tampa gana sudėtinga, jei norite išleisti net kelis dolerius. Dabar įsivaizduokite, kad jauko sumą padidinome iki 1000. Už kiekvieną norimą išleisti dolerį turėsite neštis apie 1001 dolerį. Norėdami nusipirkti vieną saldainį, turėsite nešiotis portfelį! Svarbu pažymėti, kad žiedo parašai neveikia taip, pavyzdžiui, patys jaukai nėra parašo dalis, o tik nuorodos į juos, tačiau tikimės, kad ši analogija gali būti šiek tiek naudinga vaizduojant pagrindines sąvokas.< /p>

Panašiai veikia blokų grandinės jaukai. Kiekvienas pridėtas masalas padidina operacijos laiką ir padidina patikrinimo išlaidas. Kiekvienas mazgas turi atsisiųsti visą kiekvienos operacijos žiedo parašą, o kiekviename žiediniame paraše yra tikroji išvestis, taip pat jaukai. Negana to, jis turi patikrinti matematiką, ar bent vienas iš šių išėjimų yra tikras, o matematinės patikros laikas taip pat didėja su kiekvienu masalu. Tai reiškia, kad turime rasti laimingą vidurį, kai žiedo dydis yra pakankamai didelis, kad pakankamai užgožtų tikrąją išvestį, net ir prieš daugelį euristinių atakų, bet pakankamai mažas, kad blokų grandinė nepadidėtų didžiuliu greičiu. Nepakanka pasirinkti savavališką skaičių arba tiesiog padidinti žiedo dydį, kai sumažiname parašą (pvz., naudojant CLSAG). Monero bendruomenė nori konkrečių, matematinių įrodymų, dėl kurių žiedo dydis siūlo geriausius kompromisus. Skaičius per mažas, o privatumas nebus pakankamai stiprus prieš euristines atakas. Per didelis, todėl galime gauti tik nedidelę naudą privatumo srityje ir be reikalo kentėti dėl mastelio.

Paskutinis dalykas, kurį reikia paminėti. Kai kurios Monero literatūros supaprastina ir sako, kad žiediniai parašai slepia siuntėją, tačiau tai nėra visiškai tiesa, o skirtumas yra ne tik pedantiškas. Skirtumas tarp siuntėjo (žmogaus) ir išvesties (sąskaitos) yra didelis, kai reikia išsaugoti privatumą. Nors išvestis gali būti susijusi su siuntėju, pati išvestis nėra lygi siuntėjui. Taigi, net jei žiedinis parašas buvo sulaužytas, jis nebūtinai siejasi su asmens tapatybe, o suma ir gavėjas vis tiek yra paslėpti, taip sumažinant žalą visų šalių privatumui.

Tai nereiškia, kad sulaužytas žiedo parašas yra nereikšmingas. Bet kokie nutekėję metaduomenys yra blogi ir gali atskleisti daugiau informacijos, nei manome, ypač kai jie naudojami kartu su kitais metaduomenimis. Todėl stengiamės užtikrinti, kad pasirinktas žiedo dydis būtų pagrįstas akademiniu tikslumu, kiti metaduomenų nutekėjimai būtų kuo mažesni, o naudotojo patirtis būtų veikianti pagal numatytuosius nustatymus.

Tačiau jei sulaužyto parašo tikimybė vis dar kelia nerimą, horizonte yra neįtikėtinų naujienų. Naujos kartos privatumo protokolai, su kuriais dirbama, pvz., „Triptych“, „Arcturus“ ir „Lelantus“, turi tikrai puikių galimybių. Šiuose protokoluose dydis didėja logaritmiškai, o ne tiesiškai, nes didėja žiedo dydis. Tai reiškia, kad galime sutalpinti 100 jaukų, tačiau naudojama erdvė yra artimesnė 10 žiedo dydžiui senosios technologijos atveju. Tai yra didelis skirtumas ir žymiai pagerins privatumą visame pasaulyje.

Katės ir pelės žaidime, kuris yra privatumas, Monero nuolat diegia naujoves, siekdama išlikti priekyje ir užtikrinti geriausią praktinį privatumą visiems.

Papildoma literatūra