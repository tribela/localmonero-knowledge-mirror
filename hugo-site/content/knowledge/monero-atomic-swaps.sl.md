---
title: "Kako Bodo Atomske Menjave v Monero Delovale"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
V prizadevanju za decentralizacijo in neomejenega sistema je malo stvari v prostoru kriptovalut tako zaželenih, kot decentralizirane borze in atomske menjalnice. Monero pri izvajanju Atomskih menjav naleti na problem, saj funkcija popolne zasebnosti ustvari težave pri načrtovanju protokola.

Toda najprej se vrnimo nazaj. Kaj so atomske zamenjave? Atomska zamenjava je protokol, s katerim lahko dve različni kriptovaluti na različnih verigah blokov izmenjamo neomejeno in brez posrednika. To pomeni, da če bi nekdo želel zamenjati kriptovaluto A za kriptovaluto B, bi to lahko storil brez borze, centralizirane ali decentralizirane. Kot si lahko predstavljamo, je za to potrebnih precej raziskav, vse tehnične podrobnosti, ki to omogočajo, pa so precej zapletene. LocalMonero je tukaj, da vam pomaga in poda preprosto razlago za vsakogar.

Za začetek si oglejmo najpreprostejšo obliko atomske zamenjave, ki jo izvaja Bitcoin. Če želi nekdo zamenjati Bitcoin za drug kovanec, ki uporablja isto tehnologijo pogodbe o zaklepanju časa hash, lahko to stori na naslednji način. Alenka ima Bitcoin (BTC), vendar želi Litecoin (LTC), Bob pa ima LTC, vendar želi BTC. Odločita se za atomsko zamenjavo, tako da vsak od njiju dobi kovanec, ki si ga želi. Alica pošlje svoj BTC na poseben naslov, pri čemer uporabi skripte, ki zaklenejo sredstva, tako da niti ona ne more dostopati do njih. To si lahko predstavljate, kot da bi Alice svoje BTC položila v zaklenjeno skrinjico. Ko je skrinjica izdelana, dobi ključ in pošlje hash tega ključa Bobu. Zdaj Bob nima samega ključa, temveč le hash, zato še ne more dostopati do sredstev.

Bob ta hash uporabi kot seme, iz katerega ustvari svoj lockbox in tja pošlje svoj LTC, kjer je prav tako zaklenjen. Ker je bil hash Alenkinega ključa uporabljen kot seme, s katerim je bil izdelan Bobov lockbox, lahko s svojim ključem zahteva LTC v Bobovem lockboxu. Njen ključ ustreza! Toda z uporabo matematike in voodoo magije, ko s svojim ključem odpre ključavnico LTC, razkrije ključ Bobu, ki ga lahko nato uporabi za zahtevek za BTC, ki ga je položila v njen lockbox. Na ta način sta Alenka in Bob uspešno izmenjala svoje premoženje brez posrednika.

Vendar je tu majhna težava. Kaj če Alenka pošlje v njen lockbox, Bob pa se odloči, da ne želi več trgovati. Ker zdaj Alenka ne more dostopati do svojih BTC, ki jih je zaklenila, in ker Bob ne bo dokončal svojega dela transakcije, je Alenka za vedno izgubila svoj denar. No, na srečo ima Bitcoin tehnologijo, ki se imenuje povračilo transakcij, zato imajo skripte po določenem času, če Bob ne prevzame BTC, vgrajeno varovalo, po katerem se BTC samodejno vrne k Alenki. To je bila glavna ovira za implementacijo atomskih menjav v Moneru. Zaradi Monero [tehnologije zasebnosti obročnih podpisov ](/knowledge/ring-signatures) je pošiljatelj transakcije negotov. Kako lahko protokol izvede transakcijo vračila, če niti sam ne ve, od kod prihaja transakcija? 

Leta 2017 je majhna skupina raziskovalcev predstavila drugačno metodo, s katero bi delovale atomske zamenjave v Moneru. Po več letih izpopolnjevanja so raziskovalci dokončali postopek, s katerim bi se lahko izvajale Monero atomske zamenjave z Bitcoinom, tudi brez transakcij vračila. 

Kot pri mnogih tehnično zapletenih stvareh, bo razlaga nekaterih stvari preveč poenostavljena, da bi razložila idejo, vendar bo kljub temu dala dobro predstavo o mehanizmih, s katerimi bi ta postopek deloval.

Tako Alenka (ki ima XMR in želi BTC) kot Bob (ki ima BTC in želi XMR) morata prenesti in zagnati program, ki podpira atomsko zamenjavo. To je lahko implementirano v denarnicah, decentraliziranih borzah ali posebnih, specifičnih programih, vendar mora programska oprema izvajati protokol atomske zamenjave. V prvem koraku se Alenkin in Bobov klient povežeta drug z drugim in naredita več skupnih skrivnosti in ključev. V tem koraku se ustvari nov naslov Monero, pri čemer ima Alenka eno polovico ključa, Bob pa drugo. Vendar v njem ni še nobenega Monera, zato ni ničesar, kar bi lahko porabili. Še zadnja stvar, ki jo je treba omeniti pri tem naslovu, je, da imata oba ključ za vpogled v to denarnico, zato lahko oba vpogledata vanjo in vidita, ali in kdaj bo Monero prispel.

