---
title: "Kā Monero apakšadreses novērš identitātes saistīšanu"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero vienmēr ir atradis novatoriskus veidus, kā atrisināt sarežģītas privātuma problēmas. Bieži vien šīs inovācijas noved pie citiem jauninājumiem, un dažreiz šīs radītās tehnoloģijas var izmantot pat gadījumos, kas iepriekš nav izskatīti. Nekur tas nav vairāk parādīts kā Monero apakšadrešu tehnoloģijas gadījumā.

Apsveriet hipotētisku privātuma problēmu, kurā vienas adreses izmantošana vairākās platformās no šķietami nesaistītiem cilvēkiem var izraisīt minēto cilvēku sasaisti un deanonimizāciju. Vienkārši sakot, ja jūs būtu persona vārdā Billijs Džo Bobs un pārdotu ābolus par Bitcoin, jūs varētu publicēt savu Bitcoin adresi publiskā vietā, lai klienti varētu jums samaksāt. Pieņemsim, ka adrese sākas ar burtu un ciparu virkni 7XybV3... Bet, atmetot malā acīmredzamo privātuma risku, ka ikviens varēs pārbaudīt jūsu Bitcoin bilanci un redzēt, cik daudz esat pārdevis, ir otrs, par kuru netiek bieži runāts. Pieņemsim, ka jūs esat arī pagrīdes hakeris ar vārdu l33tz0r. Jūs veicat trauksmes celšanas darbu, stāstot sabiedrībai par valdības korupciju, un jums ir obligāti jāglabā sava identitāte noslēpumā. Jūs pieņemat Bitcoin ziedojumus par savu darbu un ievietojat adresi publiskā forumā. Tā ir tā pati adrese, kurā jūs pieņemat naudu no saviem Apple klientiem. 7XybV3....

Vienkāršs, bet postošs deanonimizācijas uzbrukums būtu izmantot interneta meklētājprogrammu, lai meklētu savu Bitcoin adresi. Ievietojot meklētājā adresi 7XybV3..., tiek parādīti divi dažādi rezultāti. Ābolu bizness un l33tz0r. Tas ir pietiekami, lai saistītu abas identitātes un deanonimizētu l33tz0r, kas var radīt biedējošas sekas no esošajiem spēkiem.

Ir svarīgi atzīmēt, ka šis uzbrukums ir iespējams ARĪ ar Monero. Lai gan Monero slēpj lielāko daļu ķēdes datu, šis uzbrukums neizmanto neko no tā. Tas izmanto tikai adresi, kas ir jāpublicē, lai saņemtu maksājumu. Publiski anonīmu ziedojumu gadījumā. Šis ir viens no iespējamiem veidiem, kā Monero lietotāji var netīši aizskart savu privātumu, un tas ir arī piemērs tam, ka, lai gan Monero ir visaugstākā līmeņa privātuma saglabāšanas ziņā, tas nav ložu necaurlaidīgs.

Parastais veids, kā apiet šo problēmu, bija vairāki maki. Ja katrai identitātei (vai lietošanas gadījumam) ir publicētas dažādas adreses, tās nevar saistīt. Taču šī konfidencialitāte ir spēkā tikai tad, ja lietotājs tās nekad nesajauc. Nejauši ievietojot nepareizu adresi, būtu tādas pašas sekas. Tāpat arī katras adreses sēkla ir jāglabā drošībā, palielinot drošības darbu, kas nepieciešams, ar katru jaunu maciņu.

Monero risinājums bija apakšadreses. Iespēja zem galvenās adreses izveidot absolūti milzīgu skaitu adrešu, izmantojot to kā sava veida sēklu. Katra ģenerētā apakšadrese var pieņemt Monero, un tā visa nonāk vienā makā. Izmantojot šo metodi, vienā adresē darbināmo identitāšu skaits ir milzīgs, vienlaikus samazinot drošības darbu līdz minimumam. Šīs adreses arī nav matemātiski savienojamas, tāpēc, ja vien lietotājs neizkliedz savu saistību pa pasauli, ārējam novērotājam būs lielas grūtības tās saistīt.

Bet no apakšadresēm parādījās vēl viens interesants lietojums - nīsto maksājumu ID aizstājējs.

