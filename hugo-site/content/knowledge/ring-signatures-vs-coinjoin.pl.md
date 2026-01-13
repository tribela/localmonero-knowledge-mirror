---
title: "Ring signatures w Monero vs CoinJoin jak w Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Ponieważ narzędzia poprawiające prywatność Bitcoinów zyskały większą uwagę i popularność, podlegają większej kontroli prawnej. Ta kontrola doprowadziła do [niedawnego ogłoszenie](https://twitter.com/wasabiwallet/status/1503091503207432193) od twórców portfela dodającego prywatność Bitcoinowi, portfela Wasabi, że zaczną cenzurować i odrzucać wejścia do mixerów, które uważają za nielegalne lub niezgodnie ich ToS, i zapłacą firmie analizującej blockchain za sprawdzanie wejść od uczestników mixerów. 

Zastosowaniu transakcji CoinJoin w celu ukrycia źródła Bitcoinów jest podstawą techniką poprawienia prywatności Bitcoina od wielu lat, a problemy i ryzyka związane z jej użyciem są niektórymi z podstawowych problemów, które ring signatures w Monero poprawiają i którym zapobiegają. 

W tym wpisie na blogu krótko przedstawimy porównanie CoinJoin i Ring Signatures, a także opowiemy dlaczego podejście przyjęte w Monero prowadzi do większej ochrony przed cenzurą, większej prywatności i mniejszych trudności dla użytkowników. 

## Czym jest transakcja CoinJoin?

Ponieważ wszystkie transakcje są całkowicie publiczne w Bitcoinie - ujawniają nadawcę, odbiorcę i kwoty - użytkownicy muszą podjąć dodatkowe kroki w celu zachowania prywatności, zwłaszcza przed osobami od których otrzymały Bitcoiny i osobami którym je przesyłają. W przypadku niepodjęcia żadnych kroków w celu poprawy prywatności ryzykują, że staną się obiektem cenzury, śledzenia, a nawet napadu.