V drugem koraku Bob pošlje svoje BTC na poseben naslov, podobno kot pri protokolu Atomic Swap za Bitcoin, o katerem smo že govorili. Ko Alenka v verigi blokov vidi, da na ta naslov prispe BTC, pošlje svoj Monero na naslov Monero, za katerega imata oba z Bobom polovico ključa. Bob lahko preveri, da je Monero prispel, saj ima tudi on ključ za ogled, in ko vidi, da je Monero varno v denarnici, pošlje Alenki delček ključa, ki ji bo omogočil dvig Bitcoina. Podobno kot pri drugem protokolu tudi pri postopku zahtevka za izplačilo Bitcoina razkrije svojo polovico ključa Monero Bobu. Zdaj ima Bob obe polovici, zato lahko zahteva Monero, medtem ko ima Alenka samo svojo polovico, zato ga ne more poskusiti vzeti, preden to stori on.

Če ste si vse to prebrali in ste še vedno nekoliko zmedeni, kako je Monero lahko zaobšel problem transakcij z vračilom, je odgovor precej preprost. Ker Monero sam nima transakcij vračila, naj bralec opazi, da se najprej pošlje Bitcoin (ki ima transakcije vračila) in šele ko se preveri, da je v verigi blokov, se pošlje Monero. Tako lahko Monero izkoristi Bitcoinovo zmožnost skriptiranja transakcij vračil in jih izkoristi, ne da bi moral sam imeti te zmožnosti.

Atomatska zamenjava je zdaj končana, vendar ima Bob od tu naprej nekaj možnosti za svoj na novo pridobljeni XMR. To denarnico Monero lahko uporablja tako, kot je, ali pa XMR prenese v drugo denarnico, ki jo že ima v lasti. Bob bo najverjetneje prenesel Monero v drugo denarnico, saj ima Alenka še vedno ključ vpogleda in lahko opazuje denarnico.

Zdravje tega protokola je v tem, da je še vedno precej nov in da je še veliko prostora za optimizacije. Prav tako je njegova arhitektura precej prilagodljiva, zato bi morala biti implementacija v drugih denarnicah ali decentraliziranih borzah preprosta in se čisto prilegati njihovi obstoječi arhitekturi.

Nadaljnje branje

  * [Kako Monero edinstveno omogoča krožna gospodarstva](/knowledge/monero-circular-economies/)

  * [Obročni ring podpisi Monero vs CoinJoin kot v Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Zakaj (in kako!) bi morali imeti svoje ključe](/knowledge/hold-your-keys/)

  * [Prispevek nazaj v Monero](/knowledge/contributing-to-monero/)

  * [Kako oddaljena vozlišča vplivajo na zasebnost Monera](/knowledge/remote-nodes-privacy/)

  * [Kako Monero uporablja hard-forke za nadgradnjo omrežja](/knowledge/network-upgrades/)

  * [Ogled oznak: Kako bo en bajt skrajšal čas sinhronizacije Monero denarnice za 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool in Njegova Vloga pri Decentralizaciji Monero Rudarjenja](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Kaj bo Naredil za Monero](/knowledge/seraphis-for-monero/)

  * [Ali je Pretvorba Bitcoina v Monero Enako Zasebna kot Neposredni Nakup Monera?](/knowledge/most-private-way-to-buy-monero/)

  * [Zakaj Monero Uporablja Nezaupljivo nNastavitev za Razliko od Zcasha](/knowledge/monero-trustless-setup/)

  * [Zakaj je Monero Boljši Hranilnik Vrednosti kot Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Kako lahko Monero premaga omrežne učinke Bitcoina](/knowledge/network-effect/)

  * [Zakaj ima Monero Najbolj Kritično Mislečo Skupnost](/knowledge/critical-thinking/)

  * [Prevare, na Katere Morate Biti Pozorni pri Uporabi Monera](/knowledge/monero-scams/)

  * [Kaj Mora Vsak Uporabnik Monera Vedeti, ko Gre za Mreženje](/knowledge/monero-networking/)

  * [Kako RingCT Prikrije Zneske Monero Transakcij](/knowledge/monero-ringct/)

  * [Kako Naslovi Monero Stealth Ščitijo Vašo Identiteto](/knowledge/monero-stealth-addresses/)

  * [Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet](/knowledge/monero-subaddresses/)

  * [Pojasnjeni Monero Izhodi (Outputs)](/knowledge/monero-outputs/)

  * [Najboljše Monero Prakse za Začetnike](/knowledge/monero-best-practices/)

  * [Kako Obročni Podpisi Prikrijejo Izhode Monera](/knowledge/ring-signatures/)

  * [Kako je Monero Rešil Problem Velikosti Bloka, ki muči Bitcoin](/knowledge/dynamic-block-size/)

  * [Kako bo CLSAG Izboljšal Učinkovitost Monera](/knowledge/what-is-clsag/)

  * [Zakaj Ima Monero Tail Emisijo](/knowledge/monero-tail-emission/)

  * [Kratka zgodovina Monera](/knowledge/monero-history/)

  * [Wired Magazine se Moti Glede Monera. Evo, Zakaj](/knowledge/wired-article-debunked/)

  * [Razbijamo 15 glavnih mitov in pomislekov o Monero](/knowledge/monero-myths-debunked/)

  * [Kako Dandelion++ Ohranja Zasebnost Izvora Transakcije Monero](/knowledge/monero-dandelion/)

  * [Zakaj je Monero Odprtokoden in Decentraliziran](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero rudarjenje: zakaj je RandomX tako poseben](/knowledge/monero-mining-randomx/)

  * [Zakaj je Monero Boljši od Dash, Zcash, Zcoin (tudi z Lelantusom), Grin in Bitcoin Mikserji, kot je Wasabi (posodobljeno maja 2020)](/knowledge/why-monero-is-better/)