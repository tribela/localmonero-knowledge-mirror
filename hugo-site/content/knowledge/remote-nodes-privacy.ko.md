---
title: "원격 노드가 Monero의 개인 정보에 미치는 영향"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero가 다른 암호 화폐에 비해 가지고있는 가장 큰 장점 중 하나는 체인 개인 정보 보호이지만 원격 노드를 사용할 때 Monero의 개인 정보가 어떻게 유지되는지 궁금해 한 적이 있습니까? MyMonero와 같은 "가벼운 지갑" 서버를 사용하는 경우 어떻습니까?

이 게시물에서 우리는 모네로가 원격 노드를 사용하는 경우에도 뛰어난 온 체인 개인 정보를 제공하는 방법의 세부 사항뿐만 아니라 원격 노드를 사용할 때 주의할 내용에 대해 자세히 알아봅니까?

## 노드는 Monero에서 어떤 기능을 수행합니까?

## 노드는 Monero에서 어떤 기능을 수행합니까?

Monero의 작동 방식에 익숙하지 않은 사용자를 위해 Monero 네트워크의 노드(또는 서버)는 누구나 실행할 수 있으며 노드 소유자 또는 노드가 공유하기로 선택한 다른 사람을 허용할 수 있습니다. – 블록체인 사본을 동기화하고 해당 사본을 네트워크의 다른 사람에게 제공합니다. 이 노드는 또한 네트워크에서 발생하는 모든 트랜잭션과 게시된 모든 블록을 확인하고 모두 합의에 의해 설정된 규칙을 따르는지 확인합니다.

Monero에서 노드가 제공하는 또 다른 기능은 좋아하는 Monero 지갑이 귀하에게 속한 트랜잭션을 올바르게 확인하고 새로운 트랜잭션을 수행하는 데 필요한 모든 데이터를 제공하는 방법입니다. 이 데이터는 두 가지 방법으로 노드에서 제공됩니다.

  * 블록체인의 각 블록에 있는 데이터는 지갑에서 요청하고 귀하에게 속한 트랜잭션을 검색한 다음 지갑에서 확인한 후 폐기됩니다. 
    * 이 단계는 [보기 태그](/knowledge/view-tags-reduce-monero-sync-time)덕분에 곧 크게 개선될 것입니다.
  * 트랜잭션을 보낼 때 사용하는 노드는 트랜잭션을 빌드할 때 사용할 수 있는 미끼(또는 가짜 입력) 목록을 제공하여 매번 숨길 수 있는 좋은 군중이 있는지 확인합니다. 당신은 모네로를 보냅니다. 
    * 이러한 미끼는 [링 서명](/knowledge/ring-signatures)의 일부이며, 온체인의 개인정보 보호에 대한 Monero의 접근 방식에서 중요한 부분입니다.

  * 이 단계는 [보기 태그](/knowledge/view-tags-reduce-monero-sync-time)덕분에 곧 크게 개선될 것입니다.

  * 이러한 미끼는 [링 서명](/knowledge/ring-signatures)의 일부이며, 온체인의 개인정보 보호에 대한 Monero의 접근 방식에서 중요한 부분입니다.

## Monero를 사용하는 가장 개인적이고 안전한 방법은 무엇입니까?

## Monero를 사용하는 가장 개인적이고 안전한 방법은 무엇입니까?

원격 노드를 사용할 때 Monero가 제공하는 강력한 온체인 개인정보 보호가 있더라도 가장 좋은 방법은 자신의 Monero 노드를 실행하여 Monero 블록체인의 원본 사본을 편리하게 사용할 수 있고 IP 주소가 잘 보호되어 있습니다. 자체 노드를 실행할 때의 또 다른 이점은 네트워크에 다시 기여할 수 있어 다른 노드가 노드에서 동기화하거나 다른 사용자가 지갑을 사용하여 노드에 연결할 수 있다는 것입니다.

