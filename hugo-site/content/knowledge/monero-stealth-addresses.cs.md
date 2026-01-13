---
title: "Jak skryté adresy Monero chrání vaši identitu"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero zavedlo tříbodový přístup k ochraně soukromí. Těmito technologiemi jsou [kruhové podpisy](/knowledge/ring-signatures), které skrývají skutečný výstup (odesílatele), RingCT, které skrývá částky, a skryté adresy, které skrývají příjemce. Dnes budeme diskutovat o poslední z těchto zmíněných technologií: skryté adresy.

Existuje mnoho důvodů, proč by člověk mohl chtít skrýt, komu posílá. Nikdy se nesmíme nechat nikým přesvědčit, že všechny příklady jsou nechutným chováním. Věci jako posílání peněz nepopulární politické straně, přispívání charitativním organizacím nebo podpora těch, které kultura považuje za "zrušené", jsou příklady toho, kdy člověk může chtít skrýt své výdajové chování ze strachu z postihu, ale ve své podstatě jsou naprosto legitimní.

V transparentním blockchainu jsou adresy, na které člověk posílá své transakce, viditelné pro všechny. Je důležité vzít v úvahu, že pokud sami těžaři nesouhlasí s tím, kam peníze směřují, mohou se rozhodnout, že je do bloku nevytěží, čímž tuto transakci na platformě zdánlivě odolné vůči cenzuře efektivně cenzurují. Jediný způsob, jak tuto, sice nepravděpodobnou, cenzuru znemožnit, je, že těžaři nebudou moci transakce rozlišit, protože všechna metadata na řetězci budou různými způsoby zakryta. Něco, čím je Monero známé.

Monero řeší tento problém transparentních adres implementací skrytých adres, což je technologie, kterou původně vytvořil pro Bitcoin v roce 2011 uživatel fóra Bitcoin Talk ByteCoin (vztah k Bytecoinu, který později integroval skryté adresy, není znám). Současná podoba skrytých adres má však oproti původní myšlence několik vylepšení. Abychom se však nejprve seznámili s jejich fungováním, povězme si něco o klíčích.

Je těžké pohybovat se v oblasti kryptoměn a neslyšet o klíčích. Fráze jako "zálohujte si svůj soukromý klíč" jsou běžné, ale když běžný Joe uslyší slova "veřejný klíč" a "soukromý klíč", vyděsí se a myslí si, že to bude příliš technické a matoucí, aby tomu porozuměl. Ale nebojte se. Půjdeme na to pomalu a použijeme spoustu příkladů.

Dva druhy klíčů používaných v kryptoměnách jsou, jak již bylo zmíněno, veřejné a soukromé. Tyto dva klíče se obvykle dodávají v páru, což znamená, že konkrétní veřejný a soukromý klíč jsou navzájem propojeny. Ve skutečnosti je obvykle veřejný klíč odvozen od soukromého, což znamená, že pokud znáte soukromý klíč, může vaše peněženka provést šikovnou matematiku a pokaždé přijít se správným veřejným klíčem.

Jak již názvy naznačují, veřejný klíč může být veřejný bez následků. Obvykle je to část adresy, kterou sdílíte pro příjem peněz do peněženky s kryptoměnami. Také podle svého jmenovce je soukromý klíč ten, který by neměl být sdílen. Je to věc, která vám umožňuje podepsat a utratit transakci, takže pokud je ukraden nebo sdílen, může podlá třetí strana utratit vaše peníze, obvykle sama sobě.

Snadnou analogií by byl visací zámek a klíč potřebný k jeho odemčení. Otevřený visací zámek lze volně sdílet a skutečně lze tímto zámkem zamknout cokoli, ale pouze osoba s klíčem může otevřít cokoli, na čem je visací zámek zavřený. Visací zámek lze kopírovat a sdílet, klíč by to však být neměl.

Tyto klíče jsou obvykle abstrahovány od uživatele, takže je nikdy nevidíte. V Moneru se vůbec nezobrazují jako děsivý alfanumerický řetězec. V Moneru zná běžný uživatel soukromý klíč jako svůj seed. Seed (který byste si měli zapsat, pokud jste tak neučinili), je vlastně jen lidsky čitelný soukromý klíč. 

Vidíte? Nakonec to není tak děsivé. Zpět na skryté adresy.

Jak již bylo zmíněno, skryté adresy nebyly původně vytvořeny pro Monero, ale pro Bitcoin. Stejně jako u většiny nových nápadů však tato první iterace měla problémy. Další pokus přišel, když Nicholas van Saberhagan vytvořil CryptoNote pro Bytecoin, předchůdce Monera ([viz naši historii Monera a Bytecoinu zde](/knowledge/monero-history)), a přestože to bylo jednoznačné zlepšení oproti originálu, některé jemné nedostatky.

Nakonec se objevila poslední iterace od vývojáře jiné, dnes již neexistující kryptoměny, která vyřešila zbývající problémy s ochranou soukromí a bezpečností této myšlenky. Ta se nakonec dostala do měny Monero a používá se dodnes.

Přestože byly tyto problémy se soukromím a bezpečností vyřešeny, samotné skryté adresy přidaly do blockchainových technologií jiný druh zvláštnosti, který dříve neexistoval. Potřeba skenování. Protože přijímající adresy nejsou v blockchainu veřejně zobrazeny, příjemce nikdy neví, zda je daná transakce jeho, takže musí každou příchozí transakci skenovat svým soukromým klíčem, aby zjistil, zda je jeho.

U transparentních mincí stačí zkontrolovat, zda se transakce odesílá na vaši adresu. Jednoduchá otázka ano nebo ne. Ale u skrytých adres může být každá transakce potenciálně tou, která se posílá na vás, takže se musíte pokusit každou z nich odemknout svým soukromým klíčem, abyste zjistili, zda se otevřela.

Jedná se o krok navíc, který u Bitcoinu a jeho derivátů chybí, a počáteční nastavení peněženky spolu se synchronizací peněženky, když jste ji nějakou dobu neotevřeli, je mnohem delší než u Bitcoinu. Tento kompromis je však nutný, aby se odemkly záruky soukromí, které má. Je třeba poznamenat, že na rozdíl od nejslabšího bodu trojlístku soukromí, kruhových podpisů, nejsou skryté adresy náchylné k heuristice. Spoléhá na osvědčenou kryptografii eliptických křivek, na kterou se spoléhá celý internet, takže její prolomení by znamenalo konec počítačové bezpečnosti obecně, nejen Monera.

Další čtení