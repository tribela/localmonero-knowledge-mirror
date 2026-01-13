---
title: "와사비처럼 모네로의 링 시그니처 vs 코인조인"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Bitcoin의 개인정보 보호 도구가 더 많은 관심과 사용을 얻으면서 더 많은 규제 조사를 받게 되었습니다. 이 조사로 인해 Bitcoin 개인 정보 보호 도구인 Wasabi Wallet이 [최근 발표](https://twitter.com/wasabiwallet/status/1503091503207432193) 하여 불법으로 간주되거나 ToS에 위배되는 것으로 간주되는 믹스에 대한 수신 입력을 검열 및 거부하고 체인 분석 비용을 지불할 것이라고 발표했습니다. 회사에서 들어오는 믹스 참가자를 "검토"합니다.

Bitcoin의 자금 출처를 난독화하기 위해 CoinJoin 거래를 사용하는 것은 수년 동안 Bitcoin 개인 정보 보호의 핵심이었으며 사용에 내재된 문제와 위험은 Monero의 링 서명이 갖는 핵심 문제 중 일부입니다. 수정하고 예방합니다.

이 블로그 게시물에서 우리는 CoinJoin과 링 서명을 비교하고 Monero에서 취한 접근 방식이 검열 저항을 강화하고 개인 정보를 보호하며 사용자의 번거로움을 줄이는 이유에 대해 간략하게 알아볼 것입니다.

## CoinJoin 거래란 무엇입니까?

## CoinJoin 거래란 무엇입니까?

Bitcoin에서는 모든 거래가 완전히 투명하여 발신인, 수취인, 금액이 공개되므로 사용자는 이전 발신인과 향후 자금 수취인으로부터 개인 정보를 보호하기 위해 추가 조치를 취해야 하며 물리적 폭력.

오늘날 Bitcoin의 개인 정보 보호를 위한 최상의 솔루션은 ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/)이라는 도구로, 2명 이상의 사용자가 함께 작업하여(보통 중앙 조정자를 통해) 특별한 거래를 생성합니다. 외부 관찰자가 입력과 출력을 연결하기 어렵습니다. 각 참가자는 자금 관리를 포기하지 않고 거래를 공동으로 구축하기 위해 통신하고 외부 관찰자에게 이전 기록이 현재 명확하지 않은(또는 난독화된) 마지막 출력을 받습니다.

이는 특정 UTXO의 기록을 깨고 비트코인 사용자가 거래할 때 약간의 순방향 비밀성을 얻을 수 있도록 합니다. 그러나 CoinJoin(비트코인용으로 가장 많이 사용되는 두 가지 CoinJoin 도구인 Wasabi Wallet 및 Samourai Wallet에서 구현됨)에는 몇 가지 주요 단점이 있습니다.

  * CoinJoin 거래는 완전히 선택적이고 적극적인 참여가 필요하기 때문에 , 모든 참가자는 "정상적인" 비트코인 사용자보다 더 큰 프라이버시를 추구한다는 것을 필연적으로 보여주므로 잠재적으로 이들을 선별하여 많은 규제 대상 거래소 또는 단체에서 자금을 지출하는 데 문제를 일으킬 수 있습니다. 각 사용자는 CoinJoin 거래에 참여했음을 부인할 수 없습니다.
  * CoinJoin에 대한 다른 사람을 찾기 위해 CoinJoin(와사비 지갑 포함)에 대한 대부분의 접근 방식은 참가자를 연결하고 적절한 CoinJoin 거래를 구축하고 의사 소통하는 데 도움이 되는 중앙 조정자를 사용합니다. 이 중앙 조정자는 사용자 자금을 관리하지 않지만 조정하는 거래에 대한 광범위한 통찰력을 얻고 들어오는 입력을 검열할 수 있으며(와사비 지갑의 경우와 같이) CoinJoin 참가자에 대한 정보를 수집하거나 공유하도록 압력을 받을 수 있습니다.
  * CoinJoin에 대한 많은 자금이 있는 사용자는 CoinJoin에 참여할 충분한 참가자를 찾기 위해 몇 시간(또는 심지어 며칠!)을 기다려야 할 수 있으므로 사용자가 자금을 수령한 시점부터 지출할 수 있는 시점까지 큰 지연이 발생합니다. 그들을 개인적으로.
  * CoinJoin 거래에 의해 제공되는 개인 정보는 다른 참가자가 KYC 교환, ID가 필요한 판매자 등을 통해 자금을 사용하거나 출력을 자신의 ID에 연결함에 따라 시간이 지남에 따라 저하됩니다. 이는 사용자가 이상적으로 CoinJoin에서 자금을 지속적으로 휘젓는 것을 의미합니다. 익명성 세트(“숨기려는 군중”)를 가능한 한 최신 상태로 유지하기 위한 거래.
  * 대부분의 CoinJoin 접근 방식에서 참가자는 CoinJoin 트랜잭션의 입력과 출력을 연결하기 어렵게 만들기 위해 고정 크기 UTXO(즉, 0.1 BTC)를 사용해야 합니다. 이는 더 높은 수수료(큰 입력당 더 많은 별도의 거래가 필요함), 더 많은 "유해한 변경"(프라이버시에 대한 심각한 위험 없이 사용할 수 없는 자금)으로 이어지며, 더 작은 사용자가 자산을 가지고 있지 않은 경우 전혀 혼합할 수 없도록 할 수 있습니다. 필요한 최소 잔액.

