---
title: "P2Pool과 Monero Mining의 탈중앙화에서의 역할"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero 프로젝트의 핵심 목표 중 하나는 오늘날 암호 화폐 네트워크를 보호하는 주요 방법인 작업 증명(PoW) 마이닝에 대한 새롭고 혁신적인 접근 방식을 통해 공정하고 분산된 안전한 네트워크를 구현하는 것입니다.

RandomX 와 같은 고유한 마이닝 알고리즘 [은 컴퓨터가 있는 모든 사람이 네트워크 보안에 상당한 금액을 기여할 수 있도록 하므로 이 목표에 매우 중요하지만 RandomX는 문제를 해결하지 못합니다. 풀 마이닝으로 인해 발생할 수 있습니다. 풀 마이닝은 지금까지 Monero를 포함하여 오늘날 암호 화폐를 마이닝하는 가장 일반적인 방법이지만 고맙게도 p2pool 마이닝의 출현으로 빠르게 변화하고 있습니다.](/knowledge/monero-mining-randomx)

## 풀 마이닝이란 무엇입니까?

풀 마이닝은 채굴자가 네트워크의 블록을 해결한 다음 풀이 찾은 모든 블록에 대해 보상을 균등하게 공유하려고 시도하는 작업을 공유하는 방법입니다. 이것은 광부가 마이닝 Monero 에 혼자 지불하는 주파수를 고르게하는 데 대단히 도움이되지만 심각한 중앙 집중 화 문제가없는 것은 아닙니다.

각 광부가 풀에 기여함에 따라, 그들은 그들이하는 모든 일을 통제하고 수영장 자체에 발견 블록, 수영장이 정직하고 공정하게 각 수행 한 작업의 양에 따라 모든 광부 들 사이의 보상을 공유 할 것이라고 신뢰. 모든 것이 잘 되면 풀 운영자는 모든 광부의 작업을 수집하고 네트워크에 제출하고 보상을 동등하게 공유합니다.

## 풀 마이닝의 문제점은 무엇입니까?

불행히도, 이것은 전적으로 신뢰에 의존하고 풀 운영자가 광부에 의해 수행되는 작업으로 사악한 일을 할 수 있게합니다. 풀 운영자는 네트워크를 공격하거나, 자금을 두 번 지출하려고 시도하거나(풀이 충분히 큰 경우) 수행중인 작업을 사용하거나 광부가 스스로 지불하고 광부에게 제대로 보상하지 않는 작업을 사용할 수 있습니다.

네트워크의 가장 큰 위험은 네트워크의 51% 이상을 보유한 풀(또는 여러 풀)이 이를 사용하여 자금을 두 번(이중 지출 공격)하거나 네트워크 규칙을 변경하려고 시도할 수 있다는 것입니다.

## 피투풀이란?

p2pool은 원래 다시 비트 코인을 채굴하기 위해 만들어진 개념입니다 2011, 하지만 광범위한 채택을 본 적이 비트 코인에 실질적으로 사용되지 않는 남아있다. 고맙게도, RandomX 뒤에 주요 개발자 중 하나, SChernykh, p2풀의 비트 코인 구현과 문제 중 일부에 대한 해결책을 마련하고 처음부터 모든 소프트웨어를 다시 작성 하는 그의 휴가를 보냈다.

p2pool을 사용하면 채굴자가 함께 협력하여 작업을 공유하기 위해 p2pool용 특수 노드 소프트웨어를 사용하여 블록을 해결하고 Monero 네트워크를 보호할 수 있습니다.

이것은 각 광부가 수행하는 작업, 지갑 주소 및 Monero가 얻은 금액을 보관하고 신뢰가 없고 분산된 방식으로 보상을 지불하는 새로운 블록 체인 ("사이드 체인")을 사용하여 수행됩니다. 이 사이드 체인은 훨씬 적은 광부를 가지고, 그것은 찾기 및 주요 모네로 네트워크보다 그것에 블록을 제출하는 것이 훨씬 쉽습니다, 광부가 혼자 마이닝 에 비해 일관된 지불금을 얻을 수 있도록.

