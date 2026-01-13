---
title: "Jak ring signatures chowają wyjścia Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero jest powszechnie znane w przestrzeni kryptowalut jako lider walut prywatnych. Podczas gdy wszyscy wiedzą, że Monero oferuje dobrą prywatność, nie tak wielu rozumie, jak ona działa.

Wiele innych walut prywatności publikuje infografiki z wykresami porównującymi technologię prywatności każdej kryptowaluty. Głównie przypisują Monero tylko technologię RingCT, ale to tylko częściowo prawda. Monero ma w rzeczywistości trzystronne podejście do prywatności. Pierwsza technologia ukrywa odbiorcę transakcji, druga wysłaną wartość, a trzecia użyte wyjście. Są to odpowiednio: stealth addresses, RingCT i ring signuatures.

To wielostronne podejście oznacza, że jeśli któraś technologia przestałaby działać prawidłowo, to dwie pozostałe nadal zapewniłyby prywatność. Ring signatures są najsłabszym ogniwem z wszystkich trzech; słowo słaby oznacza tu najbardziej podatny na ataki. Przyjrzyjmy się im bliżej.

Jak wspomniano powyżej, celem ring signatures jest zamaskowanie wyjścia użytego w transakcji. Jeśli terminologia "wejścia/wyjścia" kryptowaluty jest dla Ciebie zagmatwana, nie martw się, bo w rzeczywistości nie jest to tak skomplikowane jak się wydaje. Kiedy słyszysz słowo "wyjście", pomyśl o czeku. Rzecz, która nie jest już taka powszechna, ale idealnie odzwierciedla działanie transakcji kryptowalutowych. Czek, tak samo jak kryptowaluta, może mieć dowolną wartość np. 10 dolarów lub 32,50 dolarów. Jest on wymieniany między stronami transakcji. Wyjście działa tak samo, najpierw znajduje się w posiadaniu nadawcy, a po finalizacji transakcji trafia do odbiorcy.

Kiedy ktoś zapłaci Ci 10 Monero, to otrzymasz wyjście 10 XMR. Wyjście to ma wartość 10 i jest pobierane z portfela nadawcy w ten sam sposób, gdy płacisz za usługę. Wtedy banknot opuszcza Twój fizyczny portfel i jest przekazywany osobie, u której dokonujesz zakupu.

Wyjście ukrywane jest za pomocą konstruowania ringu (stąd ta nazwa) składającego się z różnych wyjść (wabików), których zadaniem jest odwracanie uwagi od prawdziwego wyjścia. Nie są one sztucznie wygenerowanymi wyjściami, a prawdziwymi przeszłymi wyjściami z blockchaina. Nie mają one nic wspólnego z aktualną transakcją, ale dla zewnętrznego obserwatora wyglądają tak samo jak faktyczne wyjście. Wyjścia wabiki oraz prawdziwe wyjście to rozmiar ringu. Aktualny rozmiar ringu w Monero wynosi 11. Zatem składa się na niego 10 "nieprawdziwych" wyjść oraz 1 prawdziwe.

Skoro im więcej "nieprawdziwych" wyjść tym trudniej rozpoznać prawdziwe wyjście, to dlaczego zatem nie zwiększymy rozmiaru do 100 czy nawet 1000? Mając na względzie aspekt prywatności jest to prawdą, ale istnieją inne rzeczy, które powinniśmy uwzględnić. Posłużmy się przykładem, aby lepiej to zobrazować. Jeśli chciałbyś ukryć jednego ze swoich banknotów wśród dziesięciu nieprawdziwych, musiałbyś nosić w portfelu jedenaście dolarów na każdy dolar, który chciałbyś wydać. Jeden prawdziwy dolar i dziesięć fałszywych. To już wystarczająco utrudnia proces, nawet jeśli chcesz wydać tylko kilka dolarów. Teraz wyobraź sobie, że zwiększyliśmy ilość wabików do 1000. Teraz musiałbyś nosić przy sobie 1001 dolarów na każdy jeden dolar, który chcesz wydać. Musiałbyś nosić ze sobą teczkę pieniędzy, tylko po to, by móc kupić sobie batonika! Ważne jest, aby zdawać sobie sprawę, że ring signatures nie działają dokładnie w ten sposób, np. wabiki same w sobie nie są częścią signature, a tylko referencjami służącymi do skonstruowania ringu. Mamy nadzieję, że ta analogia choć trochę pomogła w zobrazowaniu podstawowych pojęć.

