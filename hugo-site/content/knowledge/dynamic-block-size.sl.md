---
title: "Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Opomba:** Zelo priporočamo, da bralec prebere naše zapise ["Zakaj ima Monero Tail emisijo"](/knowledge/monero-tail-emission) in ["Rudarjenje Monero: Kaj naredi RandomX tako poseben"](/knowledge/monero-mining-randomx). Ta članek temelji na tam predstavljenih konceptih._

Kadar koli posamezniki razpravljajo o težavah z verigo blokov, bo ena od prvih besed, ki se pojavi, 'razširitev'. Ni skrivnost, da se verige blokov slabo prilagajajo, vendar večina ljudi ne ve, zakaj.

Resnica je, da je skaliranje pravzaprav krovni izraz, ki zajema dve različni kategoriji: podporo za protokol in tehnološko podporo v danem trenutku. V tem članku se bomo osredotočili na eno, podpora protokolu je v bistvu merilo, koliko transakcij lahko protokol obravnava v določenem času.

Bitcoin ima omejitev velikosti bloka, kar pomeni, da ko je v blok vključenih dovolj transakcij, bodo morale vse dodatne transakcije čakati v vrsti za naslednji blok. Koristna analogija bi bila razmišljanje o vlaku. Vlak pripelje do postaje in tisti v vrsti se zgrinjajo noter. Ko je vlak poln, bo vsak, ki ostane zunaj, moral počakati na naslednjega.

Bitcoin uporablja pristojbine, da določi, kdo bo vstopil v blok in kdo ne. Če se vrnemo k analogiji z vlakom, si lahko predstavljamo, da eden od potencialnih potnikov, ki bo ostal zadaj, ponudi strojevodji pet dolarjev, da mu odstopi sedež. Drugi potniki mu sledijo in sčasoma se začne licitacijska vojna, kdo bo dobil kateri sedež. Strojevodja se mora odločiti, ali bo spoštoval pravilo "kdor prej pride, prej melje", vendar je v njegovem finančnem interesu, da čim bolj poveča svoj prihodek, tako da na vlak vzame tiste, ki ponudijo največ.

V tej analogiji so rudarji strojevodje. V blok lahko vključijo katere koli transakcije želijo, vendar bodo običajno izbrali tiste, ki imajo najvišje plačane pristojbine.

Alternativno, če bloki niso zelo polni, ljudje niso motivirani za plačevanje visokih pristojbin, saj je na voljo veliko prostih sedežev.

V času največjega razcveta kriptovalut leta 2017 je bil Bitcoin preplavljen s transakcijami, zato so se pristojbine za tiste, ki so želeli biti vključeni v naslednji blok ali kateri koli bližnji blok, povzpele v nebo. Tistim, ki niso bili pripravljeni plačati visokih pristojbin, so se njihove transakcije prestavile za več ur, dni ali celo povsem izpadle iz čakalne vrste.

To je bil pretresljiv vpogled v to, kako bi se Bitcoinu godilo, če bi prišlo do "množičnega sprejetja", o katerem se pogosto govori. Če bi Bitcoin uporabljale množice, bi bilo stanje še slabše kot leta 2017, Bitcoin pa bi bil nedostopen vsem, razen premožnim, preprosto zato, ker je prepustnost zaradi fiksne velikosti bloka majhna, zaradi česar bi prevladal trg pristojbin.

Monero je to predvidel in želel narediti nekaj drugačnega. Tako so Monero razvijalci implementirali dinamično velikost bloka.

V bistvu ima tudi Monero omejitev velikosti bloka, vendar gre za mehko omejitev. Ko je vrsta čakajočih transakcij predolga, lahko rudarji povečajo velikost blokov. Z našo analogijo z vlakom si lahko predstavljate, da bi dodali več vagonov, da bi lahko namestili dodatne potnike. Ko se čakalna vrsta izprazni, se bloki zmanjšajo na prvotno velikost, ki jo imajo v nadaljevanju.

Če se zdi, da je ta zamisel elegantna, se zdi smiselno vprašati, zakaj je Monero edina kriptovaluta, ki je to izvedla. Zakaj je ne bi dodali tudi pri Bitcoinu, da bi tako zaustavili težave s prepustnostjo? 

Na žalost to ni mogoče. Razlogov za to je več in potrudili se bomo, da jih pojasnimo.

Rudarju je vedno v interesu, da ima velike bloke. Z velikimi bloki lahko izvedejo več transakcij in zaslužijo več denarja s pristojbinami ter nagradami za bloke. To lahko privede do spam napadov, ko nekdo pošlje veliko majhnih transakcij z majhnimi pristojbinami, da bi napolnil verigo. Rudarji bi samo povečali velikost bloka in jih vključili vse, saj je denar še vedno denar, ne glede na to, kako majhen je. To bi privedlo do stalno velikih blokov z majhnimi ekonomskimi koristmi. Bitcoin to rešuje z umetnim omejevanjem velikosti blokov, s čimer ustvarja trg pristojbin. Napadalci na spam bi morali s pristojbinami preplačati druge uporabnike, kar ni več poceni. To pa pomeni, da se bloki zapolnijo, zaradi česar nekatere transakcije čakajo, kot je navedeno zgoraj.

Kako torej lahko Monero uporablja dinamične velikosti blokov, a se hkrati izogne napadom s spamom? Odgovor je preprost, a pameten. Ko je blok večji od običajnega, se uvede kazen za nagrado za blok. Če želi rudar povečati velikost bloka, bo nagrada, ki jo dobi za iskanje tega bloka, manjša, kot bi jo dobil sicer. Zato bodo povečali velikost bloka le, če bodo plačane pristojbine za transakcije uporabnikov odtehtale izgubljeni del nagrade za blok. Na primer, če bi rudar s povečanjem velikosti bloka izgubil 0,5 XMR, vsota plačanih pristojbin za transakcije pa bi znašala 0,4 XMR, bi bila neto izguba 0,1 XMR, če bi povečali velikost, zato tega ne bi storili. In obratno, če bi se seštevek pristojbin za transakcije povzpel na 0,7 XMR, bi bila neto pridobitev 0,2 XMR, čeprav bi izgubili 0,5 XMR zaradi kazni za nagrado za blok, zato bo rudar povečal velikost.

Ti dinamični bloki omogočajo organično rast omrežja, ne da bi obenem aritmetično omejevali velikost blokov, da bi ustvarili prisilni trg pristojbin, hkrati pa se še vedno izogibajo spam napadom. Obstaja še več zornih kotov, s katerih lahko pogledamo na to zamisel, in več razlogov, zakaj je ne bi bilo mogoče dodati Bitcoinu, vendar za zdaj upamo, da bralec razume, kako Monero zaobide več težav v Bitcoinu in njegovih derivatih ter kako namerava v prihodnosti povečati svojo prepustnost.

Nadaljnje branje