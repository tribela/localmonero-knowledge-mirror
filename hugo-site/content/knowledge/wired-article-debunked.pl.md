---
title: "Oto dlaczego magazyn Wired myli się co do Monero"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Zarówno w sferze prywatności, jak i kryptowalut, często panoszą się dezinformacje. Mamy [ artykuł, który przedstawia piętnaście powszechnych, nieprawdziwych i nieaktualnych założeń na temat Monero](/knowledge/monero-myths-debunked). Oprócz tego chcemy jeszcze poświęcić czas na odniesienie się do jednego konkretnego artykułu, który jest często cytowany i rozpowszechniany przez sceptyków Monero.

Ten numer magazynu Wired opublikował [artykuł](https://www.wired.com/story/monero-privacy/) 27 marca 2018 r. Był on odpowiedzią na świeżo wydany artykuł pt. „Analiza empiryczna możliwości śledzenia w blockchainie Monero” napisany przez różnych naukowców.

Mimo że artykuł był także stworzony przez osoby z wyraźnym konfliktem interesów (czytaj: są doradcami oraz mają swój udział w Zcashu), został on w miarę dobrze przyjęty przez społeczność Monero. Potwierdzał rzeczy, które społeczność już wiedziała i pisała we własnych artykułach Monero Research Lab ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) i [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)), z których najwcześniejszy z nich został opublikowany cztery lata wcześniej niż „Analiza empiryczna […]”. Pojawiło się kilka frustracji związanych z tym artykułem tj. konflikty interesów, fakt, że problemy były już znane, omówione, a w niektórych przypadkach nawet rozwiązane oraz błędny opis gwarancji prywatności Monero. Społeczność Monero skomentowała wstępny wydruk pracy, a wiele z ich zaleceń pojawiło się w ostatecznej wersji artykułu.

Które informacje były tak naprawdę błędne? Fakt, że Monero nie miało wad omawianych w gazecie od ponad roku. Transakcje sprzed 2017 roku były rzeczywiście podatne na pewną formę wycieku prywatności, ale w momencie publikacji Monero rozwiało większość z wad. Aby być szczerym wobec autorów, omawiają oni środki zaradcze Monero w jakimś stopniu, ale nie na tyle by wpłynęły na ogólny efekt jaki wywarły one na ówczesny cykl kryptowalut. Z tego powodu Wired wydało publikację odnoszącą się do tego artykułu.

Chociaż możemy zbadać omawiany artykuł Wired jako pracę z okresu wcześniejszego, na ile była ona prawdziwa i nieprawdziwa w owym czasie, to fakt, że jest on nadal udostępniany jako uzasadnienie, dlaczego gwarancje prywatności Monero są słabe, w rzeczywistości zachęca do analizy tego jak artykuł sprawdza się w obecnym czasie. Chętnie podejmiemy się tego zadania.

Szybkie przeczytanie artykułu oferuje nam kilka zaskakujących linijek, takich jak „[Odkrycia] nie powinny martwić nikogo, kto próbuje potajemnie wydać dziś Monero” oraz całą część, która postuluje, że badania są „nowe”, oparte w dużej mierze na publikacji. Sam artykuł naukowy zawiera zalecenia, takie jak ostrzeżenie dla użytkujących Monero przed potencjalnym kompromisem swojej anonimowości, pomimo faktu, że te dyskusje toczą się od 2014 roku i były nawoływane przez społeczność, że kupowanie Monero jest eksperymentalne.

Ale co z samokrytyką? Rzeczywistość jest taka, że wiele problemów związanych z Monero będącą prywatną walutą albo nie dotyczy już Monero albo obawy dotyczą wszystkich walut z kategorii prywatnych opartych na blockchainach. Omówmy te kwestie.

Jedną z najczęściej cytowanych krytyk wobec Monero jest to, że ze względu na trwałość i niezmienność blockchaina, jeśli przyszła technologia miałaby złamać prywatność, to wszystkie przeszłe transakcje Monero zostałyby odsłonięte. Innymi słowy, Twoja prywatność jest tykającym zegarem.

