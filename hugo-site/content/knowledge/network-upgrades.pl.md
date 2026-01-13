---
title: "Jak Monero używa hard forków do aktualizacji sieci"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
W tym poście opowiemy o tym, czym są hard forki, dlaczego są ważne dla Monero i jaką rolę możesz na nich odegrać w przyszłości.

## Dlaczego Monero musi nadal aktualizować sieć?

Społeczność Monero zobowiązała się do iterowania i ulepszania projektu w czasie. Wydaje się, że zaangażowanie sprowadza się do dwóch kluczowych aspektów etosu społeczności: 

  1. Jakby na to nie patrzeć Projekt Monero jest ostatecznie oprogramowaniem - kodem - napisanym przez ludzi. Może to oznaczać potrzebę naprawy błędów, dodania ulepszeń i odkryć opracowywanych na bieżąco. Uwzględnia to również modernizacje protokołu lub po prostu utrzymanie projektu. Jest to podobne pod wieloma względami do każdego innego oprogramowania (takiego jak przeglądarka, w której to czytasz!). Je również należy stale aktualizować, aby dodawać nowe funkcje i naprawiać błędy. 

  2. Projekt Monero jest narzędziem do prywatności, a prywatność to ciągły wyścig zbrojeń. Ludzie i organizacje, które marzą o tym żeby pozbawić świat prywatności (zarówno finansowej, jak i osobistej), stale poprawiają swoją technologię oraz rozwijają i wymyślają nowe sposoby atakowania nowatorskich podejść do zachowania prywatności, takich jak te używane w Monero. Gdy wrogowie prywatności wymyślają te nowe podejścia, sieć Monero musi być w stanie się dostosować i naprawić, aby wywalczyć ochronę naszej prywatności finansowej. 

Jakby na to nie patrzeć Projekt Monero jest ostatecznie oprogramowaniem - kodem - napisanym przez ludzi. Może to oznaczać potrzebę naprawy błędów, dodania ulepszeń i odkryć opracowywanych na bieżąco. Uwzględnia to również modernizacje protokołu lub po prostu utrzymanie projektu. Jest to podobne pod wieloma względami do każdego innego oprogramowania (takiego jak przeglądarka, w której to czytasz!). Je również należy stale aktualizować, aby dodawać nowe funkcje i naprawiać błędy. 

Projekt Monero jest narzędziem do prywatności, a prywatność to ciągły wyścig zbrojeń. Ludzie i organizacje, które marzą o tym żeby pozbawić świat prywatności (zarówno finansowej, jak i osobistej), stale poprawiają swoją technologię oraz rozwijają i wymyślają nowe sposoby atakowania nowatorskich podejść do zachowania prywatności, takich jak te używane w Monero. Gdy wrogowie prywatności wymyślają te nowe podejścia, sieć Monero musi być w stanie się dostosować i naprawić, aby wywalczyć ochronę naszej prywatności finansowej. 

## Czym jest hard fork?

Aby zrozumieć jak skomplikowana jest modernizacja Monero, musisz zrozumieć jak bardzo różni się ona od aktualizacji czegoś takiego jak przeglądarki internetowej.

W kryptowalutach zasady sieci (rzeczy takie jak schemat transakcji, działanie kopania i weryfikacja każdego bloku) muszą zostać uzgodnione przez sieć. Nazywa się to „konsensusem”. Gdy którakolwiek z tych zasad musi zostać zmieniona lub zaktualizowana, sieć musi uzgodnić nowe zasady, wywołując „hard fork” - sytuację, w której sieć dzieli się na dwa blockchainy - jeden na starych zasadach i jeden na nowych. 

Kiedy wszyscy w społeczności zgadzają się na zmianę reguł, zjawisko to nazywa się „non-contentious hard-fork”, a blockchain, który wciąż ma stare zasady, umiera i nie jest wydobywany po hard forku. Tak było w przypadku prawie każdego hard forka Monero, a jedyną kontynuacją starych zasad były projekty próbujące czerpać korzyści z hard forka. 

Podczas gdy jednomyślne hard forki są jedynym sposobem na prawidłowe ulepszenie ważnych aspektów sieci Monero, mają one również frustrujące efekty uboczne - stare oprogramowanie, wydane przed zaplanowaniem hard forka, nie rozumie nowych zasad sieci, a zatem nie funkcjonuje po hard forku! Może to doprowadzić do tego, że użytkownicy będą myśleli, że stracili pieniądze i będą przekonani, że blockchain Monero się zatrzymał i nie będą w stanie przesłać pieniędzy, dopóki nie uaktualnią swojego portfela. 

## Kto decyduje, kiedy sieć Monero się ulepsza i na jaki sposób?

Ponieważ nie ma centralnego planowania, dyrektora generalnego, ani prezesa Monero, podejmowanie decyzji takich jak, kiedy uaktualnić sieć, co zmienić i jak to zrobić, spada na _nas samych_. Czyli na tych ludzi w społeczności Monero, którzy decydują się angażować i prowadzić interakcje i dyskusje! Jest to zarówno niezwykle ważna część zdecentralizowanego projektu, ponieważ planowanie i podejmowanie decyzji dotyczących projektu jest ostatecznie zdecentralizowane, ale jest to również wykorzystanie pomysłów społeczności.

