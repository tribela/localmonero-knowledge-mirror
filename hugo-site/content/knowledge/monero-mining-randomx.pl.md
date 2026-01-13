---
title: "Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30 listopada 2019 r. Monero przeszło swój półroczny hard fork, przy czym najbardziej oczekiwaną zmianą było przejście ze starego algorytmu PoW, cryptonight na zupełnie nowy, opracowany wewnętrznie, RandomX. Społeczność Monero uważa, że RandomX jest daleko idącym krokiem w kierunku kopania egalitarnego, ale zastanówmy się głębiej, czy faktycznie tak jest.

## Powód

Aby ocenić, czy RandomX jest ulepszeniem, musimy najpierw zrozumieć, jaki jest cel miningu. Mining zabezpiecza blockchain przed podwójnym wydaniem środków za pośrednictwem konsensusu Nakamoto. Dokładne zawiłości tego, jak to działa są poza zakresem tego artykułu, ale można się o nich dowiedzieć z wielu różnych źródeł w Internecie. Liczy się to, że bezpieczeństwo pochodzi z hashów generowanych przez komputery (minerów), w konkurencji ze sobą, aby znaleźć matematyczne rozwiązanie niezbędne do stworzenia nowego bloku. Gdy to zrobią, dodają nowe transakcje do blockchaina. W zamian za ich pracę (hashe) otrzymują rekompensatę w formie nowych Monero.   
  
Istnieje wiele problemów, które mogą wystąpić w tej konfiguracji i wymaga ona odpowiedniego zachęcenia minerów do tego, żeby system pracował prawidłowo, ale skupmy się na jednym konkretnym problemie. Jeśli wydobycie ma być konkurencją, to co się stanie, gdy jeden miner zyska przewagę?

## Kontekst

Omówmy trochę sprzęt minerów. Minerzy używają komputerów do wykonywania pracy, ale wszyscy wiemy, że nie każdy komputer jest taki sam. Niektóre komputery są wystarczająco wydajne, aby obsługiwać sieci AI lub intensywne gry, podczas gdy inne mają problemy nawet z prostymi zadaniami. Te różnice w mocy obliczeniowej wpływają również na hashrate, czyli szybkość, z jaką szukają nowych bloków.   
  
Ale nawet te różnice między komputerami bledną w porównaniu z hashrate wyspecjalizowanego sprzętu, znanego również jako specjalizowane układy scalone (ASIC), które osiągają hashrate kilka rzędów wielkości większy niż zwykłe komputery.  
  
Poświęćmy trochę czasu na zbadanie, co sprawia, że układy ASIC są tak potężne. Wyobraź sobie, że moc wszystkich komputerów mieści się gdzieś na spektrum, które waha się od możliwości robienia wielu rzeczy, ale żadnej specjalnie szybko, do robienia tylko jednej rzeczy, ale robienia jej bardzo szybko. Procesory i układy ASIC znajdują się na przeciwległych krańcach tego spektrum.  
  
Procesory, które są we wszystkich standardowych komputerach, znajdują się na początku spektrum. Mogą robić wiele rzeczy, takich jak przeglądanie sieci, gra w gry lub renderować wideo, ale żadnej z nich nie wykonują szczególnie szybko. Elastyczność odbywa się kosztem wydajności.  
  
ASIC są na drugim końcu spektrum, mogą tylko jedną rzecz, ale robią ją w niewiarygodnym tempie. Mogą wykonywać tylko jedną funkcję matematyczną, ale ponieważ mogą ignorować wszystko inne, wzrost wydajności jest astronomiczny. Ta wydajność odbywa się jednak kosztem elastyczności, więc jeśli funkcja zmieni się nawet nieznacznie - na przykład x + y = z zmienia się na 2x + y = z - wtedy ASIC całkowicie przestanie działać.   
  
Nie każdy posiada układ ASIC, ale każdy ma komputer ze standardowym procesorem. Wymaganie układów ASIC może prowadzić do nieuczciwej przewagi dla osób, które mają możliwość w nie zainwestować.

## Zabawna analogia

Jeśli nadal jest to skomplikowane, być może pomoże następująca analogia. Wyobraź sobie loterię, w której tysiąc dolarów jest przyznawane co godzinę, a ta loteria pozwala wydrukować własne bilety! Zaczynasz drukować jak najwięcej biletów w swojej drukarce domowej, która może wydrukować jeden bilet na sekundę. Po odjęciu kosztów energii elektrycznej i atramentu widać, że nadal możesz zarobić, nawet jeśli wygrasz loterię tylko raz na kilka tygodni.   
  
