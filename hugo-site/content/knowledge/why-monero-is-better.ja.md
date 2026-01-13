---
title: "Monero が Dash、Zcash、Zcoin (Lelantus を使用しても)、Grin、およびWasabi のような Bitcoin ミキサーよりも優れている理由 (2020 年 5 月更新)"
slug: "why-monero-is-better"
date: "2024-01-01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
すべてのプライバシー中心のコインが、100% プライバシー、追跡不可能性、セキュリティ、および代替可能性をトラストレスなセットアップで 100% 分散化されたコインで提供できるわけではありません。これらの属性とその重要性は次のとおりです。

## コイン分析

これは、匿名性および/または追跡不可能性を主要な差別化要因として主張する有名な暗号通貨の分析です。ビットコイン自体は、匿名であると主張されていないため、この分析の範囲外です。

このサイトはモネロユーザーによって作られました。私たちがモネロのユーザーではなく、金銭的なプライバシーについて懸念していた時期がありました。私たちはプライベートであると主張するコインを調査し、このページは私たちの調査結果です。それが、私たちがMoneroを選んだ理由です。したがって、私たちが偏見を持っているように見える場合、偏見はありますが、偏見は以下で読んで自分で確認できる事実に基づいていると考えています。

### 概要

ロゴを選択して、そのコインの分析にジャンプします。

### Monero

