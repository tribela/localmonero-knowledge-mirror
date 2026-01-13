---
title: "Dlaczego Monero ma Tail Emission"
slug: "monero-tail-emission"
date: "2020-07-30"
image: "/images/emission.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Gdy większość osób myśli o tym, co wyróżnia Monero, ma na myśli jego prywatność. To prawda, że dla wielu prywatność i umożliwiona przez nią zamienność, definiują Monero i stanowią główną jego siłę w porównaniu z innymi kryptowalutami. Jednak większość osób nie zdaje sobie sprawy, że Monero różni się od Bitcoina na więcej sposobów, przy czym wiele z nich być może równie ważna co prywatność. W tym artykule przyjrzymy się jednej z nich: tail emissions

Zacznijmy od zdefiniowania tego pojęcia. Tail emissions to niekończąca się nagroda za wykopanie bloku, emitowana nawet po wykopaniu "ostatniego" Monero. Innymi słowy nagroda za blok Monero nigdy nie spada do zera, lecz spada, aż do osiągnięcia 0,6 XMR za blok i pozostaje na tym poziomie na zawsze. Minersi zawsze otrzymają zapłatę za kopanie Monero i nigdy nie będą zmuszeni do tego, żeby polegać wyłącznie na opłatach za transakcje.

Ale cofnijmy się trochę i spójrzmy na kopanie. Minersi Monero są zachęcani do zabezpieczenia sieci licząc hashe. Zachętą jest szansa na zarobienie Monero, jeśli znajdą nowy blok. To Monero składa się z dwóch części. Najpierw miner dostaje opłaty transakcyjne od każdego użytkownika, który wysłał transakcje znajdujące się w tym nowym bloku. Są to opłaty transakcyjne, które płacisz, gdy wysyłasz transakcję. W drugiej części, miner otrzymuje pewną zawczasu ustaloną ilość Monero od samego protokołu. Przeważnie ta nagroda za blok od protokołu jest znacznie większa niż opłaty od użytkowników i na niej głównie minersi zarabiają. Ta nagroda zachęca minerów do zabezpieczenia sieci, ale również wprowadza nowe Monero do obrotu.

W większości protokołów kryptowalut ta nagroda za blok maleje z czasem. Większość pochodnych Bitcoina posiada tak zwane halvenings - ustalone daty, po których nagroda za blok spada o połowę (np: z 20 BTC na 10 BTC). Te halvenings mają miejsce co kilka lat i za każdym razem, gdy do nich dochodzi bezpieczeństwo sieci spada. Dlaczego? Cóż, zachęcamy czytelnika do przeczytania naszego [artykułu na temat kopania i RandomX](/knowledge/monero-mining-randomx), aby dowiedział się, że kopanie kryptowalut to wyścig. Nagrody za bloki są przyznawane jedynie temu, który znajdzie blok, a jest wielu konkurentów do tego. Im nagrody za bloki są wyższe, tym więcej ludzi jest zainteresowanych, podczas gdy przy niskich nagrodach, mniej osób jest chętnych, nawet jeśli posiadają sprzęt, jako, że wymaga to czasu i kosztownych zasobów, aby mieć szansę na zdobycie drobnej nagrody.

Zaczynamy rozumieć więc powody, dla których Monero ma tail emissions. Monero też ma spadającą nagrodę za blok, jednak w przeciwieństwie do Bitcoina, nie ma halvenings. Zamiast tego każdy kolejny blok ma nieco mniejszą nagrodę, więc redukcja jest o wiele łagodniejsza. Pytaniem dla każdej kryptowaluty jest co, gdy nagroda za nowy blok spadnie do 0? To dziwne pytanie, bo jednocześnie znamy i nie znamy odpowiedzi. Wiemy, że nie będzie już nagrody za nowy blok, co oznacza, że minerzy będą musieli się zmotywować jedynie opłatami za transakcje. Nie wiemy jednak, czy te opłaty wystarczą, aby zabezpieczyć blockchain.

Jak wspomnieliśmy wcześniej, na tę chwilę nagroda za nowy blok jest znacznie większa niż opłaty za transakcje, więc jest nadzieja, że gdy więcej osób skorzysta z sieci to opłaty wzrosną, a więc minerom będzie się opłacać kopanie. Jest też inny punkt widzenia na ten scenariusz - punkt widzenia użytkowników. Jeśli opłaty za transakcje będą zbyt wysokie, wówczas korzystanie z sieci będzie bardzo drogie, potencjalnie zbyt drogie dla mniej zamożnych użytkowników. Z drugiej strony, jeśli opłaty za transakcje pozostaną niskie, a nagroda za nowy blok spadnie do 0, wówczas bardzo niewielu minerów będzie zabezpieczać sieć pozostawiając ją podatną na ataków 51% oraz ryzyko cofniętych transakcji.