Planowanie terminu i funkcji zawartych w każdej aktualizacji sieci w Monero odbywa się w dwóch głównych miejscach: 

  1. Na IRC i Matrixie, najczęściej używanych platformach czatowych w społeczności Monero (są one połączone razem). Platformy te pozwalają na duże czaty grupowe i tam właśnie odbywają się wszystkie zaplanowane spotkania społeczności Monero, spotkania deweloperskie i spotkania laboratorium badawczego. Te spotkania są najlepszym sposobem na posłuchanie (lub przedstawienie swoich poglądów!) o planach i dyskusjach na temat aktualizacji sieci w Monero. 

  2. Na GitHubie - głównej platformie komunikacyjnej na dłuższe dyskusje o Monero, planowanie i organizację. Społeczność Monero wykorzystuje GitHub do organizowania spotkań, omawiania nowych funkcji i pomysłów oraz koordynowania planowanych aktualizacji sieci, a do tego przechowywania kodu projektu Monero. 

Na IRC i Matrixie, najczęściej używanych platformach czatowych w społeczności Monero (są one połączone razem). Platformy te pozwalają na duże czaty grupowe i tam właśnie odbywają się wszystkie zaplanowane spotkania społeczności Monero, spotkania deweloperskie i spotkania laboratorium badawczego. Te spotkania są najlepszym sposobem na posłuchanie (lub przedstawienie swoich poglądów!) o planach i dyskusjach na temat aktualizacji sieci w Monero. 

Na GitHubie - głównej platformie komunikacyjnej na dłuższe dyskusje o Monero, planowanie i organizację. Społeczność Monero wykorzystuje GitHub do organizowania spotkań, omawiania nowych funkcji i pomysłów oraz koordynowania planowanych aktualizacji sieci, a do tego przechowywania kodu projektu Monero. 

Jeśli masz dobry pomysł na aktualizację sieci, nie podoba Ci się realizowane podejście lub masz obawy dotyczące terminu aktualizacji, ważne jest, aby o tym mówić i przedstawić swoją opinię społeczności! 

## Jak mogę pomóc w aktualizacjach sieci?

Jako że aktualizacje sieci Monero wymagają koordynacji i zatwierdzenia społeczności wraz z aktualizacjami oprogramowania, niezwykle ważne jest, aby jak najwięcej osób zaangażowało się w proces planowania, testowania i komunikacji aktualizacji sieci. 

Oto kilka łatwych sposobów, w jakich możesz pomóc podczas aktualizacji sieci: 

  1. Dołącz do spotkań na temat planowania [publikowanych na GitHubie](https://github.com/monero-project/meta/issues), posłuchaj i powiedz, jeśli masz coś czym chcesz się podzielić. 
  2. Przekaż szczegóły dotyczące aktualizacji sieci (po ich ustaleniu!) swojej ulubionej giełdzie, portfelowi lub minerom. Prawidłowe powiadomienie wszystkich użytkowników Monero o aktualizacji może być trudne, więc ważne jest, abyśmy wszyscy się do tego przyczynili. 
  3. Testuj oprogramowanie przed aktualizacją sieci. Przed aktualizacją sieci, zarówno na Testnecie, jak i na StageNecie odbędzie się testowanie, aby upewnić się, że każdy aspekt aktualizacji został odpowiednio zaplanowany i zaimplementowany w oprogramowaniu. Im więcej osób angażuje się i dokładnie przetestuje nowe wersje, tym bardziej prawdopodobne jest, że aktualizacja sieci przejdzie bez zarzutu! 
  4. Gdy opublikowane zostaną wersje kompatybilne z aktualizacją sieci, pamiętaj o natychmiastowej aktualizacji! Im więcej osób jest zaktualizowanych i gotowych do aktualizacji sieci, tym płynniej sieć sobie z nią poradzi. 

## Czego mogę się spodziewać w następnej aktualizacji sieci Monero?

Chociaż nie ma jeszcze ustalonej daty, wkrótce nastąpi aktualizacja sieci mająca na celu zaimplementowanie kilku kluczowych aktualizacji i funkcji w Monero: 

  1. Wzrost rozmiaru ringa z 11 do 16 zwiększający zbiór anonimowości (czytaj: lepsza prywatność) każdej transakcji w sieci 
  2. [View tagi, genialny sposób na redukcję czasu synchronizacji portfela o 30-40%](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Zmiany opłat, poprawa bezpieczeństwa i odporności sieci na szybkie zmiany na rynku opłat lub ataki ze strony złośliwych podmiotów 
  4. [Bulletproofs+, a further improvement in the efficiency of Monero transactions](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Te zmiany przyniosą daleko idące usprawnienia prywatności, wydajności i bezpieczeństwa sieci, jednocześnie torując drogę dla [Seraphisa](https://localmonero.co/knowledge/seraphis-for-monero) \- protokołu transakcji nowej generacji dla Monero.

## Jak mogę się dowiedzieć więcej?

Temat hard forków i aktualizacji sieci jest ogromny, a w Monero lista ich jest długa. Sprawdź poniższe linki, aby dowiedzieć się więcej o historii i planowanych aktualizacjach sieci! 

  * [Monero v15 hard-fork planning](https://github.com/monero-project/meta/issues/630)
  * [Scheduled software upgrades (in Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [A note on scheduled protocol upgrades](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Więcej do przeczytania