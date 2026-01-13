---
title: "P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Eden od temeljnih ciljev projekta Monero je omogočiti pošteno, decentralizirano in varno omrežje z novimi in inovativnimi pristopi k rudarjenju z dokazi o delu (PoW), glavnemu načinu, s katerim so danes zaščitena omrežja kriptovalut.

Medtem ko je edinstven rudarski algoritem [, kot je RandomX](/knowledge/monero-mining-randomx), izredno pomemben za ta cilj, saj pomaga zagotoviti, da lahko vsakdo z računalnikom pošteno prispeva k varnosti omrežja, RandomX ne reši težav ki se lahko pojavijo zaradi bazenskega rudarjenja. Rudarjenje v bazenu je danes daleč najpogostejši način rudarjenja kriptovalut, vključno z Monero, a na srečo pojav rudarjenja p2pool to hitro spreminja.

## Kaj je bazensko rudarjenje?

Rudarjenje v bazenu je način za rudarje, da si delijo nalogo poskusa reševanja bloka v omrežju in nato enakomerno delijo nagrade za vse bloke, ki jih bazen najde. Čeprav to izjemno pomaga izenačiti pogostost plačila rudarjev v primerjavi s samim rudarjenjem Monero, ni brez resnih težav s centralizacijo.

Ko vsak rudar prispeva delo v skupino, se odreče nadzoru nad vsem delom, ki ga opravi, in blokom, ki jih najdejo v skupini samem, pri čemer verjamejo, da bo skupina pošteno in pravično razdelila nagrade med vse rudarje na podlagi količine delo, ki ga je opravil vsak. Če gre vse v redu, operater bazena zbere delo vseh rudarjev, ga predloži omrežju in enakomerno razdeli nagrade.

## Kakšna je težava pri rudarjenju v bazenu?

Na žalost je to v celoti odvisno od zaupanja in upravljavcu bazena omogoča, da z delom rudarjev počne nečedne stvari. Upravljavec sklada lahko opravljeno delo uporabi za napade na omrežje, poskuša podvojiti porabo sredstev (če je sklad dovolj velik) ali pa preprosto uporabi delo rudarjev za svoje plačilo in rudarjev nikoli ustrezno ne nagradi za njihovo delo. 

Največje tveganje za omrežje je, da ima bazen (ali več bazenov, ki delujejo skupaj) pod svojim nadzorom več kot 51 % zgoščene vrednosti omrežja, saj bi to lahko uporabili za goljufanje in dvakratno porabo sredstev (dvojna poraba). napad) ali poskušati spremeniti pravila omrežja.

## Kaj je p2pool?

p2pool je koncept, ki je bil prvotno ustvarjen za rudarjenje bitcoinov že leta 2011, vendar nikoli ni bil široko sprejet in ostaja praktično neuporabljen na bitcoinih. K sreči je SChernykh, eden ključnih razvijalcev za RandomX, svoj dopust preživel v iskanju rešitev za nekatere težave z implementacijo p2pool v bitcoinih in ponovnem pisanju vse programske opreme iz nič.

p2pool v Monero omogoča popolnoma nezaupljiv način za rudarje, da sodelujejo pri reševanju blokov in zaščitijo omrežje Monero z uporabo posebne programske opreme za vozlišča za p2pool, da si delijo delo.

To se izvede z uporabo novega blockchaina ("stranska veriga"), ki vodi evidenco dela, ki ga opravi vsak rudar, naslov njihove denarnice in koliko Monera so zaslužili, nato pa nagrado izplača v skrbništvu - manj in decentraliziran način. Ker ima ta stranska veriga veliko manj rudarjev, je veliko lažje najti in predložiti bloke v njej kot v glavnem omrežju Monero, zaradi česar rudarji lažje dobijo dosledna izplačila v primerjavi z rudarjenjem Monero samo.

## Kako p2pool rešuje težave bazenskega rudarjenja?

