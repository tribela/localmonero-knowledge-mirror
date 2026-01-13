---
title: "Dlaczego Monero nie wykorzystuje specjalnej konfiguracji w przeciwieństwie do Zcasha"
slug: "monero-trustless-setup"
date: "2021-02-13"
image: "/images/trust.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Niewiele pomysłów w przestrzeni kryptowalut otrzymuje tyle uwagi i dyskusji, co pojęcie zaufania i nie bez powodu. W końcu całym sensem blockchaina jest eliminacja zaufania wobec stron trzecich.

Dla tych, którzy nie w pełni rozumieją tę ideę, prezentujemy następujący wstęp. W tradycyjnym systemie finansowym strony trzecie są zazwyczaj wykorzystywane do różnych zadań. Banki służą do zabezpieczenia pieniędzy w Twoim imieniu przed kradzieżą. Escrowy są używane, aby transakcje biznesowe mogły zostać wykonane między dwiema stronami, które nie mają wzajemnego zaufania. Firmy wydające karty kredytowe wypłacają pieniądze za towary i usługi w Twoim imieniu, przyjmując na siebie ryzyko, że możesz im nie spłacić.

Każda z tych instancji wymaga zaufania. W przypadku banków i escrowów wierzysz, że nie uciekną one z Twoimi pieniędzmi, a w przypadku firm wydających karty kredytowe ufasz, że nie wypłacą pieniędzy w Twoim imieniu bez Twojej zgody, a w rzeczywistości oczywiście mogliby to zrobić. Robimy, co w naszej mocy, aby uchronić się przed takimi sytuacjami. Współpracujemy tylko z zaufanymi firmami i osobami oraz prawnie zakazujemy powyższych scenariuszy i staramy się egzekwować konsekwencje wobec przestępców, tym niemniej do opisanych scenariuszy i tak czasem dochodzi.

Ponadto wymienione usługi nie są bezpłatne. Escrowy i banki pobierają opłaty za swoje usługi, a karty kredytowe naliczają odsetki od pożyczonych pieniędzy.

Blockchain został stworzony, aby wyeliminować tych pośredników oraz związane z nimi zaufanie i opłaty. Na mocy konsensusu użytkownicy mogą sami egzekwować płatności, bez ufania komukolwiek innemu oraz bez polegania na stronach trzecich, aby dowiedzieć się ile mają pieniędzy i bez ryzyka, że owe strony trzecie uciekną z ich środkami.

Tak duży nacisk kładziony jest na tę cechę braku konieczności zaufania, że każda zmiana lub dodatek technologiczny, który dodaje element zaufania z powrotem do blockchaina, spotyka się z wielkim sceptycyzmem i krytyką, a niektóre projekty wprost odrzucają wszystkie takie pomysły. Ciekawe jest to, że nie przejmują się aż tak prywatnością.

Gdy przyjrzymy się reszcie świata zauważymy, że zbyt często nasza prywatność jest na łasce „zaufanych” stron trzecich. Gdy podajemy nasze fizyczne adresy, aby umożliwić dostawę zamawianego produktu, mamy nadzieję, że sklep nie wykorzysta tych informacji do niecnych celów ani nie sprzeda jej innym. To samo dotyczy naszych osobistych przemyśleń lub zdjęć, które publikujemy w mediach społecznościowych. Dotyczy to nawet naszych finansów, a są pewne firmy w branży księgowej lub aplikacje finansowe, które publikują wewnętrznie, na co ludzie wydają pieniądze (np. robi tak Venmo).

Monero dostrzega to zobowiązanie wobec braku wymagania zaufania w blockchainie i stosuje analogiczny standard wobec prywatności. Nasza prywatność nie powinna zależeć od strony trzeciej, która obiecuje ją chronić, tak samo jak nasze finanse nie powinny zależeć od innych osób, które obiecują nam, że nie uciekną z naszymi oszczędnościami. Z tego względu Monero dba, aby wszelkie technologie poprawiające prywatność nie wymagały zaufania.

Istnieją też inne technologie ochrony prywatności. Wymagają zaufania i trzeba przyznać, mają swoje zalety. Zcash wykorzystuje pewne typy systemów udowadniających, że klocki w swoim protokole confidential transactions, które mają bardzo silne gwarancje prywatności, z dużymi zbiorami anonimowości i jeśli są użyte prawidłowo, mogą być skuteczne w zapewnieniu prywatności. Wadą tego podejścia jest jednak to, że w ramach początkowej konfiguracji tej technologii musi istnieć zestaw parametrów, który należy wybrać, a następnie o nim zapomnieć. Jeśli ktokolwiek zachowa ten parametr, będzie miał możliwość tworzenia fałszywych dowodów SNARK i skutecznie drukować pieniądze bez niczyjej wiedzy, ponieważ środki są ukryte. Ale czy to wpływa na prywatność? Niektórzy twierdzą, że tak, podczas gdy inni, że nie. Konieczne są dodatkowe badania, aby uzyskać ostateczną odpowiedź.

Tak czy siak, proces minimalizacji zaufania brzmi podobnie jak scenariusze omawiane na początku tego artykułu. Podobnie do tradycyjnego świata, tego, od którego próbujemy się zdystansować. Blockchain nie redukuje zaufania wobec stron trzecich, on je eliminuje. Społeczność Monero uważa, że ten sam standard eliminacji, a nie redukcji, powinien być stosowany również do technologii zapewniających prywatność. Tylko dlatego, że nie zostało ostatecznie udowodnione, czy zaufane konfiguracje mogą lub nie mogą naruszać prywatności, nie oznacza, że powinniśmy pobłażliwie zezwolić na powrót konieczności zaufania w naszych finansach.

Oczywiście, każdy postęp w przestrzeni prywatności jest poprawą, a często prywatność wymagająca zaufania jest jedynie odskocznią do niewymagającej. W takich przypadkach cieszymy się, że przestrzeń posuwa się naprzód. A jednocześnie społeczność Monero po prostu nie może z czystym sumieniem wdrożyć technologii prywatności na naszym blockchainie, która osłabiłaby cel naszej rewolucji.

Często słyszymy pytania kiedy Monero zamierza wdrożyć tę, lub inną, nową technologię usprawniającą prywatność. Te pytania często pochodzą od niedoinformowanych użytkowników, którzy nie rozumieją kompromisów, a jedynie papugują nowe modne hasła. Odpowiedź na te pytania jest prosta. Monero nieustannie przygląda się i bada nowe protokoły prywatności, które mogłyby wzmocnić gwarancje prywatności na blockchainie, ale nie chcemy zagłębiać się w świat zaufanej prywatności, aby osiągnąć ten cel, nawet jeśli gwarancje są teoretycznie silniejsze.

Niektórzy twierdzą, że to podejście okaże się przestarzałe, ale uważamy, że ci ludzie zapomnieli dlaczego tu jesteśmy.

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