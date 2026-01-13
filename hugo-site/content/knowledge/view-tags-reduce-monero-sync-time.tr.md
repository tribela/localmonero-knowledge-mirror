---
title: "Etiketleri görüntüle: Bir bayt, Monero cüzdan senkronizasyon sürelerini nasıl %40'tan fazla azaltır?"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero'yu günlük olarak kullanmayla ilgili en yaygın şikayetlerden biri, Monero'yu göndermeden önce bir cüzdanı senkronize etmenin zaman almasıdır. Neyse ki, Monero topluluğundaki geliştiriciler ve araştırmacılar, herhangi bir ek blockchain şişkinliği, ücret vb. olmadan cüzdanınızı senkronize etmek için harcadığınız süreyi %40'ın üzerinde azaltmanın harika bir yolunu buldular.

Her işlemin verilerine bir baytlık ek olan "etiketleri görüntüle"yi girin; bir sonraki ağ yükseltmesinde Monero'ya gelecek!

## Monero'nun cüzdan senkronizasyonu neden Bitcoin'inkinden daha yavaş?

Etiketleri görüntüleme gibi bir çözüme olan ihtiyacı daha iyi anlamak için yanıtlamamız gereken ilk sorulardan biri, Monero'nun cüzdan senkronizasyonunun neden Bitcoin gibi kripto para birimlerinden daha yavaş olduğudur.

Bitcoin'de, tüm işlemler özel olmadığından ve harcanan paraları, tutarları ve zincirdeki adresleri ortaya çıkardığından, Bitcoin cüzdanları, belirli bir cüzdan için harcanmamış işlem çıktılarını (UTXO'lar) veya kullanılmış adresleri kolayca arayabilir , hangi paraların cüzdanınıza ait olduğunu ve harcanabileceğini bulmak için blok zincirini yalnızca bu adreslere ait UTXO'lar için hızlı bir şekilde tarar.

Ancak Monero'da tüm işlemler, göndereni, alıcıyı ve her işlemde yer alan tutarları gizleyerek kullanıcının gizliliğini korur. Bu gizlilik, ağ kullanıcılarının korunması açısından hayati öneme sahip olmakla birlikte, aynı zamanda daha yavaş cüzdan senkronizasyonunu da beraberinde getirir. Monero'da cüzdanınızın, ağda bulunan her işlem çıkışını (TXO) cüzdanınızın özel anahtarlarıyla karşılaştırması gerekir.

Tüm tutarlar, adresler ve harcandığı bilinen çıktılar (veya madeni paralar) Monero'da zincir üzerinde gizlendiğinden, bu karşılaştırma bir çıktının gerçekten size ait olduğunu doğrulamak için birçok karmaşık matematik ve kriptografi içerir.

## Görünüm etiketleri nedir?