Najlepszym rozwiązaniem poprawiającym prywatność w Bitcoinie jest narzędzie o nazwie [„ Coinjoin ”](https://bitcoiner.guide/qna/coinjoin/), w którym dwóch lub więcej użytkowników współpracuje (zwykle za pośrednictwem scentralizowanego koordynatora) w celu utworzenia specjalnej transakcji, która utrudnia zewnętrznym obserwatorom powiązanie wejść z wyjściami. Każdy uczestnik komunikuje się, aby wspólnie zbudować transakcję bez przekazywania kontroli nad swoimi środkami. Ostatecznie otrzymuje wyjście, którego poprzednia historia jest niejasna dla obserwatora.

To zaburza historię konkretnych UTXO, umożliwiając użytkownikom Bitcoinów zyskanie odrobiny prywatności. Jednak CoinJoin (jako zaimplementowany w portfelu Wasabi i Samourai, dwóch najpopularniejszych narzędziach do wykonywania CoinJoinów Bitcoinami) ma kilka wad: 

  * Ponieważ transakcje CoinJoin są całkowicie dobrowolne i wymagają aktywnego uczestnictwa, każdy uczestnik jednoznacznie informuje, że potrzebuje większej prywatności niż „normalni” użytkownicy Bitcoinów, potencjalnie wyróżniając się i powodując problemy z wydawaniem ich na wielu giełdach lub sklepach. Żaden użytkownik nie może zaprzeczyć, że uczestniczył w transakcji CoinJoin. 
  * Aby znaleźć innych chętnych, większość implementacji CoinJoina (w tym portfel Wasabi) używa scentralizowanego koordynatora, który łączy uczestników i pomaga im komunikować się oraz budować odpowiednią transakcję CoinJoin. Ten scentralizowany koordynator nigdy nie kontroluje funduszy użytkowników ale zyskuje szeroki wgląd w koordynowane transakcje, może cenzurować przychodzące wejścia (jak w przypadku portfela Wasabi) i można na niego naciskać, aby gromadził lub dzielił się informacjami o uczestnikach CoinJoinów. 
  * Użytkownicy chętni do wykonania CoinJoina o dużej wartości często czekają godzinami (a nawet dniami!), aby znaleźć wystarczającą liczbę uczestników, z którymi mogliby skoordynować operację. Prowadzi to do dużych opóźnień od momentu gdy użytkownik otrzyma fundusze, do momentu kiedy może wydać prywatnie. 
  * Prywatność zapewniana przez transakcję CoinJoin z czasem maleje, ponieważ inni uczestnicy wydają fundusze lub łączą swoje wyjścia ze swoją tożsamością za pośrednictwem giełd, bądź sklepów wymagających KYC. Oznacza to, że użytkownicy powinni regularnie przeprowadzać operacje CoinJoin, aby zachować prywatność.
  * W większości implementacji CoinJoina uczestnicy muszą użyć UTXO o stałej wielkości (tj. 0,1 BTC), aby utrudnić połączenie wejść i wyjść transakcji CoinJoin. Prowadzi to do wyższych opłat (z uwagi na więcej zbędnych transakcji w celu rozbicia dużej sumy), większej „toksycznej reszty” (środków, których nie można wydać bez utraty prywatności) i pozbawia mniejszych użytkowników możliwości poprawy prywatności, jeśli nie mają co najmniej tej stałej kwoty. 

## W jaki sposób ring signatures rozwiązują te problemy?

[W przeszłości pisaliśmy dogłębnie o ring signatures](/knowledge/ring-signatures), nie będę więc tutaj ich szczegółowo opisywać. Przyjrzymy się, w jaki sposób podejścia przyjęte w Monero rozwiązują znane problemy z CoinJoinem. 

> CoinJoin jest dobrowolny 

Ring signatures Monero są rdzenną cechą prywatnego protokołu, a _każda_ transakcja w sieci Monero je wykorzystuje. Oznacza to, że żadne transakcje nie wyróżniają się jako tych , którzy poszukują więcej prywatności niż „normalni” użytkownicy Monero, a wszyscy użytkownicy zyskują wiarygodną zaprzeczalność, że wydali środki w jakiejś dowolnej transakcji. Ponieważ wyjścia użytkownika nie koordynują ani nie uczestniczą z wabikami w transakcji, użytkownicy, którzy są właścicielami wejść wybieranych jako wabiki, mogą więc szczerze powiedzieć, że nie uczestniczyli w tej transakcji. 

> Zastosowanie scentralizowanego koordynatora 

Ponieważ ring signatures Monero są całkowicie nieskoordynowane i wymagają jedynie, aby rzeczywisty wydawca środków tworzył transakcję, nie ma potrzeby scentralizowanego koordynatora w Monero. Zapewnia to, że _nikt_ nie może odmówić Ci dostępu do prywatności w Monero i nie ma scentralizowanej jednostki, na którą można naciskać oraz żadnego łatwego ataku Sybil itp. O ile transakcja płaci odpowiednie opłaty, zyskujesz niemożliwy do ocenzurowania dostęp do prywatności, bezpieczeństwa i anonimowości w Monero. 

> CoinJoin wymaga płynności 

„Płynność” dostępna dla każdego, kto wydaje Monero, żeby wykorzystać jako wabik, zawsze jest całkowitym zestawem wyjść do łańcucha, więc nigdy nie brakuje wabików, wśród których można ukryć Monero. Ktoś, kto chce wydać Monero, może to zrobić w ~20 minut po otrzymaniu środków i nie musi wykonywać żadnych dodatkowych kroków, aby uzyskać silną prywatność w Monero. 

> Prywatność CoinJoina degraduje z czasem 

Ponieważ wyjścia Monero nigdy nie są znane przez sieć, prywatność dostarczana przez ring signatures jest znacznie mniej podatna na degradację po jakimś czasie. Użytkownik nie musi stale przesuwać wyjść przez sieć Monero, a poza niezwykle rzadkimi okolicznościami, nie traci prywatności w miarę upływu czasu. 

Jeśli użytkownik chce „odświeżyć” wabiki używane z wyjściem, może po prostu odesłać fundusze do siebie i być w stanie wydać je ~20 minut później. 

> CoinJoin zwykle wymaga wejść o stałej wielkości 

Jako, że kwoty są ukryte w każdej transakcji za pomocą [“Confidential Transactions”](/knowledge/monero-ringct) (stanowiących część „RingCT”), wabiki stosowane w każdej transakcji mogą mieć dowolny rozmiar. Nie ma potrzeby martwić się heurystyką opartą na ilości w Monero, dlatego transakcje są znacznie prostsze do zbudowania i mogą wykorzystać wabiki z dowolnego bloku i jakiejkolwiek kwoty na całym blockchainie Monero. 

## Jak mogę się dowiedzieć więcej?

Jeśli jesteś ciekaw i chcesz lepiej zrozumieć ring signatures lub transakcje CoinJoin, sprawdź poniższe linki: 

  * [Jak Ring Signatures Chowają Wyjścia w Monero](/knowledge/ring-signatures)
  * [Ring Signature - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [CoinJoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin Omówienie](https://6102bitcoin.com/coinjoin-overview/)

Więcej do przeczytania