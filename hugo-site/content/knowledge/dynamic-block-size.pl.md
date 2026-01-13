---
title: "Jak Monero rozwiązało problem rozmiaru bloku nękający Bitcoina"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Uwaga:** Zdecydowanie zalecamy czytelnikowi przeczytanie naszych artykułów ["Czemu Monero ma Tail Emissions"](/knowledge/monero-tail-emission) i ["Kopanie Monero: Co czyni RandomX tak wyjątkowym” ](/knowledge/monero-mining-randomx). Ten artykuł opiera się na koncepcjach tam przedstawionych._

Ilekroć ludzie dyskutują o problemach z blockchainem, jednym z pierwszych tematów, które poruszą, będzie „skalowanie”. Nie jest tajemnicą, że blockchainy nie skalują się dobrze, ale większość ludzi nie wie dlaczego.

Prawda jest taka, że skalowanie to właściwie ogólny termin, który obejmuje dwie różne kwestie: możliwości protokołów i możliwości technologiczne w danej chwili. W tym artykule skupimy naszą uwagę na pierwszej kwestii. Możliwości protokołów są zasadniczo miarą liczby transakcji, które protokół może obsłużyć w danym momencie.

Bitcoin ma limit rozmiaru bloku, co oznacza, że po uwzględnieniu wystarczającej liczby transakcji w bloku wszelkie dodatkowe transakcje będą musiały czekać w kolejce na następny blok. Pomocną analogią byłoby wyobrażenie sobie pociągu. Pociąg podjeżdża na stację, a ci, którzy stoją w kolejce, wchodzą. Gdy pociąg jest pełny, każdy, kto zostanie na peronie, będzie musiał czekać na następny pociąg. 

Bitcoin wykorzystuje opłaty, aby określić, kto dostanie się do bloku, a kto nie. Wracając do analogii z pociągiem, można sobie wyobrazić, że jeden potencjalny pasażer, który ma zostać w tyle, oferuje maszyniście pięć dolarów za ustąpienie mu miejsca. Inni pasażerowie idą jego śladem i ostatecznie dochodzi do licytacji, aby ustalić, kto dostanie które miejsca. Do maszynisty należy decyzja, czy chce przestrzegać zasady „kto pierwszy, ten lepszy”, ale w jego najlepszym interesie finansowym leży maksymalizacja dochodów poprzez przyjmowanie na pokład pasażerów, którzy zaoferują najwyższą cenę.

W tej analogii minersi są maszynistami. Mogą zawierać dowolne transakcje w bloku, ale przeważnie wybiorą te, które mają najwyższe opłaty.

Alternatywnie, jeśli bloki nie są bardzo pełne, ludzie nie mają powodów do płacenia wysokich opłat, ponieważ jest mnóstwo wolnych miejsc.

W szczytowym okresie boomu kryptowalut w 2017 r. Bitcoin został zalany transakcjami, a opłaty gwałtownie wzrosły dla tych użytkowników, którzy chcieli zostać włączeni do następnego bloku lub dowolnego bloku w najbliższym czasie. Ci, którzy nie chcieli płacić wysokich opłat, widzieli, jak ich transakcje były opóźniane o godziny, dni, a nawet całkowicie wypadały z kolejki.

To był wstrząsający wgląd w to, jak Bitcoin może sobie radzić, gdyby doszło do często wspominanej „masowej adopcji”. Gdyby Bitcoin miał być używany przez masę ludzi, sytuacja byłaby jeszcze gorsza niż w 2017 r., a Bitcoin byłby niedostępny dla nikogo poza bogatymi, po prostu dlatego, że przepustowość jest niewielka ze względu na stały rozmiar bloku, wymuszając aukcje opłat.

Monero przewidziało tą sytuację i postanowiło zrobić coś innego. Dlatego programiści Monero wdrożyli dynamiczny rozmiar bloku.

Zasadniczo Monero również ma limit wielkości bloku, ale jest to miękki limit. Gdy kolejka oczekujących transakcji staje się zbyt długa, minersi mogą zwiększyć rozmiar bloków. Korzystając z naszej analogii pociągu, możesz sobie wyobrazić dodanie większej liczby wagonów, aby pomieścić dodatkowych pasażerów. Gdy kolejka jest pusta, bloki zmniejszają się do pierwotnego rozmiaru. 

Jeśli wydaje się to fajnym pomysłem, nasuwa się pytanie, dlaczego Monero jest jedyną kryptowalutą, która coś takiego zaimplementowała. Dlaczego nie dodać tego rozwiązania do Bitcoina celem położenia kresu problemom z przepustowością?

Niestety nie jest to możliwe. Jest kilka powodów, które postaramy się wyjaśnić.

Duże bloki zawsze leży w najlepszym interesie minera. Dzięki dużym blokom mogą zmieścić większą ilość transakcji i zarobić więcej pieniędzy na opłatach, a także na nagrodach blokowych. Może to prowadzić do ataków spamowych, w których ktoś wysyła wiele małych transakcji z niewielkimi opłatami, aby zapchać blockchain. Minersi po prostu zwiększyliby rozmiar bloku, przyjmując je wszystkie, ponieważ im się to opłaca, bez względu na to, jak niskie są opłaty tych kolejnych transakcji. Prowadziłoby to do coraz większych bloków. Bitcoin rozwiązuje ten problem, sztucznie ograniczając rozmiar bloku, wymuszając w ten sposób licytację opłat. Osoby spamujące musiałyby zapłacić więcej niż inni użytkownicy, a to nie jest takie tanie. Ale to oznacza, że bloki się zapełniają, pozostawiając niektóre transakcje oczekujące, jak wspomnieliśmy wcześniej. 

W jaki sposób Monero może mieć dynamiczne rozmiary bloków unikając ataków spamu? Odpowiedź jest prosta, ale sprytna. Kara za nagrodę za blok jest wprowadzana, gdy blok jest większy niż normalnie. Jeśli miner chce zwiększyć rozmiar bloku, nagroda, jaką otrzyma za znalezienie tego bloku, będzie mniejsza niż w innym przypadku. Zwiększa więc rozmiar bloku tylko wtedy, gdy opłaty transakcyjne uiszczane przez użytkowników przewyższą utraconą część nagrody za blok. Na przykład, jeśli miner straciłby 0,5 XMR poprzez zwiększenie rozmiaru bloku, a suma zapłaconych opłat transakcyjnych wyniosłaby 0,4 XMR, to gdyby zwiększył rozmiar bloku, poniósłby stratę w wysokości 0,1 XMR, więc tego nie zrobi. I odwrotnie, jeśli suma opłat transakcyjnych wyniosłaby 0,7 XMR, zysk netto wyniósłby 0,2 XMR, mimo że straci 0,5 XMR kary za blok, więc miner zwiększy rozmiar.

Te dynamiczne bloki pozwalają sieci rozwijać się organicznie, bez sztucznego ograniczania rozmiaru bloków w celu wymuszenia licytacji opłat transakcyjnych, przy jednoczesnym zapobieganiu spamowi. Jest jeszcze inny punkt widzenia, z którego możemy spojrzeć na tą ideę, i więcej powodów, dla których dodanie jej do Bitcoina nie byłoby możliwe, ale na razie mamy nadzieję, że czytelnik rozumie, w jaki sposób Monero omija kilka problemów występujących w Bitcoinie, i jego pochodnych, i jak Monero planuje skalować swoją przepustowość w przyszłości.

Więcej do przeczytania