V p2pool ni centraliziranega bazena, upravljavca centraliziranega bazena ali ene same osebe, ki hrani sredstva in razdeljuje izplačila. Vse delo, ki ga kolektivno opravijo tisti, ki rudarijo prek p2pool, preveri veriga blokov p2pool in drugi operaterji vozlišč, da zagotovijo, da je zakonito, vsi rudarji pa so plačani glede na delo, ki so ga opravili takoj, ko je blok najden neposredno iz nagrade v tem najdenem bloku.

Ko se rudarji odločijo za uporabo p2pool namesto centraliziranega bazena, odstranijo vso moč in zaupanje upravljavcev bazena ter zagotovijo, da njihovo delo prispeva v dobro omrežja in k njihovim lastnim nagradam, zmanjša tveganje omrežnih napadov, zlorabe njihovega dela ali kraje nagrad, ki jim jih dolgujejo.

Ne samo, da jim to pomaga zaščititi lastne interese, ampak zmanjša tveganje, ki ga lahko centralizirana združenja predstavljajo za omrežje Monero kot celoto. Uporaba p2pool prav tako izjemno pomaga zmanjšati tveganje, ki bi ga lahko nacionalne države ali regulatorji predstavljali za zdravje omrežja, saj ni centraliziranih operaterjev bazenov, na katere bi lahko pritiskali, ni geografske koncentracije bazenov, na katere bi se lahko oprli, ali katere koli druge preproste točke pritiska za uporabo proti Monero.

## Kakšne so slabosti?

Na srečo je bil p2pool v Monero dobro zasnovan in dobro zgrajen ter deluje izjemno dobro! Vendar pa je glavna pomanjkljivost rudarjenja p2pool ta, da mora vsak rudar, ki želi uporabljati p2pool, zagnati lastno vozlišče Monero, zaradi česar je postopek začetka nekoliko bolj vključen. Vendar se to vozlišče nato uporabi za izračun vseh informacij, potrebnih za gradnjo in preverjanje blokov, ter zagotavlja, da ima rudar popoln nadzor nad svojim delom. Vozlišče lahko deluje tudi kot oddaljeno vozlišče za lastno denarnico rudarjev, prispeva k omrežju in še veliko več.

Druga ključna razlika od centraliziranega rudarjenja je, da bodo imeli majhni rudarji, ki uporabljajo p2pool, nekoliko več "variance" ali časa med izplačili kot veliki centralizirani bazen -- vendar 'je _izjemno_ pomembno je omeniti, da to sčasoma ne bo povzročilo manjšega zaslužka Monero! p2pool bo sčasoma enako donosen tudi za majhne rudarje kot centralizirana bazena. Nekaj te razlike je izravnano tudi s tem, da ima p2pool prvotno 0-odstotne provizije, saj ni centraliziranega operaterja bazena, ki bi plačeval njihove storitve! 

## Kako lahko začnem?

K sreči, zaradi odlične zasnove implementacije p2pool Monera' in številnih ljudi v skupnosti, ki so si vzeli čas za pomoč pri poenostavitvi postopka rudarjenja prek p2pool, je začetek sčasoma preprostejši. Obstaja več načinov za začetek rudarjenja s p2pool, a ker tehnične podrobnosti presegajo obseg tega članka, vas prosimo, da skočite na spodnjo povezavo, odvisno od vašega operacijskega sistema: 

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Kako lahko izvem več?

Če je to vzbudilo vašo radovednost glede rudarjenja p2pool, si spodaj oglejte nekaj dodatnih povezav in pojasnil o p2pool, kako deluje in kaj pomeni za Monero: 

  * [Uradni Github za p2pool](https://github.com/SChernykh/p2pool)
  * [Uradni dokumenti o uporabi p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool je zdaj live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, neke vrste "raziskovalec blokov" za p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: O njegovem razvoju P2Pool decentraliziranega XMR rudarskega bazena ](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Nadaljnje branje