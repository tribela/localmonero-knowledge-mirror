---
title: "P2Pool と Monero マイニングの分散化におけるその役割"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero プロジェクトの主な目的の 1 つは、今日の暗号通貨ネットワークを保護する主な方法であるプルーフ オブ ワーク (PoW) マイニングへの新しく革新的なアプローチを通じて、公平で分散化された安全なネットワークを実現することです。

RandomX のような独自のマイニング アルゴリズム [ は、この目的にとって非常に重要です。コンピュータを持っている人なら誰でもネットワークのセキュリティにかなりの量を貢献できるようにするのに役立ちますが、RandomX は問題を解決しません。プールマイニングが原因で発生する可能性があります。プールマイニングは、Monero を含む今日の暗号通貨をマイニングする最も一般的な方法ですが、ありがたいことに、p2pool マイニングの出現により、それが急速に変化しています。](/knowledge/monero-mining-randomx)

## プールマイニングとは？

プールマイニングは、マイナーがネットワーク上のブロックを解決しようとするタスクを共有し、プールが見つけたすべてのブロックの報酬を均等に共有する方法です。これは、Monero のみをマイニングする場合と比較して、マイナーが支払われる頻度を均等にするのに非常に役立ちますが、深刻な集中化の問題がないわけではありません。

各マイナーがプールに仕事を提供するとき、自分が行った作業と見つけたブロックの管理をプール自体に委ね、プールが各マイナーの作業量に応じた報酬を誠実かつ公平に分配してくれることを信じている。すべてがうまくいけば、プール オペレーターはすべてのマイナーから作業を収集し、それをネットワークに送信し、報酬を均等に分配します。

## プールマイニングの問題点とは？

残念ながら、これは信頼に完全に依存しているため、マイナーが行っている作業に対してプール オペレーターが悪意のあることを行うことができます。プールのオペレーターは、実行中の作業を使用してネットワークを攻撃したり、資金を二重に使用しようとしたり (プールが十分に大きい場合)、または単にマイナーが行っている作業を使用して自分自身を支払い、マイナーに作業に対して適切な報酬を与えない可能性があります。 

ネットワークに対する最大のリスクは、ネットワーク ハッシュレートの 51% 以上を制御下に置くプール (または複数のプールが連携して動作する) のリスクです。攻撃) またはネットワークのルールを変更しようとします。

## p2poolとは？

p2pool は、もともと 2011 年にビットコインのマイニングのために作成された概念ですが、広く採用されることはなく、ビットコインでは実質的に使用されていません。ありがたいことに、RandomX の背後にいる主要な開発者の 1 人である SChernykh は、休暇を利用して、p2pool のビットコイン実装に関するいくつかの問題の解決策を考え出し、すべてのソフトウェアをゼロから書き直しました。

Monero の p2pool は、マイナーが協力してブロックを解決し、作業を共有するために p2pool 用の特別なノード ソフトウェアを使用して Monero ネットワークを保護するための完全にトラストレスな方法を可能にします。

これは新しいブロックチェーン (「サイドチェーン」) を使用して行われ、各マイナーが実行する作業、ウォレット アドレス、獲得した Monero の記録を保持し、報酬をトラストで支払います。 少ない分散型の方法。このサイドチェーンにはマイナーがはるかに少ないため、メインの Monero ネットワークよりもブロックを見つけて送信する方がはるかに簡単で、Monero だけをマイニングするよりも、マイナーが一貫したペイアウトを得ることが容易になります。

## p2pool はプール マイニングの問題をどのように解決しますか?

p2poolでは、集中型プール、オペレーター、または資金を保持して支払いを分配する 1 人の人物は存在しません。 p2poolを介したマイニングによって集合的に行われているすべての作業は、p2poolブロックチェーンと他のノード オペレーターによってチェックされ、その見つかったブロックの報酬が正当であることが確認されます。

マイナーが中央集権的なプールの代わりにp2poolを使うことを選択した場合、彼らはプール運営者からすべての権力と信頼を取り除き、自分の仕事がネットワークの利益と自分の報酬に貢献することを保証し、ネットワーク攻撃、自分の仕事の悪用、または自分が負うべき報酬の盗難のリスクを減らすことができます。

これは、彼ら自身の利益を保護するのに役立つだけでなく、集中プールがMoneroネットワーク全体にもたらすリスクを軽減します。また、p2pool の使用は、国家や規制当局がネットワークの健全性に与える可能性のあるリスクを軽減するのに非常に役立ちます。これは、集中化されたプール オペレーターに圧力をかけたり、頼りになるプールの地理的な集中や、その他の簡単な圧力ポイントがないためです。彼らがMoneroに対して使用するため。

## 欠点は何ですか？

ありがたいことに、Monero の p2pool は適切に設計され、適切に構築されており、機能も非常に優れています。ただし、p2pool マイニングの主な欠点は、p2pool を使用したい各マイナーが独自の Monero ノードを実行する必要があるため、開始プロセスが少し複雑になることです。ただし、このノードは、ブロックの構築とチェックに必要なすべての情報を計算するために使用され、マイナーが実行中の作業を完全に制御できるようにします。このノードは、マイナー自身のウォレットのリモート ノードとして機能したり、ネットワークに貢献したりすることもできます。

