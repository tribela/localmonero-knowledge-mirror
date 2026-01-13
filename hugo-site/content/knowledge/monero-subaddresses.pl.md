---
title: "Jak subadresy zapobiegają łączeniu tożsamości"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero zawsze znajdowało innowacyjne sposoby na rozwiązywanie trudnych problemów związanych z prywatnością. Często te innowacje prowadziły do innych. Czasami te nowo powstałe technologie okazywały się być użyteczne w innych aspektach niż zamierzano. Nigdzie nie jest to bardziej widoczne niż w przypadku technologii subadresu Monero.

Wyobraź sobie hipotetyczny problem z zakresu prywatności, w którym użycie jednego adresu na wielu platformach przez pozornie niepowiązane osoby może doprowadzić do powiązania i identyfikacji tych osób. Mówiąc prościej, jeśli byłbyś osobą o imieniu Billy Joe Bob i sprzedawałbyś jabłka za Bitcoiny, mógłbyś opublikować swój adres Bitcoina w miejscu publicznym, aby klienci mogli Ci szybciej zapłacić. Powiedzmy, że adres jest ciągiem alfanumerycznym zaczynającym się od 7XybV3. Pomijając oczywiste ryzyko naruszenia prywatności związane z tym, że każdy może zobaczyć Twoje saldo Bitcoin, ile sprzedałeś itd; to istnieje też drugie ryzyko, o którym rzadko ktokolwiek wspomina. Załóżmy teraz, że jesteś także hakerem pod pseudonimem l33tz0r. Informujesz nieświadomych ludzi o różnego rodzaju nieprawidłowościach tj. korupcji w rządzie. Konieczne jest abyś zachował swoją tożsamość w tajemnicy. Za swoją pracę otrzymujesz datki w postaci Bitcoinów. Przesyłane są one na adres, który wcześniej zamieściłeś na publicznym forum. Jest to ten sam adres, na który otrzymujesz zapłaty od klientów, którym sprzedajesz jabłka, czyli 7XybV3....

Prostym, ale niszczycielskim atakiem deanonimizacji byłoby użycie wyszukiwarki internetowej do wyszukania adresu Bitcoina. Umieszczenie adresu 7XybV3... w wyszukiwarkę zwróciłoby dwa różne wyniki - biznes jabłkowy i l33tz0r. To by wystarczyło, aby połączyć dwie tożsamości i zdeanonimizować l33tz0r, z potencjalnie przerażającymi konsekwencjami ze strony władzy.

Ważne jest to żeby pamiętać, że ten atak jest RÓWNIEŻ możliwy w Monero. Mimo że Monero ukrywa większość danych, on chain atak nie wykorzystuje żadnych. Wykorzystuje tylko adres, który trzeba udostępnić, aby otrzymać płatność. Natomiast w przypadku anonimowych darowizn udostępnić publicznie. Jest to jeden z potencjalnych sposobów, w jakich użytkownicy Monero mogą nieświadomie osłabić swoją prywatność, a także pokazuje, że mimo najwyższego standardu prywatności on chain Monero nie jest niezadowne.

Najczęstszym sposobem obejścia tego problemu było posiadanie wielu portfeli. Z różnym adresem opublikowanym na każdą tożsamość (lub przypadek użycia), nie można było ich połączyć. Ale ta prywatność obowiązuje tylko wtedy, gdy użytkownik nigdy ich nie pomyli. Przypadkowe umieszczenie nieprawidłowego adresu skutkowałoby ich powiązaniem. Co więcej, seed każdego adresu musi być bezpieczny, wymuszając więcej ilości niezbędnej pracy wraz z każdym nowym portfelem.

Rozwiązaniem dla Monero były subadresy - możliwość tworzenia gigantycznej liczby adresów z jednego adresu głównego, używając go jako swego rodzaju zalążka. Każdy wygenerowany subadres może akceptować Monero, a całość trafia do tego samego portfela. Korzystając z tej metody, liczba tożsamości, które mogą być obsługiwane przez jeden adres, jest ogromna, przy znikomej konieczności przestrzegania zasad infosec. Te adresy również nie są matematycznie powiązane, więc jeśli użytkownik nie wykrzyczy ich powiązania w świat, zewnętrzny obserwator będzie miał duże trudności z ich połączeniem.

