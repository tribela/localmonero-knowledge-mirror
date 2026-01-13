---
title: "Kā Monero darbosies atomiskā apmaiņa"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Tiecoties pēc decentralizācijas un pilnīgas bezatļauju sistēmas, ne daudzas lietas kriptovalūtu telpā ir tik iekārotas kā decentralizētas biržas un atomiskās apmaiņas. Kopš darbības sākuma Monero ir cīnījies, lai īstenotu atomisko apmaiņu, jo privātuma funkcijas rada specifiskas problēmas, mēģinot izstrādāt protokolu.

Bet vispirms atkāpsimies. Kas ir atomiskā apmaiņa? Atomiskā apmaiņa ir protokols, ar kuru dažādās blokķēdēs var apmainīties ar divām dažādām kriptovalūtām bezuzticības veidā bez starpniekiem. Tas nozīmē, ka, ja kāds vēlētos apmainīt kriptovalūtu A pret kriptovalūtu B, viņš to varētu izdarīt bez centralizētas vai decentralizētas biržas. Kā varētu iedomāties, tas prasa ievērojamu izpēti, un visas tehniskās detaļas, kas to padara iespējamu, kļūst diezgan sarežģītas. Atkal LocalMonero ir šeit, lai palīdzētu un sniegtu vienkāršu skaidrojumu parastajam cilvēkam.

Lai sāktu, apskatīsim vienkāršāko atomiskās apmaiņas veidu, ko ieviesis Bitcoin. Ja kāds vēlas apmainīt Bitcoin pret citu monētu, kas izmanto to pašu hash time lock kontrakta tehnoloģiju, viņš to var izdarīt šādā veidā. Alisei ir Bitcoin (BTC), bet viņa vēlas Litecoin (LTC); Bobam ir LTC, bet viņš vēlas BTC. Viņi nolemj veikt atomisko apmaiņu, lai katrs saņemtu monētu, kuru vēlas. Alise nosūta savu BTC uz īpašu adresi, izmantojot skriptus, kas bloķē līdzekļus, lai pat viņa nevarētu tiem piekļūt. Jūs varat to iedomāties šādi: Alise ieliek savu BTC slēdzamā kastē. Kad kaste ir izgatavota, viņa saņem atslēgu un nosūta šīs atslēgas hash Bobam. Tagad Bobam nav pašas atslēgas, tikai hash, tāpēc viņš vēl nevar piekļūt līdzekļiem.

Bobs izmanto šo hash kā sēklu, no kuras viņš ģenerē savu bloķēšanas kastīti, un nosūta savu LTC uz to, kur tas arī tiek bloķēts. Tā kā Alises atslēgas hash tika izmantots kā sēkla, no kuras tika izgatavota Boba slēdzamā kaste, viņa var izmantot savu atslēgu, lai pieprasītu LTC Boba kastē. Viņas atslēga der! Bet, izmantojot matemātikas voodoo maģiju, kad viņa izmanto savu atslēgu, lai atvērtu LTC slēdzeni, viņa atklāj atslēgu Bobam, kurš pēc tam var to izmantot, lai pieprasītu BTC, ko viņa ievietoja savā kastē. Tādā veidā, bez starpnieka, Alise un Bobs ir veiksmīgi apmainījuši savus līdzekļus.

Taču ir neliela problēma. Ko darīt, ja Alise nosūta uz savu kasti, un Bobs nolemj, ka vairs nevēlas tirgoties? Tagad, tā kā Alise nevar piekļūt savam BTC, ko viņa bloķēja, un Bobs nepabeigs savu darījuma daļu, Alise vienkārši zaudē savu naudu uz visiem laikiem. Par laimi, Bitcoin ir neliela tehnoloģija, ko sauc par atmaksas pārskaitījumiem, un tāpēc pēc kāda laika, ja Bobs nav pieprasījis BTC, skriptos ir iebūvēts atteices drošinātājs, kurā BTC automātiski tiks atgriezts Alisei. Tas bija galvenais Monero atomiskās apmaiņas ieviešanas kavēklis. Monero [gredzenveida parakstu privātuma tehnoloģijas ](/knowledge/ring-signatures) dēļ pārskaitījuma sūtītājs nav zināms. Kā protokols var veikt atmaksas pārskaitījumu, ja pat tas nezina, no kurienes tika veikts pārskaitījums?

