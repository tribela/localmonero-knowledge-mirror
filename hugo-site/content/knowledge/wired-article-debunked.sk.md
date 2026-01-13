---
title: "Wired Magazine sa o Monere mýli, tu je dôvod"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
V oblasti súkromia aj kryptomien sa často šíria dezinformácie. Máme [článok, v ktorom je načrtnutých pätnásť bežných nesprávnych alebo zastaraných predpokladov o Monero](/knowledge/monero-myths-debunked), ale chceli by sme venovať čas jednému konkrétnemu článku, ktorý často citujú a šíria skeptici Monero.

V publikácii Wired bol 27. marca 2018 uverejnený [článok](https://www.wired.com/story/monero-privacy/), ktorý bol sám napísaný ako odpoveď na ďalší čerstvý článok publikovaný rôznymi akademikmi s názvom: „Empirická analýza sledovateľnosti v Monero Blockchain“.

Aj keď bol dokument spoluautorom jednotlivcov s jasným konfliktom záujmov (čítaj: sú poradcami a majú podiel v Zcash), dokument bol mierne prijatý komunitou Monero ako potvrdenie vecí, ktoré komunita už vedela a písali o nich vo svojich vlastných dokumentoch Monero Research Lab ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) a [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), z ktorých najskorší bol publikovaný pred štyrmi rokmi. Vyskytlo sa však aj niekoľko frustrácií, najmä konflikt záujmov, skutočnosť, že problémy už boli známe, prediskutované a v niektorých prípadoch aj napravené, a v tom čase hrubá nesprávna charakteristika záruk ochrany súkromia spoločnosti Monero. Komunita sa vyjadrila k predtlači diela a mnohé z ich odporúčaní sa dostali až do finálneho dokumentu.

Ale čo presne bolo nesprávne charakterizované? Skutočnosť, že Monero nemal nedostatky, o ktorých sa hovorilo v novinách viac ako rok. Transakcie pred rokom 2017 boli skutočne zraniteľné voči určitej forme úniku súkromia, ale v čase zverejnenia spoločnosť Monero riešila väčšinu obáv. Aby sme boli spravodliví voči autorom, diskutujú o nápravných opatreniach spoločnosti Monero v malej miere, ale nie natoľko, aby ovplyvnili vplyv, ktorý to malo na mediálny cyklus kryptomien v tom čase. Preto článok Wired.

Aj keď môžeme predmetný článok Wired skúmať ako dobový článok a nakoľko bol v tom čase pravdivý alebo nepravdivý, skutočnosť, že sa dodnes zdieľa ako dôvod, prečo sú záruky ochrany osobných údajov spoločnosti Monero slabé, si v skutočnosti vyžaduje analýzu o tom, ako sa diel drží v súčasnosti. Radi prijímame toto pozvanie.

Rýchle prečítanie článku ukazuje niekoľko senzáciechtivých riadkov, ako napríklad „[Tieto zistenia] by nemali znepokojovať nikoho, kto sa dnes pokúša tajne minúť Monero“ a celý tón článku, ktorý postuluje výskum ako „nový“, založené prevažne na publikácii. Samotná akademická práca obsahuje odporúčania, ako napríklad varovanie používateľov Monero pred potenciálnym ohrozením ich anonymity, a to aj napriek skutočnosti, že tieto diskusie nielenže prebiehali od roku 2014, ale komunita vyzývala ľudí, aby si Monero nekupovali a že bol veľmi experimentálny.

Ale čo samotná kritika? Realita je taká, že mnohé problémy s Monero ako súkromnou mincou buď už nie sú pravdivé pre Monero, alebo zdieľajú obavy týkajúce sa osobných mincí ako kategórie kryptomien založených na blockchaine. Začnime sa venovať týmto.

Jednou z najčastejšie citovaných kritík spoločnosti Monero je, že ak by budúca technológia mala narušiť súkromie, kvôli stálosti a nemennosti blockchainu by boli všetky minulé transakcie spoločnosti Monero odhalené. Inými slovami, vaše súkromie má na sebe tikajúce hodiny.

