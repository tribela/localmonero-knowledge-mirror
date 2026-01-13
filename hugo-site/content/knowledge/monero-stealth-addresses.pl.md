---
title: "Jak stealth addresses chronią Twoją tożsamość"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Prywatność Monero składa się z trzech technologii. Są to [ring signatures](/knowledge/ring-signatures), które ukrywają prawdziwe wyjście (nadawcę), RingCT, który ukrywa wartości transakcji oraz stealth addresses, które ukrywają odbiorcę. W tym artykule będziemy omawiać ostatnią z wspomnianych technologii: stealth addresses.

Istnieje wiele powodów, dla których ktoś może chcieć ukryć to z kim robi transakcje. Nie możemy pozwolić, aby ktokolwiek próbował nam wmówić, że wszystkie przykłady tego typu zachowań są podejrzane. Sprawy takie jak wysyłanie pieniędzy do niepopularnej partii politycznej, przekazywanie datków na cele charytatywne, czy wspieranie tych, których uznano za "wykluczonych" są przykładami, w których ktoś może chcieć ukryć odbiorców transakcji w obawie przed negatywnymi konsekwencjami, ale są to zachowania całkowicie legalne.

Na transparentnym blockchainie adresy, na które wysyłane są transakcje, są widoczne dla wszystkich. Należy pamiętać, że jeśli sam miner nie zgadza się z tym, gdzie trafiają kwoty, może zdecydować się na nieuwzględnienie ich w blockchainie i w następstwie ocenzurować tę transakcję na pozornie odpornej na cenzurę platformie. Jedyna szansa na to, aby ta cenzura nie była możliwa, jest wtedy kiedy minerzy nie mogą rozróżnić transakcji, ponieważ wszystkie metadane on-chain są w różny sposób ukryte. Z tego znane jest między innymi Monero.

Monero rozwiązuje problem jawnych adresów właśnie za pomocą stealth adresów. Jest to technologia, która została stworzona z myślą o Bitcoinie w 2011 roku przez użytkownika forum Bitcoin Talk, ByteCoina (związek z Bytecoinem, który później wprowadził adresy stealth, nie jest znany). Aktualna wersja adresów stealth jest wzbogacona o kilka ulepszeń względem początkowej wersji. Najpierw jednak, aby zobaczyć jak działają, porozmawiajmy o kluczach.

Wyczynem jest obracanie się w przestrzeni kryptowalut i nieusłyszenie nigdy o kluczach. Sformułowania takie jak "zrób kopię zapasową swojego klucza" często się powtarzają, ale kiedy przeciętny użytkownik Internetu zobaczy słowa takie jak "klucz publiczny" czy "klucz prywatny", przestraszy się i pomyśli, że są to zbyt techniczne i skomplikowane pojęcia, aby był w stanie je zrozumieć. Ale nie martw się, jak zawsze użyjemy dużo przykładów, abyś wszystko zrozumiał.

Dwa rodzaje kluczy używanych w kryptowalutach to, jak wspomniano powyżej, publiczny i prywatny. Te dwa klucze zazwyczaj występują w parze, co oznacza, że konkretny publiczny oraz prywatny klucz są ze sobą powiązane. W rzeczywistości, zazwyczaj klucz publiczny pochodzi z klucza prywatnego, czyli jeśli znasz klucz prywatny, to Twój portfel może wykonać pewne zgrabne obliczenia i wymyślić prawidłowy klucz publiczny za każdym razem.

Jak sugerują nazwy, klucz publiczny może być publiczny bez żadnych poważnych konsekwencji. Zazwyczaj jest częścią adresu, który udostępniasz, aby otrzymać pieniądze do swojego portfela kryptowalut. Również sugerując się nazwą, klucz prywatny nie powinien być udostępniany. Jest narzędziem, które pozwala na podpisanie oraz przeprowadzenie transakcji. Jeśli zostałby skradziony albo udostępniony, to osoba, w której ręce się dostanie, może wydawać Twoje kwoty z portfela.

Prostą analogią do tego byłaby kłódka i klucz potrzebny do jej otworzenia. Otworzona kłódka może być swobodnie używana przez inne osoby, ale jedyną osobą, która może ją otworzyć, gdziekolwiek by nie powędrowała, jest osoba posiadająca klucz. Kłódka może być kopiowana i udostępniana, klucz nie powinien być.

Te klucze są zazwyczaj oderwane daleko od użytkownika, więc nigdy ich tak naprawdę nie zobaczysz. W Monero nie są one przerażającymi, alfanumerycznymi ciągami. Zwykły użytkownik zna swój klucz prywatny pod pojęciem seeda. Seed (pojęcie, które powinieneś zapisać, jeśli jeszcze tego nie zrobiłeś) jest kluczem prywatnym przedstawionym w prostszej formie, czytelnej dla użytkownika.

Widzisz, to nie aż takie straszne jak się wydawało na początku. Wróćmy z powrotem do omawiania adresów stealth.

Jak wspomniano wcześniej, adresy stealth nie były pierwotnie stworzone dla Monero, tylko dla Bitcoina. Jednak jak w przypadku większości nowych pomysłów, ta pierwsza wersja miała pewne wady. Następna próba nadeszła, gdy Nicholas van Saberhagan stworzył CryptoNote dla Bytecoina, prekursora Monero ([ zobacz historię Monero i Bytecoina tutaj](/knowledge/monero-history)) i chociaż był to zdecydowany postęp w stosunku do oryginału, nawet on miał kilka subtelnych wad.

W końcu jedna ostatnia wersja powstała z inicjatywy dewelopera innej, nieistniejącej już kryptowaluty, która naprawiła wyraźne problemy związane z prywatnością i bezpieczeństwem tamtego pomysłu. Ta wersja trafiła do Monero i jest tym, co jest używane dzisiaj.

Mimo, że kwestie prywatności i bezpieczeństwa zostały rozwiązane, stealth adresy dodały dziwny, niepoprawny rodzaj zachowania do technologii blockchaina, który nie występował nigdy wcześniej - konieczność skanowania. Ponieważ adresy odbiorcze nie są publicznie wyświetlane na blockchainie, odbiorca nigdy nie wie, czy dana transakcja jest jego, więc musi skanować każdą przychodzącą transakcję za pomocą swojego klucza prywatnego, aby sprawdzić, która do niego należy.

W transparentnych walutach, wszystko, co musi zrobić, to sprawdzić czy transakcja jest wysyłana na jego adres. Z adresami stealth jest już trochę trudniej. Każda transakcja może być potencjalnie tą, która jest wysyłana do Ciebie. Musisz po kolei próbować otworzyć każdą z nich swoim kluczem prywatnym, aż któraś pozytywnie zareaguje.

Jest to dodatkowy krok, który Bitcoin i waluty z tej samej kategorii nie mają. Początkowa konfiguracja portfela oraz jego synchronizacja, kiedy nie otwierałeś go przez jakiś czas, trwa o wiele dłużej niż na przykład w Bitcoinie. Kompromis jest jednak konieczny, aby odblokować gwarancje prywatności, które posiada. Należy jednak zauważyć, że w przeciwieństwie do najsłabszej technologii prywatności Monero (ring signatures), adresy stealth nie są podatne na ataki. Polegają na wypróbowanej i prawdziwej krzywej eliptycznej kryptografii, na której opiera się cały Internet, więc złamanie ich oznaczałoby koniec bezpieczeństwa komputerowego na całym świecie, a nie tylko w Monero.

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