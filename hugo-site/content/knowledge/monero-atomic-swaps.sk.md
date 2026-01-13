---
title: "Ako budú fungovať atómové swapy v Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
V snahe o decentralizáciu a skutočný systém bez povolení je len málo vecí v priestore kryptomien tak žiadaných ako decentralizované burzy a atómové swapy. Od svojho založenia sa Monero snažilo implementovať atómové swapy, pretože funkcie ochrany osobných údajov vytvárajú jedinečné problémy pri navrhovaní protokolu.

Najskôr sa však uistime čo sú atómové swapy? Atómový swap je protokol, pomocou ktorého je možné vymieňať dve rôzne kryptomeny na rôznych blockchainoch nedôveryhodným spôsobom bez sprostredkovateľa. To znamená, že ak by niekto chcel vymeniť kryptomenu A za kryptomenu B, mohol by to urobiť bez výmeny, centralizovanej alebo decentralizovanej. Ako si možno predstaviť, vyžaduje si to rozsiahly výskum a úplné technické detaily, ktoré to umožňujú, sú dosť komplikované. LocalMonero je tu, aby pomohol a poskytol jednoduché vysvetlenie pre bežného človeka.

Na začiatok zvážme najjednoduchšiu formu atómového swapu, ako ju implementuje Bitcoin. Ak chce niekto vymeniť bitcoiny za inú mincu, ktorá používa rovnakú technológiu kontraktu hash time lock, môže tak urobiť nasledujúcim spôsobom. Alica má bitcoiny (BTC), ale chce Litecoin (LTC) a Bob má LTC, ale chce BTC. Rozhodnú sa urobiť atómovú výmenu, takže každý dostane mincu, ktorú chce. Alica posiela svoje BTC na špeciálnu adresu pomocou skriptov, ktoré uzamknú prostriedky, takže k nim nemá prístup ani ona. Môžete si to predstaviť tak, že Alica vloží svoje BTC do skrinky. Keď je skrinka vyrobená, dostane kľúč a pošle ho hash Bobovi. Teraz Bob nemá samotný kľúč, iba hash, takže zatiaľ nemá prístup k finančným prostriedkom.

Bob používa tento hash ako zárodok, z ktorého si vygeneruje svoj vlastný lockbox a pošle tam svoj LTC, kde je tiež uzamknutý. Keďže hash Alicinho kľúča bol použitý ako zárodok, z ktorého bola vyrobená Bobova skrinka, môže použiť svoj kľúč na získanie LTC v Bobovej skrinke. Jej kľúč sedí! Ale pomocou matematickej mágie voodoo, keď použije svoj kľúč na otvorenie zámku LTC, odhalí kľúč Bobovi, ktorý ho potom môže použiť na získanie BTC, ktoré vložila do svojej skrinky. Týmto spôsobom, bez sprostredkovateľa, Alica a Bob úspešne vymenili svoje aktíva.

Je tu však malý problém. Čo ak Alice pošle do svojej skrinky a Bob sa rozhodne, že už nechce obchodovať. Teraz, keďže Alica nemá prístup k svojim BTC, ktoré zamkla, a Bob nedokončí svoju časť transakcie, Alica navždy stratí svoje peniaze. Našťastie má bitcoin malú technológiu nazývanú transakcie vrátenia peňazí, a tak po určitom čase, ak Bob nenárokuje BTC, skripty majú zabudovaný bezpečnostný systém, kde sa BTC automaticky vráti Alici. Toto bola primárna rýchlosť pre implementáciu atómových swapov spoločnosti Monero. Vďaka technológii ochrany osobných údajov [ spoločnosti Monero na ochranu súkromia ](/knowledge/ring-signatures) je odosielateľ transakcie vždy neistý. Ako môže protokol vykonať transakciu vrátenia peňazí, ak ani on nevie, odkiaľ transakcia pochádza?

V roku 2017 malá skupina výskumníkov načrtla inú metódu, ktorou by výmena atómov fungovala v Monero. Po niekoľkých rokoch zdokonaľovania výskumníci dokončili proces, pomocou ktorého by Monero bolo schopné vykonávať atómové swapy s bitcoinmi, dokonca aj bez refundačných transakcií.

Ako pri mnohých veciach tejto úrovne technickej zložitosti, naše vysvetlenie niektoré veci príliš zjednoduší, aby vyjadrilo myšlienku, ale stále poskytne solídnu predstavu o mechanizmoch, pomocou ktorých by tento proces fungoval.

Alica (ktorá má XMR a chce BTC) aj Bob (ktorý má BTC a chce XMR) si musia stiahnuť a spustiť program, ktorý podporuje atómovú výmenu. Toto môže byť implementované do peňaženiek, decentralizovaných búrz alebo špeciálnych špecifických programov, ale v softvéri musí byť spustený protokol atomic swap. V prvom kroku sa klienti Alica a Bob navzájom spoja a vytvoria niekoľko spoločných tajomstiev a kľúčov. V tomto kroku sa vytvorí nová adresa Monero, pričom Alica má jednu polovicu kľúča a Bob druhú. Zatiaľ tam nie je žiadne Monero, takže nie je čo míňať. Posledná vec, ktorú treba poznamenať k tejto adrese, je, že obaja majú kľúč na zobrazenie tejto peňaženky, takže môžu obaja nahliadnuť dovnútra a zistiť, či alebo kedy príde Monero.

V druhom kroku Bob odošle svoje BTC na špeciálnu adresu, podobnú protokolu Bitcoin atomic swap, o ktorom sme už hovorili. Keď Alica vidí, že BTC prichádza na túto adresu na blockchaine, pošle svoje Monero na Monero adresu, ku ktorej majú ona aj Bob polovicu kľúča. Bob si môže overiť, že Monero prišlo, pretože má aj kľúč na zobrazenie, a keď uvidí, že Monero je bezpečne v peňaženke, pošle Alici kúsok kľúča, ktorý jej umožní vybrať bitcoiny. Podobne ako pri inom protokole, proces nárokovania Bitcoinu odhaľuje Bobovi jej polovicu kľúča Monero. Teraz má Bob obe polovice, takže si môže nárokovať Monero, zatiaľ čo Alica má len svoju polovicu, takže sa ju nemôže pokúsiť vziať skôr ako on.

Ak ste sa na to všetko pozreli a stále ste trochu zmätení v tom, ako Monero dokázalo obísť problém vrátenia peňazí, odpoveď je celkom jednoduchá. Keďže samotné Monero nemá transakcie vrátenia peňazí, čitateľ by si mal všimnúť, že bitcoin (ktorý má transakcie vrátenia peňazí) je odoslaný ako prvý a až po overení, že je na blockchaine, sa odošle Monero. To umožňuje spoločnosti Monero využívať schopnosť bitcoinu skriptovať pri refundačných transakciách a využívať ich bez toho, aby bolo potrebné mať tieto schopnosti.

Výmena atómu je teraz dokončená, ale odtiaľto má Bob niekoľko možností pre svoj novo nárokovaný XMR. Môže použiť túto peňaženku Monero tak, ako je, alebo presunúť XMR do inej peňaženky, ktorú už vlastní. Bob s najväčšou pravdepodobnosťou presunie Monero do inej peňaženky, pretože Alica má stále kľúč na zobrazenie a vidí dovnútra.

Krása tohto protokolu je v tom, že je stále celkom nový a je tu veľa priestoru na optimalizáciu. Je tiež dosť flexibilný vo svojej architektúre, takže implementácia v iných peňaženkách alebo decentralizovaných burzách by mala byť jednoduchá a presne zapadať do ich existujúcej architektúry.

Ďalšie čítanie