Nikt nie ma dobrych odpowiedzi na ten scenariusz i żadna wiodąca kryptowaluta jeszcze nie osiągnęła tego etapu, więc nie mamy przykładów z rzeczywistego świata. To są tylko spekulacje. Bitcoin zakłada, że opłaty za transakcje wystarczą, aby zachęcić minerów, nawet jeśli wykluczy to mniej zamożnych użytkowników. Monero zakłada inaczej – przyjmuje, że opłaty za transakcje nie wystarczą, aby zabezpieczyć sieć i dlatego tail emissions są częścią protokołu.

Przypominamy, że nagroda za nowy blok nigdy nie spadnie poniżej 0,6 XMR. Czy to wystarczy, aby zmotywować minerów? Nie mamy pewności, ale zdecydowanie jest to lepsze niż 0, które jest stosowane przez niemal każdą inną kryptowalutę.

Główna krytyka stosowana wobec tego rozwiązania to spostrzeżenie, że teoretycznie Monero ma nieskończoną podaż powodującą inflację, podczas gdy ilość innych kryptowalut jest ograniczona, a ich niedobór się nasila i zwiększa ich wartość z czasem. Sądzimy, że ten argument jest niewystarczający z kilku powodów.

Po pierwsze, na co niedostatek drogiej kryptowaluty skoro można ją łatwo zaatakować, ocenzurować, lub inaczej przejąć z uwagi na niskie zabezpieczenia? Jeśli już, to te niskie zabezpieczenia obniżą wartość bardziej, niż niedostatek ją podwyższy. Po drugie, podaż Monero jest teoretycznie nieograniczona, inflacja jest liniowa i dąży do zera jako procent, w przeciwieństwie do fiata, którego podaż rośnie wykładniczo.

Inflacja Monero jest dokładnie znana zawczasu i może być dokładnie przewidziana, w przeciwieństwie do fiata, gdzie zmienia się ona w zależności od kaprysów władzy. Rozwiązanie Monero pozostawia duch cypherpunk, zgodnie z którym eliminuje się możliwość skorompowania przez kogoś, dzięki technologii blockchain, z tą zaletą, że bezpieczeństwo Monero będzie dostępne da świata tak długo jak będzie to potrzebne.

Ostatnim punktem jest kwestia sprawiedliwości. Pieniądze są wykorzystywane na różne sposoby – jako przechowywanie wartości, jako środek wymiany, czy też jako jednostka miary. W świecie, w którym jego podaż jest ograniczona inflacji nie będzie, co oznacza, że stosujący walutę jako sposób na przechowywanie wartości będą z niej korzystać za darmo. Zyskują na bezpieczeństwie zapewnianym przez minerów bez płacenia za nie, skoro bez inflacji ich pieniądze nie tracą wartości z czasem. Natomiast, każdy kto wykorzystuje walutę jako środek wymiany jest karany (poprzez wysokie opłaty transakcyjne). To zachęca ludzi do przechowywania, ale nie do wydawania i zaburza sprawiedliwość protokołu na korzyść przechowujących. Tail emissions balansują system i jego użytkowników. Wówczas przechowujący również płacą niski podatek, drogą inflacji, za bezpieczeństwo protokołu. Tail emissions sprawiają, że system jest bardziej sprawiedliwy dla wszystkich.

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

  * [Jak RingCT ukrywa ilości w transakcjach Monero](/knowledge/monero-ringct)/

  * [Jak stealth addresses chronią Twoją tożsamość](/knowledge/monero-stealth-addresses)/

  * [Jak subadresy zapobiegają łączeniu tożsamości](/knowledge/monero-subaddresses)/

  * [Wyjścia Monero wyjaśnione](/knowledge/monero-outputs)/

  * [Dobre praktyki Monero dla początkujących](/knowledge/monero-best-practices)/

  * [Jak ring signatures chowają wyjścia Monero](/knowledge/ring-signatures)/

  * [Jak Monero rozwiązało problem rozmiaru bloku nękający Bitcoina](/knowledge/dynamic-block-size)/

  * [Jak CLSAG poprawi wydajność Monero](/knowledge/what-is-clsag)/

  * [Krótka historia Monero](/knowledge/monero-history)/

  * [Oto dlaczego magazyn Wired myli się co do Monero](/knowledge/wired-article-debunked)/

  * [15 najczęstszych obalonych mitów i obaw o Monero](/knowledge/monero-myths-debunked)/

  * [Jak Dandelion++ prywatyzuje źródło transakcji Monero](/knowledge/monero-dandelion)/

  * [Dlaczego Monero jest open source i zdecentralizowane](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy](/knowledge/monero-mining-randomx)/

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better)/

Więcej do przeczytania