## p2pool은 풀 마이닝 문제를 어떻게 해결합니까?

p2pool에는 중앙 집중식 수영장, 중앙 집중식 수영장 운영자 또는 자금을 보유하고 지불금을 배포하는 한 사람이 없습니다. p2pool을 통해 채굴하는 모든 작업은 p2pool 블록 체인 및 기타 노드 운영자가 합법적임을 확인하기 위해 검사되며 모든 광부는 블록이 발견 된 블록의 보상에서 직접 발견 될 때 즉시 수행 한 작업에 따라 지불됩니다.

광부가 중앙 집중식 풀 대신 p2pool을 사용하기로 선택할 때 풀 운영자의 모든 전력과 신뢰를 제거하고 자신의 작업이 네트워크의 양호와 자신의 보상에 기여하도록 보장하고 네트워크 공격의 위험을 감소, 작업의 오용, 또는 그들이 빚진 보상의 도난.

이것이 그들이 자신의 이익을 보호하는 데 도움이 될뿐만 아니라 중앙 집중식 풀이 전체적으로 Monero 네트워크에 제기 할 수있는 위험을 줄입니다. p2pool 사용은 또한 국가 또는 규제 기관이 네트워크의 건강에 제기 할 수있는 위험을 줄이는 데 대단히 도움이, 압력에 중앙 집중화 풀 사업자가 없기 때문에, 에 의지 풀의 지리적 농도, 또는 그들이 Monero에 대해 사용하는 다른 쉬운 압력 지점.

## 단점은 무엇입니까?

고맙게도 Monero의 p2pool은 잘 설계되고 잘 구축되었으며 매우 잘 작동합니다. 그러나 p2pool 마이닝의 주요 단점은 p2pool을 사용하려는 각 마이너가 자신의 Monero 노드를 실행해야 하므로 시작 프로세스가 조금 더 복잡해진다는 것입니다. 그러나 이 노드는 블록을 만들고 확인하는 데 필요한 모든 정보를 계산하는 데 사용되며 광부가 수행 중인 작업을 완전히 제어할 수 있도록 합니다. 노드는 또한 광부 자신의 지갑에 대한 원격 노드로 기능하고 네트워크에 기여하는 등의 작업을 수행할 수 있습니다.

중앙 집중식 채굴과의 또 다른 주요 차이점은 p2pool을 사용하는 소규모 채굴자는 대규모 중앙 집중식 풀보다 "분산"또는 지불 간격 시간이 더 많다는 것입니다. 그러나' _이것은 시간이 지남에 따라 Monero 수입이 줄어들지 않는다는 점에 매우_ 중요합니다! p2pool은 시간이 지남에 따라 중앙 집중식 풀만큼 소규모 광부에게도 수익성이 있을 것입니다. 이 편차 중 일부는 서비스 비용을 지불할 중앙 집중식 풀 운영자가 없기 때문에 기본적으로 0% 수수료를 갖는 p2pool에 의해 상쇄됩니다!

## 시작하려면 어떻게 해야 하나요?

고맙게도 Monero'의 p2pool 구현의 탁월한 디자인과 p2pool을 통한 마이닝 프로세스를 단순화하는 데 시간을 투자한 커뮤니티의 많은 사람들 덕분에 시간이 지남에 따라 시작하는 것이 더 간단해지고 있습니다. p2pool을 사용하여 마이닝을 시작하는 방법에는 여러 가지가 있지만 기술적인 세부 사항은 이 문서의 범위를 벗어나므로 운영 체제에 따라 아래 링크로 자유롭게 이동하십시오.

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## 자세히 알아보려면 어떻게 해야 하나요?