Ale inne interesujące zastosowanie wyłoniło się z subadresów; jako zamiennik powszechnie znienawidzonych payment IDs.

Payment IDs umożliwiały sprzedawcom identyfikację klienta, który wysłał daną płatność. Ponieważ informacje Monero są ukryte on chain, odbiorca transakcji nie jest w stanie zobaczyć, z którego adresu nadawca ją wysłał. Oznacza to, że jeśli istnieją produkty o podobnej cenie i jest wiele zamówień i wówczas określenie, kto co wysłał, może stać się niemożliwe. Identyfikatory płatności to unikalny, losowy ciąg znaków generowany przez sprzedawcę i przekazywany klientowi. Klient dodaje go do osobnego pola podczas wysyłania transakcji. Ten losowy ciąg jest umieszczany na blockchainie jako część transakcji, dzięki czemu sprzedawca może identyfikować i sortować przychodzące płatności.

To rozwiązanie było problematyczne z kilku powodów. Po pierwsze, szkodziło jednolitości danych w on chain. Dodatkowe, unikalne metadane mogą wyróżnić niektóre transakcje z tłumu, umożliwiając tym samym analizę heurystyczną. Jest to szczególnie ważne, gdy te metadane nie są wymuszane na wszystkich obowiązkowo. Uczynienie ich obowiązkowymi dla wszystkich zwiększyłoby jednak niepotrzebnie przestrzeń zajmowaną przez blockchain i nie zostałoby zrealizowane. Ponadto, gdyby Payment ID został kiedykolwiek ponownie użyty, z jakiegokolwiek powodu, powiązanie dwóch transakcji jako połączonych byłoby trywialne. Zwykle miało to miejsce w przypadku wpłat na giełdę i każdy mógł łatwo połączyć transakcje jako wpłaty od jednej osoby.

Po drugie, z perspektywy użytkownika, Payment IDs tworzą drugi krok, do którego użytkownicy kryptowalut migrujący z innych monet nie są przyzwyczajeni, a jeśli zostanie on pominięty, to spowoduje to ogromne utrudnienia u sprzedawcy, który musi zidentyfikować te transakcje za pomocą innych sposobów. Zwykle robiono to, rozmawiając bezpośrednio z każdym klientem, który zapomniał podać Payment ID, oraz potwierdzając inne informacje identyfikujące, które tylko on mógł znać, takie jak kombinacja kwoty, daty wysłania i identyfikator transakcji.

Ten dodatkowy krok był pomijany przez wielu i doprowadziło to do sytuacji, w której niektóre giełdy zaczęły pobierać pieniądze od klientów, jeśli ich Monero musiały zostać odzyskane ręcznie z powodu niepodania Paymentu ID. Inni zaciskali zęby i pokrywali dodatkowe koszty obsługi klienta, ale nikt nie był z tego zadowolony.

Powstało jedno rozwiązanie - zintegrowane adresy, które łączyły adres i Payment ID w jeden ciąg, więc nie można było o nim zapomnieć, ale niewielu użytkowników zdecydowało się korzystać z tej technologii pomimo korzyści, jakie handlowcy zyskaliby z jej użycia. 

Ostatecznie zadebiutowały subadresy i rozwiązały problem. Zdolność generowania wielu subadresów dla jednego adresu głównego i rozpoznawania transakcji na podstawie ich docelowego subadresu, pozwoliła sprzedawcom na pozbycie się payment IDs w elegancki sposób, przy jednoczesnym przyjęciu technologii nowej generacji w Monero. Od tego czasu większość giełd i narzędzi dla sprzedawców przeszła na subadresy jako podstawowy sposób identyfikacji transakcji.

Zaczęło się od rozwiązania problemu prywatności, a przekształciło się w coś znacznie więcej, co ostatecznie rozwiązało poważny problem związany z prostotą użycia zarówno dla sprzedawców, jak i klientów. Innowacja rodzi więcej innowacji i często doprowadza do nieoczekiwanych usprawnień dla wszystkich. Monero przechodziło to wielokrotnie i społeczność wkłada ogromny wysiłek w poszerzanie możliwości technologii blockchain. Kto wie, co jeszcze możemy wspólnie osiągnąć?

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