Monero は当初から 100% オープン ソースであり、誰でもソフトウェアの [ ソース コード ](https://github.com/monero-project/bitmonero) を表示して、バックドアが存在せず、ソフトウェアが安全であることを確認できます。

Monero には [ 査読済みの研究論文 ](https://lab.getmonero.org/) もあり、上記のすべての特性を数学的かつ体系的に検証しています。

### DASH

DASHは[リッチリスト](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html)を持っているので、プライベートコインではありません。コイン アドレスの財務の詳細は、ブロックチェーンを調べている人なら誰でも見ることができます。

> DASH は、暗号的に非公開ではありません。実際、私はデッキに「DASH、LOL」のようなスライドを持っていました。 
> 
> **Gregory Maxwell** 、Bitcoin Core 開発者兼暗号学者、Coinbase への [ プレゼンテーション ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH は、暗号的に非公開ではありません。実際、私はデッキに「DASH、LOL」のようなスライドを持っていました。 

**Gregory Maxwell** 、Bitcoin Core 開発者兼暗号学者、Coinbase への [ プレゼンテーション ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**ピーター・トッド** 、別のビットコイン・コアの開発者であり、暗号学者でもあり、[同様の声明](https://twitter.com/petertoddbtc/status/622022840330682368)を行った。

### Zcash

ジーキャッシュの取引はブロックチェーン上で見ることができます。それらは非表示のトランザクションを有効にしますが、[ トランザクションの 1% 未満が完全にシールドされています ](http://stat.bloxy.info/superset/dashboard/zcash/) 。非表示のトランザクションはオプションであり、デフォルトではないため (言うまでもなく、めったに使用されません)、[ の非表示のトランザクションはブロックチェーン ](http://weuse.cash/2016/06/09/btc-xmr-zcash/) で目立ち、注目を集めます。

> ところで、Zcash は WannaCry のような犯罪者の追跡が可能でありながら、完全にプライベートな & 代替可能にすることができると思います。 
> 
> **Zooko Wilcox** 、Zcash CEO、[ツイート ](https://twitter.com/zooko/status/863202798883577856)

ところで、Zcash は WannaCry のような犯罪者の追跡が可能でありながら、完全にプライベートな & 代替可能にすることができると思います。 

**Zooko Wilcox** 、Zcash CEO、[ツイート ](https://twitter.com/zooko/status/863202798883577856)

ジーキャッシュが「あまりにも追跡可能」である場合、完全にプライベートまたは代替可能になることはありません。 

通常の取引は透過的です。隠しトランザクションは zk-SARKS を使用します。これは、特定の条件下で確かに堅牢なプライバシーを保証します。問題は、これらの条件が満たされているかどうかであり、シールドされた機能を使用しているごく少数の人々を見て、疑問のままです。

Zcash は会社であり、現在 [ は、創設者の報酬 ](https://z.cash/blog/funding.html) として採掘されたすべての ZEC の 20% を取ります。 

Zcash には **Trusted Setup** が必要です。これは、システムが正直にセットアップされたことを信頼する必要があることを意味します。正直に設定しなければ[誰にも知られずに無制限にZECを作成できた](https://blog.okturtles.com/2016/03/the-zcash-catch/)。これにより、ハッカーは金持ちになり、ZEC の価値が下がります。 Trusted Setup が正直に実行されたかどうかを知る方法はありません。私たちは彼らの言葉を信じなければなりません。これは、他のほとんどすべての暗号通貨に対抗する人間の障害点をシステムにもたらします.人間ではなく、暗号通貨の数学と検証可能なソース コードを信頼するだけでよいのです。 [ Microsoft](https://www.gnu.org/proprietary/proprietary-back-doors.en.html)、[ Apple](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/)、さらには政府など、ほぼすべての大規模ソフトウェア企業で見られるように、それらは信頼されるべきではありません。 

[ が Zcash Trusted Setup に ](https://github.com/zcash/mpc/blob/master/README.md) 参加した Bitcoin Core 開発者の Peter Todd は、これを " [ バックドア ](https://twitter.com/petertoddbtc/status/793584540891643906) " と呼んでいます。 

> Zcash は無条件に健全ではなく、現在の技術を使用することはできません...信頼できるセットアップが必要です … 暗号を時間の経過とともにアップグレードするには、[信頼できるセットアップ] の手順をやり直す必要があるため、脆弱性です。 
> 
> Coinbase への [ プレゼンテーションで、Bitcoin Core 開発者および暗号学者である Gregory Maxwell 氏。 ](https://youtu.be/LHPYNZ8i1cU#t=29m30s)

Zcash は無条件に健全ではなく、現在の技術を使用することはできません...信頼できるセットアップが必要です … 暗号を時間の経過とともにアップグレードするには、[信頼できるセットアップ] の手順をやり直す必要があるため、脆弱性です。 

Coinbase への [ プレゼンテーションで、Bitcoin Core 開発者および暗号学者である Gregory Maxwell 氏。 ](https://youtu.be/LHPYNZ8i1cU#t=29m30s)

### Zcoin

**注:** Zcoin は、現在のシグマ方式から、新しい取り組みである Lelantus に依存する新しいプロトコルに移行しています。 Lelantus は段階的に実装される予定です。この記事では、すべての段階が完了し、実装されていると仮定して、予測される実装時間とともに適切な比較を行います。

Zcoin が、Zcash ではなく、将来のプロトコルで判断されるという贅沢を与えられた理由は、Zcoin がアクティブ化の一般的なタイミングを含むロードマップを持っているのに対し、Zcash の「デフォルトのプライバシー」計画は曖昧であり続けているためです。

Zcoin (XZC) はリッチリストがないため非公開になります。デフォルトでは、必須のプライバシーは 2021 年に有効になると予想されます。実装されると、リッチ リストを作成することはできなくなります (ただし、現在 [ には ](https://www.coinexplorer.net/XZC/richlist) があります)。

### Grin

### Bitcoin Mixers

すべてのビットコイン トランザクションはブロックチェーン上で可視化され、[ ビットコイン リッチ リスト ](http://www.bitcoinrichlist.com/top100) があるため、ビットコインは非公開ではありません。ビットコインは [ 仮名](https://bitcoin.org/en/you-need-to-know) であり、匿名ではありません。 

**ビットコイン ミキサー** については、彼らがデータを安全に保つことができ、政府、ハッカー、またはその他の団体によって所有または協力されていないことを信頼する必要があります。 

2017 年 7 月、最大のビットコイン ミキシング サービスである BITMIXER.IO の創設者は、閉鎖を発表し、その理由を次のように述べました。 

BITMIXER.IO、[ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) での閉鎖の発表 (原文で強調)。 

数週間後、さまざまなプライバシー中心のコインを検討した後、彼は次のように述べました。 

> 詳細な調査の結果、MONERO が最高のプライバシー通貨であることを確認しました。したがって、特別なプライバシーが必要なすべての人に MONERO を強くお勧めします。 
> 
> [ フォローアップ投稿 ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378) の BITMIXER.IO。 

詳細な調査の結果、MONERO が最高のプライバシー通貨であることを確認しました。したがって、特別なプライバシーが必要なすべての人に MONERO を強くお勧めします。 

[ フォローアップ投稿 ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378) の BITMIXER.IO。 

すべてのビットコイン トランザクションはブロックチェーン上で可視化されるため、すべてのビットコイン トランザクションを追跡できます。ビットコイン ミキサーはトランザクションを高度に難読化することができるため、誰かがビットコインを追跡することははるかに困難になりますが、不可能ではありません。技術が進歩し、Bitcoin トランザクションの追跡を専門とする企業が普及するにつれて、高度に難読化されたトランザクションは比較的簡単に追跡できるようになります。 

  * [ 法執行機関はビットコイン追跡サービスへの投資を続けています ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: ビットコインは思ったより追跡しやすい ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: 法執行のためにビットコインの追跡を専門とする会社 ](https://www.elliptic.co/)

Google で検索すると、上記のような記事が多数表示されます。また、過去の任意の時点で発生したトランザクションはブロックチェーン上にあり、ミキシング サービスが使用されたとしても追跡される可能性があることを忘れないでください。実際、ミキシング サービスを使用すると、これらのトランザクションに注意が向けられる可能性があります。 

すべてのビットコインが等しく、同じ価値を持つわけではありません。一部のビットコインはブラックリストに登録され、複数のエンティティによってブロックされているため、これらのコインは他のコインよりも価値が低くなります。過去に違法な目的で使用されたビットコインを受け取った場合、違法行為とは関係なくても、ビットコインがブラックリストに登録される可能性があります。または、政府、雇用主、またはその他のエンティティが、資産の凍結または没収と同様に、将来的にビットコインをブラックリストに載せることを決定したとします。あなたにできることは何もないでしょう。ミキサーはビットコインの追跡を難しくするだけなので、このカテゴリは「代替不可」とマークされています。 

<リ> アンドレアス アントノプロス (元ビットコイン コア開発者で、ビットコインやその他の暗号通貨コミュニティで尊敬されている) は、[YouTube ビデオ](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu でビットコインの代替性の問題を認めています。 .be&t=33m9s)。 <リ> [ Bitcointalk.org でのビットコインの代替可能性の問題に関する議論 ](https://bitcointalk.org/index.php?topic=1190707.0)