集中型マイニングとのもう 1 つの重要な違いは、p2pool を使用する小規模なマイナーは " 分散 "、または支払い間の時間が、大きな集中型プールよりも ' よりも _大きいことです。非常に_ これにより、時間の経過とともにモネロの収益が減少するわけではないことに注意することが重要です! p2pool は、時間の経過とともに小規模なマイナーにとっても、集中型プールと同じくらい収益性が高くなります。この差異の一部は、サービスの料金を支払う集中型プール オペレーターが存在しないため、p2pool がネイティブに 0% の料金を請求することによっても相殺されます!

## どうすれば始められますか?

ありがたいことに、Monero' の p2pool 実装の優れた設計と、p2pool を介したマイニングのプロセスを簡素化するために時間を割いてくれたコミュニティの多くの人々のおかげで、時間の経過とともに簡単に始めることができます。 p2pool でマイニングを開始するにはいくつかの方法がありますが、技術的な詳細はこの記事の範囲を超えているため、お使いのオペレーティング システムに応じて、以下のリンクに自由にジャンプしてください。

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## どうすれば詳細を知ることができますか?

これが p2pool マイニングに関する好奇心を刺激した場合は、p2pool に関する追加のリンクと説明、その仕組み、および Monero にとっての意味について以下を参照してください。

  * [p2pool](https://github.com/SChernykh/p2pool)
の公式Github 
  * [p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
の使用に関する公式ドキュメント 
  * [Monero P2Pool が稼働中](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer、p2pool](https://p2pool.observer/)
の " ブロック エクスプローラー " の種類 
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: 分散型 XMR マイニング プールである P2Pool の開発について](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

参考文献

  * [Monero が独自に循環型経済を実現する方法](/knowledge/monero-circular-economies/)

  * [モネロのリング署名とWasabiのような CoinJoin の比較](/knowledge/ring-signatures-vs-coinjoin/)

  * [なぜ (そしてどのように!) 自分の鍵を保持する必要があるのか](/knowledge/hold-your-keys/)

  * [モネロへの寄付](/knowledge/contributing-to-monero/)

  * [リモートノードが Monero のプライバシーに与える影響](/knowledge/remote-nodes-privacy/)

  * [Monero がハードフォークを使用してネットワークをアップグレードする方法](/knowledge/network-upgrades/)

  * [タグを表示: 1 バイトで Monero ウォレットの同期時間を 40% 以上短縮する方法](/knowledge/view-tags-reduce-monero-sync-time/)

  * [セラフィス: モネロに何をもたらすか](/knowledge/seraphis-for-monero/)

  * [ビットコインをモネロに変換することは、モネロを直接購入することと同じくらいプライベートですか?](/knowledge/most-private-way-to-buy-monero/)

  * [Monero が Zcash とは異なりトラストレス設定を使用する理由](/knowledge/monero-trustless-setup/)

  * [モネロがビットコインより優れた価値の保存手段である理由](/knowledge/monero-better-store-of-value/)

  * [モネロがビットコインのネットワーク効果を克服する方法](/knowledge/network-effect/)

  * [モネロが最も批判的思考のコミュニティを持っている理由](/knowledge/critical-thinking/)

  * [モネロを使用する際に注意すべき詐欺](/knowledge/monero-scams/)

  * [モネロでアトミックスワップがどのように機能するか](/knowledge/monero-atomic-swaps/)

  * [ネットワーキングに関してすべての Monero ユーザーが知っておくべきこと](/knowledge/monero-networking/)

  * [RingCT がモネロの取引金額を隠す方法](/knowledge/monero-ringct/)

  * [Monero ステルス アドレスが個人情報を保護する方法](/knowledge/monero-stealth-addresses/)

  * [Monero のサブアドレスが ID リンクを防止するしくみ](/knowledge/monero-subaddresses/)

  * [モネロのアウトプットの説明](/knowledge/monero-outputs/)

  * [初心者のためのモネロのベストプラクティス](/knowledge/monero-best-practices/)

  * [リング署名がMoneroの出力を覆い隠す方法](/knowledge/ring-signatures/)

  * [Monero がビットコインを悩ませているブロックサイズの問題をどのように解決したか](/knowledge/dynamic-block-size/)

  * [CLSAG がモネロの効率を改善する方法](/knowledge/what-is-clsag/)

  * [モネロにテールエミッションがある理由](/knowledge/monero-tail-emission/)

  * [モネロの簡単な歴史](/knowledge/monero-history/)

  * [ワイアード・マガジンはモネロについて間違っている、その理由はここにある](/knowledge/wired-article-debunked/)

  * [トップ15のモネロの神話と懸念が暴かれる](/knowledge/monero-myths-debunked/)

  * [Dandelion++ が Monero のトランザクションの起点を非公開にする方法](/knowledge/monero-dandelion/)

  * [モネロがオープンソースで分散化されている理由](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero マイニング: RandomX が特別な理由](/knowledge/monero-mining-randomx/)

  * [Monero が Dash、Zcash、Zcoin (Lelantus を使用しても)、Grin、およびWasabi のような Bitcoin ミキサーよりも優れている理由 (2020 年 5 月更新)](/knowledge/why-monero-is-better/)