이 p2풀 광산 주위에 호기심을 자극 한 경우, p2풀에 몇 가지 추가 링크와 설명에 대한 아래를 살펴, 그것이 어떻게 작동하는지, 그리고 모네로에 대한 의미:

  * [p2풀에 대한 공식 Github](https://github.com/SChernykh/p2pool)
  * [p2풀](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [을 사용하는 공식 문서는 이제 p2pool.observer에](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [살고있다, "블록 익스플로러는 p2풀](https://p2pool.observer/)
  * [모네로 p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [세르게이 체르니크에 대한 종류의" : P2Pool의 개발에 분산 된 XMR 광산 풀](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies/)

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin/)

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys/)

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero/)

  * [원격 노드가 Monero의 개인 정보에 미치는 영향](/knowledge/remote-nodes-privacy/)

  * [Monero가 하드 포크를 사용하여 네트워크를 업그레이드하는 방법](/knowledge/network-upgrades/)

  * [태그 보기: 1바이트가 Monero 지갑 동기화 시간을 40% 이상 줄이는 방법](/knowledge/view-tags-reduce-monero-sync-time/)

  * [세라피스: 모네로를 위해 할 일](/knowledge/seraphis-for-monero/)

  * [몬에로를 직접 구매하는 것과 마찬가지로 비트코인을 모네로로 변환하는 것이 사적인 것입니까?](/knowledge/most-private-way-to-buy-monero/)

  * [Monero가 Zcash와 달리 신뢰할 수없는 설정을 사용하는 이유](/knowledge/monero-trustless-setup/)

  * [Monero가 Bitcoin보다 더 나은 가치 저장소 인 이유](/knowledge/monero-better-store-of-value/)

  * [Monero가 Bitcoin의 네트워크 효과를 극복하는 방법](/knowledge/network-effect/)

  * [Monero가 가장 비판적인 사고 커뮤니티를 보유한 이유](/knowledge/critical-thinking/)

  * [Monero를 사용할 때주의해야 할 사기](/knowledge/monero-scams/)

  * [Monero에서 원자 스왑이 작동하는 방법](/knowledge/monero-atomic-swaps/)

  * [모든 Monero 사용자가 네트워킹에 대해 알아야 할 사항](/knowledge/monero-networking/)

  * [RingCT가 모네로 거래량을 숨기는 방법](/knowledge/monero-ringct/)

  * [모네로 비밀주소가 신상을 보호하는 방법](/knowledge/monero-stealth-addresses/)

  * [모네로 2차주소가 실제 신상과 연결되는 걸 방지하는 방법](/knowledge/monero-subaddresses/)

  * [모네로 출력에 대하여](/knowledge/monero-outputs/)

  * [초보자를 위한 모네로 사용 습관 추천](/knowledge/monero-best-practices/)

  * [링서명이 모네로 출력을 숨기는 방법](/knowledge/ring-signatures/)

  * [모네로는 어떻게 비트코인의 고질적인 문제인 규모의 문제를 해결했을까](/knowledge/dynamic-block-size/)

  * [CLSAG는 어떻게 모네로의 효율을 높였을까](/knowledge/what-is-clsag/)

  * [모네로가 꼬리자르기를 도입한 이유](/knowledge/monero-tail-emission/)

  * [모네로의 간단한 역사](/knowledge/monero-history/)

  * [Wired지는 모네로에 대해 틀렸으며, 왜 그런지 알려드리겠습니다](/knowledge/wired-article-debunked/)

  * [모네로에 관한 15가지 미신과 우려, 그리고 그 해답](/knowledge/monero-myths-debunked/)

  * [Dandelion++가 모네로 거래의 출처를 보호하는 방법](/knowledge/monero-dandelion/)

  * [모네로는 왜 탈중앙화와 오픈소스를 선택했는가](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [모네로 채굴: RandomX가 특출난 이유](/knowledge/monero-mining-randomx/)

  * [모네로가 Dash, Zcash, (Lelantus를 적용해도) Zcoin, Grin 그리고 Wasabi같은 비트코인 세탁 서비스보다 뛰어난 이유 (2020년 5월 업데이트)](/knowledge/why-monero-is-better/)