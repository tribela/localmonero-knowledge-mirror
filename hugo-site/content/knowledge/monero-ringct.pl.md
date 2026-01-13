---
title: "Jak RingCT ukrywa ilości w transakcjach Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Prywatność Monero nie jest zależna od jednej konkretnej technologii. Dlatego, gdy coś nagle przestanie działać tak jak powinno, żadna z informacji o transakcji nie zostanie ujawniona. Trzy technologie, na których opiera się prywatność Monero współpracują ze sobą, aby zapewnić kompleksową prywatność i zrównoważyć nawzajem swoje słabości. Składają się na nie [ ring signatures ](/knowledge/ring-signatures), RingCT oraz [ stealth addresses](/knowledge/monero-stealth-addresses). Ukrywają one odpowiednio: prawdziwe wyjście (nadawcę), wartość i odbiorcę. W tym artykule omówimy RingCT.

RingCT jest prawdopodobnie najbardziej zaawansowaną technologią ze wszystkich trzech i dlatego może być trudne do zrozumienia, więc nie będziemy podejmować się próby wyjaśnienia jak dokładnie działa. Za to pokażemy jak to jest możliwe, że nie znając wartości transakcji jesteśmy w stanie potwierdzić jej prawdziwość. Aby wszystko było zrozumiałe jak zawsze użyjemy wielu przykładów. 

Najpierw dowiedzmy się czemu weryfikacja wartości jest taka ważna. Czemu nie możemy po prostu trzymać tego całkowicie w sekrecie? Istnieją różne sposoby, za których pomocą ludzie mogą tworzyć pieniądze z niczego. Jak może coś takiego w ogóle działać? Posłużmy się przykładem, by odpowiedzieć na to pytanie.

Chcesz zakupić jakiś przedmiot od swojego przyjaciela. On w zamian chce dostać 10 dolarów. Na początku on nie ma żadnych pieniędzy, a ty masz 10 dolarów. Po zapłaceniu mu za przedmiot, ty masz zero pieniędzy, a on ma 10 dolarów, które poprzednio należało do Ciebie. Podczas tej wymiany żadne pieniądze nie zostały zniszczone.

W sferze kryptowalut zdarza się, że bystry użytkownik zapłaci komuś 10 dolarów i zamiast nie dostać niczego, otrzyma 2 dolary reszty. Sytuacja, w której osoba kupująca ma 0 dolarów, a osoba sprzedająca 10 dolarów, zamienia się w zdarzenie, które nie powinno mieć miejsca. Osoba otrzymująca płatność nadal posiada tylko 10 dolarów, a osoba wykonująca płatność 2 dolary. Dwa dolary zostały właśnie wytworzone z niczego. Można sobie wyobrazić jaką wartość jest w stanie wykreować użytkownik, gdy często powtarza ten proces.

W Bitcoinie i w innych tego typu kryptowalutach, byłoby to łatwe do wykrycia. Dane wyjściowe i wejściowe są jawne, więc wystarczy sprawdzić czy wartość wysłana zgadza się z wartością odebraną. Jeśli te informacje byłyby zaszyfrowane i niewidoczne, tak jak jest w przypadku Monero, użytkownik nie miałby możliwości sprawdzenia czy wartości byłyby sobie równe.

Z zamysłem powiększenia prywatności Bitcoina, Gregory Maxwell stworzył Confidential Transactions (CT), nową technologię, która szyfruje wartości oraz jednocześnie pozwala sprawdzić czy nic nie zostało sfałszowane w transakcji. Tak jak większość projektów z zakresu prywatności, ten także nie przyjął się przez Bitcoina, ale za to przez Monero już tak. Był tylko jeden problem. Wdrożona już wcześniej technologia ring signatures była niekompatybilna z zaproponowanym pomysłem. Jeden z badaczy MRL w tamtym czasie, Shen Noether, zmodyfikował CT tworząc RingCT, wersję, która stała się kompatybilna z ring signatures.

Dla podkreślenia powtórzymy jeszcze raz. To jak działają RingCT jest dosyć techniczne, zatem trudne do wyjaśnienia w artykule wprowadzającym w ich temat. Dla entuzjastów kryptografii, którzy chcą zrozumieć jak działają, istnieje pełno artykułów, które zagłębiają się w wewnątrz CT. W tym artykule omówimy tylko jak to możliwe, że możemy ukryć wartości swojej transakcji, ale nadal mieć możliwość sprawdzenia czy jakieś wartości zostały sztucznie wytworzone lub zniszczone.

