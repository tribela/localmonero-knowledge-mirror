---
title: "P2Pool i jego rola w decentralizacji kopania Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jednym z głównych celów projektu Monero jest umożliwienie uczciwej, zdecentralizowanej i bezpiecznej sieci poprzez wykorzystanie nowego i innowacyjnego podejścia do kopania proof-of-work (PoW) - wiodącego sposobu, w jaki sieci kryptowalut są dziś zabezpieczane. 

Co prawda unikalny algorytm kopania [taki jak RandomX](/knowledge/monero-mining-randomx) jest niezwykle ważny, aby osiągnąć ten cel, ponieważ sprawia, że każdy, kto ma komputer, może pomóc w zabezpieczaniu sieci, jednak RandomX nie rozwiązuje problemów, które mogą wystąpić z powodu kopania w poola. Kopanie w poolu jest zdecydowanie najczęstszym sposobem kopania kryptowalut dzisiaj, w tym Monero, ale na szczęście pojawienie się p2poola szybko to zmienia. 

## Czym jest mining w poolu?

Kopanie w poolu jest sposobem dla minerów na podzielenie się zadaniem rozwiązania bloku, a następnie równomiernego udostępniania nagród ze wszystkich bloków, które odnajdzie pool. Chociaż pomaga to bardzo wyrównać częstotliwość, z jaką minersi zarabiają w porównaniu z samodzielnym kopaniem, to wynikają z tego poważne problemy związane z centralizacją. 

Ponieważ każdy miner przyczynia się do pracy w poolu, to rezygnują oni z kontroli nad blokami na korzyść poola, ufając, że pool będzie szczerze i uczciwie dzielić nagrody między wszystkimi minerami w oparciu o ilość pracy wykonanej przez każdego z uczestników. Jeśli wszystko pójdzie dobrze, operator poola zbierze prace od wszystkich minerów, prześle je do sieci i równo podzieli nagrody.

## Jaki jest problem z pool mining?

Niestety opiera się to całkowicie na zaufaniu i pozwala operatorowi poola na zrobienie nikczemnych rzeczy z pracą wykonywaną przez minerów. Operator poola mógłby skorzystać z pracy w celu zaatakowania sieci, spróbować dwukrotnie wydać środki (jeśli pool jest wystarczająco duży) lub po prostu wykorzystać pracę wykonaną przez minerów, aby zapłacić sobie i nigdy nie nagrodzić minerów za ich pracę. 

Największym ryzykiem dla sieci jest pool (lub wiele pooli współpracujących ze sobą), posiadający ponad 51% hashrate sieci pod swoją kontrolą, ponieważ mógłby wykorzystać to do oszukania i wydania jednych środków dwukrotnie (atak double-spend) lub spróbować zmienić reguły sieci. 

## Czym jest p2pool?

p2pool to pomysł pierwotnie stworzony do kopania Bitcoinów w 2011 roku, ale nigdy nie doczekał się powszechnego wykorzystania i pozostał praktycznie nieużywany w Bitcoinie. Na szczęście jeden z kluczowych programistów RandomX, SChernykh, spędził wakacje opracowując rozwiązania na niektóre problemy w implementacji p2pool Bitcoina i napisał całe oprogramowania od podstaw. 

p2pool w Monero umożliwia współpracę w celu rozwiązania bloku i zabezpieczenia sieci Monero, bez wymagania zaufania. Jest to możliwe dzięki wykorzystaniu specjalnego oprogramowania p2pool w celu dzielenia się pracą. 

Odbywa się to przy użyciu nowego blockchaina („side-chaina”), który śledzi ile pracy wykonał każdy miner, ich adres portfela i to, ile zarobili Monero, a następnie płaci nagrodę w zdecentralizowany sposób niewymagający zaufania. Ponieważ ten sidechain ma znacznie mniej minerów, to o wiele łatwiej jest znaleźć i przesłać bloki niż w głównej sieci Monero, ułatwiając minerom uzyskanie częstych wypłat w porównaniu z główną siecią Monero. 

