---
title: "Monero'da Atomik Takaslar Nasıl Çalışacak?"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Merkeziyetsizlik ve gerçekten izinsiz bir sistem arayışında, kripto para birimi alanında merkezi olmayan borsalar ve atomik takaslar kadar çok az şeye imreniliyor. Monero, başlangıcından bu yana atomik takasları uygulamakta zorlandı çünkü gizlilik özellikleri, bir protokol tasarlamaya çalışırken benzersiz sorunlar yaratıyor.

Ama önce yedekleme yapalım. Atom takasları nedir? Atomik takas, farklı blok zincirlerindeki iki farklı kripto para biriminin hiçbir aracı olmadan güvenilmez bir şekilde değiştirilebildiği bir protokoldür. Bu, eğer birisi A kripto parasını B kripto parasıyla değiştirmek isterse, bunu merkezi veya merkezi olmayan bir takas olmadan yapabileceği anlamına gelir. Tahmin edilebileceği gibi bu, ciddi bir araştırma gerektirir ve bunu mümkün kılan tüm teknik ayrıntılar oldukça karmaşık hale gelir. LocalMonero bir kez daha sıradan insanlara yardımcı olmak ve basit bir açıklama yapmak için burada.

Başlamak için, Bitcoin tarafından uygulanan en basit atomik takas biçimini ele alalım. Birisi Bitcoin'i aynı hash time lock sözleşme teknolojisini kullanan başka bir parayla değiştirmek isterse, bunu aşağıdaki şekilde yapabilir. Alice'in Bitcoin'i (BTC) var ama Litecoin'i (LTC) istiyor ve Bob'un LTC'si var ama BTC istiyor. Her birinin istediği parayı alması için atomik takas yapmaya karar verirler. Alice, BTC'sini özel bir adrese göndererek, kendisinin bile erişememesi için fonları kilitleyen komut dosyaları kullanır. Bunu Alice'in BTC'sini kilitli bir kutuya koyması gibi düşünebilirsiniz. Kilitli kutu yapıldığında, bir anahtar alır ve bu anahtarın bir karmasını Bob'a gönderir. Artık Bob'un elinde anahtar yok, yalnızca karma var, dolayısıyla henüz fonlara erişemiyor.

Bob bu karmayı kendi kilitli kutusunu oluşturmak için bir tohum olarak kullanır ve LTC'sini oraya, kendisinin de kilitli olduğu yere gönderir. Alice'in anahtarının karması, Bob'un kilitli kutusunun yapıldığı tohum olarak kullanıldığından, Alice anahtarını Bob'un kilitli kutusundaki LTC'yi almak için kullanabilir. Anahtarı uyuyor! Ancak matematik voodoo büyüsünü kullanarak LTC kilidini açmak için anahtarını kullandığında, anahtarı Bob'a açıklar ve Bob bunu daha sonra kilitli kutusuna koyduğu BTC'yi almak için kullanabilir. Bu şekilde Alice ve Bob hiçbir aracı olmadan varlıklarını başarıyla takas ettiler.

Fakat küçük bir sorun var. Ya Alice kilitli kutusuna para gönderirse ve Bob artık takas yapmak istemediğine karar verirse? Artık Alice kilitlediği BTC'sine erişemediğinden ve Bob işlemin kendine düşen kısmını tamamlayamayacağından Alice parasını sonsuza kadar kaybeder. Neyse ki, Bitcoin'in geri ödeme işlemleri adı verilen küçük bir teknolojisi var ve bu nedenle bir süre sonra, eğer BTC Bob tarafından talep edilmezse, komut dosyalarında BTC'nin otomatik olarak Alice'e geri döneceği bir arıza güvenliği yerleşik olarak bulunur. Bu, Monero'nun atomik takas uygulaması için birincil hız artışıydı. Monero'nun [halka imza gizlilik teknolojisi](/knowledge/ring-signatures) nedeniyle, bir işlemin göndereni her zaman belirsizdir. Protokol, işlemin nereden geldiğini bilmese bile nasıl geri ödeme işlemi yapabilir?

