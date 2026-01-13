---
title: "Jak CLSAG poprawi wydajność Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Protokół Monero jest stale ulepszany. Wykonując badania zarówno w technologiach on-chain, jak i off-chain, społeczność Monero poszukuje obszarów do poprawy, aby uczynić Monero bardziej prywatnym, bardziej skalowalnym i bardziej dostępnym dla wszystkich. Jedną z ostatnich innowacji jest zastąpienie schematu linkable ring signature, MLSAG, na CLSAG - Concise Linkable Spontaneous Anonymous Group.

Wdrożenie CLSAG zmniejszy o 25% najpopularniejsze transakcje postaci 2 wejścia i 2 wyjścia. Ponadto o 10% skróci czas weryfikacji transakcji.

Ale czym dokładnie jest CLSAG? Co robi i czym różni się od starej wersji MLSAG? Poświęćmy chwilę, aby przypomnieć sobie, jak korzystać z ring signatures, abyśmy mogli lepiej zrozumieć tę ideę. Ring signatures pozwalają na nieinteraktywne, nieodróżnialne wejścia za pomocą wybranych przez sygnatariusza zbiorów anonimowości poprzednich wyjść. Mówiąc wprost, pozwala to użytkownikowi ukryć swoje wyjście wśród wyjść niepowiązanych transakcji. Robi to bez konieczności udziału nikogo innego. Wszystko czego potrzebujesz to kopia blockchaina. Wydaje się, że każde z tych wyjść jest równie prawdopodobne, tym samym chowając metadane nadawcy.

Stwarza to jednak pewien problem. Co by było, gdyby użytkownik skonstruował ring signature z wyłącznie wyjściami wabika? Skąd ktoś miałby wiedzieć, że nieznany nadawca nie ma uprawnień do wysłania żadnego z nich? Czy ten użytkownik będzie mógł wydawać fałszywe pieniądze? Odpowiedź brzmi nie. W ring signatures można udowodnić, że ​​przynajmniej jedno z wyjść jest własnością nieznanego nadawcy, bez ujawniania, które to jest. W rzeczywistości zarówno CLSAG, jak i MLSAG (odtąd znane jako SAG) są częścią ring signatures, w których można to udowodnić. Co ciekawe, operacja jednocześnie dowodzi, że kwota transakcji, choć ukryta za confidential transactions (RingCT), jest poprawna. To, że w SAG można udowodnić dwie rzeczy - że jedno wyjście jest własnością kogoś z ringu i że salda transakcji są prawidłowe jest ważne, i właśnie stąd oszczędności w zakresie wielkości transkacji i czasu jej weryfikacji. Jeśli robi się to zagmatwane, nie martw się, wkrótce dojdziemy do zabawnej i łatwej do zrozumienia analogii.

Stary schemat sygnatur, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) pozwala udownić te same dwie rzeczy co ring signatures, ale dowodzi każdą z osobna. Użycie oddzielnych obliczeń dla kluczy signing i commitment oznacza wolniejsze operacje. Współczesny komputer może wykonać te obliczenia w ciągu milisekund, co nie wydaje się dużo, i rzeczywiście, w przypadku jednej transakcji tak nie jest. Ale gdy weźmiemy pod uwagę samą liczbę transakcji w blockchainie Monero i to, że węzeł synchronizujący się od zera będzie musiał pobrać i zweryfikować każdą z nich, bajty i milisekundy zaczynają się szybko nawarstwiać.

CLSAG łączy obliczenia niezbędne do udowodnienia obu własności w jedne obliczenia, które wykonuje bezpiecznie. Co to oznacza? Cóż, aby to wyjaśnić, a także, miejmy nadzieję, nadać całości sens, przyjrzyjmy się tej zapowiadanej zabawnej analogii.

Powiedzmy, że musisz iść zarówno do sklepu spożywczego, jak i do sklepu z narzędziami, aby kupić dwie różne rzeczy: żywność i toksyczne środki czyszczące. Nie chcesz, aby się zmieszały, ponieważ w razie wypadku chemikalia rozleją się na żywność, czyniąc ją niejadalną. Postanawiasz być super bezpieczny i jedziesz z domu do sklepu spożywczego, kupujesz jedzenie, a następnie wracasz do domu. Dopiero po wyładowaniu jedzenia wracasz do samochodu, jedziesz do sklepu z narzędziami i wracasz do domu z chemikaliami. Odbyłeś dwie oddzielne podróże, aby zapewnić bezpieczeństwo zakupom. Chociaż jest to rzeczywiście bezpieczny sposób, jest nieefektywny. Reprezentuje to MLSAG, w którym przechowywane są dwa różne zestawy danych matematycznych i wykonywane są dwie różne „podróże”, aby je obliczyć.