Podkreślamy raz jeszcze. Dosłownie każda prywatna waluta, która wykorzystuje metody on chain do zaciemniania i uzyskania prywatności, ma tę wadę, a mimo to jest to często używane przeciwko Monero (jak na ironię, wiele razy przez konkurencyjne prywatne waluty, które posiadają przecież ten sam problem) i jest również użyte w tym artykule. Odpowiedź na tę krytykę może być dla niektórych zaskakująca, ale Monero w rzeczywistości może być na to mniej podatne niż inne prywatne waluty ze względu na fakt, że ma wieloaspektowe podejście do prywatności.

Monero ukrywa wyjścia (nadawcę), wartości i odbiorców za pomocą trzech różnych technologii, odpowiednio ring signatures, RingCT i stealth addresses. Spośród nich ring signatures są najsłabsze i najbardziej wrażliwe zarówno na współczesną heurystykę, jak i teoretyczne, przyszłe technologie, które mogłyby złamać prywatność gwarantowaną przez Monero. To jest znane społeczności Monero już od lat, dlatego trwają badania, które mają ulepszyć lub zastąpić ring signatures całkowicie.

Jednak nawet jeśli ring signatures zostałyby całkowicie złamane, ujawnione byłyby tylko wyjścia. NIE nadawca (jako indywidualna osoba), ale wyjście. Powiązanie danych wyjściowych z tożsamością nie jest niemożliwe, ale wymagałoby większej ilości metadanych i zasobów. W połączeniu z faktem, że RingCT i stealth addresses NIE zostaną ujawnione, jeszcze bardziej zmniejsza to prawdopodobieństwo.

Należy zauważyć, że artykuł w magazynie Wired omawia powyższe informacje w części, w której zwrócili się do Riccardo „fluffypony” Spagni o komentarz, ale prawie nie poświęcili temu czasu i niemalże schowali pod dywan te istotne informacje. Brak zrozumienia jest tym bardziej widoczny podczas starań, aby przedyskutować te kluczowe informacje z ludźmi, którzy do dzisiaj chętnie dzielą się tym artykułem.

Kolejną krytyką, do której o wiele trudniej jest się odnieść, jest to, jak świat zewnętrzny postrzega Monero i jaki ma to wpływ na postrzeganie waluty przez jego społeczność. Idealnego przykładu na to nie trzeba szukać dalej niż w samym tytule artykułu: „Ulubiona waluta Dark Web jest mniej niewykrywalna, niż się wydaje”.

Każda osoba, która spędza znaczną ilość czasu w społeczności Monero, może zaświadczyć, że społeczność Monero dokłada wszelkich starań, aby pokazać, jak trudno jest osiągnąć prawdziwą prywatność, nawet ze szkodą dla działań marketingowych lub adopcyjnych. Jeśli społeczność zapewni obszerne zasoby dokładnie omawiające walutę i jej wady, to ignorancja stanie się winą użytkownika, który uważa, że waluta jest wszystkim, czego potrzebuje, aby mieć 100% prywatności.

W tym momencie powinno być oczywiste, że społeczność Monero poważnie traktuje zarówno swoją prywatność, jak i uczciwość w odniesieniu do jej słabości i późniejszych ulepszeń. Artykuły, takie o których mowa była powyżej, całkowicie przeoczają ducha innowacji Monero. To przyrównuje Monero do innych grup kryptowalut, które tworzą okazałe zapewnienia, myśląc tylko o zyskach i żerując na niewykształconych inwestorach-wannabes.

Rzeczywistość nie mogłaby się bardziej różnić. Monero zdaje sobie sprawę ze swoich słabości. Stale próbuje się ich pozbyć oraz osiągnąć realne, ale bardzo trudne cele jakimi są zapewnienie światu prywatności oraz zamiennej kryptowaluty, która mogłaby być używana przez wszystkich w sposób uczciwy, zdecentralizowany oraz przede wszystkim byłaby napędzana przez swoją społeczność. Może to czas żeby przestać skupiać się na sensacjach i udostępniać artykuły jako promowanie konkurencji oraz fanatyków.

Więcej do przeczytania