2017'de küçük bir grup araştırmacı, Monero'da atomik takasların işe yarayacağı farklı bir yöntemin ana hatlarını çizdi. Birkaç yıl süren geliştirmelerden sonra araştırmacılar, Monero'nun geri ödeme işlemleri olmadan bile Bitcoin ile atomik takaslar yapabileceği bir süreci tamamladılar.

Bu seviyedeki teknik karmaşıklığa sahip pek çok şeyde olduğu gibi, açıklamamız fikri aktarmak için bazı şeyleri fazlasıyla basitleştirecek, ancak yine de bu sürecin işleyeceği mekanizmalar hakkında sağlam bir fikir verecektir.

Hem Alice (XMR'ye sahip olan ve BTC isteyen) hem de Bob (BTC'ye sahip olan ve XMR isteyen) atomik takası destekleyen bir program indirip çalıştırmalıdır. Bu, cüzdanlara, merkezi olmayan borsalara veya özel, spesifik programlara uygulanabilir, ancak yazılımın atomik takas protokolünü çalıştırması gerekir. İlk adımda Alice ve Bob'un müşterileri birbirine bağlanır ve birçok paylaşılan sır ve anahtar oluşturur. Bu adımda, anahtarın bir yarısı Alice'e, diğer yarısı da Bob'a sahip olacak şekilde yeni bir Monero adresi oluşturulur. Henüz orada Monero yok, dolayısıyla harcayacak hiçbir şey yok. Bu adresle ilgili dikkat edilmesi gereken son şey, her ikisinin de bu cüzdanın görüntüleme anahtarına sahip olmasıdır, böylece her ikisi de Monero'nun gelip gelmeyeceğini veya ne zaman geleceğini görmek için içeriye göz atabilirler.

İkinci adımda Bob, BTC'sini daha önce tartıştığımız Bitcoin atomik takas protokolüne benzer şekilde özel bir adrese gönderir. Alice, BTC'nin blok zincirindeki bu adrese ulaştığını gördükten sonra Monero'sunu kendisinin ve Bob'un anahtarın yarısının bulunduğu Monero adresine gönderir. Bob, görüntüleme anahtarına da sahip olduğundan Monero'nun geldiğini doğrulayabilir ve Monero'nun güvenli bir şekilde cüzdanda olduğunu görünce Alice'e Bitcoin'i çekmesine olanak sağlayacak bir anahtar parçası gönderir. Diğer protokole benzer şekilde, Bitcoin'i talep etme süreci Monero anahtarının yarısını Bob'a açıklar. Artık Bob'un her iki yarısı da var, dolayısıyla Monero'yu talep edebilir, oysa Alice yalnızca kendi yarısına sahip olduğundan Monero'yu ondan önce almaya çalışamaz.

Tüm bunlara baktığınızda ve Monero'nun geri ödeme işlemleri sorununu nasıl çözebildiği konusunda hala kafanız karıştıysa, cevap oldukça basittir. Monero'nun kendisi iade işlemlerine sahip olmadığından, okuyucu ilk önce Bitcoin'in (geri ödeme işlemleri olan) gönderildiğini ve Monero'nun yalnızca blockchain üzerinde olduğu doğrulandıktan sonra gönderildiğini fark etmelidir. Bu, Monero'nun Bitcoin'in geri ödeme işlemlerinde komut dosyası oluşturma yeteneğinden yararlanmasına ve bu yeteneklere sahip olmasına gerek kalmadan bunlardan yararlanmasına olanak tanır.

Atom takası artık tamamlandı, ancak buradan itibaren Bob'un yeni talep ettiği XMR'si için birkaç seçeneği var. Bu Monero cüzdanını olduğu gibi kullanabilir veya XMR'yi halihazırda sahip olduğu başka bir cüzdana taşıyabilir. Bob büyük olasılıkla Monero'yu başka bir cüzdana taşıyacaktır çünkü Alice hâlâ görüntüleme anahtarına sahiptir ve içini görebilir.

Bu protokolün güzelliği, hâlâ oldukça yeni olması ve optimizasyon için bolca yer bulunmasıdır. Mimarisi de oldukça esnek olduğundan, diğer cüzdanlarda veya merkezi olmayan borsalarda uygulanması basit olmalı ve mevcut mimarilerine temiz bir şekilde uymalıdır.

