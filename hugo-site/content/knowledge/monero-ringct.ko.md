---
title: "RingCT가 모네로 거래량을 숨기는 방법"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
모네로의 보안은 한번의 실패로 모든 거래내역이 공개될 수 있는 한가지 장치로 인한 것이 아니라, 3가지의 장치를 함께 사용해 서로의 약점을 보완해 모두의 보안을 보장합니다. 이 세가지 방법은 [링서명비밀주소](/knowledge/ring-signatures)입니다. 이 세 가지 기술로 (송금인의) 출력, 거래량, 그리고 수취인을 숨길수 있습니다. 여기서는 RingCT에 대해 알아보겠습니다.

RingCT는 3가지 중 가장 기술적으로 복잡하며 이해하기 어려워 정확히 어떻게 작동하는지에 대해 설명하기보다 거래량을 모르면서 어떻게 검증이 가능한지에 대해 알아보겠습니다. 이해를 돕기 위해 충분한 예시를 들테니 걱정하지 않으셔도 됩니.

천번째로, 왜 거래량을 검증하는 것이 중요한지에 대해 알아봅시다. 왜 그냥 거래량을 숨길 수 없을까? 그 이유는, 사람들이 기회만 보이면 돈을 뽑아낼 생각을 하고 있기 때문입니다. 이게 어떻게 가능할까? 예시를 들어봅시다.

친구에게서 무언가를 구매하고 싶고 친구는 만원을 원한다면, 초기에 당신은 만원을 갖고 있고 친구는 0원을 갖고 있습니다. 친구에게 만원을 주고 나면, 당신은 0원 친구는 만원을 갖고 있습니다. 당신이 만원으로 시작했지만 이제 친구가 만원이 있습니다. 이 과정에서 돈이 새로 생기거나 사라지지 않았습니다.

가상화폐에서 똑똑한 인물은 만원을 지불하고 잔돈 0원을 받는 대신 이천원을 받을 수 있습니다. 0과 10000이 10000과 0이 되는 (10000 = 10000) 대신 0과 10000이 10000과 20000이 (10000 = 12000) 되었습니다. 여기서 2개의 모네로가 갑자기 생성된 것입니다. 이 행위가 여러번 반복되면, 작은 거래 몇번으로 엄청나 금액을 만들 수 있을 것입니다.

비트코인 및 다른 가상화폐는 이를 감지하기 쉽습니다. 그저 거래내역을 확인해서 입력과 출력이 같은지만 확인하면 됩니다. 하지만 이 내용이 암호화되면 유저가 보낸 양과 받는 양을 확인할 수 없습니다.

비트코인의 개인정보보호를 위해 Gregory Maxwell이 거래내역은 암호화하면서 보낸 양과 받는 양을 확인하는 Confidential Transactions (CT)를 만들었습니다. 대부분의 개인정보보호 기술과 마찬가지로 CT는 비트코인에 도입되지 않았지만 모네로는 이를 눈여겨 보고 있었습니다. 하지만 도입하기에는 한가지 문제가 있었는데, 이미 사용중인 링서명 기술과 호환이 불가능하다는 것이였습니다. 그래서 당시 MRL 연구자였던 Shen Noether가 CT를 링서명과 호환 가능한 RingCT로 개선하였습니다.

다시 말씀드리지만 작동원리는 기술적으로 복잡하기에 이 게시글에서 설명하기 어렵습니다. 꼭 알고 싶은 사람이 있다면, 인터넷에 CT의 작동원리를 설명해놓은 글이 많이 있습니다. 우리같은 나머지 일반인들에게는 이 글이 어떻게 거래량을 숨기면서 돈을 마법처럼 생성하지 않는지 검증하는지에 대해 설명드리겠습니다.

영희가 철수에게 돈을 보내고 싶다고 생각해봅시다. 영희는 철수에게 10 XMR을 보내고 철수는 10 XMR을 받을 것입니다. 10=10이니 여기서 문제는 없습니다. 하지만 영희는 누군가에게 얼마를 보냈는지 아무도 모르게 하고 싶습니다. 그렇기에 철수와 영희는 한가지 비밀숫자를 만들어 공유합니다. 예를 들어 그 숫자가 22라고 합시다. 이제 영희가 여기에 10(실제로 영희가 보내는 수량)을 곱하면 결과는 220이고, 이 숫자가 영희가 네트워크와 공유하는 숫자입니다. This is the number she shares with the network.

광부들은 비밀숫자를 모릅니다. 만약 알았다면, 공개된 숫자를 비밀숫자로 나눠 실제 거래량을 알 수 있을 것입니다. 하지만 모르기 때문에 이는 불가능합니다. 그들이 알 수 있는건 철수도 220을 받았다는 것입니다. 220을 보내고, 220을 받으니 220 = 220. 이렇게 되면, 네트워크가 실제 거래량을 알지 못해도 보낸 모네로와 받은 모네로가 같다는 것을 알 수 있습니다.

철수가 비밀숫자를 아고 있으니, 돈을 받고 그 숫자를 비밀숫자로 나누면 영희가 보낸 10을 알 수 있습니다. 영희와 철수는 둘을 제외한 모두에게 가짜 거래량을 알려주면서 둘만은 받은 양과 보낸 양을 정확히 알 수 있습니다.

다시 말씀드리지만, 이는 CT의 실제 작동원리가 아니지만, 이러한 방법이 어떻게 가능한지 보여줍니다. 실제 작동원리는 페데르센 약속, 두가지 거래량(실거래량과 네트워크에 알리는 허위거래량) 등의 기술을 사용합니다. 벌써부터 헷갈리기 시작합니다...

한가지 명심해야할 것은 RingCT가 거래량을 숨기지만 다른 두가지 숫자들은 숨기지 않는다는 것입니다.

첫번째는 코인베이스 거래입니다. 코인베이스 거래란 광부들이 블록을 채굴하면서 얻는 보상입니다. 이 정보는 공개되어 있습니다. 프로토콜이 광부에게 어느 정도의 보상을 주었는지 누구나 볼 수 있습니다. 이를 통해서 모든 코인베이스 거래를 합산하면 현재 모네로의 총량을 알 수 있습니다. 이는 모네로의 유통량과 같을 것입니다.

두번째는 광부에게 지불하는 거래수수료입니다. 거래수수료가 투명해야 광부가 어떤 거래를 우선적으로 포함할 지 결정할 수 있습니다. 하지만 만약 매번 같은 거래수수료를 이용한다면 (0.12345라든가) 거래와 신상을 연결할 수 있어 보안에 치명적일 수 있습니다.

이를 제외하고는 RingCT는 2017년부터 모네로 거래량을 숨겨왔으며 그 덕분에 모두의 보안이 강화되었습니다.

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