---
title: "세라피스: 모네로를 위해 할 일"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Serapis: Monero 거래를 위한 모듈식 설계 업그레이드

이 게시물은 익명의 연구 기고자 [`koe`](https://github.com/UkoeHB) 이(가) Monero 생태계를 위해 개발했으며 지속적인 보안 분석을 통해 거래 프로토콜 구조 및 추상화 집합인 [Seraphis](https://github.com/UkoeHB/Seraphis)에 대해 설명합니다. 익명 기고자 [`cointudent2048`](https://github.com/coinstudent2048).  
우리는 명확성을 위해 일부를 단순화하고 특정 기술 세부 사항을 생략합니다. 이러한 이유로 그리고 Seraphis의 설계가 아직 진행 중이기 때문에 관심 있는 독자는 최신 정보에 대해 Seraphis 문서를 참조해야 합니다.

## 모네로에서의 거래

프로토콜은 _출력_ 전송 할 수있는 값의 표현인 작업의 소위 "출력 모델"에 의존합니다.  
트랜잭션은 보낸 사람이 제어하는 하나 이상의 출력을 소비하고 받는 사람(또는 변경으로 보낸 사람에게 다시 보낸 사람에게 다시) 지시된 새 출력을 생성합니다. 트랜잭션은 소비된 출력에 새 출력의 값과 정확히 동일한 총 값을 포함해야 한다는 점에서 균형을 유지해야 합니다(네트워크 부과 수수료).  
비트코인과 같은 많은 프로토콜에서 출력에 포함된 값은 수신자와 마찬가지로 명확합니다.  
또한 블록 체인을 살펴보면 출력이 소비되었는지( 즉, 나중에 트랜잭션에서 소비된 경우, 어떤 트랜잭션을 소비했는지)를 확인하는 것은 사소한 것입니다. 반면,

Monero와 같은 프로토콜은 다른 디자인을 소개합니다:

  * 출력 값이 숨겨져 있고 블록 체인에 표시되지
  * 받는 사람 주소는 일회용 주소 지정 프로토콜의 사용에 의해 숨겨져
  * 출력이 사용되었는지 여부가 모호한 서명의 사용에 의해 가려집니다

외부 정보가 없는 결과 지정된 출력이 지출되었는지, 그 값이 무엇인지, 받는 사람이 누구인지 를 파악하기가 어렵습니다.

현재 Monero 트랜잭션 프로토콜은 _RingCT_ 라고 하며 이러한 설계 목표를 달성하기 위해 여러 암호화 구성 요소를 사용합니다.

  * _약정은 수학적으로 유용한 방법으로 양을 숨길_
  * _레인지 증명은 공급_
  * _연결 형 링 서명을 팽창시킬 수 있는 오버플로를 방지할 수_ 서명자 모호성을 제공하고 계약 거래 잔액을 주장하기 약속 오프셋을 방지할
  * __

이러한 빌딩 블록은 RingCT 프로토콜을 구축하기 위해 신중하게 얽혀 있습니다.

RingCT 프로토콜의 유용한 속성은 일부 빌딩 블록을 전체 설계 및 속성을 그대로 유지하지만 효율성이나 보안 개선을 제공할 수 있는 방식으로 변경하거나 업그레이드할 수 있다는 것입니다. 실제로 이러한 종류의 업그레이드는 Monero의 역사에서 여러 번 발생하거나 발생할 계획입니다. 원래 RingCT 프로토콜의 범위 증거는 부피가 크고 느렸습니다. 그들은 나중에 더 나은 보안 분석으로 거래를 더 작고 빠르게 만든 [방탄](https://eprint.iacr.org/2017/1066) 라는 건설로 업데이트되었으며, 더 큰 효율성 이점을 위해 [방탄 +](https://eprint.iacr.org/2020/735) 라는 새로운 건설로 업데이트 될 계획입니다.

링크링 시그니처 빌딩 블록과 유사한 프로세스가 진행되었습니다. 원래 프로토콜에서 mlSAG [라는 구조가 사용되었습니다. 이것은 나중에 더 빠르고, 더 작은 트랜잭션을 초래하고, 더 나은 보안 분석을 가지고 [clSAG](https://eprint.iacr.org/2019/654) 라는 새로운 건설로 업데이트되었습니다. [Triptych](https://eprint.iacr.org/2020/018) 기반으로 한 최신 링크링 시그니처 구성이 제안되었지만 다중 서명 작업에 미치는 영향 때문에 배포를 위해 선택되지 않았습니다.](https://ledger.pitt.edu/ojs/ledger/article/view/34)

## 세라피스

Seraphis는 이 아이디어를 한 단계 더 발전시켰습니다.  
기존 RingCT 트랜잭션 프로토콜의 개별 빌딩 블록을 업데이트하는 대신 다른 빌딩 블록을 활용하고 향상된 기능을 제공할 수 있는 다른 프로토콜을 도입합니다.

## 빌딩 블록

Seraphis는 다양한 암호화 빌딩 블록 세트를 사용하여 설계 목표를 달성합니다.

  * _약정_ 여전히 금액 숨기기
  * _범위 증명_ 여전히 오버플로 및 공급 인플레이션 방지
  * _회원 증명_ 서명자 모호성 제공
  * _약정 오프셋_ 여전히 잔액 주장
  * _증명 승인_ 이중 지출 시도 방지

여기에서 변경 사항을 확인하세요. 연결 가능한 링 서명이 회원 증명과 승인 증명의 조합으로 대체되었습니다. 대략적으로 말하면, 멤버십 증명은 소비된 출력이 RingCT에서 발생하는 것과 유사한 더 큰 세트의 일부임을 보여줍니다. 그러나 RingCT와 달리 회원 증명에는 연결 태그가 전혀 포함되지 않습니다! 인증 증명은 연결 태그가 유효하고 최종 거래에 서명하는 데 사용됨을 보여줍니다.

RingCT는 연결 태그를 모호한 서명으로 굽기 때문에 서명(및 다중 서명) 작업은 계산 집약적이며 다른 태그 관련 기능을 구축하는 것이 더 어려워집니다. 그러나 Seraphis에서 멤버십 증명을 구성하는 것은 고도로 신뢰할 수 있는 장치(하드웨어 지갑과 같이 컴퓨팅 성능이 제한적일 수 있음)에서 덜 신뢰할 수 있는 장치로 안전하게 위임할 수 있으며 서명(및 다중 서명) 작업은 훨씬 간단한 인증 증명을 사용하여 훨씬 쉽습니다. .

다행스럽게도 Seraphis가 필요로 하는 구성 요소 중 일부는 이미 다른 곳에 존재하므로 처음부터 설계할 필요가 없습니다. Bulletproofs 및 Bulletproofs+ 구성 모두 범위 증명으로 사용할 수 있습니다. Schnorr 유형 증명 시스템에 대한 수정은 증명을 승인하는 데 사용할 수 있습니다. 그리고 Triptych, [Lelantus](https://eprint.iacr.org/2019/373)및 [Spark](https://eprint.iacr.org/2021/1173)* 의 기반으로 이미 사용되는 효율적인 [증명 시스템](https://eprint.iacr.org/2015/643) 은 회원 증명을 위해 수정할 수 있습니다.

* Cypher Stack은 Spark 개발 자금을 받습니다.

## 주소 지정

유감스럽게도 현재 사용 중인 Monero 주소는 Seraphis와 호환되지 않습니다. 사용자는 Seraphis가 구현된 경우 Monero를 받기 위해 지갑 키에서 새 주소를 생성해야 합니다. 그러나 이 생태계 비용에는 많은 이점이 있습니다.

위에서 논의한 구조적 이점 외에도 Seraphis 설계는 다양한 주소 구성 가능성을 수용할 수 있으며 각 가능성에는 장단점이 있습니다. Seraphis에서 사용할 최종 주소 구성은 [아직 결정](https://github.com/monero-project/research-lab/issues/92) 중이지만(많은 관심을 받고 있는 한 체계를 [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)이라고 함) 몇 가지 일반적이고 유용한 기능을 설명할 수 있습니다.

Monero 주소가 _보기 키_ 기능을 제공한다는 사실을 알고 계실 것입니다. 여기서 보기 키를 기기나 제3자에게 제공하고 사용자를 대신하여 들어오는 출력을 감시하도록 허용할 수 있지만 지출을 포기하지 않아도 됩니다. 권한. 이는 지출 키를 안전하게 잠근 상태로 유지하면서 업데이트 상태를 유지할 수 있는 지갑에 유용합니다. 투명성을 제공하는 공공 자선 단체나 회계 부서가 있는 회사와 같이 외부 보기 액세스를 원하는 경우에도 유용합니다.

Monero 보기 키의 단점은 완전하거나 세분화된 보기 액세스를 제공하지 않는다는 것입니다. 지갑이 언제 자금을 지출하는지 안정적으로 감지할 수 없기 때문에 지출 키를 사용할 수 없을 때 지갑 잔액을 제대로 계산하기 어렵습니다. 또한 해당 출력에 포함된 값을 학습하지 않고 수신 출력을 감지하는 것도 현재 불가능합니다(즉, 수신 출력을 찾는 책임이 있는 모든 타사가 귀하가 획득하는 Monero의 양을 정확히 알 수 있음을 의미합니다).

Seraphis addressing 구조는 이 문제를 해결할 수 있습니다. Seraphis를 사용하면 주소에 다양한 작업을 수행할 수 있는 다양한 키가 함께 제공됩니다.

  * 들어오는 출력을 주시하지만 값을 숨깁니다
  * 들어오는 출력을 주시하지만 값을 표시합니다
  * 나가는 출력을 주시합니다
  * 거래하지만 서명하지 않음
  * 새 주소 생성(소매업체 또는 고객이 많은 교환에 유용)

주소 보유자는 다른 기기나 제3자에게 위임할 권한의 양을 결정할 수 있습니다.

## 큰 그림

세라피스는 모네로 생태계에 큰 변화입니다. 주소 및 트랜잭션 구성 요소를 수정하는 작업이 포함되지만 설계는 오늘날의 RingCT 프로토콜에서는 불가능한 유연성과 유용한 기능을 제공합니다. 대부분의 설계가 완료되고 구현 [개발되는 동안 주소 설계 및 보안 분석이 진행 중입니다. 세라피스(Seraphis)는 모네로 생태계를 발전시킬 수 있는 훌륭한 기회를 제공합니다!](https://github.com/UkoeHB/monero/tree/seraphis_lib)

더 보기

  * [Monero가 순환 경제를 가능하게 하는 방법](/knowledge/monero-circular-economies/)

  * [와사비처럼 모네로의 링 시그니처 vs 코인조인](/knowledge/ring-signatures-vs-coinjoin/)

  * [자신의 키를 보유해야 하는 이유(및 방법!)](/knowledge/hold-your-keys/)

  * [모네로에 다시 기여하기](/knowledge/contributing-to-monero/)

  * [원격 노드가 Monero의 개인 정보에 미치는 영향](/knowledge/remote-nodes-privacy/)

  * [Monero가 하드 포크를 사용하여 네트워크를 업그레이드하는 방법](/knowledge/network-upgrades/)

  * [태그 보기: 1바이트가 Monero 지갑 동기화 시간을 40% 이상 줄이는 방법](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool과 Monero Mining의 탈중앙화에서의 역할](/knowledge/p2pool-decentralizing-monero-mining/)

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