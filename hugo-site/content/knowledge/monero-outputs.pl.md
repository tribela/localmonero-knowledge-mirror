---
title: "Wyjścia Monero wyjaśnione"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, podobnie jak inne kryptowaluty, wykorzystuje wyjścia jako sposób rozliczania środków. Wielu doświadczonych użytkowników kryptowalut prawdopodobnie słyszało ten termin wcześniej, ale nie wszyscy rozumieją, co oznacza i jak działa. Jak wyjaśniliśmy w naszym[ artykule o ring signatures](/knowledge/ring-signatures), wyjścia są rzeczywistą jednostką wymienianą na blockchainie między stronami transakcji. Są podobne do banknotu dolarowego, ale ich wartość nie jest żadnym stałym nominałem.

Wyobraźmy sobie hipotetyczną sytuację, w której otrzymujesz za jakąś pracę 16 dolarów w postaci banknota jednodolarowego, pięciodolarowego i dziesięciodolarowego. Masz teraz 16 dolarów, ale w portfelu masz trzy różne banknoty. Jeśli chciałbyś zapłacić komuś 6 dolarów, mógłbyś użyć banknotu pięciodolarowego i jednodolarowego, ale jeśli chciałbyś zapłacić komuś 8 dolarów, mógłbyś użyć tylko banknotu dziesięciodolarowego i otrzymać 2 dolary reszty. Albo gdybyś chciał zapłacić komuś 14 dolarów, musiałbyś użyć wszystkich trzech banknotów i otrzymałbyś 2 dolary z powrotem w reszcie. W chwili kiedy przekazujesz wszystkie trzy banknoty, nie masz pieniędzy w portfelu, dopóki nie dostaniesz reszty z powrotem.

Monero działa na podobnych zasadach. Wyobraźmy sobie kolejną sytuację. Tym razem prowadzisz sklep i dokonujesz trzech sprzedaży trzech różnych przedmiotów. Twoja zapłata to 1,5 XMR, 2,25 XMR oraz 5,25 XMR, w sumie 9 XMR. Masz teraz w swoim portfelu trzy różne wyjścia o podanych nominałach. Podobnie jak w przypadku dolarów, możesz chcieć zapłacić komuś 3 XMR. Aby to zrobić, możesz użyć nominału 5,25 XMR i otrzymać w reszcie 2,25 XMR, albo połączyć wyjścia 1,5 oraz 2,25 XMR i dostać z powrotem 0,75 XMR.

Jak tylko wyślesz transakcję, wyjścia, których użyłeś, będą wprowadzone w stan "zablokowany", co oznacza, że będą niedostępne, dopóki nie otrzymasz z powrotem swojej należytej reszty. Protokół odblokowuje środki (oddaje Ci resztę) po 10 potwierdzeniach, czyli około 20 minutach. Tak samo jak nie możesz użyć ponownie banknotów po przekazaniu ich kasjerowi, tylko resztę, którą od niego dostaniesz, tak samo też Twoje Monero jest niedostępne, dopóki nie otrzymasz z powrotem reszty.

Wróćmy z powrotem do przykładu, w którym chcesz komuś wysłać 3 XMR wykorzystując do tego wyjście, które zawiera 5,25 XMR. Nie możesz użyć tego wyjścia ponownie dopóki nie dostaniesz z powrotem swoich 2,25 XMR reszty. Natomiast nadal możesz posługiwać się swoimi pozostałymi wyjściami, ponieważ nie zostały one w żaden sposób wykorzystane. Nawiązując jeszcze raz do przykładu z dolarami, jeśli zapłaciłbyś komuś 8 dolarów banknotem dziesięciodolarowym, nie byłbyś w stanie wykorzystać 2 dolarów, których oczekujesz z powrotem, dopóki ich nie dostaniesz. W swoim portfelu nadal masz inne banknoty, których możesz używać i tak samo jest z pozostałymi wyjściami, które nie są aktualnie używane do żadnej transakcji.

Użytkowników często wprawia to w konfuzję. Zakładają, że mogą użyć jednego wyjścia równocześnie do wykonania kilku transakcji. Wyobraźmy sobie, że użytkownik posiada tylko jedno wyjście równowarte 20 XMR. Nie ma innych wyjść w swoim portfelu, a pragnie przekazać darowiznę dwóm fundacjom. Wysyła 5 XMR do jednej organizacji charytatywnej i jest zdezorientowany, bo był przekonany, że powinno mu zostać jeszcze 15 XMR. Tak jak się pewnie domyślasz, ich 15 XMR jest aktualnie zablokowane i będzie mogło być wykorzystane, kiedy zostanie zwrócone w postaci reszty (musi nastąpić 10 potwierdzeń, ten proces trwa mniej więcej 20 minut). Dopiero po odblokowaniu jego środków, może dokonać drugiej darowizny.

Powtórzmy jeszcze raz dla jasności. Powyższy problem nie zaistniałby, gdyby użytkownik posiadał kilka wyjść np. dwa wyjścia 10 XMR. Byłby w stanie wysłać obie darowizny jedną po drugiej bez konieczności czekania, ponieważ na każdą darowiznę przypada jedno wyjście. 

Niektóre portfele kryptowalut posiadają funkcję zwaną "zarządzanie wyjściem", która najzwyczajniej pokazuje wszystkie wyjścia (także ich równowartość) oraz umożliwia użytkownikowi wybór konkretnego wyjścia, na co i kiedy chce.

Na chwilę obecną, Monero GUI (portfel monero) wybiera wyjścia automatycznie za użytkowników, ponieważ często ta czynność wprawia ich w konfuzję, a nawet w niektórych przypadkach, gdy sami dokonują selekcji, prowadzi do naruszenia ich prywatności. Portfele, które posiadają funkcje zarządzania wyjściami, są aktualnie w trakcie tworzenia. Jest to między innymi nowy projekt - portfel Feather. 

Szczegółowo omówiliśmy jak wygląda transakcja od strony nadawcy. Ale co dzieje się na jej drugim końcu? Wróćmy znowu do przykładu, w którym wysyłamy komuś 3 XMR używając do tego wyjść 1,5 XMR oraz 2,25 XMR, czyli w sumie 3,75 XMR. Odbiorca NIE otrzymuje całej tej sumy, tylko jedno wyjście o wartości 3 XMR.

Protokół łączy wszystkie wyjścia wykorzystane do zapłaty, daje odbiorcy jedno wyjście o wartości zapłaty oraz wysyła jedno wyjście z powrotem do nadawcy o wartości reszty. Obie strony, nadawca i odbiorca, otrzymują jedno wyjście z powrotem. Nie ma tutaj znaczenia czy nadawca użył dwóch, trzech czy dziesięciu wyjść do wykonania transakcji.

Mamy nadzieję, że to rozjaśniło niezrozumienie dotyczące wyjść, tego jak działa rozliczanie transakcji przez protokół oraz zablokowanych środków. W następnym artykule zajmiemy się tym jak zarządzać swoimi wyjściami, aby zmniejszyć czas oczekiwania na odblokowanie środków.

Więcej do przeczytania