2017\. gadā neliela pētnieku grupa izklāstīja atšķirīgu metodi, ar kuras palīdzību atomiskās apmaiņas darījumi darbotos Monero. Pēc vairāku gadu pilnveidošanas pētnieki pabeidza procesu, kurā Monero varētu veikt atomiskās apmaiņas darījumus ar Bitcoin, pat bez atmaksas pārskaitījumiem.

Tāpat kā ar daudzām šāda līmeņa tehniskās sarežģītības lietām, mūsu skaidrojums pārlieku vienkāršo dažas lietas, taču tas joprojām sniegs stabilu priekšstatu par mehānismiem, uz kuriem šis process balstīts.

Gan Alisei (kurai ir XMR un vēlas BTC), gan Bobam (kuram ir BTC un kurš vēlas XMR) ir jālejupielādē un jāpalaiž programma, kas atbalsta atomiskās apmaiņas darījumu. To var ieviest makos, decentralizētās apmaiņās vai īpašās programmās, taču programmatūrā ir jādarbojas atomiskās apmaiņas protokolam. Pirmajā solī Alises un Boba programmatūras izveido savienojumu viena ar otru un izveido vairākus kopīgus noslēpumus un atslēgas. Šajā darbībā tiek izveidota jauna Monero adrese, kurā Alisei ir viena atslēgas puse, bet Bobam - otra. Tomēr Monero vēl nav un arī nav, ko tērēt. Pēdējā lieta, kas jāatzīmē saistībā ar šo adresi, ir tāda, ka viņiem abiem ir šī maka skata atslēga, lai viņi abi varētu ieskatīties iekšā un redzēt, vai Monero pienāk un kad tas pienāk.

Otrajā darbībā Bobs nosūta savu BTC uz īpašu adresi, kas ir līdzīga Bitcoin atomiskās apmaiņas protokolam, par kuru mēs jau runājām. Kad Alise redz, ka BTC ierodas šajā blokķēdē, viņa nosūta savu Monero uz Monero adresi, uz kuru viņai un Bobam ir viena atslēgas puse. Bobs var pārbaudīt, vai Monero ir pienācis, jo viņam ir arī skata atslēga, un, tiklīdz viņš redz, ka Monero ir droši ievietots makā, viņš nosūta Alisei atslēgas gabalu, kas ļaus viņai izņemt Bitcoin. Līdzīgi kā citā protokolā, Bitcoin pieprasīšanas process atklāj Bobam pusi no Monero atslēgas. Tagad Bobam ir abas puses, tāpēc viņš var pieprasīt Monero, savukārt Alisei ir tikai viņas puse, tāpēc viņa nevar mēģināt to paņemt pirms viņa.

Tātad, ja aplūkojat visu šo informāciju un joprojām esat mazliet neizpratnē par to, kā Monero varēja apiet atmaksas pārskaitījumu problēmu, atbilde ir pavisam vienkārša. Tā kā Monero pašam nav atmaksas pārskaitījumu, lasītājam vajadzētu pamanīt, ka vispirms tiek nosūtīts Bitcoin (kuram ir atmaksas pārskaitījumi), un tikai pēc tam, kad ir pārbaudīts, ka tas ir blokķēdē, tiek nosūtīts Monero. Tas ļauj Monero izmantot Bitcoin spēju programmēt atmaksas darījumus un izmantot to priekšrocības, pašam neizmantojot šīs iespējas.

Atomiskā apmaiņa tagad ir pabeigta, taču no šejienes Bobam ir dažas iespējas savam nesen pieprasītajam XMR. Viņš var izmantot šo Monero maku tādu, kāds tas ir, vai pārvietot XMR uz citu maku, kas viņam jau pieder. Bobs, visticamāk, pārvietos Monero uz citu maku, jo Alisei joprojām ir apskates atslēga un viņa var ieskatīties.

Šī protokola skaistums ir tajā, ka tas joprojām ir diezgan jauns, un tajā ir daudz vietas uzlabojumiem. Tas ir arī diezgan elastīgs savā uzbūvē, tāpēc ieviešana citos makos vai decentralizētajās apmaiņās būtu vienkārša un saderīga ar to esošo uzbūvi.

Lasīt tālāk