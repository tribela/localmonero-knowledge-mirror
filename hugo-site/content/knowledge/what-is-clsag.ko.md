---
title: "CLSAG는 어떻게 모네로의 효율을 높였을까"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
모네로는 프로토콜로서 지속적으로 발전하고 있습니다. 모네로 커뮤니티는 체인 내/외부에서 모네로를 더욱 익명성과 보안이 보장되고, 누구나, 어떤 규모로든 이용할 수 있도록 지속적으로 연구를 하고 있습니다. 가장 최근 발명 중 하나는 추적이 가능한 링서명인 MLSAG를 drop-in replacement CLSAG(Concise Linkable Spontaneous Anonymous Group)(연결 가능한 즉흥적인 익명 축약 그룹)로 대체하였습니다.

표면적으로 CLSAG의 도입은 가장 흔한 거래인 2입력 2출력 거래를 25% 가량 줄일 것이고, 검증시간 또한 10% 감소할 것입니다.

하지만 CLSAG란 도대체 무엇일까? CLSAG는 어떻게 작동하며 구버전인 MLSAG와 차이점은 뭘까? 일단 링서명이란 무엇이고 어떻게 작동하는지에 대해 알아봅시다. 링서명은 이전 출력을 이용해 상호작용이 필요없는 구분 불가능한 입력을 이용 가능하게 합니다. 간단히 말해, 유저는 다른 사람의 도움 없이 자신의 출력을 다른 유저들의 출력들 사이에 섞어 숨길 수 있습니다. 필요한 것은 블록체인 뿐입니다. 이 출력들은 외부에서 구분 불가능해 전부 진짜 출력일 가능성이 있어 보여 입력자의 정보를 숨기게 됩니다.

하지만 여기에도 문제는 있습니다. 유저가 진짜 출력은 없는 가짜 출력만으로 링서명을 만들면 어떻게 될까? 이 유저가 다른 유저들의 출력만을 사용하면 가짜로 돈을 보낼 수 있지 않을까? 답은 아닙니다. 링서명은 입력자가 누구인지 밝히지 않으면서 최소 1개 이상의 출력은 입력자의 것임을 확인할 수 있는 방법이 있습니다. CLSAG와 MLSAG (추후 SAG로 표기) 둘 다 이 방법이 사용 가능합니다. 흥미롭게도 이 방법은 동시에 (숨겨진) 거래의 거래량을 확인할 필요 없이 거래를 검증합니다. SAG가 최소 1개의 출력이 링서명 유저의 소유라는 것과 거래량이 검증된다는 것을 보여주는 것은 중요합니다. 곧 이해하기 쉬운 예시를 들테니 아직 어려워도 걱정하지 않으셔도 됩니다.

구식 서명인 MLSAG(Multilayered Linkable Spontaneous Anonymous Group)(연결 가능한 다중 즉흥 익명 그룹)는 링서명을 이용하여 방금 말한 2가지를 검증하지만, 따로 검증됩니다. 따로 검증하게 되면 2번의 검증이 필요하기 때문에 검증 속도가 느려집니다. 오늘날의 컴퓨터는 이를 거래당 0.001초 안에 계산할 수 있습니다. 매우 빠르다고 생각될 수 있지만, 모네로 블록체인 전체의 거래량을 감안하고 새로 노드를 운영할 때 모든 거래를 다운받고 검증받는다는 것을 생각했을 때, 소요시간과 데이터량은 엄청나게 많습니다.

CLSAG는 보안을 유지하면서 필요한 계산을 하나로 합쳐 한번에 계산합니다. 보안을 유지하면서 이게 어떻게 가능할까? 간단히 설명하기 위해 또 아까 약속한 재미난 예시를 들겠습니다.

음식과 청소용액 구매를 위해 식료품점과 철물점 두 곳을 들러야 한다고 생각해 봅시다. 음식과 청소용액이 섞이면 안되기 때문에 두 가지를 같이 보관하고 싶지 않습니다. 안전하게 하기 위해 당신은 먼저 식료품점에 들려 음식을 사고 다시 집에 돌아가서 음식을 집에 갖다 놓습니다. 음식을 집에 내려놓은 이후에야 당신은 철물점에 가서 청소용품을 구매하고 귀가합니다. 당신의 안전을 위해 2번의 심부름을 따로 했습니다. 안전하긴 하겠지만, 비효율적입니다. 이게 MLSAG입니다; 2번의 계산이 2번의 '심부름'으로 나뉘어져 있습니다.

하지만 시간낭비가 심해서 다른 방법을 찾고 싶다고 생각해봅시다. 한두번 심부름한다고 인생에 큰 영향이 생기지는 않겠지만, 매번 심부름을 2번에 나눠서 해야 한다고 생각하면 낭비하는 시간이 꽤 많아집니다. 그래서 어떻게 한번에 해결할 수 없을까 고민하기 시작합니다; 집, 식료품점, 철물점, 귀가. 하지만 모든 물품을 같이 보관하면 안전하지 않습니다. 그래서 당신은 안전하지만 확실하게 물품들을 보관하기 위해 차 안에 물품들의 지정석을 정하기로 합니다. 이렇게 하면 두번의 심부름을 한번으로 줄이면서 음식과 청소용액이 섞일 걱정도 하지 않아도 됩니다. 이게 CLSAG입니다. 2번의 검증을 서로 섞이지 않게 1번의 계산으로 할 수 있게 됩니다. 아직도 1번의 심부름은 해야하지만, 소요시간을 반으로 줄였습니다.

이게 가능하다면, 어떻게 소요시간을 더 줄이는 방법이 있지 않을까? 답은 가능하지만 SAG는 안된다 입니다. MRL 연구자들에 의하면, SAG의 사이즈와 속도는 더 이상 최적화하기 불가능합니다; 하지만 Arcturus, Omniring, RCT3, 또는 Triptych 같은 서명은 다른 계산식을 이용해 더 향상된 사이즈와 검증이 가능합니다. 하지만 이 '차세대' 방안은 대신 도입하는 데 어려움이 있어서 아직은 연구가 더 필요합니다.

모네로는 항상 진화하고 있습니다.

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies)/

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin)/

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

  * [모네로가 꼬리자르기를 도입한 이유](/knowledge/monero-tail-emission)/

  * [모네로의 간단한 역사](/knowledge/monero-history)/

  * [Wired지는 모네로에 대해 틀렸으며, 왜 그런지 알려드리겠습니다](/knowledge/wired-article-debunked)/

  * [모네로에 관한 15가지 미신과 우려, 그리고 그 해답](/knowledge/monero-myths-debunked)/

  * [Dandelion++가 모네로 거래의 출처를 보호하는 방법](/knowledge/monero-dandelion)/

  * [모네로는 왜 탈중앙화와 오픈소스를 선택했는가](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [모네로 채굴: RandomX가 특출난 이유](/knowledge/monero-mining-randomx)/

  * [모네로가 Dash, Zcash, (Lelantus를 적용해도) Zcoin, Grin 그리고 Wasabi같은 비트코인 세탁 서비스보다 뛰어난 이유 (2020년 5월 업데이트)](/knowledge/why-monero-is-better)/

더 보기