---
title: "Co każdy użytkownik Monero musi wiedzieć o jego sieci"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Nikogo nie powinno zaskoczyć, że Monero, a właściwie wszystkie kryptowaluty, działają w internecie. Mimo, że to stwierdzenie wydaje się być oczywiste, wielu nie bierze pod uwagę tego, co to oznacza dla ich prywatności. Innymi słowy, są pewne rzeczy, przed którymi Monero nie może uchronić swoich użytkowników. Wynikają one właśnie z tego, że platformą, na której działa Monero jest Internet. Niektóre z tych kwestii są tylko zwyczajnymi niedogodnościami, podczas gdy inne są znacznie poważniejsze i wymagają całkowitej prywatności. Najpierw przyjrzyjmy się jak interakcje między użytkownikami Monero wpływają na ich prywatność. 

Zacznijmy od czegoś banalnego. Jeśli użytkownik nie ma dostępu do internetu, to nie może pobierać nowych bloków, poszerzać transakcji w imieniu innych, ani wysyłać własnych transakcji. Co ciekawe, użytkownik z full node może bez dostępu do internetu przygotować transakcję i wysłać ją później, kiedy będzie mieć możliwość. Wynika to z faktu, że ring signatures potrzebują jedynie danych wyjściowych z blockchaina, aby móc je ukryć. Krótkie przypomnienie[, o tym jak działają ring signatures](/knowledge/ring-signatures). Ukrywają one prawdziwe dane wyjściowe, które użytkownik podaje razem z innymi niepowiązanymi wyjściami przeszłych transakcji. Jeśli użytkownik ma dostęp do tych danych wyjściowych w postaci w pełni pobranego blockchaina (full node), wtedy może stworzyć ring signature z przeszłych wyjść, a po wznowieniu połączenia sfinalizować transakcje.

Użytkownik korzystający z remote node nie ma takiej możliwości. Kiedy tworzy swój ring signature, nie może dotrzeć do swoich przeszłych wyjść, ponieważ są one dostępne tylko przez Internet.

Zanim przejdziemy do kolejnych rozważań dotyczących prywatności, rzućmy szybko okiem na Internet jako całość. Internet to nic innego jak tylko sieć komputerów połączona ze sobą. Twój ulubiony blog? Kilka plików znajdujących się na czyimś dysku. Strona internetowa, na której czytasz ten artykuł (LocalMonero)? Tak samo, trochę kodu i kilka plików hostowanych gdzieś na komputerze. Youtube? Po prostu pliki wideo znajdujące się na gigantycznych systemach komputerowych Google'a. To ty łączysz się z nimi przez swój własny komputer i załadowujesz plik z filmem, aby móc go później obejrzeć.

Komputery są w stanie siebie odróżnić, ponieważ każdy z nich podłączony do Internetu otrzymuje unikalny numer identyfikacyjny zwany adresem IP. Zazwyczaj są to cztery zestawy liczb oddzielone kropkami, na przykład: 172.66.35.7. Warto o tym pamiętać, gdy zastanawiamy się nad tym jak informacje związane z Monero przemieszczają się w Internecie. Monero to sieć peer-to-peer (P2P), co oznacza, że komputery łączą się bezpośrednio ze sobą, a nie korzystają z pośrednika. Pobieranie nowo wykrytego bloku za pomocą full node nie odbywa się przez serwer centralny, tylko między użytkownikami. Wadą tego jest fakt, że użytkownicy, łącząc się bezpośrednio ze sobą, znają swoje adresy IP.

Co jest w tym takiego złego? Przecież to tylko jakiś numer. Nie do końca. Adresy IP zawierają informacje o użytkowniku, takie jak kraj pochodzenia i dostawca sieci. Jakby tego było mało, dostawcy usług internetowych (ISP) znają adres IP każdej osoby korzystającej z ich usług. Oznacza to, że ISP oraz ich partnerzy mogą obserwować aktywność użytkownika w internecie i przy pomocy pewnych technik odkryć, że korzysta on z Monero. Zanim się przestraszysz, przeczytaj poprzednie zdanie uważnie. Jedynym co mogą zobaczyć jest to, że dana osoba łączy się z innymi węzłami w sieci Monero. Ze względu na technologię prywatności Monero, żadne inne informacje nie są w stanie wycieknąć. Ani informacje na temat węzłów, ani na temat transakcji. Nawet kiedy zostanie już ona wysłana, to żadna informacja nie jest ujawniona. Wszystkim, co dostawcy usług internetowych mogą zobaczyć jest to, że jeden z użytkowników łączy się z siecią Monero.

Dla niektórych osób nawet ta pojedyncza informacja może wystarczyć, żeby zaszkodzić reputacji czy nadszarpnąć poczucie wolności. Fakt, że ktoś narusza ich prywatność i dowiaduje się, co robią w internecie, jest dla nich nie do przyjęcia. Zachęcamy te osoby do łączenia się z siecią Monero wyłącznie za pomocą VPN, Tor lub I2P. Wszystkie są usługami ukrywającymi adres IP użytkownika i jego aktywność przed dostawcą usług internetowych. Różnice między tymi usługami wykraczają poza tematykę tego artykułu, ale istnieje wiele wysokiej jakości artykułów na ten temat, więc zainteresowanych użytkowników namawiamy do zapoznania się z nimi!

Dla większości z nas fakt, że inni wiedzą, że jesteśmy podłączeni do sieci Monero, nie jest aż tak wielkim problemem. W końcu rzeczywista zawartość naszych transakcji jest ukryta, więc co w tym złego? Chociaż może to być prawdą, to głównym zamysłem kryptowalut jest bycie swoim własnym bankiem, więc zachęcamy do rozważenia tego jak zarządzasz swoją prywatnością. Zważając na fakt, że musisz chronić swój klucz prywatny, bo jego utrata to również utrata wszystkich środków, lepiej być przezornym. 

Bycie swoim własnym bankiem oznacza nie tylko rozważenie swojego cyfrowego bezpieczeństwa, ale również fizycznego. Ujawniona informacja o tym, że dana osoba łączy się z siecią Monero, może sprowadzić na nią niepożądaną uwagę, niekoniecznie ze strony podmiotów działających na dużą skalę, takich jak państwa, ale także mniejszych, mających bardziej egoistyczne powody. Mamy tu na myśli głównie hakerów szukających łatwego zarobku. W całej sferze kryptowalut istnieją niezliczone historie gdzie taki scenariusz miał miejsce.

Ten artykuł nie ma na celu siać strachu, ale raczej zachęcić użytkowników do doinformowania się na temat sposobów na ochronę swoich danych przeglądania. Zdobyta wiedza przeniesie się na ogólne korzystanie z Internetu, a nie tylko z Monero. W świecie, który coraz bardziej staje się połączony z Internetem użytkownik, który gromadzi odpowiednią wiedzę i umiejętności, aby pozostać bezpiecznym i zależnym tylko od siebie, jest krok do przodu od innych.

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