Z czasem poszerzysz swoją działalność, aż będziesz miał cały pokój poświęcony drukarkom. W sumie 20. Wszystko jest ok ... aż do jednego fatalnego dnia.   
  
Okazuje się, że ktoś wynalazł nowy rodzaj drukarki. Może drukować tylko bilety na loterię. Nie może drukować zdjęć, dokumentów biurowych ani drukować dwustronnie, tylko bilety na loterię. Ale może wydrukować je z prędkością 1000 biletów na sekundę. Patrzysz na swój mały pokój drukarek. Masz ich 20. Potrzebujesz 980 więcej drukarek, aby nadążyć za jedną z tych nowych drukarek, a co jeśli ktoś ma dwie nowe?...   
  
Niestety przestajesz grać na loterii, ponieważ nie możesz już uzasadniać kosztów energii elektrycznej i atramentu.   
  
Ale poczekaj! Kilka tygodni później są nowe wiadomości! Projekt biletu zmienił się. Teraz liczby, które kiedyś znajdowały się na górze, są na dole. Nowe drukarki są tak nieelastyczne, że nie nadążają . Mogły tylko wydrukować poprzedni bilet. Nie mija dużo czasu, zanim ponownie z radością drukujesz. Przynajmniej dopóki ktoś nie stworzy nowej drukarki do nowego projektu biletu.

## RandomX

Gdzie w tym wszystkim pasuje RandomX? Ma on na celu wyrównanie przewagi ASICs, poprzez utrudnienie opracowania i produkcji ASICs. Robi to, wymagając od minerów stworzenia i wykonania losowego kodu zamiast hashowania opartego na algorytmie.   
  
Może to być wątpliwe, jak to rzeczywiście w czymkolwiek pomaga, więc wróćmy do naszej analogii drukarki. Pamiętasz, co się stało, gdy projekt się zmienił? Stare drukarki giganty stawały się przestarzałe każdej nocy, a nowe musiały zostać opracowane z myślą o nowym projekcie. Co by się stało, gdyby każdy nowy bilet na loterię musiałby przestrzegać nowego standardu projektowania każdego kolejnego losowania?   
  
Stworzenie nowej drukarki giganta stałoby się niezwykle trudne. Nie mógłbyś już planować tylko jednego projektu biletu. Ponieważ projekt jest losowy, producenci drukarki giganta musieliby dodać możliwości kolorów, sposoby drukowania różnych napisów, granic, kształtów i innych. Krótko mówiąc, maszyna, którą ostatecznie wymyślą, byłaby standardową, zwykłą drukarką, taką jaka jest dostępna dla każdego innego.   
  
Wdrażając tę ​​losowość w projektowanie biletów, znacznie zmniejszyliśmy wielką przewagę uzyskaną przez specjalistyczny sprzęt. RandomX robi to samo, ale z minerami.   
  
W ten sposób zalety uzyskane przez wybrane zamożne grupy są zminimalizowane, tak żeby rzeczywiście inwestowali w tworzenie „ASICs” dla RandomX i wymyślili silniejsze, lepsze procesory, które przyniosą korzyść całemu światu.   
  
Oznacza to, że szary człowiek z 20 drukarkami biletów powrócił do gry. Być może nadal będzie mu trudno, ponieważ te zamożne osoby nadal mogą kupić więcej drukarek niż on, ale przynajmniej teraz nie jest zdyskwalifikowany przez rzędy wielkości jednej maszyny. Jest konkurencyjny na swój mały sposób.   
  
Wiedząc, że nawet szary człowiek może być konkurencyjny w kopaniu Monero, zachęcamy wszystkich do wypróbowania tego czy to w portfelu GUI Monero, który ma obsługę kopania solo czy też pobierając oprogramowanie stworzone przez społeczność. Jest to łatwe, konkurencyjne i otwarte dla wszystkich.

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

  * [Dlaczego Monero ma Tail Emission](/knowledge/monero-tail-emission)/

  * [Krótka historia Monero](/knowledge/monero-history)/

  * [Oto dlaczego magazyn Wired myli się co do Monero](/knowledge/wired-article-debunked)/

  * [15 najczęstszych obalonych mitów i obaw o Monero](/knowledge/monero-myths-debunked)/

  * [Jak Dandelion++ prywatyzuje źródło transakcji Monero](/knowledge/monero-dandelion)/

  * [Dlaczego Monero jest open source i zdecentralizowane](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better)/