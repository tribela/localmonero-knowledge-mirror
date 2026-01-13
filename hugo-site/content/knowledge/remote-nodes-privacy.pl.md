---
title: "Jak zdalne węzły wpływają na prywatność Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Jedną z największych zalet Monero w porównaniu do innych kryptowalut jest prywatność on-chain, ale czy zastanawiałeś się kiedyś, jak utrzymuje się prywatność Monero, gdy używasz cudzego węzła? Co jeśli używasz „lekkiego portfela”, takiego jak MyMonero? 

W tym poście zagłębimy się w niektóre szczegóły, dzięki którym Monero zapewnia wyjątkową prywatność on-chain, nawet podczas korzystania z cudzego węzła, a także powiemy, na co należy uważać podczas korzystania z cudzych węzłów. 

## Jaką funkcję pełnią node'y w Monero?

## Jaką funkcję pełnią node'y w Monero?

Dla osób mniej zaznajomionych z tym, jak działa Monero, węzły (lub serwery) w sieci Monero mogą być uruchamiane przez każdego (lub innych, z którymi zdecydują się go udostępnić!) i pozwalać właścicielowi węzła na zsynchronizowanie kopii blockchaina i przesłanie tej kopii innym w sieci. Węzły te weryfikują również wszystkie transakcje odbywające się w sieci, a także wszystkie publikowane bloki i zapewniają, że wszystkie są zgodne z regułami ustalonymi przez konsensus. 

Inną funkcją, którą obsługują węzły w Monero, jest sposób na dostarczenie wszystkich danych, które potrzebuje Twój ulubiony portfel Monero, aby właściwie sprawdzić transakcje należące do Ciebie i dokonać nowych transakcji. Dane te są dostarczane przez węzły na dwa sposoby: 

  * Dane z każdego bloku na blockchainie są pobierane przez portfel, skanowane pod kątem transakcji należących do Ciebie, a następnie odrzucone po sprawdzeniu. 
    * Ten krok zostanie wkrótce drastycznie ulepszony dzięki [view tagom](/knowledge/view-tags-reduce-monero-sync-time).
  * Podczas wysyłania transakcji używany węzeł zawiera listę możliwych wabików (lub fałszywych danych wejściowych) do użycia podczas budowania transakcji, dzięki czemu możesz upewnić się czy masz dobre wabiki do ukrycia Twojej transakcji. 
    * Te wabiki są częścią [ring signatures](/knowledge/ring-signatures), ważnego elementu podejścia Monero do prywatności on-chain.

  * Ten krok zostanie wkrótce drastycznie ulepszony dzięki [view tagom](/knowledge/view-tags-reduce-monero-sync-time).

  * Te wabiki są częścią [ring signatures](/knowledge/ring-signatures), ważnego elementu podejścia Monero do prywatności on-chain.

## Jaki jest najbardziej prywatny i najbezpieczniejszy sposób korzystania z Monero?

## Jaki jest najbardziej prywatny i najbezpieczniejszy sposób korzystania z Monero?

Najlepszą rzeczą do zrobienia, nawet przy silnej prywatności on-chain dostarczanej przez Monero podczas korzystania z cudzych węzłów, jest uruchomienie własnego węzła Monero, aby upewnić się, czy masz nieskazitelną kopię blockchaina Monero i czy Twój adres IP jest dobrze chroniony. Drugą korzyścią podczas uruchamiania własnego węzła jest to, że wtedy wspierasz sieć, pozwalając innym węzłom zsynchronizować się z Twoim węzłem lub nawet pozwalając innym użytkownikom na połączenie się z Twoim węzłem ze swojego portfela. 

