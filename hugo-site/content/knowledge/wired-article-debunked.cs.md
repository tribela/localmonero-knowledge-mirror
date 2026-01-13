---
title: "Wired Magazine se o Moneru mýlí, tady je důvod"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jak v oblasti soukromí, tak v oblasti kryptoměn se dezinformace často množí. Máme [článek, který nastiňuje patnáct běžných nesprávných nebo zastaralých předpokladů o Monero](/knowledge/monero-myths-debunked), ale chceme věnovat čas tomu, abychom se věnovali jednomu konkrétnímu článku, který je často citován a šířen Monero skeptiky.

Publikace Wired vydala [článek](https://www.wired.com/story/monero-privacy/) dne 27. března 2018, který sám byl napsán v reakci na další čerstvý článek publikovaný různými akademiky s názvem: „Empirická analýza sledovatelnosti v Monero Blockchain“.

Přestože spoluautory článku jsou osoby, které jsou v jasném střetu zájmů (čtěte: jsou poradci společnosti Zcash a mají v ní podíl), byl článek komunitou Monero přijat mírně pozitivně, protože potvrzuje věci, které komunita již znala a o kterých psala ve svých vlastních dokumentech Monero Research Lab ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) a [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), z nichž první byl publikován před čtyřmi lety. Bylo s tím však spojeno i několik problémů, především střet zájmů, skutečnost, že o problémech se již vědělo, byly projednány a v některých případech i odstraněny, a hrubé zkreslení tehdejších záruk ochrany osobních údajů společnosti Monero. Komunita se vyjádřila k preprintu práce a mnohá z jejich doporučení se dostala do finální verze dokumentu.

Ale co přesně bylo špatně popsáno? Skutečnost, že Monero nemělo nedostatky, o kterých se v článku hovoří, již více než rok. Transakce před rokem 2017 byly skutečně náchylné k určité formě úniku soukromí, ale v době publikování článku Monero většinu obav vyřešilo. Abychom byli k autorům spravedliví, diskutují o nápravných opatřeních Monera v malé míře, ale ne natolik, aby to ovlivnilo vliv, který to v té době mělo na mediální cyklus o kryptoměnách. Proto vyšel článek v časopise Wired.

Přestože můžeme dotyčný článek časopisu Wired zkoumat jako dobový článek a posoudit, nakolik byl v té době pravdivý či nepravdivý, skutečnost, že je dodnes sdílen jako odůvodnění toho, proč jsou záruky ochrany osobních údajů společnosti Monero slabé, vlastně vybízí k analýze toho, jak tento článek obstojí v současnosti. Rádi toto pozvání přijímáme.

Krátké přečtení článku ukazuje několik senzacechtivých řádků, jako například "[Zjištění] by neměla znepokojovat jen ty, kteří se dnes snaží kradmo utrácet Monero", a celý tón článku, který postuluje výzkum jako "nový", vychází z velké části z publikace. V samotném akademickém článku se objevují doporučení, jako je varování uživatelů Monera před možným ohrožením jejich anonymity, a to navzdory skutečnosti, že tyto diskuse probíhaly nejen od roku 2014, ale že komunita volala po tom, aby lidé Monero nekupovali a že je velmi experimentální.

Ale co samotná kritika? Skutečnost je taková, že mnoho problémů s Monerem jako mincí na ochranu soukromí se buď již netýká Monera, nebo sdílí obavy s mincemi na ochranu soukromí jako kategorií kryptoměn založených na blockchainu. Začněme se jimi zabývat.

Jednou z nejčastěji citovaných výtek vůči Moneru je, že pokud by nějaká budoucí technologie narušila soukromí, byly by díky stálosti a neměnnosti blockchainu odhaleny všechny minulé transakce Monera. Jinými slovy, vaše soukromí má na sobě tikající hodiny.

Nemůžeme to dostatečně zdůraznit. Tuto chybu má doslova každá mince na ochranu soukromí, která využívá metody obfuskace a ochrany soukromí na řetězci, a přesto je často používána proti Moneru (paradoxně mnohokrát konkurenčními mincemi na ochranu soukromí se stejným problémem) a je použita i v tomto článku. Reakce na tuto kritiku může být pro někoho překvapivá, ale Monero může být ve skutečnosti méně zranitelné než jiné mince na ochranu soukromí, a to díky tomu, že má vícestranný přístup k ochraně soukromí.

Monero skrývá výstupy (odesílatele), částky a příjemce pomocí tří různých technologií, a to pomocí kruhových podpisů, RingCT a skrytých adres. Z nich jsou kruhové podpisy nejslabší a nejvíce náchylné jak na moderní heuristiku, tak na teoretické, budoucí technologie narušující soukromí. To je komunitě Monero známo již několik let a probíhá aktivní výzkum, jehož cílem je vylepšit nebo zcela nahradit schéma kruhových podpisů.

I kdyby však byl kruhový podpis zcela porušen, odhalil by se pouze skutečný výstup. NE odesilatel (jako jednotlivec), ale výstup. Spojit výstup s identitou není nemožné, ale vyžadovalo by to více metadat a prostředků. V kombinaci se skutečností, že RingCT a skrytá adresa by NEBYLY odhaleny, se dopad ještě snižuje.

Je třeba poznamenat, že v článku Wired se výše uvedené informace lehce rozebírají v části, kde oslovili Riccarda 'fluffyponyho' Spagniho, aby se k nim vyjádřil, ale čas věnovaný této informaci je krátký a téměř se zdá, že tuto zásadní informaci odbyl. Nepochopení je patrné zejména při pokusu o diskusi o těchto věcech s lidmi, kteří článek chtě nechtě sdílejí v dnešní době.

Další kritika, kterou je mnohem těžší řešit, se týká toho, jak se na Monero dívá okolní svět a jak to souvisí s tím, jak se na minci dívá komunita kolem Monera. Pro příklad se čtenáři nemusí dívat dál než na samotný název článku: "Oblíbená měna Dark Webu je méně nevystopovatelná, než se zdá".

Každý člověk, který tráví v komunitě Monero delší dobu, může potvrdit, že komunita Monero vynakládá velké úsilí, aby ukázala, jak těžké je dosáhnout skutečného soukromí, a to i na úkor marketingového úsilí nebo úsilí o přijetí. Pokud komunita poskytuje dostatek zdrojů, které přesně diskutují o minci a jejích nedostatcích, v určitém okamžiku se neznalost stává vinou uživatele, který věří, že mince je vše, co potřebuje k tomu, aby byl 100% soukromý.

V tuto chvíli by mělo být zřejmé, že komunita Monero bere vážně jak své soukromí, tak upřímnost ohledně jeho nedostatků a následných vylepšení. Články, jako je tento, se s tímto duchem inovací v Moneru zcela míjejí. Přirovnávají Monero k houfům jiných kryptoměn, které si dělají velkolepé nároky, přičemž myslí pouze na zisk a na kořistění nevzdělaných investorů-rádců.

Skutečnost nemůže být odlišnější. Monero si je velmi dobře vědomo svých slabin, snaží se pokračovat v budování tak, aby je vylepšilo, utáhlo uvolněné spoje a dosáhlo velmi reálného, ale velmi těžkého cíle - dát světu soukromou, zastupitelnou kryptoměnu, kterou mohou používat všichni, a to vše způsobem, který je spravedlivý, decentralizovaný a řízený komunitou. Možná je na čase odložit senzacechtivost a sdílení článků jako prostředku k šuntování tašek a propagaci konkurence. Možná je čas vyprávět jiný příběh.

Další čtení