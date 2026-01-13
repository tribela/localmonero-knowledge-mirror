---
title: "Jak wymiany atomiczne będą działały w Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Dążąc do decentralizacji i systemu naprawdę niewymagającego zaufania, niewiele rzeczy jest aż tak pożądanych w przestrzeni kryptowalut jak zdecentralizowane giełdy i wymiany atomiczne. Od początku Monero zmagało się z trudnością wdrożenia implementacji wymiany atomicznej. Cechy, które umożliwiają prywatność stwarzają też unikalne trudności podczas próby zaprojektowania protokołu wymiany atomicznej.

Ale chwila, czym właściwie są wymiany atomiczne? Wymiana atomiczna (atomic swap ang.) to protokół, za pomocą którego dwie różne kryptowaluty, na różnych blockchainach, mogą być wymieniane w sposób niewymagający zaufania ani pośredników. Oznacza to, że gdyby ktoś chciał wymienić kryptowalutę A na kryptowalutę B, mógłby to zrobić bez giełdy, scentralizowanej lub zdecentralizowanej. Jak można sobie wyobrazić, niełatwo zaprojektować taki system, a pełne szczegóły techniczne, które go umożliwiają, są bardzo skomplikowane. Kolejny raz LocalMonero angażuje się, aby pomóc i stworzyć proste wyjaśnienie dla zwykłych ludzi.

Na początku rozważmy najprostszą formę wymiany atomicznej zaimplementowaną na Bitcoinie. Jeśli ktoś chce wymienić Bitcoiny na inną kryptowalutę, która wykorzystuje tę samą technologię hash time lock contract, może to zrobić w następujący sposób. Alicja ma Bitcoina (BTC) ale chce Litecoina (LTC), a Bob ma LTC ale chce BTC. Decydują się na atomiczną wymianę, aby każdy dostał kryptowalutę, którą chce. Alicja wysyła swoje BTC na specjalny adres wykorzystujący skrypty, które blokują fundusze, więc nawet ona nie ma do nich dostępu. Możesz to sobie wyobrazić w taki sposób, że Alicja wkłada BTC do sejfu. Kiedy sejf jest utworzony, dostaje klucz i wysyła skrót (hash ang) tego klucza do Boba. Teraz Bob nie ma samego klucza, tylko skrót, więc nie ma jeszcze dostępu do funduszy.

Bob używa tego skrótu jako seeda, z którego generuje własny sejf i wysyła tam swój LTC, gdzie również zostaje on zablokowany. Ponieważ skrót klucza Alicji został użyty jako seed, dzięki któremu powstał sejf Boba, może ona użyć swojego klucza, aby odebrać LTC w sejfie Boba. Jej klucz pasuje! Ale używając matematycznej magii voodoo, kiedy używa swojego klucza do otwarcia zamka LTC, ujawnia klucz Bobowi, który może go następnie użyć, aby odebrać BTC, którego włożyła do swojego sejfu. W ten sposób, bez pośrednika, Alice i Bob pomyślnie wymienili się kryptowalutami.

Ale jest mały problem. Co jeśli Alicja wyśle do swojego sejfu, a Bob zdecyduje, że nie chce już handlować? Teraz, ponieważ Alicja nie może uzyskać dostępu do swojego BTC, którego zamknęła, a Bob nie zakończy swojej części transakcji, Alicja po prostu traci pieniądze na zawsze. Cóż, na szczęście Bitcoin ma technologię zwaną transakcjami zwrotu pieniędzy, więc po pewnym czasie, jeśli BTC nie zostanie odebrany przez Boba, skrypty będą miały wbudowane zabezpieczenie, w którym BTC automatycznie wróci do Alicji. Była to główna przeszkoda spowalniająca implementację wymiany atomicznej w Monero. Ze względu na [technologię ring signatures](/knowledge/ring-signatures), nadawca transakcji jest zawsze niepewny. W jaki sposób protokół może dokonać transakcji zwrotu, jeśli nawet nie wie, skąd pochodzi transakcja?

