---
title: "Ako Monero Stealth adresy chránia vašu identitu"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero implementovalo trojrozmerný prístup k ochrane súkromia. Týmito technológiami sú [vyzváňacie podpisy](/knowledge/ring-signatures), ktoré skryjú skutočný výstup (odosielateľa), RingCT, ktoré skryje sumy, a tajné adresy, ktoré skryjú príjemcu. Dnes budeme diskutovať o poslednej z týchto spomenutých technológií: stealth adresy.

Existuje veľa dôvodov, prečo by jednotlivec mohol chcieť skryť, komu posiela. Nikdy nesmieme dovoliť, aby sa nás niekto pokúšal presvedčiť, že všetky príklady tohto správania sú nechutné. Veci ako posielanie nepopulárnej politickej strane, darovanie charitatívnym organizáciám alebo podpora tých, ktoré kultúra považuje za „zrušené“, sú príklady toho, kde by niekto mohol chcieť skryť svoje míňacie správanie zo strachu z následkov, ale sú vo svojej podstate úplne legitímne.

Na transparentnom blockchaine sú adresy, na ktoré odosielate svoje transakcie, viditeľné pre všetkých. Je dôležité vziať do úvahy, že ak samotní baníci nesúhlasia s tým, kam peniaze idú, môžu sa rozhodnúť neťažiť ich do bloku, čím efektívne cenzurujú túto transakciu na platforme, ktorá je zdanlivo odolná voči cenzúre. Jediný spôsob, ako znemožniť túto, pravdaže nepravdepodobnú, cenzúru je, ak baníci nedokážu rozlíšiť medzi transakciami, pretože všetky metadáta v reťazci sú zakryté rôznymi prostriedkami. Niečo, čím je Monero známe.

Monero rieši tento problém transparentných adries implementáciou stealth adries, čo je technológia, ktorá bola pôvodne vytvorená pre Bitcoin v roku 2011 používateľom fóra Bitcoin Talk ByteCoin (vzťah k Bytecoinu, ktorý by neskôr integroval utajené adresy, nie je známy). Súčasná podoba stealth adries má však oproti pôvodnej myšlienke niekoľko vylepšení. Ale najprv, aby sme videli, ako fungujú, povedzme si niečo o kľúčoch.

Je ťažké byť v priestore kryptomien nepočuť o kľúčoch. Frázy ako „zálohujte si svoj súkromný kľúč“ sú bežné, ale keď priemerný Joe počuje slová „verejný kľúč“ a „súkromný kľúč“, zľakne sa a bude si myslieť, že to bude príliš technické a mätúce na pochopenie. Ale nebojte sa. Pôjdeme pomaly a použijeme veľa príkladov.

Dva druhy kľúčov používaných v kryptomenách sú, ako už bolo spomenuté, verejné a súkromné. Tieto dva kľúče sa zvyčajne dodávajú v páre, čo znamená, že konkrétny verejný a súkromný kľúč sú navzájom prepojené. V skutočnosti je verejný kľúč zvyčajne odvodený od súkromného kľúča, čo znamená, že ak poznáte súkromný kľúč, vaša peňaženka môže urobiť šikovnú matematiku a zakaždým prísť so správnym verejným kľúčom.

Teraz, ako už názov napovedá, verejný kľúč môže byť verejný bez následkov. Zvyčajne je to časť adresy, ktorú zdieľate, aby ste dostali peniaze do svojej kryptomenovej peňaženky. Aj podľa svojho menovca je súkromný kľúč kľúčom, ktorý by sa nemal zdieľať. Je to vec, ktorá vám umožňuje podpísať a minúť transakciu, takže ak dôjde k odcudzeniu alebo zdieľaniu, potom môže zbabelá tretia strana minúť vaše peniaze, zvyčajne pre seba.

Jednoduchou analógiou by bol visiaci zámok a kľúč potrebný na jeho odomknutie. Otvorený visiaci zámok je možné voľne zdieľať a skutočne je možné s týmto visiacim zámkom zamknúť čokoľvek, ale iba osoba s kľúčom môže otvoriť čokoľvek, na čom je visiaci zámok zatvorený. Visiaci zámok je možné kopírovať a zdieľať, kľúč by nemal byť.

Tieto klávesy sú zvyčajne vzdialené od používateľa, takže ich v skutočnosti nikdy neuvidíte. V Monero sa vôbec nezobrazujú ako strašidelný alfanumerický reťazec. V Monero bežný používateľ pozná súkromný kľúč ako svoj základ. Semienko (ktoré by ste si mali zapísať, ak ste to neurobili), je v skutočnosti len ľudský čitateľný súkromný kľúč. 

Vidíte? Nie je to až také strašidelné. Späť na skryté adresy.

Ako už bolo spomenuté, stealth adresy neboli pôvodne vytvorené pre Monero, ale pre Bitcoin. Ako pri väčšine nových nápadov, aj táto prvá iterácia mala problémy. Ďalší pokus prišiel, keď Nicholas van Saberhagan vytvoril CryptoNote pre Bytecoin, predchodcu Monera ([pozri našu históriu Monera a Bytecoinu tu](/knowledge/monero-history)), a hoci to bolo jednoznačné zlepšenie oproti originálu, niektoré jemné nedostatky.

Nakoniec vznikla posledná iterácia od developera pre inú už neexistujúcu kryptomenu na ochranu osobných údajov, ktorá vyriešila výnimočné problémy so súkromím a bezpečnosťou tohto nápadu. To sa nakoniec dostalo do Monera a dnes sa používa.

Aj keď tieto problémy so súkromím a bezpečnosťou boli vyriešené, samotné stealth adresy pridali k technológiám blockchainu iný druh vtipu, ktorý predtým neexistoval. Potreba skenovania. Keďže prijímacie adresy nie sú verejne zobrazené na blockchaine, príjemca nikdy nevie, či je nejaká transakcia jeho, takže musí skenovať každú prichádzajúcu transakciu pomocou svojho súkromného kľúča, aby zistil, či je jeho.

Pri transparentných minciach stačí skontrolovať, či sa transakcia odosiela na vašu adresu. Jednoduchá otázka áno alebo nie. Ale so skrytými adresami môže byť každá transakcia potenciálne odoslaná vám, takže sa musíte pokúsiť odomknúť každú pomocou svojho súkromného kľúča, aby ste zistili, či sa otvorí.

Toto je ďalší krok, ktorý Bitcoin a jeho deriváty nemajú, a robí počiatočné nastavenie peňaženky spolu so synchronizáciou peňaženky, keď ste ju nejaký čas neotvorili, oveľa dlhšie ako Bitcoin. Kompromis je však potrebný na odomknutie záruk ochrany osobných údajov, ktoré má. Je potrebné poznamenať, že na rozdiel od najslabšej stránky trifecty ochrany osobných údajov, krúžkových podpisov, stealth adresy nie sú citlivé na heuristiku. Spolieha sa na osvedčenú a skutočnú kryptografiu eliptickej krivky, na ktorú sa spolieha celý internet, takže jej prelomenie by znamenalo koniec počítačovej bezpečnosti vo všeobecnosti, nielen Monero.

Ďalšie čítanie