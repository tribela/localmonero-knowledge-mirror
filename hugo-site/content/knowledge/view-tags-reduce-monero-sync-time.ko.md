---
title: "태그 보기: 1바이트가 Monero 지갑 동기화 시간을 40% 이상 줄이는 방법"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero를 매일 사용하는 데 있어 가장 일반적인 불만 중 하나는 Monero를 보내기 전에 지갑을 동기화하는 데 걸리는 시간입니다. 고맙게도, Monero 커뮤니티의 개발자와 연구원은 추가 된 블록 체인 bloat, 수수료 등없이 지갑을 40 % 이상 동기화하는 데 걸리는 시간을 줄이는 훌륭한 방법을 발견했습니다

다음 네트워크 업그레이드에서 Monero에 오는 각 트랜잭션의 데이터에 1바이트 추가인 "보기 태그"를 입력합니다!

## Monero의 지갑 동기화가 Bitcoin보다 느린 이유는 무엇입니까?

보기 태그와 같은 솔루션의 필요성을 더 잘 이해하기 위해 답해야 하는 첫 번째 질문 중 하나는 Monero의 지갑 동기화가 Bitcoin과 같은 암호화폐보다 느린 이유입니다.

비트코인에서는 모든 거래가 비공개가 아니며 사용된 코인, 금액 및 온체인 관련 주소가 공개되므로 비트코인 지갑은 사용되지 않은 거래 출력(UTXO) 또는 사용된 주소를 간단히 찾을 수 있습니다. 주어진 지갑에서 해당 주소가 소유한 UTXO에 대해서만 블록체인을 빠르게 스캔하여 지갑에 속하고 사용할 수 있는 코인을 알아냅니다.

그러나 Monero에서는 모든 거래가 각 거래에 관련된 보낸 사람, 받는 사람 및 금액을 숨김으로써 사용자의 개인 정보를 보호합니다. 이 개인 정보는 네트워크 사용자를 보호하는 데 중요하지만 지갑 동기화 속도가 느려집니다. Monero에서 지갑은 네트워크에 존재하는 모든 트랜잭션 출력(TXO)을 지갑의 개인 키와 비교해야 합니다.

이 비교에는 모든 금액, 주소 및 알려진 지출 출력(또는 동전)이 Monero의 온체인에 숨겨져 있기 때문에 출력이 진정으로 귀하의 것인지 확인하기 위해 복잡한 수학 및 암호화가 많이 포함됩니다.

## 보기 태그는 무엇입니까?

Monero 지갑의 동기화 시간을 줄이는 데 도움이 되는 방법으로 [UkoeHB라는 연구원이 새로운 접근 방식을 고안했습니다.](https://github.com/monero-project/research-lab/issues/73) – 알려진 공유 비밀을 사용하여 각 트랜잭션에 1바이트 "태그" 추가 그 거래의 발신자와 수신자에게.

이 공유 비밀은 수신자가 제공한 주소를 사용하여 발신자가 생성하며 발신자와 수신자의 적극적인 협력이 필요하지 않습니다. 이 공유 비밀의 첫 번째 바이트(또는 문자)는 Monero 네트워크에 게시할 때 트랜잭션 데이터에 추가됩니다.

해당 거래의 참여자 중 한 명이 나중에 네트워크의 모든 TXO에 대해 복잡한 수학 및 암호화를 모두 수행할 필요 없이 자신의 지갑을 Monero 블록체인과 동기화하기를 원할 때 지갑은 이제 각 트랜잭션에서 해당 1바이트 필드를 확인한 다음에만 해당 태그가 있는 트랜잭션에 대해 시간이 많이 소요되는 검증을 수행하십시오(정확히 말하면 네트워크의 1/256 TXO)!

이 태그는 트랜잭션에 대한 정보를 외부 뷰어에게 공개하지 않으며 트랜잭션 크기에 1바이트(미미한 양)만 추가하지만 동기화 시간을 40% 이상 줄일 수 있습니다. 복잡한 검증이 필요합니다!

## 태그 보기: 단순화된 예

한 방에 4,096개의 상자가 있고 그 중 5개의 상자만 자신의 것이라고 상상해 보세요. 상자는 모두 외부와 완전히 구별할 수 없으며, 상자가 당신을 위한 것인지 알 수 있는 유일한 방법은 상자를 열고 안에 적힌 시간 소모적인 수학 문제를 풀고 당신의 것인지 확인하는 것입니다.

이제 이 5개의 상자를 보내는 사람이 귀하의 주소를 사용하여 특수 코드를 생성하도록 하고 생성된 코드의 첫 번째 문자만 전송되는 각 상자의 외부에 넣기로 결정했다고 상상해 보십시오. 다른 모든 사람들은 상자에 대해 동일한 작업을 수행하지만(모든 상자를 여전히 구별할 수 없도록 하기 위해) 이제 상자 외부에 있는 하나의 문자 코드를 보고 해당 문자가 있는 상자만 열 수 있습니다.

다른 상자는 귀하의 코드와 일치하지만 일부 상자는 귀하가 소유하지 않은 상자라도 열어서 수학 문제를 풀어야 하는 상자의 수는 이제 16개(1/256 상자!)에 불과합니다. 모두 4,096

이제 16개의 상자를 열고 수학 문제를 풀고 해당 그룹에서 실제로 자신에게 속한 5개의 상자를 유지합니다!

## 언제부터 Monero에서 보기 태그를 사용할 수 있습니까?

보기 태그는 현재 [예정된 네트워크 업그레이드](https://github.com/monero-project/meta/issues/630)에 포함될 예정인 기능 중 하나이며 올 봄에 출시될 예정입니다. 커뮤니티 [는 보기 태그의 개발 및 구현을 장려하기 위해 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (작성 당시)을 올렸으며 결과적으로 Monero 코드 기반에 보기 태그를 포함하는 작업의 대부분이 이미 완료되었습니다. 리뷰어 및 연구원과 협력하여 j-berman이 완성했습니다.

네트워크에서 보기 태그를 적용하면 네트워크 업그레이드 후 전송되는 모든 트랜잭션은 크게 개선된 지갑 동기화 시간의 이점을 누릴 수 있습니다. 보기 태그 사용을 시작하기 위해 특별한 작업을 수행할 필요가 없습니다. 모네로에서 가장 좋아하는 지갑은 네트워크 업그레이드 후 자동으로 태그를 사용하기 시작합니다!

## 자세히 알아보려면 어떻게 해야 하나요?

이것이 보기 태그에 대한 호기심을 불러일으켰다면 주제에 대해 자세히 설명하는 몇 가지 추가 링크를 아래에서 살펴보십시오.

  * [1바이트로 스캔 시간 단축- 출력별 '보기 태그'](https://github.com/monero-project/research-lab/issues/73)
  * [출력에 보기 태그를 추가하여 지갑 스캔 시간을 줄입니다.](https://github.com/monero-project/monero/pull/8061)

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies/)

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin/)

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys/)

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero/)

  * [원격 노드가 Monero의 개인 정보에 미치는 영향](/knowledge/remote-nodes-privacy/)

  * [Monero가 하드 포크를 사용하여 네트워크를 업그레이드하는 방법](/knowledge/network-upgrades/)

  * [P2Pool과 Monero Mining의 탈중앙화에서의 역할](/knowledge/p2pool-decentralizing-monero-mining/)

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