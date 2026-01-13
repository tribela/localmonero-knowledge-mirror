---
title: "모네로 출력에 대하여"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
모네로는 다른 가상화폐와 마찬가지로 '출력'을 통해 자금의 회계감사를 합니다. 가상화폐 경험이 많은 사람들은 '출력'에 대해 들어보았지만 이것이 무엇이고 어떤 원리로 작동하는지 이해하지 못하고 있습니다. [링서명 게시글](/knowledge/ring-signatures)에서 설명했듯이, 출력은 블록체인에서 거래되는 단위입니다. 원(화폐)과 비슷하지만, 차이점은 그 양이 고정되지 않았다는 점입니다.

노동에 대한 대가로 천원권, 오천원권, 만원권 총 만육천원을 받았다고 생각해봅시다. 당신은 지갑에 총 세 장의 화폐인 만육천원을 갖고 있습니다. 누군가에게 육천원을 주고 싶다면 오천원권과 천원권을 사용할 수 있지만, 누군가에게 팔천원을 주고 싶다면 만원권만 사용 가능하고 대신 이천원을 돌려받을 것입니다. 또, 누군가에게 만사천원을 주고 싶다면, 화폐 세 장을 모두 사용하고 이천원을 돌려받겠지만, 화폐 세 장을 넘겨준 그 순간에는 잔돈을 돌려받기 전까지 지갑에 더 이상 돈이 없습니다.

모네로도 비슷한 원리를 이용합니다. 당신이 가게를 운영하고 있다고 가정하고 세 가지 각기 다른 물품을 하나씩 팔았다고 생각해봅시다. 1.5 XMR, 2.25 XMR, 그리고 5.25 XMR를 받아 총 9 XMR을 받았지만, 3개의 다른 '출력'을 지갑에 받았습니다. 원을 사용할 때와 같이, 누군가에게 3 XMR을 주고 싶다고 하면, 5.25 XMR 출력을 사용하고 2.25 XMR을 돌려받거나, 1.5와 2.25 XMR 출력을 사용하고 0.75 XMR을 돌려받을 수도 있습니다.

하지만 모네로는 송금을 하는 순간 사용한 출력이 "잠김" 상태가 되어, 잔돈을 돌려받기 전까지 사용이 불가능해집니다. 프로토콜은 10번의 검증 (약 20분) 이후 자금을 '풀어'줍니다 (=잔돈을 돌려준다). or around 20 minutes. 원화를 이용해 잔돈을 돌려받기 전까지 사용이 불가능한 것처럼, 지갑에서 출력을 사용하면, 잔돈을 돌려받기 전까지 모네로는 사용 불가능합니다.

누군가에게 3 XMR을 주기 위해 5.25 XMR 출력을 이용하는 상황으로 돌아가 봅시다. 해당 출력을 이용하면, 잔돈 1.75 XMR을 돌려받기 전까지 이용 불가능합니다. 이 1.75 XMR은 당신이 현재 사용하지 못합니다. 하지만 1.5 XMR와 2.25 XMR 출력은 건들지 않았기 때문에 사용할 수 있습니다. 원화 예시로 돌아가서, 누군가에게 팔천원을 주었다면, 잔돈 이천원은 돌려받기 전까지 사용 불가능하지만, 다른 화폐는 아직 사용되지 않고 지갑에 있습니다. 이 화폐는 잔돈을 돌려받기 기다리는 동안 어디든 사용 가능합니다. 모네로도 마찬가지입니다.

이러한 모네로를 처음 접하는 사람들은 여기서 많이 헷갈려 합니다. 거래소에서 샀든 친구에게 받았든 많은 사람들이 종종 지갑에 하나의 출력만을 보관합니다. 그 출력이 20 XMR라고 가정해 봅시다. 이 지갑에는 그 한 개의 출력 외에는 아무것도 없습니다. 이제 이 사람이 두 곳에 기부를 하고 싶다고 생각해봅시다. 그는 첫 단체에 5 XMR만을 보내서 15 XMR이 남아야 하는데 곧바로 다음 단체에 기부를 하려고 하니 (출력이 없어서) 기부가 불가능해 혼란스러워 합니다. 지금쯤이면 아시겠지만, 그 이유는 잔돈 15 XMR이 '잠겨있기' 때문입니다. 잔돈으로 돌려받을 때(10번의 검증 또는 대략 20분 정도)까지 사용이 불가능합니다. 잔돈이 풀리고 나면 이제 두번째 단체에 기부를 할 수 있습니다.

다시 말하자면, 그가 10 XMR 출력 두개 등 여러개의 출력을 가지고 있었다면 이런 문제는 없었을 것입니다. 첫 번째 기부에 첫 10 XMR 출력을 사용하고 (5 XMR 잔돈은 10번의 검증 이후에 받고) 두 번쨰 기부에 다른 10 XMR 출력을 사용해 두 번의 기부 모두 바로 할 수 있었을 것입니다.

어떤 가상화폐 지갑들은 '출력 관리'라는 기능이 있어서, 유저가 현재 어떤 출력(총액 포함)을 갖고 있는 지 보여주어 가상화폐를 사용할 시 어떤 출력을 이용할 지 선택할 수 있게 해줍니다.

현재 모네로 GUI는 혼란관 개인정보 유출을 방지하기 위해 자동으로 유저를 위해 출력을 선택해줍니다. 현재 Feather 지갑같은 출력관리를 지원하는 지갑들이 개발중에 있습니다.

지금까지는 송금하는 사람 입장에서만 얘기했지만, 받는 사람 입장에서도 흥미로운 일이 생깁니다. 누군가에게 3 XMR를 보내는 예시로 돌아가서, 1.5 XMR과 2.25 XMR 출력을 사용했을 때, 수취인은 1.5와 2.25 XMR에 해당하는 2개의 출력을 받지 않습니다. 그들은 한 개의 3 XMR 출력을 받습니다.

프로토콜은 뒤에서 사용된 모든 출력을 합쳐 수취인에게 한개의 출력을 보내주며, 송금인에게 한개의 출력으로 잔돈을 되돌려줍니다. 송금인이 2,3, 또는 10개의 출력을 사용하더라도 잔돈은 한개의 출력으로 되돌려 받습니다.

이 글이 출력과 프로토콜 자체의 내부 회계감사에 대한 이해를 도왔기 바라고, 잠긴 자금에 대한 궁금점도 해결됐기 바랍니다. 다른 글에서 다른 거래를 기다리게 될 가능성을 최소화하는 출력관리에 대해 다루겠습니다.

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies/)

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin/)

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys/)

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero/)

  * [원격 노드가 Monero의 개인 정보에 미치는 영향](/knowledge/remote-nodes-privacy/)

  * [Monero가 하드 포크를 사용하여 네트워크를 업그레이드하는 방법](/knowledge/network-upgrades/)

  * [태그 보기: 1바이트가 Monero 지갑 동기화 시간을 40% 이상 줄이는 방법](/knowledge/view-tags-reduce-monero-sync-time/)

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