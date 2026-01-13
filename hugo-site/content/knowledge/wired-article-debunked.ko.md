---
title: "Wired지는 모네로에 대해 틀렸으며, 왜 그런지 알려드리겠습니다"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
가상화폐와 보안의 세계에서 잘못된 정보는 만연합니다. [모네로에 관한 15가지 미신과 우려](/knowledge/monero-myths-debunked)란 글이 따로 있지만, 모네로 불신론자들이 자주 퍼뜨리는 한가지에 집중 설명하겠습니다.

Wired지는 2018년 3월 27일, 갓 출시된 “An Empirical Analysis of Traceability in the Monero Blockchain”라는 논문에 대한 [기사](https://www.wired.com/story/monero-privacy/)를 냈습니다.

이해충돌의 여지가 다분하지만 (저자중 일부가 Zcash를 보유하거나 Zcash의 고문), 해당 논문 자체는 모네로 커뮤니티가 이미 빠르면 4년 전에 자체 연구([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf)과 [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf))를 통해 인지하고 있는 부분이기에 겸허하게 받아들였습니다. 물론 이해충돌, 이미 연구된 결과, 어느 정도 해소된 문제라는 점, 그리고 당시 모네로의 개인정보보호 보장을 부정적이게 포장하는 등에 대한 불만은 있었습니다. 커뮤니티는 해당 기사의 견본인쇄에 대한 의견을 전했으며, 기사는 대부분의 의견이 반영된 후 출시되었습니다.

하지만 어떤 식으로 불리하게 포장되었을까? 바로 해당 기사에 지적된 문제점은 이미 해결된지 일년이 넘었다는 것입니다. 2017년 이전 거래는 개인정보 유출의 문제가 있었지만, 기사가 출시될 당시에는 이미 해당 문제를 포함한 많은 문제를 해결했었습니다. 기사 저자의 편을 들자면, 기사에서도 모네로의 해결방안을 언급은 하지만, 당시 가상화폐 세계에서 중요하다고 인지할 정도는 아니었습니다. 그 결과가 Wired지의 기사입니다.

해당 기사를 당시에 맞든 아니든 구시대의 산물로 생각할 수 있지만, 아직도 해당 기사를 인용해 모네로의 개인정보보호를 의심하고 있는 사람들은 지금도 그 기사의 내용이 맞는지 분석해달라고 합니다. 저희는 기꺼이 분석해드리겠습니다.

기사를 읽어보면 중요한 문구가 몇 있는데, “[이 결과가] 아무도 모르게 모네로를 사용하고 싶은 사람에게는 걱정요소가 아니다” 와 기사의 토대가 된 논문을 기반으로 한 기사 전반적으로 느껴지는 해당 결과가 ‘새로운’ 결과라는 어조. 해당 논문은 2014년도부터 논의되어온 문제임에도 불구하고 모네로 유저들에게 개인정보 유출을 조심하라고 추천하거나 커뮤니티의 의견을 모네로는 실험적이기 때문에 구매를 추천하지 않는다고 주장했습니다.

해당 비판이 정말 유효할까? 현실은 모네로의 보안코인으로서의 문제는 이미 해결됐거나 남은 문제는 블록체인 기반의 가상화폐 중 보안코인이 공통적으로 가지고 있는 문제입니다. 여기에 대한 이야기를 해보겠습니다.

모네로에 대해 자주 나오는 비판 중 하나는 블록체인 자체의 수정 불가능한 영구성에 관해서인데, 만약 미래의 신기술이 이를 뚫을 수 있다면, 모네로의 과거 모든 거래내역이 노출된다는 것입니다. 한마디로, 개인정보 유출은 시간문제라는 것입니다.

아무리 강조해도 부족하지만, 이는 블록체인을 기반으로 한 모든 보안코인에 해당되는 문제이지만, 모네로에만 유독 이러한 비판이 (역설적이게도 같은 문제가 있는 다른 보안코인으로부터) 자주 나타나고, 이 기사에서도 인용됩니다. 많은 사람들이 이에 대한 답을 듣고 놀라겠지만, 모네로는 보안 삼신기의 이용으로 다른 보안코인에 비해 이 문제에 덜 취약합니다.

모네로는 출력(송금인), 거래량, 수취인을 링서명, RingCT, 그리고 비밀주소를 통해 숨기고 있습니다. 물론, 링서명이 이 중 반복적인 공격이나 미래의 이론상 가능한 개인정보 공격 기술에 가장 취약합니다. 모네로 커뮤니티는 이를 몇년동안 인지하고 있었으며 링서명을 개선하거나 통째로 교체하기 위해 연구중입니다.

하지만, 링서명이 완전히 실패하더라도, 출력만이 노출될 뿐입니다. 승금인이 아닌 출력만이 노출됩니다. 출력과 실제 인물을 연관짓는게 불가능하지만, 더 많은 메타데이터와 자원이 필요할 것입니다. RingCT와 비밀주소가 노출되지 않는 것을 감안하면 링서명의 실패로 인한 충격은 미미할 것입니다.

Wired지의 기사는 위의 문제를 Riccardo ‘fluffypony’ Spagni의 의견을 묻는 중 간단히만 언급하며 이 중요한 내용을 대충 짚어넘깁니다. 이런 기술에 대한 이해부족은 특히 이 기사를 인용해 비판을 제기하는 사람들과 논의할 때 잘 나타납니다.

좀 더 답하기 어려운 것은 일반 사람들이 모네로를 바라보는 시각에 대한 비판인데, 이는 모네로 커뮤니티가 모네로를 어떻게 인식하는지가 중요합니다. 이는 해당 기사에서도 명확히 들어납니다: “다크웹의 최애 코인은 생각보다 추적불가능하지 않다 (The Dark Web’s Favorite Currency Is Less Untraceable Than It Seems)”.

모네로 커뮤니티에 어느정도 시간을 투자하면 그 누구라도 알겠지만 커뮤니티는 (마케팅이나 도입 면에서 타격을 입더라도)진정한 개인정보 보호가 얼마나 어려운지 보여주기 위해 많은 노력을 들이고 있습니다. 커뮤니티가 코인과 코인의 부족한 점에 대해 충분히 정보를 제공하고 논의한다면, 코인에 대한 무지함은 모네로 하나가 100% 개인정보를 보장해 줄 수 있다고 믿는 유저의 탓입니다.

여기서 알 수 있다시피, 커뮤니티는 모네로의 보안과 모네로에 대한 부족함과 그를 보완하기 위한 기술개발에 전력을 다하고 있습니다. 지금 이같은 기사는 이런 모네로의 혁신을 위한 노력을 무시하고 있습니다. 모네로를 무지한 이들의 수익만을 노리고 말도 안되는 주장을 하는 다른 가상화폐와 같은 수준으로 치부합니다.

현실은 이 정반대입니다.모네로는 취약점을 정확하게 인지하고 있으며, 계속적인 발전을 위해 노력하고 있습니다. 이를 통해 탈중앙화되고 커뮤니티 주도의 개발이 이루어지는 대체성 있는 보안코인의 보급이라는 어렵지만 달성 가능한 목표를 향해 나아가고 있습니다.이제 이런 자아도취와 기사를 통한 경쟁자를 폄훼하는 행위는 그만할 때라고 생각합니다. 이제는 다른 이야기를 할 시대입니다.

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

  * [모네로 출력에 대하여](/knowledge/monero-outputs/)

  * [초보자를 위한 모네로 사용 습관 추천](/knowledge/monero-best-practices/)

  * [링서명이 모네로 출력을 숨기는 방법](/knowledge/ring-signatures/)

  * [모네로는 어떻게 비트코인의 고질적인 문제인 규모의 문제를 해결했을까](/knowledge/dynamic-block-size/)

  * [CLSAG는 어떻게 모네로의 효율을 높였을까](/knowledge/what-is-clsag/)

  * [모네로가 꼬리자르기를 도입한 이유](/knowledge/monero-tail-emission/)

  * [모네로의 간단한 역사](/knowledge/monero-history/)

  * [모네로에 관한 15가지 미신과 우려, 그리고 그 해답](/knowledge/monero-myths-debunked/)

  * [Dandelion++가 모네로 거래의 출처를 보호하는 방법](/knowledge/monero-dandelion/)

  * [모네로는 왜 탈중앙화와 오픈소스를 선택했는가](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [모네로 채굴: RandomX가 특출난 이유](/knowledge/monero-mining-randomx/)

  * [모네로가 Dash, Zcash, (Lelantus를 적용해도) Zcoin, Grin 그리고 Wasabi같은 비트코인 세탁 서비스보다 뛰어난 이유 (2020년 5월 업데이트)](/knowledge/why-monero-is-better/)