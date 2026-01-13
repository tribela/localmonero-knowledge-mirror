---
title: "View tags: Jak jeden bajt skróci czas synchronizacji portfela Monero o 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jedną z najczęstszych skarg związanych z używaniem Monero na co dzień jest czas jaki zajmuje synchronizacja portfela, zanim można wysłać z niego Monero. Na szczęście programiści i badacze ze społeczności Monero znaleźli genialny sposób na skrócenie czasu, jaki zajmuje zsynchronizowanie portfela o 40%+ bez wielkiego powiększania blockchaina, opłat, itp. 

„View tags” to jedno-bajtowy dodatek do danych każdej transakcji - dostępny w Monero od najbliższej aktualizacji sieci! 

## Dlaczego synchronizacja portfela Monero jest wolniejsza niż Bitcoina?

## Dlaczego synchronizacja portfela Monero jest wolniejsza niż Bitcoina?

Jednym z pierwszych pytań, na które musimy odpowiedzieć, aby lepiej zrozumieć potrzebę rozwiązania takiego jak view tags, jest to, dlaczego synchronizacja portfela Monero jest wolniejsza niż kryptowalut takich jak Bitcoin. 

W Bitcoinie, ponieważ wszystkie transakcje są nieprywatne i ujawniają wydawane monety, kwoty i adresy on-chain, portfele Bitcoina mogą po prostu szukać dowolnych niewydanych wyjść transakcji (UTXO) lub używanych adresów dla danego portfela , szybko skanując blockchain zapamiętując pasujące UTXO, aby dowiedzieć się, które monety należą do nich. 

Jednak w Monero wszystkie transakcje są prywatne, więc ukrywają nadawcę, odbiorcę i kwoty. Ta prywatność, choć jest niezbędna do ochrony użytkowników sieci, oznacza również wolniejszą synchronizację portfela. W Monero Twój portfel musi porównać każde wyjście transakcyjne (TXO), które istnieje w sieci z Twoimi kluczami prywatnymi.

To porównanie obejmuje wiele skomplikowanych obliczeń i kryptografii, aby potwierdzić, że wyjście jest naprawdę Twoje, ponieważ wszystkie kwoty, adresy i znane wyjścia (lub monety) są ukryte on-chain w Monero. 

## Czym są view tags?

## Czym są view tags?