W 2017 r. mała grupa badaczy przedstawiła inną metodę, dzięki której wymiany atomiczne mogły zadziałać w Monero. Po kilku latach udoskonaleń sfinalizowali proces, dzięki któremu Monero byłoby w stanie dokonywać wymian atomicznych z Bitcoinem, nawet bez transakcji zwrotu.

Podobnie jak w przypadku wielu rzeczy na tym poziomie złożoności technicznej, nasze wyjaśnienie nadmiernie uprości niektóre rzeczy, aby przekazać ideę, ale nadal da solidne pojęcie o mechanizmach, dzięki którym ten proces będzie działał.

Zarówno Alicja (która ma XMR i chce BTC), jak i Bob (który ma BTC i chce XMR) muszą pobrać i uruchomić program obsługujący wymiany atomiczne. Może to być w portfel, zdecentralizowaną giełdę lub inny specjalny program. W pierwszym kroku programy Alicji i Boba łączą się ze sobą i tworzą kilka wspólnych sekretów i kluczy. W tym kroku tworzony jest nowy adres Monero, w którym Alicja ma jedną połowę klucza, a Bob drugą. Jednak nie ma tam jeszcze Monero, więc nie ma nic do wydania. Ostatnią rzeczą, o której należy pamiętać w przypadku tego adresu, jest to, że oboje mają klucz widoku do tego portfela, więc oboje mogą zajrzeć do środka, aby sprawdzić, czy i kiedy Monero dotrze.

W drugiej kolejności Bob wysyła swoje BTC na specjalny adres, podobny do protokołu wymiany atomicznej Bitcoina, który już omówiliśmy. Gdy Alicja widzi, że BTC dotarły na ten adres na blockchainie, wysyła swoje Monero na adres Monero, do którego ona i Bob mają połówki klucza. Bob może sprawdzić, czy Monero dotarło, ponieważ ma również klucz widoku, a gdy zobaczy, że Monero jest bezpieczne w portfelu, wyśle Alicji kawałek klucza, który pozwoli jej wypłacić Bitcoiny. Podobnie jak w przypadku poprzedniego protokołu, proces odbierania Bitcoina ujawnia Bobowi jej połowę klucza Monero. Teraz Bob ma obie połówki, więc może odebrać Monero, podczas gdy Alicja ma tylko swoją połowę, więc nie może spróbować ich przejąć zanim on to zrobi.

Jeśli przeczytałeś to wszystko i nadal jesteś trochę zdezorientowany jak Monero poradziło sobie z problemem transakcji zwrotu pieniędzy, odpowiedź jest dość prosta. Ponieważ samo Monero nie posiada transakcji zwrotu pieniędzy, zauważ, że Bitcoin (który ma transakcje zwrotu) jest wysyłany jako pierwszy, a Monero wysyłane jest dopiero po zweryfikowaniu, że znajduje się w poprawnym adresie. Pozwala to Monero na wykorzystanie zdolności Bitcoina do skryptowania w transakcjach zwrotu i korzystania z nich bez konieczności posiadania tych możliwości w samym Monero.

Atomiczna wymiana jest już zakończona, ale od tego momentu Bob ma kilka opcji ze swoim nowo odebranym XMR. Może użyć tego portfela Monero bez zmian lub przenieść XMR do innego portfela, który już posiada. Bob najprawdopodobniej przeniesie Monero do innego portfela, ponieważ Alicja nadal ma klawisz widoku i może zajrzeć do środka.

Piękno tego protokołu polega na tym, że wciąż jest całkiem nowy i jest dużo miejsca na optymalizacje. Jest również dość elastyczny w swojej architekturze, więc implementacja w innych portfelach lub zdecentralizowanych giełdach powinna być prosta i pasować do ich istniejącej architektury.

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