Nemôžeme to dostatočne zdôrazniť. Doslova každá minca na ochranu súkromia, ktorá využíva metódy on-chain na zahmlievanie a ochranu súkromia, má túto chybu, a napriek tomu sa často používa proti spoločnosti Monero (ironicky, mnohokrát konkurenčnými mincami na ochranu súkromia s rovnakým problémom) a používa sa aj v tomto článku. Reakcia na túto kritiku môže byť pre niektorých prekvapujúca, ale Monero môže byť v skutočnosti menej zraniteľné ako iné mince na ochranu súkromia, pretože má mnohostranný prístup k súkromiu.

Monero skrýva výstupy (odosielateľov), sumy a príjemcov prostredníctvom troch rôznych technológií, vyzváňacích podpisov, RingCT a tajných adries. Z nich sú prsteňové podpisy najslabšie a najviac náchylné na modernú heuristiku a teoretické, budúce technológie narúšajúce súkromie. Toto je komunite Monero známe už roky a prebieha aktívny výskum s cieľom úplne vylepšiť alebo nahradiť schému kruhových podpisov.

Avšak aj keby bol podpis zvonenia úplne porušený, odhalil by sa iba skutočný výstup. NIE odosielateľa (ako u jednotlivca), ale výstup. Spojenie výstupu s identitou nie je nemožné, ale vyžadovalo by si to viac metadát a zdrojov. Spolu so skutočnosťou, že RingCT a stealth adresa NEBUDE odhalená, ešte viac znižuje dopad.

Treba poznamenať, že článok Wired zľahka rozoberá vyššie uvedené informácie v časti, v ktorej požiadali Riccarda 'fluffyponyho' Spagniho o komentár, ale čas, ktorý mu bol venovaný, je krátky a takmer sa zdá, že táto zásadná informácia bola preč mávnutím ruky. Nedostatok porozumenia je zjavný najmä vtedy, keď sa pokúšate diskutovať o týchto veciach s ľuďmi, ktorí v modernej dobe zdieľajú tento článok chtiac-nechtiac.

Ďalšia kritika, ktorú je oveľa ťažšie riešiť, sa týka toho, ako sa na Monero pozerá vonkajší svet a ako to súvisí s tým, ako sa na mincu pozerá komunita okolo Monera. Napríklad, čitatelia nemusia hľadať ďalej ako názov samotného článku: „Obľúbená mena Dark Webu je menej nezistiteľná, ako sa zdá.“.

Každá osoba, ktorá trávi značné množstvo času v komunite Monero, môže potvrdiť, že komunita Monero zachádza do veľkej miery, aby ukázala, aké ťažké je dosiahnuť skutočné súkromie, a to aj na úkor marketingového úsilia alebo úsilia o adopciu. Ak komunita poskytuje dostatok zdrojov na presné diskusie o minci a jej nedostatkoch, v určitom bode sa neznalosť stane chybou používateľa, ktorý verí, že minca je všetko, čo potrebuje, aby bola 100% súkromná.

V tomto bode by malo byť zrejmé, že komunita Monero berie vážne aj svoje súkromie, ako aj svoju úprimnosť o jeho slabinách a následných vylepšeniach. Článkom, ako je ten, o ktorom ide, úplne chýba tento duch inovácie v Monero. Prirovnáva Monero k zástupom iných kryptomien, ktoré robia grandiózne nároky, pričom myslia len na zisk a na korisť nevzdelaných investorov-chtivých.

Realita nemôže byť odlišnejšia. Monero si je veľmi dobre vedomé svojich slabých stránok, snaží sa pokračovať v budovaní, aby ich vylepšoval, uťahoval uvoľnené spoje a dosiahol veľmi reálny, no veľmi ťažký cieľ dať svetu súkromnú, zameniteľnú kryptomenu, ktorú môžu používať všetci, a robte to všetko spôsobom, ktorý je spravodlivý, decentralizovaný a riadený komunitou. Možno je načase odložiť senzácie a zdieľanie článkov ako prostriedok na skracovanie a propagáciu konkurentov. Možno je čas povedať ďalší príbeh.

Ďalšie čítanie