Zdecydowałeś jednak, że potrzebujesz szybszego sposobu, żeby tak robić. To za dużo straconego czasu. Jasne, zrobienie tego raz lub dwa razy nie zabierze Ci za dużo czasu, ale przy konieczności robienia tego w kółko godziny zaczynają się dodawać. Zaczynasz się zastanawiać, czy zamiast tego możesz odbyć jedną podróż. Z domu, do sklepu spożywczego, do sklepu z narzędziami i z powrotem do domu. Nie możesz tak po prostu wrzucić wszystkiego do samochodu na chybił trafił. To nie jest bezpieczne. Zamiast tego wyznaczasz różne miejsca w samochodzie na różne rzeczy i upewniasz się, że wszystko pasuje na swoje miejsce. W ten sposób możesz bezpiecznie odbyć jedną podróż do obu sklepów i trzymać rzeczy z dala od siebie. To reprezentuje CLSAG. Obecnie w tej transakcji przechowywany jest tylko jeden zestaw danych matematycznych, aby udowodnić te dwie rzeczy i jest to robione z dala od siebie, aby nie przeszkadzały sobie nawzajem. Wciąż trzeba odbyć podróże, ale drastycznie zmniejszyłeś ich liczbę.

Wszystko to brzmi całkiem ekscytująco. Ale czy uda nam się znaleźć inne skróty lub inne sposoby na zaoszczędzenie czasu i miejsca? Odpowiedź brzmi tak i nie. Według obecnych badaczy MRL, prawdopodobnie nie jest możliwe dalsze modyfikowanie konstrukcji typu SAG w celu uzyskania mniejszego rozmiaru lub wyższej prędkości; jednak inne konstrukcje, takie jak Arcturus, Omniring, RCT3 lub Triptych zapewniają znacznie lepsze skalowanie i korzyści weryfikacyjne przy użyciu różnych metod matematycznych. Jednak każde z tych podejść „następnej generacji” do protokołów z nieznanym sygnatariuszem wiąże się z kompromisami w szczegółach implementacji i musi być poddane dogłębnym badaniom.

Koniec końców Monero zawsze się usprawnia.

Więcej do przeczytania

  * [Jak Monero jednoznacznie umożliwia circular economies](/knowledge/monero-circular-economies/)

  * [Ring signatures w Monero vs CoinJoin jak w Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Dlaczego (i jak!) powinieneś trzymać własne klucze ](/knowledge/hold-your-keys/)

  * [Wspieranie Monero](/knowledge/contributing-to-monero/)

  * [Jak zdalne węzły wpływają na prywatność Monero](/knowledge/remote-nodes-privacy/)

  * [Jak Monero używa hard forków do aktualizacji sieci](/knowledge/network-upgrades/)

  * [View tags: Jak jeden bajt skróci czas synchronizacji portfela Monero o 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool i jego rola w decentralizacji kopania Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis - Co zrobi dla Monero](/knowledge/seraphis-for-monero/)

  * [Czy sprzedaż Bitcoinów za Monero jest tak samo prywatna jak kupno Monero?](/knowledge/most-private-way-to-buy-monero/)

  * [Dlaczego Monero nie wykorzystuje specjalnej konfiguracji w przeciwieństwie do Zcasha](/knowledge/monero-trustless-setup/)

  * [Dlaczego Monero lepiej przechowuje wartości niż Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Jak Monero może pokonać efekt sieciowy Bitcoina](/knowledge/network-effect/)

  * [Dlaczego Monero ma najbardziej krytycznie myślącą społeczność](/knowledge/critical-thinking/)

  * [Oszustwa, na które należy uważać korzystając z Monero](/knowledge/monero-scams/)

  * [Jak wymiany atomiczne będą działały w Monero](/knowledge/monero-atomic-swaps/)

  * [Co każdy użytkownik Monero musi wiedzieć o jego sieci](/knowledge/monero-networking/)

  * [Jak RingCT ukrywa ilości w transakcjach Monero](/knowledge/monero-ringct/)

  * [Jak stealth addresses chronią Twoją tożsamość](/knowledge/monero-stealth-addresses/)

  * [Jak subadresy zapobiegają łączeniu tożsamości](/knowledge/monero-subaddresses/)

  * [Wyjścia Monero wyjaśnione](/knowledge/monero-outputs/)

  * [Dobre praktyki Monero dla początkujących](/knowledge/monero-best-practices/)

  * [Jak ring signatures chowają wyjścia Monero](/knowledge/ring-signatures/)

  * [Jak Monero rozwiązało problem rozmiaru bloku nękający Bitcoina](/knowledge/dynamic-block-size/)

  * [Dlaczego Monero ma Tail Emission](/knowledge/monero-tail-emission/)

  * [Krótka historia Monero](/knowledge/monero-history/)

  * [Oto dlaczego magazyn Wired myli się co do Monero](/knowledge/wired-article-debunked/)

  * [15 najczęstszych obalonych mitów i obaw o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ prywatyzuje źródło transakcji Monero](/knowledge/monero-dandelion/)

  * [Dlaczego Monero jest open source i zdecentralizowane](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy](/knowledge/monero-mining-randomx/)

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better/)