Monero cüzdanları için senkronizasyon süresini azaltmaya yardımcı olmanın bir yolu olarak, [UkoeHB adlı bir araştırmacı yeni bir yaklaşım geliştirdi](https://github.com/monero-project/research-lab/issues/73) \- yalnızca bilinen bir paylaşılan sırrı kullanarak her işleme 1 baytlık bir "etiket" ekleyin bu işlemin göndericisine ve alıcısına.

Bu paylaşılan sır, gönderen tarafından, alıcı tarafından kendisine sağlanan adres kullanılarak oluşturulur ve gönderen ile alıcının herhangi bir aktif işbirliğini gerektirmez. Bu paylaşılan sırrın ilk baytı (veya karakteri), daha sonra Monero ağında yayınlanırken işlemin verilerine eklenir.

Bu işlemdeki katılımcılardan biri daha sonra cüzdanını Monero blok zinciriyle senkronize etmek istediğinde, ağdaki her bir TXO için tüm karmaşık matematik ve kriptografi işlemlerini gerçekleştirmek yerine, cüzdan artık yalnızca her işlemde bu 1 baytlık alanı kullanın ve ancak bundan sonra bu etikete sahip işlemlerde zaman alıcı doğrulamayı gerçekleştirin - kesin olarak söylemek gerekirse ağdaki 1/256 TXO!

Bu etiket, işlemle ilgili herhangi bir bilgiyi dışarıdaki izleyicilere göstermez, işlem boyutlarına yalnızca 1 bayt (göz ardı edilebilir bir miktar) ekler ve yine de karmaşık doğrulamaları azaltarak senkronizasyon sürelerini %40'ın üzerinde azaltmamıza olanak tanır gerekli!

## Etiketleri görüntüle: basitleştirilmiş bir örnek

Bir odada 4.096 kutunuzun olduğunu ve bunlardan yalnızca 5'inin size ait olduğunu hayal edin. Kutuların hepsi dışarıdan tamamen ayırt edilemez ve bir kutunun size uygun olup olmadığını anlamanın tek yolu, onu açmak ve size ait olduğundan emin olmak için içine yazılmış, zaman alan bir matematik problemini çözmektir.

Şimdi, size bu 5 kutuyu gönderen kişinin adresinizi kullanarak özel bir kod oluşturmasına karar verdiğinizi ve ardından oluşturulan kodun yalnızca ilk karakterini size gönderilen her kutunun dışına koymaya karar verdiğinizi hayal edin. Herkes kendi kutuları için aynı şeyi yapıyor (tüm kutuların hala ayırt edilemez olduğundan emin olmak için), ancak artık kutunun dışındaki tek karakterli koda bakabilir ve yalnızca üzerinde o karakterin bulunduğu kutuları açabilirsiniz.[ X753X] 

Diğer kutular kodunuzla eşleşirken, bazıları size ait olmasa da, açmanız ve bir matematik problemini çözmeniz gereken kutu sayısı artık 4.096 yerine yalnızca 16 (1/256 kutu!). 

Şimdi o 16 kutuyu açıyorsunuz, matematik problemlerini çözüyorsunuz ve aslında size ait olan 5 kutuyu o gruptan tutuyorsunuz!

Diğer kutular kodunuzla eşleşirken, bazıları size ait olmasa da, açmanız ve bir matematik problemini çözmeniz gereken kutu sayısı artık 4.096 yerine yalnızca 16 (1/256 kutu!). 

Şimdi o 16 kutuyu açıyorsunuz, matematik problemlerini çözüyorsunuz ve aslında size ait olan 5 kutuyu o gruptan tutuyorsunuz!

## Monero'da görüntüleme etiketleri ne zaman kullanıma sunulacak?

Görünüm etiketleri, şu anda [yaklaşan ağ yükseltmesine](https://github.com/monero-project/meta/issues/630) dahil edilmesi planlanan özelliklerden biridir ve bu baharda piyasaya sürülmesi planlanmaktadır. Topluluk [görünüm etiketlerinin geliştirilmesini ve uygulanmasını teşvik etmek için 23,3XMR'yi](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) artırdı (bu yazının yazıldığı sırada) ve sonuç olarak görünüm etiketlerini Monero kod tabanına dahil etmeye yönelik çalışmaların büyük çoğunluğu zaten yürütüldü j-berman tarafından hakemler ve araştırmacıların işbirliğiyle tamamlandı.

Görüntüleme etiketleri ağ tarafından zorunlu kılındıktan sonra, ağ yükseltmesinden sonra gönderilen tüm işlemler, büyük ölçüde iyileştirilmiş cüzdan senkronizasyon süresinden yararlanacaktır. Görünüm etiketlerini kullanmaya başlamak için özel bir şey yapmanıza gerek kalmayacak; Monero için favori cüzdanınız, ağ yükseltmesinden sonra otomatik olarak bunları kullanmaya başlayacak!

## Daha fazlasını nasıl öğrenebilirim?

Bu, görünüm etiketleri konusunda merakınızı artırdıysa, konuyu derinlemesine ele alan bazı ek bağlantılar için aşağıya göz atın:

  * [Çıkış başına 1 bayt 'görüntüleme etiketi' ile tarama sürelerini azaltın](https://github.com/monero-project/research-lab/issues/73)
  * [Cüzdan tarama süresini azaltmak için çıkışlara görünüm etiketleri ekleyin](https://github.com/monero-project/monero/pull/8061)

daha fazla okuma

  * [Monero döngüsel ekonomileri benzersiz bir şekilde nasıl mümkün kılıyor?](/knowledge/monero-circular-economies/)

  * [Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı](/knowledge/ring-signatures-vs-coinjoin/)

  * [Neden (ve nasıl!) kendi anahtarlarınızı tutmalısınız?](/knowledge/hold-your-keys/)

  * [Monero'ya geri katkıda bulunmak](/knowledge/contributing-to-monero/)

  * [Uzak düğümler Monero'nun gizliliğini nasıl etkiler?](/knowledge/remote-nodes-privacy/)

  * [Monero ağı yükseltmek için hard fork'ları nasıl kullanıyor?](/knowledge/network-upgrades/)

  * [P2Pool ve Monero Madenciliğinin Merkezi Olmamasındaki Rolü](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Monero İçin Ne Yapacak?](/knowledge/seraphis-for-monero/)

  * [Bitcoin'i Monero'ya Dönüştürmek Doğrudan Monero Satın Almak Kadar Özel mi?](/knowledge/most-private-way-to-buy-monero/)

  * [Monero Neden Zcash'ten Farklı Olarak Güvenilir Bir Kurulum Kullanıyor?](/knowledge/monero-trustless-setup/)

  * [Monero Neden Bitcoin'den Daha İyi Bir Değer Deposu?](/knowledge/monero-better-store-of-value/)

  * [Monero, Bitcoin'in Ağ Etkilerinin Üstesinden Nasıl Gelebilir?](/knowledge/network-effect/)

  * [Monero Neden En Eleştirel Düşünme Topluluğuna Sahip?](/knowledge/critical-thinking/)

  * [Monero Kullanırken Dikkat Edilmesi Gereken Dolandırıcılıklar](/knowledge/monero-scams/)

  * [Monero'da Atomik Takaslar Nasıl Çalışacak?](/knowledge/monero-atomic-swaps/)

  * [Konu Ağ Oluşturmaya Geldiğinde Her Monero Kullanıcısının Bilmesi Gerekenler](/knowledge/monero-networking/)

  * [RingCT Monero İşlem Tutarlarını Nasıl Gizliyor?](/knowledge/monero-ringct/)

  * [Monero Gizli Adresleri Kimliğinizi Nasıl Korur?](/knowledge/monero-stealth-addresses/)

  * [Monero Alt Adresleri Kimlik Bağlantısını Nasıl Önler?](/knowledge/monero-subaddresses/)

  * [Monero Çıktılarının Açıklaması](/knowledge/monero-outputs/)

  * [Yeni Başlayanlar İçin Monero En İyi Uygulamaları](/knowledge/monero-best-practices/)

  * [Halka İmzaları Monero'nun Çıktılarını Nasıl Gizliyor?](/knowledge/ring-signatures/)

  * [Monero, Bitcoin'i Saldıran Blok Boyutu Sorununu Nasıl Çözdü?](/knowledge/dynamic-block-size/)

  * [CLSAG Monero'nun Verimliliğini Nasıl Artıracak?](/knowledge/what-is-clsag/)

  * [Monero'nun Neden Kuyruk Emisyonu Var?](/knowledge/monero-tail-emission/)

  * [Monero'nun Kısa Tarihi](/knowledge/monero-history/)

  * [Wired Magazine Monero Konusunda Yanılıyor, İşte Nedeni](/knowledge/wired-article-debunked/)

  * [En Önemli 15 Monero Efsanesi ve Endişesi Çürütüldü](/knowledge/monero-myths-debunked/)

  * [Dandelion++ Monero'nun İşlem Kaynaklarını Nasıl Gizli Tutuyor?](/knowledge/monero-dandelion/)

  * [Monero Neden Açık Kaynaklı ve Merkezi Değildir?](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Madenciliği: RandomX'i Bu Kadar Özel Kılan Nedir?](/knowledge/monero-mining-randomx/)

  * [Monero Neden Dash, Zcash, Zcoin (Lelantus ile Bile), Grin ve Wasabi Gibi Bitcoin Karıştırıcılarından Daha İyidir (Mayıs 2020'de Güncellendi)](/knowledge/why-monero-is-better/)