Maksājumu ID bija veids, kā tirgotāji varēja noteikt, kurš klients kādu maksājumu nosūtījis. Tā kā Monero informācija ķēdē ir aizklāta, pārskaitījuma saņēmējs nevar redzēt, kura adrese to nosūtīja. Tas nozīmē, ka, ja ir līdzīgas cenas preces un vairāki pasūtījumi, var kļūt neiespējami noteikt, kurš ko nosūtījis. Maksājumu ID ir unikāla, nejauša virkne, ko ģenerē tirgotājs un piešķir klientam. Klients to pievieno kā atsevišķu lauku, nosūtot pārskaitījumu. Šī nejaušā virkne tiek ievietota blokķēdē kā daļa no pārskaitījuma, un šādā veidā tirgotājs var identificēt un kārtot ienākošos pārskaitījumus.

Šī metode bija kļūdaina vairākos veidos. Pirmkārt, tas mazina ķēdē esošo datu vienveidību. Papildu, unikāli metadati var padarīt dažus pārskaitījumus atšķirīgus no pūļa, tādējādi ļaujot veikt heiristisko analīzi. Tas jo īpaši attiecas uz gadījumiem, kad šie metadati nav ieviesti kā obligāti visiem. Tomēr, ja tas būtu obligāti visiem, blokķēdei tiktu pievienota nevajadzīga vieta, un tas netika īstenots. Tāpat, ja maksājuma ID kādreiz tiktu izmantots atkārtoti kāda iemesla dēļ, būtu elementāri saistīt divus pārskaitījumus. Tas parasti tika darīts ar maiņas noguldījumiem, un ikviens varēja viegli saistīt pārskaitījumus gan kā depozītu biržā, gan no vienas konkrētas personas.

Otrkārt, no UX perspektīvas maksājumu ID veido vēl vienu soli, pie kura kriptovalūtas lietotāji, kas nāk no citām monētām, nav pieraduši, un, ja tie tiek aizmirsti, tas rada lielas galvassāpes tirgotājam, kuram šie pārskaitījumi ir jāidentificē ar citiem līdzekļiem. . Parasti tas tika darīts, tieši sarunājoties ar katru klientu, kurš aizmirsa ievadīt maksājuma ID, un apstiprinot citu identificējošu informāciju, ko varēja zināt tikai viņi, piemēram, summas, nosūtīšanas datuma un pārskaitījuma ID kombināciju.

Šo papildu darbību daudzi palaida garām, un tas nonāca tiktāl, ka dažas biržas sāka iekasēt naudu no klientiem, ja viņu nauda bija manuāli jāidentificē, jo tika aizmirsts maksājuma ID. Citi sakoda zobus un pieņēma papildu atbalsta izmaksas, bet neviens par to nebija priecīgs.

Tam bija viens risinājums - integrētas adreses, kas apvienoja adresi un maksājuma ID vienā virknē, tāpēc to nevarēja aizmirst, taču adopcija bija diezgan vāja, neskatoties uz ieguvumiem, ko tirgotāji būtu guvuši no tā iekļaušanas. 

Interesantā notikumu pavērsienā tika izmantotas apakšadreses, lai glābtu situāciju. Iespēja ģenerēt lielu daudzumu apakšadrešu katrai galvenajai adresei un noteikt, kuri pārskaitījumi kādās apakšadresēs tika veikti, ļāva tirgotājiem elegantā veidā atbrīvoties no maksājumu ID, vienlaikus pieņemot nākamās paaudzes Monero tehnoloģiju. Kopš tā laika lielākā daļa biržu un tirgotāju rīku ir pārgājuši uz apakšadresēm kā primāro pārskaitījumu identifikācijas veidu.

Tas, kas sākās kā privātuma problēmas risinājums, kļuva par kaut ko daudz vairāk, kas atrisināja būtisku UX problēmu gan tirgotājiem, gan klientiem. Inovācijas rada vairāk jauninājumu, kas bieži vien var radīt negaidītas uzvaras ikvienam. Monero to ir redzējis atkal un atkal un pieliek lielas pūles, lai ieviestu jauninājumus, kas ir iespējams blokķēdē. Kurš zina, kādas citas lietas mēs varam atklāt kopā?

Lasīt tālāk