---
title: "Kā Monero atrisināja bloka izmēra problēmu, kas vajā Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Piezīme:** Iepriekš ieteicams izlasīt mūsu rakstus [ "Kāpēc Monero ir astes emisija"](/knowledge/monero-tail-emission) un [ "Monero mainošana: ar ko RanomX ir tik īpašs”](/knowledge/monero-mining-randomx). Šis raksts ir balstīts uz tajos ietvertajiem jēdzieniem._

Kad cilvēki apspriež problēmas ar blokķēdi, viens no pirmajiem uznirstošajiem vārdiem būs “paplašināšana”. Nav noslēpums, ka blokķēdes nav viegli paplašināmas, taču lielākā daļa cilvēku nezina, kāpēc.

Paplašināšana patiesībā ir vispārīgs termins, kas aptver divas dažādas kategorijas: protokola atbalsts un tehnoloģiskais atbalsts noteiktā laika brīdī. Šajā rakstā mēs koncentrēsimies uz vienu — protokola atbalsts būtībā ir mērs, cik pārskaitījumu protokols var apstrādāt noteiktā laikā.

Bitcoin ir bloka lieluma ierobežojums, kas nozīmē, ka, tiklīdz blokā ir iekļauts pietiekami daudz pārskaitījumu, visiem papildu pārskaitījumiem būs jāgaida rindā uz nākamo bloku. Noderīga līdzība būtu domāšana par vilcienu. Vilciens piestāj pie stacijas, un rindā esošie iestājas. Kad vilciens ir pilns, ikvienam, kas paliks ārpusē, būs jāgaida nākamais.

Bitcoin izmanto maksas, lai noteiktu, kurš iekļūst blokā vai nē. Atgriežoties pie vilciena analoģijas, var iedomāties, ka viens potenciālais pasažieris, kurš drīz tiks atstāts, piedāvā vilciena vadītājam piecus dolārus, lai iedotu viņam vietu. Citi pasažieri seko šim piemēram, un galu galā notiek solīšanas karš, lai noskaidrotu, kurš saņems kuras vietas. Vadītāja ziņā ir izlemt, vai viņš vēlas ievērot rindas kārtības politiku, taču viņa finansiālajās interesēs ir maksimāli palielināt savus ienākumus, piesaistot visaugstākās cenas solītājus.

Šajā analoģijā maineri ir vilcienu vadītāji. Viņi blokā var iekļaut jebkurus pārskaitījumus, kurus viņi vēlas, un parasti viņi izvēlas tos, kuriem ir visaugstākās maksas.

Savukārt, ja bloki nav pilni, cilvēkiem nav stimula maksāt lielas maksas, jo ir daudz brīvu sēdvietu.

2017\. gada kriptovalūtas uzplaukuma laikā Bitcoin tika pārpludināts ar pārskaitījumiem, un maksas pieauga tiem, kas vēlējās tikt iekļauti nākamajā blokā vai jebkurā tuvākajā nākotnē. Tie, kuri nevēlējās maksāt augstas maksas, redzēja, ka viņu pārskaitījumi tika atbīdīti pa stundām, dienām vai pat vispār izkrita no rindas.

Šis bija satraucošs ieskats par to, kā Bitcoin veiktos, ja notiktu bieži runātais par “masveida ieviešanu”. Ja Bitcoin izmantotu masveidā, viss būtu vēl sliktāk nekā 2017. gadā, un Bitcoin nebūtu pieejams nevienam, izņemot turīgos, vienkārši tāpēc, ka caurlaides spēja ir maza fiksēta bloka izmēra dēļ, izraisot maksu tirgus pārņemšanu. 

Monero to paredzēja un vēlējās darīt kaut ko citu. Tādēļ Monero izstrādātāji ieviesa dinamisku bloka izmēru.

Būtībā Monero ir arī bloka izmēra ierobežojums, taču tas ir elastīgs. Kad pārskaitījumu gaidīšanas rinda kļūst pārāk gara, maineri var palielināt bloku izmēru. Izmantojot mūsu vilciena analoģiju, varat iedomāties vairāk vilcienu vagonu pievienošanu, lai ietilptu papildu pasažieri. Kad rinda ir iztukšota, bloki samazinās līdz sākotnējam izmēram.

Ja šī ideja šķiet gudra, ir pamatoti jautāt, kāpēc Monero ir vienīgā kriptovalūta, kas to ir ieviesusi. Kāpēc gan to neieviest Bitcoin, lai apturētu caurlaides spējas problēmas?

Diemžēl tas nav iespējams. Tam ir vairāki iemesli un tālāk centīsimies tos izskaidrot.

Maineru interesēs vienmēr ir lieli bloki. Izmantojot lielus blokus, viņi var iekļaut vairāk darījumu un nopelnīt vairāk naudas no maksām, kā arī no bloka atlīdzības. Tas var izraisīt spamošanas uzbrukumus, kad kāds nosūta daudz mazu darījumu par nelielu samaksu, lai uzpūstu ķēdi. Maineri vienkārši palielinātu bloka izmēru, iekļaujot tos visus, jo nauda ir nauda, neatkarīgi no tā, cik maza. Tas radītu nemainīgi lielus blokus ar nelielu ekonomisku labumu. Bitcoin to atrisina, mākslīgi ierobežojot bloka lielumu, tādējādi radot maksas tirgu. Spamošanas uzbrucējiem būtu jāmaksā citiem lietotājiem maksas, un tas vairs nav lēti. Taču tas nozīmē, ka bloki kļūst pilni, atstājot dažus pārskaitījumus gaidīšanas režīmā, kā minēts iepriekš.

Kā Monero var nodrošināt dinamiskus bloku izmērus, bet izvairīties no spamošanas uzbrukumiem? Atbilde ir vienkārša, bet gudra. Ja bloks ir lielāks nekā parasti, tiek samazināta atlīdzība par bloku. Ja maineris vēlas palielināt bloka izmēru, atlīdzība, ko viņš saņem par šī bloka atrašanu, būs mazāka nekā parasti. Tātad maineri palielinās bloka izmēru tikai tad, kad lietotāju samaksātās pārskaitījumu maksas pārsniegs zaudēto bloka atlīdzības daļu. Piemēram, ja maineris zaudētu 0,5 XMR, palielinot bloka izmēru, un saņemto darījumu maksu summa būtu 0,4 XMR, tad, palielinot izmēru, būtu tīrie zaudējumi 0,1 XMR apmērā, un viņš to nedarītu. Un otrādi - ja kopējās darījumu maksas sastādītu 0,7 XMR, tīrā peļņa būtu 0,2 XMR, lai gan viņš zaudēs 0,5 XMR no bloka atlīdzības samazināšanas, tāpēc maineris palielinās izmēru.

Šie dinamiskie bloki ļauj tīklam organiski augt, mākslīgi neierobežojot bloka izmēru, lai izveidotu piespiedu maksas tirgu, vienlaikus izvairoties no spamošanas uzbrukumiem. Ir vēl vairāki aspekti, no kuriem mēs varam aplūkot šo ideju, un vairāki iemesli, kāpēc to nebūtu iespējams pievienot Bitcoin. Taču pagaidām mēs ceram, ka lasītājam ir izpratne par to, kā Monero apiet vairākas no problēmām, kas raksturīgas Bitcoin un tā atvasinājumiem, un to, kā tas plāno palielināt savu caurlaides spēju nākotnē.

Lasīt tālāk