## 링 서명은 이러한 문제를 어떻게 해결합니까?

## 링 서명은 이러한 문제를 어떻게 해결합니까?

[과거에 링 서명이 무엇인지 자세히 살펴보았으므로](/knowledge/ring-signatures)이 블로그 게시물에서는 작동 방식의 기술적 측면에 대해 자세히 설명하지 않겠습니다. 대신 Monero에서 취한 접근 방식이 위에서 논의한 CoinJoin의 문제를 어떻게 해결하는지 살펴보겠습니다.

> CoinJoin은 옵트인이며 참여가 필요합니다.

CoinJoin은 옵트인이며 참여가 필요합니다.

Monero의 링 서명은 개인정보 보호 프로토콜의 핵심 기능이며 _네트워크의 모든_ 거래 그들을 사용합니다. 이는 "일반" Monero 사용자보다 더 큰 프라이버시를 추구하는 사용자의 거래가 없으며 모든 사용자가 주어진 거래에서 자금을 지출했다는 사실을 부인할 수 있음을 의미합니다. 사용자 지출 자금은 거래의 미끼 입력을 조정하거나 참여하지 않기 때문에 미끼로 선택된 입력을 소유한 사용자는 정직하게 해당 거래에 참여하지 않았다고 말할 수 있어 개인 정보를 강화할 수 있습니다.

> 중앙 조정자 사용

중앙 조정자 사용

Monero의 링 서명은 완전히 조정되지 않고 거래를 생성하는 데 자금의 실제 지출자만 필요하므로 Monero의 중앙 조정자. 이렇게 하면 _아무도_ Monero의 개인 정보에 대한 액세스를 거부할 수 없으며 압력을 받을 수 있는 중앙 집중식 기관이 없고 유동성에 대한 쉬운 Sybil 공격 등이 없습니다. 거래가 적절한 수수료를 지불하는 한, Monero에서 개인 정보 보호, 보안 및 익명성에 대한 검열 불가능한 액세스 권한을 얻습니다.

> CoinJoin은 유동성이 필요합니다.

CoinJoin은 유동성이 필요합니다.

모네로를 미끼로 사용하는 모든 사람이 사용할 수 있는 "유동성"은 항상 온체인 출력의 총 집합이므로 결코 부족하지 않습니다. Monero와 함께 숨어있는 미끼의. Monero를 사용하려는 사람은 자금을 받은 후 ~20분 후에 그렇게 할 수 있으며 Monero에서 강력한 개인 정보를 얻기 위해 추가 단계를 수행할 필요가 없습니다.

> CoinJoin 개인 정보는 시간이 지남에 따라 저하됩니다.

CoinJoin 개인 정보는 시간이 지남에 따라 저하됩니다.

Monero의 출력은 네트워크에서 알려진 대로 사용되지 않으므로 링 서명이 제공하는 개인 정보는 시간이 지남에 따라 열화될 가능성이 훨씬 적습니다. 사용자는 Monero에서 지속적으로 출력을 변경할 필요가 없으며 극히 드문 경우를 제외하고는 시간이 지남에 따라 개인 정보를 잃지 않습니다.

그러나 사용자가 출력과 함께 사용된 미끼를 "새로 고침"하려는 경우 자금을 자신에게 다시 보내고 평소처럼 ~20분 후에 사용할 수 있습니다.

> CoinJoin은 일반적으로 고정 크기 입력이 필요합니다.

CoinJoin은 일반적으로 고정 크기 입력이 필요합니다.