Wyobraźmy sobie sytuację, w której Alice chce wysłać Bobowi pieniądze. Alice wyśle 10 XMR do Boba. Bob po jakimś czasie otrzyma 10 XMR. Alice nie chce, aby ktoś wiedział jaką wartość wysłała. W celu rozwiązania tego problemu ona oraz Bob tworzą shared secret. Jest to w zasadzie liczba, o której wiedzą tylko oni. Załóżmy, że tą liczbą jest 22. Alice mnoży faktyczną wartość, czyli 10 XMR przez sekretną liczbę i otrzymuje 220 XMR. Tę wartość dzieli z siecią.

Minersi nie są świadomi istnienia shared secretu oraz ile wynosi ta liczba. Jeśli by tak było, mogliby podzielić wartość, którą widzą przez tę sekretną liczbę i otrzymać faktyczną wartość jaka została wysłana. Jako, że nie wiedzą o jej istnieniu to jedyne, co zobaczą to, że Bob otrzymał 220 XMR oraz, że 220 XMR zostało wysłane, czyli wszystko się zgadza, 220=220. W ten sposób sieć może sprawdzić, czy żadne Monero nie zostało stworzone lub zniszczone, a wszystko to odbywa się bez znajomości prawdziwej kwoty.

Ponieważ Bob wie ile wynosi liczba przypisana do shared secretu, to kiedy otrzymuje kwotę, dzieli ją przez 22, by dostać prawdziwą wartość jaką wysłała Alice. Oboje znają prawdziwą wartość transakcji, podczas gdy wszyscy inni znają wersję sztucznie wygenerowaną.

Ponownie, nie odzwierciedla to faktycznego sposobu w jaki działa CT, ale udowadnia, że istnienie takiej technologii jest możliwe. Jedna z rzeczy, która w rzeczywistości tworzy CT, to zobowiązania Pedersena, czyli dwie wysłane wartości (jedna zaszyfrowana wartość do odbiorcy i ....). Przy dalszym tłumaczeniu wszystko komplikuje się jeszcze bardziej.

Należy jednak pamiętać, że choć RingCT ukrywa prawdziwą kwotę transakcji pomiędzy dwiema stronami, to nie ukrywa dwóch pozostałych zestawów liczb.

Pierwszy z zestawów to transakcja coinbase. Jeżeli ten termin jest Tobie nieznany, to oznacza nagrodę jaką miners otrzymuje za znalezienie kolejnego bloku. Ta wartość nie jest ukryta. Każdy może zobaczyć, ile protokół przyznał minerowi za jego usługę. Sumując wszystkie transakcje coinbase, można dowiedzieć się jaka jest aktualna ilość Monero w obiegu.

Drugą nieukrywaną liczbą jest opłata, jaką użytkownik przyznaje minerom, gdy wysyła transakcję. Opłaty te muszą być jawne, aby minersi mogli nadać każdej transakcji odpowiednią ważność. To niestety może już narazić prywatność użytkownika. Jeśli użytkownik opłaca minera w podobny sposób za każdym razem, to jego transakcje mogą zostać ze sobą powiązane.

Poza tymi przypadkami, RingCT ukrywa wartości Monero od 2017 roku, a nasza wspólna prywatność jest o niebo przez niego mocniejsza.

Więcej do przeczytania

  * [Jak Monero jednoznacznie umożliwia circular economies](/knowledge/monero-circular-economies)/

  * [Ring signatures w Monero vs CoinJoin jak w Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Dlaczego (i jak!) powinieneś trzymać własne klucze ](/knowledge/hold-your-keys)/

  * [Wspieranie Monero](/knowledge/contributing-to-monero)/

  * [Jak zdalne węzły wpływają na prywatność Monero](/knowledge/remote-nodes-privacy)/

  * [Jak Monero używa hard forków do aktualizacji sieci](/knowledge/network-upgrades)/

  * [View tags: Jak jeden bajt skróci czas synchronizacji portfela Monero o 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

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