Jako sposób na skrócenie czasu synchronizacji dla portfeli Monero, [badacz pod nazwą UkoeHB wymyślił nowatorskie podejście](https://github.com/monero-project/research-lab/issues/73) \- dodanie 1-bajtowego „tagu” do każdej transakcji przy użyciu wspólnego sekretu znanego tylko nadawcy i odbiorcy tej transakcji . 

Ten wspólny sekret jest generowany przez nadawcę za pomocą adresu podanego mu przez odbiorcę i nie wymaga żadnej współpracy przez nadawcę i odbiorcę. Pierwszy bajt (lub symbol) tego wspólnego sekretu jest następnie dodawany do danych transakcji podczas publikowania jej w sieci Monero. 

Gdy jeden z uczestników tej transakcji chce zsynchronizować swój portfel z blockchainem Monero, zamiast konieczności wykonania wszystkich skomplikowanych obliczeń i kryptografii dla każdego TXO w sieci, portfel może teraz po prostu sprawdzić to 1-bajtowe pole w każdej transakcji i tylko wtedy wykona czasochłonną weryfikację transakcji, gdy ma ten tag. Pozwala to zawęzić poszukiwania do 1 na każde 256 TXO w sieci! 

Ten tag nie ujawnia żadnych informacji o transakcji obserwatorowi zewnętrznemu, dodaje tylko 1-bajt (nieistotną ilość) do rozmiaru transakcji, a jednak pozwala nam skrócić czas synchronizacji o 40%+ poprzez ograniczenie skomplikowanych weryfikacji! 

## View tags: uproszczony przykład

## View tags: uproszczony przykład

Wyobraź sobie, że masz 4096 pudełek w pokoju, z czego tylko 5 pudełek należy do Ciebie. Wszystkie pudełka są całkowicie nierozróżnialne od zewnątrz, a jedynym sposobem na sprawdzenie, czy pudełko jest Twoje jest otwarcie i rozwiązanie czasochłonnego problemu matematycznego zapisanego w środku, aby upewnić się, że jest Twoje.

Wyobraź sobie teraz, że postanawiasz, że osoba wyśle Ci 5 pudełek i wygeneruje specjalny kod za pomocą Twojego adresu, a następnie umieści tylko pierwszy znak tego wygenerowanego kodu na zewnątrz każdego pudełka wysyłanego do Ciebie. Wszyscy inni zrobią to samo ze swoimi pudełkami (aby zapewnić, że wszystkie pudełka są nadal nie do odróżnienia), ale teraz mógłbyś po prostu spojrzeć na jeden znak na zewnątrz pudełka i otworzyć tylko te pudełka, które mają na nich ten znak.

Chociaż inne pudełka będą pasować do Twojego kodu, a nawet niektóre te, które nie są Twoją własnością, to liczba pudełek koniecznych do otworzenia i rozwiązania problemu matematycznego wyniesie wtedy tylko 16 (1/256 pudełek!) zamiast wszystkich 4 096. 

Teraz otwierasz te 16 pudełek, rozwiązujesz problemy matematyczne i zachowujesz 5 pudełek, które faktycznie należą do Ciebie z tej grupy!

## Kiedy view tags będą dostępne w Monero?

## Kiedy view tags będą dostępne w Monero?

View tags są jedną z funkcji aktualnie planowanych do uwzględnienia w [nadchodzącej aktualizacji sieci](https://github.com/monero-project/meta/issues/630) i powinny być wdrożone tej wiosny. Społeczność [zebrała 23,3 XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (do daty publikacji), aby zachęcić do badań i utworzenia implementacji view tags. W rezultacie większość pracy koniecznej do dodania view tags do kodu Monero została już zakończona przez j-berman we współpracy z recenzentami i badaczami. 

Gdy view tags będą wymagane w sieci, wszystkie transakcje wysłane po aktualizacji sieci skorzystają z drastycznie krótszego czasu synchronizacji portfela. Nie musisz robić nic specjalnego, aby zacząć używać view tags, Twój ulubiony portfel Monero po prostu zacznie ich używać po aktualizacji sieci! 

## Jak mogę się dowiedzieć więcej?

## Jak mogę się dowiedzieć więcej?

Jeśli wzbudziło to Twoją ciekawość na temat view tags, wejdź w poniższe linki, które dogłębnie omawiają temat:

  * [Redukcja czasu skanowania korzystając z 1 bajta na wyjście view tags](https://github.com/monero-project/research-lab/issues/73)
  * [Dodaj view tags do wyjść, aby zredukować czas skanowania portfela](https://github.com/monero-project/monero/pull/8061)

Więcej do przeczytania

  * [Jak Monero jednoznacznie umożliwia circular economies](/knowledge/monero-circular-economies)/

  * [Ring signatures w Monero vs CoinJoin jak w Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Dlaczego (i jak!) powinieneś trzymać własne klucze ](/knowledge/hold-your-keys)/

  * [Wspieranie Monero](/knowledge/contributing-to-monero)/

  * [Jak zdalne węzły wpływają na prywatność Monero](/knowledge/remote-nodes-privacy)/

  * [Jak Monero używa hard forków do aktualizacji sieci](/knowledge/network-upgrades)/

  * [P2Pool i jego rola w decentralizacji kopania Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis - Co zrobi dla Monero](/knowledge/seraphis-for-monero)/

  * [Czy sprzedaż Bitcoinów za Monero jest tak samo prywatna jak kupno Monero?](/knowledge/most-private-way-to-buy-monero)/

  * [Dlaczego Monero nie wykorzystuje specjalnej konfiguracji w przeciwieństwie do Zcasha](/knowledge/monero-trustless-setup)/

  * [Dlaczego Monero lepiej przechowuje wartości niż Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Jak Monero może pokonać efekt sieciowy Bitcoina](/knowledge/network-effect)/

  * [Dlaczego Monero ma najbardziej krytycznie myślącą społeczność](/knowledge/critical-thinking)/

  * [Oszustwa, na które należy uważać korzystając z Monero](/knowledge/monero-scams)/

  * [Jak wymiany atomiczne będą działały w Monero](/knowledge/monero-atomic-swaps)/

  * [Co każdy użytkownik Monero musi wiedzieć o jego sieci](/knowledge/monero-networking)/

  * [Jak RingCT ukrywa ilości w transakcjach Monero](/knowledge/monero-ringct)/

  * [Jak stealth addresses chronią Twoją tożsamość](/knowledge/monero-stealth-addresses)/

  * [Jak subadresy zapobiegają łączeniu tożsamości](/knowledge/monero-subaddresses)/

  * [Wyjścia Monero wyjaśnione](/knowledge/monero-outputs)/

  * [Dobre praktyki Monero dla początkujących](/knowledge/monero-best-practices)/

  * [Jak ring signatures chowają wyjścia Monero](/knowledge/ring-signatures)/

  * [Jak Monero rozwiązało problem rozmiaru bloku nękający Bitcoina](/knowledge/dynamic-block-size)/

  * [Jak CLSAG poprawi wydajność Monero](/knowledge/what-is-clsag)/

  * [Dlaczego Monero ma Tail Emission](/knowledge/monero-tail-emission)/

  * [Krótka historia Monero](/knowledge/monero-history)/

  * [Oto dlaczego magazyn Wired myli się co do Monero](/knowledge/wired-article-debunked)/

  * [15 najczęstszych obalonych mitów i obaw o Monero](/knowledge/monero-myths-debunked)/

  * [Jak Dandelion++ prywatyzuje źródło transakcji Monero](/knowledge/monero-dandelion)/

  * [Dlaczego Monero jest open source i zdecentralizowane](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy](/knowledge/monero-mining-randomx)/

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better)/

Więcej do przeczytania