To powiedziawszy, Monero nadal zapewnia doskonałą prywatność podczas korzystania z cudzego węzła. Jeśli chcesz uruchomić własny węzeł Monero, oto łatwy do prześledzenia przewodnik: 

  * [Uruchom Węzeł Monero](https://sethforprivacy.com/guides/run-a-monero-node/)

## Czego może się o mnie dowiedzieć cudzy node?

## Czego może się o mnie dowiedzieć cudzy node?

Podczas korzystania ze zdalnego węzła istnieje kilka kluczowych informacji, które są narażone na wyciek do węzła i kilka kluczowych sposobów, w jakich węzeł może Cię zaatakować, uniemożliwić transakcję i więcej. 

Pierwszą rzeczą, o jakiej zdalny węzeł może się dowiedzieć, jest Twój publiczny adres IP. Chociaż mając nadzieję, że zostanie to ukryte za pośrednictwem VPN lub Tora, zdalny węzeł może powiązać Twój publiczny adres IP z transakcją, pomagając zawęzić to, gdzie transaktujesz. Zdalny węzeł może znać również ostatni blok zsynchronizowany z Twoim portfelem i użyć go, aby spróbować wydedukować informacje o Tobie, na przykład kiedy zazwyczaj używasz Monero i kiedy ostatnio wydałeś Monero. Jest to szczególnie problematyczne, jeśli zawsze łączysz się z tego samego adresu IP (takiego jak Twój dom). Ostatnią kluczową rzeczą, o której zdalny węzeł może się dowiedzieć, są podstawowe informacje o przesyłanych przez Ciebie transakcjach. Chociaż mogą to być najbardziej oczywiste dane, które operator zdalnego węzła dostaje o Tobie, to ważne jest, aby zrozumieć, że można wykorzystać je do wyśledzenia nadawcy transakcji podczas łączenia tych informacji z innymi danymi off-chain. Może to być szczególnie niebezpieczne, jeśli zdalny węzeł jest prowadzony przez złośliwy podmiot, firmę analizującą blockchain lub narządy opresyjnego państwa. 

Zdalny węzeł może również próbować wywołać kłopoty ukrywając bloki przed Tobą, dzięki czemu Twój portfel będzie sądził, że został zsynchronizowany, podczas gdy będzie wiele bloków do tyłu. Może to sprawić, że pomyślisz, iż fundusze są utracone lub uniemożliwi Ci to wydawanie funduszy, dopóki nie połączysz się z innym węzłem. Ostatnią kluczową rzeczą, jaką może zrobić zdalny węzeł, jest zasilanie portfela zmanipulowaną listą wabików. Może to spowodować, że Twój portfel, albo całkowicie nie będzie mógł budować transakcji (sprawiając, że nie możesz wydać funduszy), lub nie będzie mógł pozwolić zdalnemu węzłowi na próbę dostarczenia wabików, o których wie, że są wydane w celu pogorszenia anonimowości, jaką masz w każdej transakcji.

## Jakie gwarancje prywatności nadal istnieją podczas korzystania ze zdalnego węzła?

## Jakie gwarancje prywatności nadal istnieją podczas korzystania ze zdalnego węzła?

Chociaż ten artykuł mógł Cię trochę przestraszyć, ważne jest, aby zdać sobie sprawę z tego, że prywatność dostarczana przez Monero jest wspaniała, nawet gdy używasz zdalnego węzła i znacznie przewyższa wszelkie inne kryptowaluty. Nadal zyskujesz silną prywatność on-chain dostarczoną przez Monero, ponieważ zdalny węzeł nigdy nie zna prawdziwego wejścia (jakie monety wydajesz), ilości Monero wydanego w transakcji lub adresu odbiorcy transakcji. Zewnętrzni obserwatorzy również nie widzą prawdziwego wejścia, kwoty lub adresów (bez względu na rodzaj węzła, który wybierzesz!), zapewniając, że za wyjątkiem korzystania ze zdalnego węzła, nawet adres IP, informacje o synchronizacji portfela i transakcje mają silne gwarancje prywatności .

Zdalny węzeł nigdy również nie ma dostępu do poprzednich transakcji, które wysłałeś lub otrzymałeś czy też do aktualnej ilości Monero w portfelu i traci wszelką wiedzę o transakcjach, gdy zaczynasz korzystać z innego węzła. Żadne prywatne klucze (spend lub view) nigdy nie są dostarczane do zdalnego węzła, więc Twój portfel zachowuje prywatność, bezpieczeństwo i użyteczność. Bez względu na zdalny węzeł, nigdy nie jesteś narażony na utratę Monero lub jego kradzież, ponieważ węzeł nie może edytować adresu odbiorcy, nigdy nie ma dostępu do Twoich prywatnych kluczy i nie może w żaden sposób skonfiskować Monero.

## Co na temat „lekkich portfeli” takich jak MyMonero?

## Co na temat „lekkich portfeli” takich jak MyMonero?

Chociaż temat jest nieco poza zakresem tego artykułu, chciałem zająć się specjalnym typem portfela w Monero - portfelem lekkim. Nazwa lekki portfel wynika z faktu, że portfel (na telefonie lub komputerze) nie musi wykonywać żadnej synchronizacji blockchaina, dzięki czemu jest szybszy i płynniejszy. 

Jednak takie portfele są, jak na razie, poważnym kompromisem dla prywatności - Twój portfel wysyła prywatny klucz view do zdalnego serwera, którego używasz (jak domyślnie w MyMonero), co daje pełną widoczność serwerowi zdalnego węzła na dowolne odebrane fundusze od utworzenia portfela (i dopóki nie przestaniesz z niego używać lub z tego seeda). Drastycznie zmniejsza to prywatność wobec operatora węzła i należy zwrócić na to uwagę. 

Na szczęście społeczność Monero pracuje nad ulepszeniem oprogramowania, którego możesz użyć do hostowania własnego serwera light wallet server (LWS), co pozwoli Ci na szybką synchronizację bez ufania trzeciej stronie z prywatnymi kluczami view - jako, że to Ty uruchomisz oprogramowanie, do którego Twój portfel wyśle prywatne klucze view! 

Aby uzyskać więcej informacji na temat light wallet servera, zobacz poniższe repozytorium GitHuba:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Jak mogę się dowiedzieć więcej?

## Jak mogę się dowiedzieć więcej?

Jeśli jesteś ciekaw i chcesz lepiej zrozumieć węzły w Monero oraz przyjrzeć się użyciu zdalnego węzła, bądź uruchomić własny,wejdź w poniższe linki, aby dowiedzieć się więcej:

  * [Monero World, lista węzłów prowadzonych przez członków społeczności](https://moneroworld.com/#nodes)
  * [Węzły Monero prowadzone przez Seth For Privacy, autora tego artykułu](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, lista węzłów z częstym sprawdzaniem ich łączności](https://monero.fail/)
  * [Jak połączyć się ze zdalnym węzłem w portfelu GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Remote Node](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Więcej do przeczytania

  * [Jak Monero jednoznacznie umożliwia circular economies](/knowledge/monero-circular-economies)/

  * [Ring signatures w Monero vs CoinJoin jak w Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Dlaczego (i jak!) powinieneś trzymać własne klucze ](/knowledge/hold-your-keys)/

  * [Wspieranie Monero](/knowledge/contributing-to-monero)/

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

  * [Kopanie Monero: Co sprawia, że RandomX jest wyjątkowy](/knowledge/monero-mining-randomx)/

  * [Dlaczego Monero jest lepsze niż Dash, Zcash, Zcoin (nawet z Lelantus), Grin oraz od mikserów Bitcoina takich jak Wasabi (Zaktualizowano w maju 2020 r.)](/knowledge/why-monero-is-better)/

Więcej do przeczytania