---
title: "Kako Monero Podnaslovi Preprečujejo Povezovanje Identitet"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero je vedno našel inovativne načine za reševanje težavnih težav z zasebnostjo. Te inovacije pogosto vodijo do drugih inovacij, včasih pa se te tehnologije lahko uporabijo tudi za primere uporabe, ki jih prej nismo upoštevali. Nikjer to ni tako nazorno prikazano kot v primeru tehnologije podnaslova Monero.

Pomislite na hipotetični problem zasebnosti, pri katerem lahko uporaba enega naslova na več platformah s strani navidezno nepovezanih ljudi privede do povezovanja in deanonimizacije omenjenih ljudi. Preprosto povedano, če ste oseba z imenom Billy Joe Bob in prodajate jabolka za bitcoine, lahko svoj naslov Bitcoin objavite na javnem mestu, da vam stranke lahko plačajo. Recimo, da se naslov začne z alfanumeričnim nizom 7XybV3... Če pustimo ob strani očitno tveganje za zasebnost, da lahko kdor koli preveri vaše stanje v Bitcoinu in vidi, koliko ste prodali, obstaja še drugo tveganje za zasebnost, o katerem se ne govori pogosto. Recimo, da ste tudi podzemni heker z imenom l33tz0r. Opravljate delo žvižgača, ki nič hudega slutečemu prebivalstvu pripoveduje o vladni korupciji, zato je nujno, da ohranite svojo identiteto v tajnosti. Za svoje delo sprejemate donacije v bitcoinih, naslov pa objavite na javnem forumu. To je isti naslov, na katerem sprejemate denar od svojih kupcev jabolk. 7XybV3... eden. 

Preprost, a uničujoč napad za deanonimizacijo bi bil, če bi z internetnim iskalnikom poiskali vaš naslov Bitcoin. Če v iskalnik vpišete naslov 7XybV3..., dobite dva različna rezultata. Podjetje Apple in l33tz0r. To je dovolj za povezavo obeh identitet in deanonimizacijo l33tz0r, kar bi lahko imelo strašljive posledice s strani pristojnih. 

Važno je omeniti, da je ta napad mogoč tudi z valuto Monero. Čeprav Monero skriva večino podatkov na verigi, ta napad ne uporablja nobenih. Uporablja le naslov, ki ga je treba deliti, da bi prejeli plačilo. V primeru anonimnih donacij javno. To je eden od možnih načinov, kako lahko uporabniki Monera nevede škodujejo svoji zasebnosti, in je tudi primer, kako Monero kljub temu, da je vrhunski glede ohranjanja zasebnosti, ni neprebojen.

Običajni način za izogibanje tej težavi je bil lastništvo več denarnic. Ker so za vsako identiteto (ali primer uporabe) objavljeni različni naslovi, jih ni mogoče povezati. Vendar ta zasebnost velja le, če jih uporabnik nikoli ne pomeša. Naključna objava napačnega naslova bi imela enake učinke povezovanja. Prav tako je treba ohraniti varno seme vsakega naslova, s čimer se poveča delo na področju informacijske varnosti, potrebno za vsako novo izdelano denarnico.

Monerova rešitev so bili podnaslovi. Možnost ustvarjanja ogromnega števila naslovov pod glavnim naslovom, ki se uporablja kot nekakšno seme. Vsak ustvarjen podnaslov lahko sprejema Monero, vsi pa gredo v isto denarnico. S to metodo je število identitet, ki jih je mogoče upravljati pod enim naslovom, ogromno, hkrati pa je delo z informacijsko varnostjo minimalno. Teh naslovov tudi ni mogoče matematično povezati, zato jih bo zunanji opazovalec zelo težko povezal, če uporabnik ne bo zakričal svoje povezave v svet.

Toda iz podnaslovov se je pojavil še en zanimiv primer uporabe; kot nadomestna možnost splošno osovraženih ID-jev plačil.

ID plačil so bili način, s katerim so trgovci ugotavljali, katera stranka je poslala katero plačilo. Ker so informacije Monero v verigi zakrite, prejemnik transakcije ne more videti, kateri naslov jo je poslal. To pomeni, da je pri podobnih cenah izdelkov in več naročilih nemogoče ugotoviti, kdo je kaj poslal. ID-ji plačil so edinstven, naključen niz, ki ga ustvari trgovec in ga posreduje stranki. Stranka ga doda kot ločeno polje pri pošiljanju transakcije. Ta naključni niz se kot del transakcije vnese v verigo blokov in na ta način lahko trgovec prepozna in razvrsti prejete transakcije.

Ta metoda je bila pomanjkljiva na več načinov. Prvič, zmanjšuje enotnost podatkov v verigi. Zaradi dodatnih, edinstvenih metapodatkov lahko nekatere transakcije izstopajo iz množice, kar omogoča hevristično analizo. To še posebej velja, kadar ti metapodatki niso obvezni za vse. Če bi bila ta obveznost obvezna za vse, bi to v verigi blokov po nepotrebnem povečalo prostor, zato tega nismo storili. Prav tako bi bilo v primeru, da bi se plačilni ID iz kakršnega koli razloga ponovno uporabil, trivialno povezati dve transakciji kot povezani. To se je običajno dogajalo pri depozitih na borzi in vsakdo bi lahko transakcije preprosto povezal kot depozit na borzi in kot depozit enega posameznika.

Drugo, z vidika uporabniškega vmesnika ID plačila ustvarjajo drugi korak, ki ga uporabniki kriptovalut, ki prihajajo iz drugih kovancev, niso vajeni, in če se pozabijo, to povzroči ogromen glavobol za trgovca, ki mora te transakcije identificirati z drugimi sredstvi. To je bilo običajno izvedeno tako, da se je neposredno pogovoril z vsako stranko, ki je pozabila vnesti ID plačila, in potrdil druge identifikacijske podatke, ki jih je lahko poznal samo on, kot je kombinacija zneska, datuma pošiljanja in ID transakcije.

Ta dodatni korak so številni zamudili in prišlo je do točke, ko so nekatere borze strankam začele zaračunavati denar, če je bilo treba njihov denar ročno pridobiti, ker so pozabili ID plačila. Drugi so stisnili zobe in pojedli dodatne stroške podpore, a nihče ni bil vesel tega.

Za to je obstajala ena rešitev, integrirani naslovi, ki so združili naslov in ID plačila v en niz, tako da tega ni bilo mogoče pozabiti, vendar je bilo sprejetje dokaj šibko, kljub koristim, ki bi jih trgovci prejeli od njegove vključitve. 

Po zanimivem razvoju dogodkov so podnaslovi rešili dan. Zmožnost ustvarjanja velikih količin podnaslovov na glavni naslov in ugotavljanja, katere transakcije so prišle na katere podnaslove, je trgovcem omogočila, da so se znebili plačilnih ID-jev na eleganten način, hkrati pa sprejeli naslednjo generacijo tehnologije Monero. Od takrat je večina borz in trgovskih orodij prešla na podnaslove kot primarni način identifikacije transakcij.

Kar se je začelo kot rešitev za problem zasebnosti, se je spremenilo v nekaj veliko več, kar je rešilo veliko težavo UX za trgovce in stranke. Inovacija rodi več inovacij, ki se pogosto lahko spremenijo v nepričakovane zmage za vse. Monero je to videl vedno znova in se zelo trudi inovirati, kar je mogoče na blockchainu. Kdo ve, katere stvari lahko še odklenemo skupaj? 

Nadaljnje branje