그렇지만 Monero는 원격 노드를 사용할 때 여전히 우수한 개인 정보를 제공합니다. 자신의 Monero 노드를 실행하는 데 관심이 있는 경우 다음 가이드를 따르십시오.

  * [Monero 노드 실행](https://sethforprivacy.com/guides/run-a-monero-node/)

## 원격 노드는 나에 대해 무엇을 알 수 있습니까?

## 원격 노드는 나에 대해 무엇을 알 수 있습니까?

원격 노드를 사용할 때 원격 노드에 노출되는 몇 가지 주요 정보와 노드가 사용자를 공격하고 거래를 방지할 수 있는 몇 가지 주요 방법이 있습니다.

원격 노드가 사용자에 대해 가장 먼저 알 수 있는 것은 공개 IP 주소입니다. 이것은 VPN 또는 Tor를 통해 숨겨지지만 원격 노드는 공용 IP 주소를 거래와 연결하여 거래 대상을 좁힐 수 있습니다. 원격 노드는 또한 지갑이 동기화된 마지막 블록을 학습하고 이를 사용하여 일반적으로 Monero를 사용하는 시간과 Monero를 마지막으로 사용한 시간과 같이 사용자에 대한 교육적인 추측을 시도하고 추측할 수 있습니다. 항상 동일한 IP 주소(예: 집)에서 오는 경우 특히 그렇습니다. 원격 노드가 당신에 대해 배울 수 있는 마지막 핵심은 당신이 그것을 통해 보내는 트랜잭션에 대한 기본 정보입니다. 이것은 원격 노드 운영자가 귀하에 대해 얻는 가장 명백한 데이터일 수 있지만, 해당 정보를 다른 오프체인 데이터와 결합할 때 트랜잭션 발신자를 추적하는 데 사용할 수 있다는 점을 이해하는 것이 중요합니다. 원격 노드가 악의적인 엔티티, 블록체인 분석 회사 또는 억압적인 국가에 의해 실행되는 경우 특히 위험할 수 있습니다.

원격 노드는 블록을 숨겨서 문제를 일으키려고 시도하여 지갑이 동기화되지 않았을 때 동기화된 것으로 생각하게 만들 수도 있습니다. 이것은 자금이 손실되었다고 생각하거나 다른 노드에 연결할 때까지 자금을 지출하지 못하게 할 수 있습니다. 원격 노드가 할 수 있는 마지막 핵심은 지갑에 조작된 미끼 목록을 제공하는 것입니다. 이로 인해 지갑이 거래를 구축하는 데 완전히 실패하거나(자금을 쓸 수 없게 됨) 원격 노드가 각 거래에서 받는 익명성을 줄이기 위해 지출된 것으로 알고 있는 미끼를 시도하고 제공할 수 있습니다.

## 원격 노드를 사용할 때 어떤 개인 정보 보호가 여전히 존재합니까?

## 원격 노드를 사용할 때 어떤 개인 정보 보호가 여전히 존재합니까?

이 문서는 당신을 조금 무서워 할 수 있지만, 모네로가 제공하는 개인 정보 보호는 원격 노드를 사용하는 경우에도 우수하고, 이 방법으로 사용할 때 훨씬 다른 암호 화폐를 능가한다는 것을 깨닫는 것이 중요합니다. 원격 노드는 실제 입력 (지출하는 동전), 트랜잭션에 지출 한 Monero의 양 또는 트랜잭션 수신자의 주소를 알지 못했기 때문에 Monero가 제공하는 강력한 온 체인 개인 정보를 얻을 수 있습니다. 외부 관찰자는 또한 관련 된 실제 입력, 금액 또는 주소(어떤 유형의 노드를 사용하든!)을 볼 수 없으므로 원격 노드 외부에서도 IP 주소, 지갑 동기화 정보 및 트랜잭션에 강력한 개인 정보 보호 보장이 보장됩니다.

원격 노드는 전송하거나 받은 이전 트랜잭션또는 현재 지갑에 있는 Monero의 양에 액세스할 수 없으며 다른 노드를 사용하기 시작하는 순간 트랜잭션에 대한 모든 가시성을 잃게 됩니다. 원격 노드에 개인 키(지출 또는 보기 키)가 제공되지 않으므로 지갑은 비공개, 안전 및 사용 가능한 상태로 유지됩니다. 원격 노드에 관계없이 노드가 받는 사람 주소를 편집할 수 없고 지갑 개인 키에 액세스할 수 없으며 Monero를 어떤 식으로든 압수할 수 없기 때문에 Monero를 잃거나 도난당한 위험도 없습니다.

## MyMonero와 같은 "가벼운 지갑"은 어떻습니까?

## MyMonero와 같은 "가벼운 지갑"은 어떻습니까?

주제는 이 문서의 범위를 약간 벗어나지만 저는 Monero의 고유한 유형의 지갑인 가벼운 지갑을 다루고 싶었습니다. 가벼운 지갑이라는 이름은 지갑(휴대폰이나 컴퓨터에서)이 블록체인 동기화를 수행할 필요가 없다는 사실에서 유래하여 경험을 더 빠르고 유동적으로 만듭니다.

그러나 이와 같은 지갑에는 현재 심각한 개인 정보 보호 문제가 있습니다. 지갑은 개인 보기 키를 사용하는 원격 서버(MyMonero의 기본값과 같은)로 전송하여 원격 서버에 대한 완전한 가시성을 제공합니다. 지갑 생성 이후(그리고 해당 지갑이나 시드 사용을 중단할 때까지) 받은 모든 자금. 이렇게 하면 노드 운영자로부터 받는 개인 정보가 크게 줄어들므로 주의해서 접근해야 합니다.

고맙게도 Monero 커뮤니티는 개인 보기 키로 타사를 신뢰하지 않고도 빠른 동기화를 허용하는 자체 LWS(Light Wallet Server)를 호스팅하는 데 사용할 수 있는 소프트웨어를 개선하기 위해 노력하고 있습니다. – 지갑이 개인 보기 키를 보내는 소프트웨어를 실행할 때!

커스텀 라이트 월렛 서버에 대한 자세한 내용은 아래 Github 저장소를 참조하세요.

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## 자세히 알아보려면 어떻게 해야 하나요?

## 자세히 알아보려면 어떻게 해야 하나요?

모네로의 노드를 더 잘 이해하고 원격 노드를 사용하거나 직접 실행하는 것을 보고 싶다면 아래 링크를 참조하십시오:

  * [Monero World, 세스 포 프라이버시가 운영하는 Monero 노드에](https://moneroworld.com/#nodes)
  * [사용할 수 있는 커뮤니티 실행 원격 노드 목록, 이 문서의 작성자](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, 자주 확인 된 상태와 원격 노드의 목록](https://monero.fail/)
  * [GUI 지갑](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia 내에서 원격 노드에 연결하는 방법 - 원격 노드](https://www.getmonero.org/resources/moneropedia/remote-node.html)

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies)/

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin)/

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys)/

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero)/

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