["기밀 거래"](/knowledge/monero-ringct) ("RingCT"의 일부)를 사용하는 모든 거래에 금액이 숨겨져 있기 때문에 ), 주어진 거래에 사용되는 미끼는 어떤 크기도 될 수 있습니다. Monero의 금액 기반 휴리스틱에 대해 걱정할 필요가 없으므로 거래가 훨씬 간단하게 구축되고 Monero 블록체인의 모든 시점과 금액에서 미끼를 활용할 수 있습니다.

## 자세히 알아보려면 어떻게 해야 하나요?

## 자세히 알아보려면 어떻게 해야 하나요?

당신이 호기심과 더 나은 링 서명 또는 CoinJoin 거래를 이해하려는 경우, 시작하는 좋은 장소에 대한 아래링크를 참조하십시오 :

  * [링 시그니처 모호한 모네로의 출력](/knowledge/ring-signatures)
  * [링 서명 - 모네로프디아](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Q + A](https://bitcoiner.guide/qna/coinjoin/)
  * [코인 조인 개요](https://6102bitcoin.com/coinjoin-overview/)

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies)/

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys)/

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero)/

  * [원격 노드가 Monero의 개인 정보에 미치는 영향](/knowledge/remote-nodes-privacy)/

  * [Monero가 하드 포크를 사용하여 네트워크를 업그레이드하는 방법](/knowledge/network-upgrades)/

  * [태그 보기: 1바이트가 Monero 지갑 동기화 시간을 40% 이상 줄이는 방법](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool과 Monero Mining의 탈중앙화에서의 역할](/knowledge/p2pool-decentralizing-monero-mining)/

  * [세라피스: 모네로를 위해 할 일](/knowledge/seraphis-for-monero)/

  * [몬에로를 직접 구매하는 것과 마찬가지로 비트코인을 모네로로 변환하는 것이 사적인 것입니까?](/knowledge/most-private-way-to-buy-monero)/

  * [Monero가 Zcash와 달리 신뢰할 수없는 설정을 사용하는 이유](/knowledge/monero-trustless-setup)/

  * [Monero가 Bitcoin보다 더 나은 가치 저장소 인 이유](/knowledge/monero-better-store-of-value)/

  * [Monero가 Bitcoin의 네트워크 효과를 극복하는 방법](/knowledge/network-effect)/

  * [Monero가 가장 비판적인 사고 커뮤니티를 보유한 이유](/knowledge/critical-thinking)/

  * [Monero를 사용할 때주의해야 할 사기](/knowledge/monero-scams)/

  * [Monero에서 원자 스왑이 작동하는 방법](/knowledge/monero-atomic-swaps)/

  * [모든 Monero 사용자가 네트워킹에 대해 알아야 할 사항](/knowledge/monero-networking)/

  * [RingCT가 모네로 거래량을 숨기는 방법](/knowledge/monero-ringct)/

  * [모네로 비밀주소가 신상을 보호하는 방법](/knowledge/monero-stealth-addresses)/

  * [모네로 2차주소가 실제 신상과 연결되는 걸 방지하는 방법](/knowledge/monero-subaddresses)/

  * [모네로 출력에 대하여](/knowledge/monero-outputs)/

  * [초보자를 위한 모네로 사용 습관 추천](/knowledge/monero-best-practices)/

  * [링서명이 모네로 출력을 숨기는 방법](/knowledge/ring-signatures)/

  * [모네로는 어떻게 비트코인의 고질적인 문제인 규모의 문제를 해결했을까](/knowledge/dynamic-block-size)/

  * [CLSAG는 어떻게 모네로의 효율을 높였을까](/knowledge/what-is-clsag)/

  * [모네로가 꼬리자르기를 도입한 이유](/knowledge/monero-tail-emission)/

  * [모네로의 간단한 역사](/knowledge/monero-history)/

  * [Wired지는 모네로에 대해 틀렸으며, 왜 그런지 알려드리겠습니다](/knowledge/wired-article-debunked)/

  * [모네로에 관한 15가지 미신과 우려, 그리고 그 해답](/knowledge/monero-myths-debunked)/

  * [Dandelion++가 모네로 거래의 출처를 보호하는 방법](/knowledge/monero-dandelion)/

  * [모네로는 왜 탈중앙화와 오픈소스를 선택했는가](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [모네로 채굴: RandomX가 특출난 이유](/knowledge/monero-mining-randomx)/

  * [모네로가 Dash, Zcash, (Lelantus를 적용해도) Zcoin, Grin 그리고 Wasabi같은 비트코인 세탁 서비스보다 뛰어난 이유 (2020년 5월 업데이트)](/knowledge/why-monero-is-better)/

더 보기