## W jaki sposób p2pool rozwiązuje problemy związane z pool miningiem?

W p2poolu nie ma scentralizowanego poola, scentralizowanego operatora poola oraz ani jednej osoby trzymającej wykopane środki i dystrybuującej wypłaty. Wszystkie działania minerów są weryfikowane przez blockchain p2pool i innych operatorów węzłów, aby upewnić się, że są to poprawne działania, a wszyscy minersi zarabiają proporcjonalnie do włożonej pracy natychmiast po wykopaniu nowego bloku. 

Gdy minersi decydują się na korzystanie z p2poola zamiast z poola scentralizowanego, eliminują konieczność powierzania władzy i zaufania operatorom pooli i zapewniają, że ich praca przyczynia się do dobra sieci i do ich własnego dochodu, zmniejszają ryzyko ataków na sieć i niewłaściwego użycia ich pracy lub kradzieży nagród, które są im należne. 

Nie tylko pomaga im to chronić własne interesy, ale zmniejsza zagrożenie, jakie scentralizowane poole mogą stanowić dla całej sieci Monero. Zastosowanie p2poola pomaga również znacznie zmniejszyć ryzyko, jakie rządy i ich organy, mogą stanowić dla sieci Monero, ponieważ nie ma scentralizowanych operatorów pooli pod presją, nie ma geograficznej koncentracji pooli, ani żadnego innego słabego punktu do wykorzystania przeciwko Monero. 

## Jakie są wady?

Na szczęście p2pool w Monero był dobrze zaprojektowany i zbudowany, dzięki czemu funkcjonuje wyjątkowo dobrze! Jednak główną wadą kopania w p2poolu jest to, że każdy miner, który chce korzystać z p2poola, musi uruchomić własny węzeł Monero, powodując, że proces rozpoczęcia kopania jest nieco bardziej zaawansowany. Jednak ten węzeł jest następnie wykorzystywany do obliczenia wszystkich informacji niezbędnych do budowania i sprawdzania bloków oraz zapewnia, że miner ma pełną kontrolę nad wykonywaną pracą. Węzeł może również funkcjonować jako zdalny węzeł dla portfela minera, budować sieć Monero i wiele więcej. 

Inną kluczową różnicą względem scentralizowanego kopania jest to, że mali minersi korzystający z p2poola będą czekali nieco dłużej między wypłatami niż w dużym scentralizowanym poolu, ale _bardzo ważne_ jest zauważenie tego, że z czasem nie doprowadzi to do zarabiania mniej Monero! p2pool będzie tak samo opłacalny, nawet dla małych minerów, jak scentralizowane poole. Niektóre z tych wariancji są kompensowane przez fakt, że p2pool nie ma żadnych opłat, ponieważ nie ma scentralizowanego operatora puli, któremu trzeba zapłacić za usługi! 

## Jak mogę zacząć?

Na szczęście, ze względu na doskonale zaprojektowany Monero p2pool i dzięki wielu członkom społeczności, którzy poświęcili czas, aby uprościć proces wydobycia przez p2pool, stał on się dużo łatwiejszy. Istnieje kilka sposobów na rozpoczęcie kopania z p2poola, ale ponieważ szczegóły techniczne wykraczają poza zakres tego artykułu, możesz dowiedzieć się więcej samodzielnie wchodząc w poniższe linki: 

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Jak mogę się dowiedzieć więcej?

Jeśli wzbudziło to Twoją ciekawość wokół kopania w p2poolu, zajrzyj do poniższych, dodatkowych linków z wyjaśnieniami na temat p2poola, jak działa i co oznacza dla Monero: 

  * [Oficjalna strona p2poola na GitHubie](https://github.com/SChernykh/p2pool)
  * [Oficjalna dokumentacja p2poola](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool is now live](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, a "block explorer" of sorts for p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: On his development of P2Pool a Decentralized XMR Mining Pool](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Więcej do przeczytania