Podobnie działają wabiki na blockchainie. Każdy kolejny wabik zwiększa czas i koszt weryfikacji transakcji. Każdy węzeł musi pobrać cały ring signature na każdą jedną transakcję, czyli wszystkie wyjścia, które do niego należą, również te "nieprawdziwe". Oprócz tego musi zweryfikować, czy chociaż jedno z wyjść jest tym prawdziwym. Czas tego procesu także zwiększa się wraz z ilością wyjść. Oznacza to, że musimy znaleźć kompromisowy rozmiar ringu, który jest na tyle duży, by dostatecznie ukryć prawdziwe wyjście, nawet przed atakami oraz wystarczająco mały, aby nie powodować zwiększenia blockchaina w ogromnym tempie. Nie możemy wybrać przypadkowej liczby lub po prostu zwiększyć rozmiaru ringu, kiedy chcemy "skuteczniej" ukryć prawdziwe wyjście (tak jak jest w przypadku CLSAG). Społeczność Monero wymaga konkretnych, matematycznych obliczeń, które dowodzą jaki rozmiar ringu oferuje najlepszą wymianę. Zbyt mała liczba, a prywatność nie będzie wystarczająco silna przeciwko atakom. Zbyt duża, a będziemy mogli uzyskać tylko marginalne korzyści po stronie prywatności i niepotrzebnie cierpieć przez skalowanie.

Ostatnia rzecz, o której warto wspomnieć to fakt, że niektóre artykuły upraszczają i piszą, że ring signatures ukrywają nadawcę. Nie jest to do końca prawdą, a uogólnienie to nie jest drobne. Różnica między nadawcą (człowiekiem) a wyjściem (rachunkiem) jest duża, jeśli chodzi o zabezpieczanie prywatności. Podczas gdy dane wyjściowe mogą być powiązane z nadawcą, to same w sobie nie są równe nadawcy. Nawet jeśli ring signature miałby zostać złamany, to trudno byłoby powiązać go z jakimś nadawcą, a zarówno wartość, jak i odbiorca byłyby nadal ukryte. Naruszenie prywatności użytkownika byłoby wtedy minimalne.

To nie oznacza, że złamany ring signature jest nieznaczący. Każdy wyciek metadanych to nic dobrego i może ujawnić więcej informacji niż by nam się wydawało. Dlatego robimy wszystko co w naszej mocy, aby upewnić się, czy wybrany rozmiar ringu opiera się na faktycznych badaniach, wyciek metadanych jest możliwie jak najbardziej zminimalizowany oraz czy ustawienia domyślne zapewniają użytkownikowi najlepsze możliwe rozwiązania.

Jeśli prawdopodobieństwo, że ring signature zostanie złamany nadal Cię martwi, mamy dla Ciebie dobrą wiadomość. Następna generacja protokołów prywatności, nad którymi aktualnie trwają prace, takich jak Triptych, Arcturus i Lelantus, oferuje naprawdę pomysłowe rozwiązania. Te protokoły miałyby skalować rozmiar ringu logarytmicznie wraz z jego wzrostem, a nie liniowo. Oznacza to, że możemy zmieścić 100 nieprawdziwych wyjść, ale wykorzystana przestrzeń jest bliższa rozmiarowi ringu o wartości 10 starej technologii. To spora różnica, która znacznie poprawi poziom prywatności.

W rozgrywce, jaką jest prywatność, Monero cały czas wprowadza coraz to nowsze innowacje, aby wyprzedzić wszystkich pozostałych.

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

  * [Jak Monero rozwiązało problem rozmiaru bloku nękający Bitcoina](/knowledge/dynamic-block-size/)

  * [Jak CLSAG poprawi wydajność Monero](/knowledge/what-is-clsag/)

  * [Dlaczego Monero ma Tail Emission](/knowledge/monero-tail-emission/)

  * [Krótka historia Monero](/knowledge/monero-history/)

  * [Oto dlaczego magazyn Wired myli się co do Monero](/knowledge/wired-article-debunked/)

  * [15 najczęstszych obalonych mitów i obaw o Monero](/knowledge/monero-myths-debunked/)

  * [Jak Dandelion++ prywatyzuje źródło transakcji Monero](/knowledge/monero-dandelion/)

  * [Dlaczego Monero jest open source i zdecentralizowane](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy](/knowledge/monero-mining-randomx/)

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better/)