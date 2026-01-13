---
title: "Seraphis - Co zrobi dla Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: modułowa aktualizacja projektowania transakcji Monero

Ten post opisuje [Seraphis](https://github.com/UkoeHB/Seraphis), zbiór struktur protokołu transakcji i abstrakcji opracowanych przez pseudoanonimowego badacza [`koe`](https://github.com/UkoeHB) dla ekosystemu Monero i z bieżącą analizą bezpieczeństwa przez pseudoanonimowego współpracownika [`coinstudent2048`](https://github.com/coinstudent2048).  
Dokonamy kilku uproszczeń i pominiemy pewne szczegóły techniczne, aby zachować prostotę; z tego powodu i ponieważ projekt Seraphis jest nadal w toku, zainteresowani czytelnicy powinni zapoznać się z dokumentacją Seraphisa w celu uzyskania najaktualniejszych informacji.

## Transakcje w Monero

Protokoły takie jak Bitcoina, Monero i innych polegają na operacjach opartych na tak zwanym „output modelu”, gdzie _wyjście_ jest reprezentacją wartości, którą można przesłać.   
Transakcje zużywają jedno, lub więcej wyjść zgodnie z chęciami nadawcy i generują nowe wyjścia skierowane do odbiorców (lub z powrotem do nadawcy jako reszta [ang. change]). Transakcja musi być zbilansowana, tzn. zużyte wyjścia muszą mieć wartości dokładnie równe do wartości nowych wyjść (plus opłata narzucona przez sieć).   
W wielu protokołach, takich jak Bitcoina, wartość zawarta w wyjściu jest zapisana w sposób publiczny, podobnie jak odbiorca.   
Ponadto, patrząc na blockchain, trywialne jest sprawdzenie, czy i kiedy wydano wyjście (to znaczy, czy zostało zużyte w późniejszej transakcji i która transakcja to była). 

Natomiast protokoły takie jak Monero wprowadzają inny schemat: 

  * Wartości wyjść są ukryte i nie są widoczne na blockchainie 
  * Adresy odbiorcy są ukryte za pomocą protokołu jednorazowego adresowania 
  * Niezależnie od tego, czy wyjście zostało wydane, jest ono zasłonięte przez użycie niejednoznacznych podpisów 

W rezultacie, za wyjątkiem informacji zewnętrznych, trudno jest ustalić, czy dane wyjście zostało wydane, jaka jest jego wartość i kim jest jego odbiorca. 

Obecny protokół transakcji Monero nazywa się _RingCT_ i wykorzystuje kilka kryptograficznych elementów, aby osiągnąć te cele. 

  * _Commitments_ ukrywa kwoty w sposób matematycznie przydatny 
  * _Range proofs_ zapobiega przepełnieniu, które mogłoby zwiększyć podaż Monero
  * _Linkable ring signatures_ zapewnia niejednoznaczność sygnatariusza i zapobiega próbom podwójnego wydania jednych środków 
  * _Linkable ring signatures_ zapewnia równowagę transakcji 

Te klocki są starannie połączone, aby zbudować protokół RingCT. 

Przydatną właściwością protokołu RingCT jest to, że niektóre elementy składowe można zmienić lub ulepszyć w sposób, który zachowuje ogólną konstrukcję i właściwości nienaruszonymi, ale może też zapewnić poprawę wydajności lub bezpieczeństwa. W rzeczywistości tego rodzaju ulepszenia faktycznie nastąpiły (lub są planowane) kilkakrotnie w historii Monero. Range proofs w oryginalnym protokole RingCT były nieporęczne i powolne; zostały później zaktualizowane do konstrukcji o nazwie [Bulletproofs](https://eprint.iacr.org/2017/1066). Sprawiło to, że transakcje są mniejsze i szybsze, a do tego bezpieczniejsze. Ponadto planowane są aktualizacje, aby stworzyć nowszą konstrukcję o nazwie [Bulletproofs+](https://eprint.iacr.org/2020/735) dla jeszcze lepszej wydajności. 

Podobny proces przeszła technologia linkable ring signature building block. W pierwotnym protokole konstrukcja o nazwie [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) została wykorzystana. Następnie została zaktualizowana na nowszą pod nazwą [CLSAG](https://eprint.iacr.org/2019/654), która jest szybsza, tworzy mniejsze transakcje i ma lepsze bezpieczeństwo. Jeszcze nowsza konstrukcja ring signatures oparta na [Triptych](https://eprint.iacr.org/2020/018) została zaproponowana, ale nie została wybrana do wdrożenia ze względu na jej wpływ na operacje multisignature.

## Seraphis

Seraphis idzie o krok dalej.   
Zamiast aktualizować poszczególne elementy konstrukcyjne istniejącego protokołu transakcji RingCT, wprowadza inny protokół, który może skorzystać z różnych klocków i oferować lepszą funkcjonalność. 

## Klocki

Seraphis używa innego zestawu klocków kryptograficznych, aby osiągnąć swoje cele projektowe. 

  * _Commitments_ nadal ukrywają kwoty
  * _Range proofs_ nadal zapobiegają przepełnieniom i niepożądanej inflacji
  * _Membership proofs_ zapewniają niejednoznaczność sygnatariusza
  * _Commitment offsets_ nadal podają saldo
  * _Authorizing proofs_ zapobiegają podwójnemu wydaniu jednych środków

Zwróć uwagę: linkable ring signatures są zastępowane kombinacją membership proofs i authorizing proofs. Z grubsza, membership proofs zapewniają, że zużyte wyjście jest częścią większego zestawu, podobnie jak w RingCT. Ale w przeciwieństwie do RingCT, membership proofs w ogóle nie obejmują linking tagów! Authorizing proofs zapewniają, że linking tag jest poprawny i służą do podpisania końcowej transakcji. 

Ponieważ RingCT łączy linking tag z niejednoznacznym podpisem, operacje podpisywania (i multisignature) są bardziej intensywne obliczeniowo i stają się trudniejsze do budowania innej funkcjonalności związanej z tagami. Ale w Seraphisie konstruowanie membership proofs można bezpiecznie oddelegować z zaufanego urządzenia (które mogą mieć ograniczoną moc obliczeniową, jak chociażby portfel sprzętowy) na mniej zaufane urządzenie, a operacje podpisywania (i multisignature) są znacznie łatwiejsze przy użyciu dużo prostszego authorizing proofa . 

Na szczęście niektóre klocki wymagane przez Seraphis istnieją już gdzie indziej i nie muszą być projektowane od zera. Zarówno Bulletproofs i Bulletproofs+ mogą być użyte jako range proofs. Modyfikacje systemów udowodnienia typu Schnorr mogą być wykorzystane jako authorizing proofs. Poza tym wydajny [system udowodnienia](https://eprint.iacr.org/2015/643), używany już jako podstawa dla Triptycha, [Lelantusa](https://eprint.iacr.org/2019/373), i [Sparka](https://eprint.iacr.org/2021/1173)* może zostać zmodyfikowany pod membership proofs. 

* Cypher Stack otrzymuje dofinansowanie na rozwój Spark.

## Adresowanie

Niestety, obecnie używane adresy Monero nie są kompatybilne z Seraphisem. Użytkownicy musieliby wygenerować nowe adresy ze swoich kluczy, aby otrzymać Monero, gdyby Seraphis został zaimplementowany. Jednak ten koszt dla ekosystemu przyniósłby wiele korzyści.

Oprócz omówionych powyżej korzyści strukturalnych, projekt Seraphis umożliwia wiele różnych konstrukcji adresu, z których każda zawiera kompromisy. Przy czym końcowa konstrukcja adresów, która ma być użyta w Seraphisie, jest [wciąż rozstrzygana](https://github.com/monero-project/research-lab/issues/92) (jeden schemat zyskujący dużo popularności nazywa się [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)). Możemy opisać niektóre codzienne i przydatne funkcje. 

Możesz sobie zdawać sprawę, że adresy Monero oferują funkcjonalność _view key_. Umożliwia ona podanie klucza urządzeniu, lub stronie trzeciej, który pozwala oglądać przychodzące transakcje, ale bez możliwości ich wydawania. Jest to przydatne w przypadkach, w których chcesz uzyskać możliwość wglądu z zewnątrz. Przydatne chociażby dla organizacji charytatywnych lub firmy z działem księgowym. 

Wadą view keysów jest to, że nie zapewniają one kompletnego czy też szczegółowego dostępu do wglądu. Nie można tego wiarygodnie wykryć, gdy portfel wydaje fundusze, co utrudnia prawidłowe obliczenie salda portfela, gdy klucz spend key nie jest dostępny. Obecnie nie jest też możliwe wykrywanie przychodzących transakcji bez poznania również wartości zawartych w tych transakcjach (co oznacza, że wszyscy szukający transakcji przychodzących dowiedzą się ile nabywasz Monero). 

Konstrukcja adresów Seraphisa może te problemy rozwiązać. Stosując Seraphis Twój adres jest wyposażony w różne klucze, które mogą robić rozmaite rzeczy. Oto te klucze: 

  * Widzący przychodzące wyjścia, ale bez ich wartości 
  * Widzący przychodzące wyjścia wraz z ich wartością 
  * Widzący wychodzące wyjścia 
  * Pomagający Ci generować transakcje, ale niemogący ich podpisać
  * Generujący nowe adresy (przydatne dla sprzedawców lub giełd z wieloma klientami) 

Jako właściciel adresu możesz decydować, ile uprawnień przekazujesz innym urządzeniom lub stronom trzecim. 

## Konkluzja

Seraphis jest znaczną zmianą dla ekosystemu Monero. Chociaż modyfikuje adresy i składowe tworzenia transakcji, to oferuje elastyczność i przydatną funkcjonalność, które nie są możliwe z aktualnym protokołem RingCT. Podczas, gdy znaczna część projektu jest sfinalizowana i zrealizowana w [implementacji](https://github.com/UkoeHB/monero/tree/seraphis_lib), projektowanie schematu adresów i analizy bezpieczeństwa wciąż trwają. Seraphis oferuje doskonałą okazję do posunięcia ekosystemu Monero do przodu! 

Więcej do przeczytania