daha fazla okuma

  * [Monero döngüsel ekonomileri benzersiz bir şekilde nasıl mümkün kılıyor?](/knowledge/monero-circular-economies)/

  * [Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı](/knowledge/ring-signatures-vs-coinjoin)/

  * [Neden (ve nasıl!) kendi anahtarlarınızı tutmalısınız?](/knowledge/hold-your-keys)/

  * [Monero'ya geri katkıda bulunmak](/knowledge/contributing-to-monero)/

  * [Uzak düğümler Monero'nun gizliliğini nasıl etkiler?](/knowledge/remote-nodes-privacy)/

  * [Monero ağı yükseltmek için hard fork'ları nasıl kullanıyor?](/knowledge/network-upgrades)/

  * [Etiketleri görüntüle: Bir bayt, Monero cüzdan senkronizasyon sürelerini nasıl %40'tan fazla azaltır?](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool ve Monero Madenciliğinin Merkezi Olmamasındaki Rolü](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Monero İçin Ne Yapacak?](/knowledge/seraphis-for-monero)/

  * [Bitcoin'i Monero'ya Dönüştürmek Doğrudan Monero Satın Almak Kadar Özel mi?](/knowledge/most-private-way-to-buy-monero)/

  * [Monero Neden Zcash'ten Farklı Olarak Güvenilir Bir Kurulum Kullanıyor?](/knowledge/monero-trustless-setup)/

  * [Monero Neden Bitcoin'den Daha İyi Bir Değer Deposu?](/knowledge/monero-better-store-of-value)/

  * [Monero, Bitcoin'in Ağ Etkilerinin Üstesinden Nasıl Gelebilir?](/knowledge/network-effect)/

  * [Monero Neden En Eleştirel Düşünme Topluluğuna Sahip?](/knowledge/critical-thinking)/

  * [Monero Kullanırken Dikkat Edilmesi Gereken Dolandırıcılıklar](/knowledge/monero-scams)/

  * [Konu Ağ Oluşturmaya Geldiğinde Her Monero Kullanıcısının Bilmesi Gerekenler](/knowledge/monero-networking)/

  * [RingCT Monero İşlem Tutarlarını Nasıl Gizliyor?](/knowledge/monero-ringct)/

  * [Monero Gizli Adresleri Kimliğinizi Nasıl Korur?](/knowledge/monero-stealth-addresses)/

  * [Monero Alt Adresleri Kimlik Bağlantısını Nasıl Önler?](/knowledge/monero-subaddresses)/

  * [Monero Çıktılarının Açıklaması](/knowledge/monero-outputs)/

  * [Yeni Başlayanlar İçin Monero En İyi Uygulamaları](/knowledge/monero-best-practices)/

  * [Halka İmzaları Monero'nun Çıktılarını Nasıl Gizliyor?](/knowledge/ring-signatures)/

  * [Monero, Bitcoin'i Saldıran Blok Boyutu Sorununu Nasıl Çözdü?](/knowledge/dynamic-block-size)/

  * [CLSAG Monero'nun Verimliliğini Nasıl Artıracak?](/knowledge/what-is-clsag)/

  * [Monero'nun Neden Kuyruk Emisyonu Var?](/knowledge/monero-tail-emission)/

  * [Monero'nun Kısa Tarihi](/knowledge/monero-history)/

  * [Wired Magazine Monero Konusunda Yanılıyor, İşte Nedeni](/knowledge/wired-article-debunked)/

  * [En Önemli 15 Monero Efsanesi ve Endişesi Çürütüldü](/knowledge/monero-myths-debunked)/

  * [Dandelion++ Monero'nun İşlem Kaynaklarını Nasıl Gizli Tutuyor?](/knowledge/monero-dandelion)/

  * [Monero Neden Açık Kaynaklı ve Merkezi Değildir?](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Monero Madenciliği: RandomX'i Bu Kadar Özel Kılan Nedir?](/knowledge/monero-mining-randomx)/

  * [Monero Neden Dash, Zcash, Zcoin (Lelantus ile Bile), Grin ve Wasabi Gibi Bitcoin Karıştırıcılarından Daha İyidir (Mayıs 2020'de Güncellendi)](/knowledge/why-monero-is-better)/

daha fazla okuma