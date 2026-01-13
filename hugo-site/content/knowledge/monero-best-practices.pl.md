---
title: "Dobre praktyki Monero dla początkujących"
slug: "monero-best-practices"
date: "2020-09-18"
image: "/images/practices.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Wielu użytkowników może być zszokowanych, gdy dowie się, że eksperci uważają, iż możliwe jest nieprawidłowe użycie kryptowalut. W zależności od tego, przed czym użytkownik się broni, istnieją pewne kroki i środki ostrożności, które należy podjąć w celu zachowania prywatności, uniknięcia oszustw i zapewnienia właściwego i terminowego dostarczania transakcji. Na szczęście deweloperzy Monero zrobili wszystko co w ich mocy, aby ustawić rozsądne wartości domyślne w tych obszarach, więc użytkownicy korzystający z oprogramowania portfeli są bezpieczni. To powiedziawszy, chcielibyśmy poświęcić trochę czasu, aby spojrzeć na kilka przypadków, w których pomocne może być pomyślenie i koncentracja podczas wydawania.

## ZAPISZ SWÓJ SEED!

Pierwszym i najważniejszym sposobem na zabezpieczenie kryptowalut jest zapisanie seeda mnemotechnicznego Monero, które jest krótką listą słów pokazaną podczas tworzenia portfela. Jeśli masz ten seed, ale komputer/telefon umiera, możesz odzyskać Monero. Jeśli nie masz tego seeda i tracisz portfel, to Twoje Monero jest utracone i nikt nie może pomóc Ci go odzyskać. Nie dziel się również tym seedem z nikim. Jeśli ktoś ma tę listę słów, to ma pełny dostęp do Twojego Monero. Wielu nieostrożnych z zabezpieczeniem seeda straciło swoje pieniądze. Zalecamy jego zapisanie. Fizycznie. Nie przechowywanie go cyfrowo i upewnianie się, czy masz kilka kopii w różnych miejscach. To jest najistotniejsza rzecz, którą możesz zrobić, aby zabezpieczyć swoje Monero. ZAPISZ SWÓJ SEED! 

## Dwukrotnie sprawdź swoje adresy

Niektóre oszustwa wykorzystują złośliwe oprogramowanie na komputerze, które zmienia funkcjonalność kopiowania/wklejania, aby wkleić adres twórcy złośliwego oprogramowania zamiast zamierzonego odbiorcy. Ponieważ adresy Monero są długie i nieporęczne, może być kuszące, aby po prostu zweryfikować kilka pierwszych cyfr i liter i uznać, że wystarczy, albo w ogóle nie sprawdzać adresu. Chociaż prawdopodobnie nie jest konieczna weryfikacja całego adresu, sprawdzenie pierwszych kilkunastu i ostatnich znaków adresu wystarczy w większości przypadków. W przypadku adresów, na które często wysyłasz, wiele portfeli ma funkcję książki adresowej, która automatycznie wprowadza zapisany adres. Nadal jednak najlepiej dokonać szybkiej kontroli. 

## Poznaj różnicę między portfelami hot i cold

Portfele hot i cold są powszechną terminologią w przestrzeni kryptowalut, a koncepcja jest naprawdę dość prosta. Portfel hot to taki, który często otwierasz i używasz. Jest „hot” od bycia w tylnej kieszeni. Portfele cold to te, które nie są często dotykane, podobnie jak pieniądze w banku. Tak jak nie jest wskazane noszenie tysięcy złotych w swoim portfelu, ale ogólnie jest to możliwe do zrobienia na koncie bankowym. Użytkownicy powinni zastanowić się, ile Monero jest rozsądnie nosić w portfelach hot, takich jak portfele mobilne i ile najlepiej zostawić w drugim porfelu - cold. W ten sposób utrata telefonu, kradzież lub inny wypadek nie spowoduje utraty wszystkich środków.

## Czy portfele sprzętowe są odpowiednie dla Ciebie?

Jeśli pomysł, aby Twoje środowisko cyfrowe było całkowicie wolne od wirusów i złośliwego oprogramowania w celu ochrony Monero, jest dla Ciebie przerastający, możesz rozważyć portfel sprzętowy [ang. hardware wallet]. Zasadniczo portfel sprzętowy trzyma prywatne klucze na urządzeniu, z dala od komputera. Więc nawet jeśli komputer zostanie przejęty, to hakerzy nie będą mieli dostępu do Twojego seeda. Będziesz mógł wydać środki tylko wtedy, gdy portfel sprzętowy będzie podłączony do komputera i będzie podpisywał transakcję. To przenosi bezpieczeństwo kluczy z komputera, który jest używany do wielu rzeczy i można go łatwo zaatakować, do portfela sprzętowego, który jest używany tylko do jednej rzeczy i ma znacznie mniej szans na atak. Dla zwykłej osoby, która nie zna tajników bezpieczeństwa komputerowego, jest to realna opcja, aby zapewnić bezpieczeństwo środków. 

## W razie wątpliwości wybierz opcje domyślne (z Monero)

W sferze, gdzie każdy stara się mieć jak największą prywatność, łatwo o przypadkowy wyciek danych, który może później posłużyć do zidentyfikowania. Przykładem tego są spersonalizowane rozmiary ringów. Jeśli ich domyślna wartość to 11, to większość osób będzie używać właśnie jej. Niektórzy wybierają zastosowanie ringu o rozmiarze 54, ponieważ im wyższa wartość, tym lepsza anonimowość. Są błędnie przekonani, że przez to będą bardziej prywatni, ale wręcz przeciwnie. Ich transakcje są teraz łatwiejsze do zidentyfikowania, ponieważ wyróżniają się pośród wszystkich pozostałych. Na szczęście Monero dokonało aktualizacji, aby uchronić swoich użytkowników przed ich własnymi błędami, która ustaliła stały rozmiar ringów na 11.

W innych sferach kryptowalutowych takich jak Bitcoin istnieje kilka czynności, które można zrobić i przypadkowo zaszkodzić swojej prywatności. Wybieranie reputable mixer, nienabywanie waluty poprzez KYC/AML, nieużywanie ponownie adresów oraz odpowiednie zarządzanie wyjściami są działaniami, które są konieczne, kiedy próbujemy zmniejszyć prawdopodobieństwo wycieku metadanych. Monero unika wielu z tych problemów poprzez swoje obowiązkowe funkcje prywatności oraz odpowiednie wartości domyślne. Wcześniejszy przykład dotyczący stałego rozmiaru ringu potwierdza to sformułowanie.

Większość użytkowników zostałaby urażona, gdyby usłyszała stwierdzenie, że oprogramowanie automatycznie robi wszystko za nich. Nic nie może być dalsze od prawdy. Jeśli chodzi o prywatność, większość kryptowalut ma dużo braków w tej kategorii. Ilość starań jakie użytkownik musi włożyć, żeby uzyskać jakikolwiek poziom prywatności, jest zbyt duża i wymagająca dla niedoświadczonego użytkownika. Jest tak także w przypadku innych kryptowalut skupiających się na prywatności! Monero stara się, aby prywatność jaką oferuje była automatyczna, nie wymagała od użytkownika interakcji na poziomie protokołu, jeśli to możliwe oraz polegała na domyślnych ustawieniach portfela, jeśli tamto byłoby niemożliwe.

Więcej do przeczytania