---
title: "Monero Alt Adresleri Kimlik Bağlantısını Nasıl Önler?"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero her zaman zor gizlilik sorunlarını çözmek için yenilikçi yollar bulmuştur. Çoğu zaman bu yenilikler başka yeniliklere yol açar ve bazen ortaya çıkan bu teknolojiler daha önce düşünülmemiş kullanım durumları için bile kullanılabilir. Bu hiçbir yerde Monero'nun alt adres teknolojisinden daha fazla örneklenmemiştir.

Varsayımsal bir gizlilik sorununu düşünün; burada görünüşte ilgisiz kişilerden gelen birden fazla platformda tek bir adresin kullanılması, söz konusu kişilerin bağlantısına ve anonimleştirilmesine yol açabilir. Basitçe söylemek gerekirse, Billy Joe Bob adında bir kişiyseniz ve Bitcoin karşılığında elma satıyorsanız, müşterilerin size ödeme yapması için Bitcoin adresinizi halka açık bir yerde yayınlayabilirsiniz. Diyelim ki adres alfanümerik 7XybV3 dizisiyle başlıyor... Ancak herhangi birinin Bitcoin bakiyenizi kontrol edip ne kadar sattığınızı görebilmesi gibi bariz gizlilik riskini bir kenara bırakırsak, gizlilik riski hakkında pek konuşulmayan bir saniye daha var. Diyelim ki aynı zamanda l33tz0r adıyla çalışan bir yeraltı hacker'ısınız. Hiçbir şeyden haberi olmayan halka hükümet yolsuzluğu hakkında bilgi vererek ihbarda bulunuyorsunuz ve kimliğinizi gizli tutmanız zorunludur. Çalışmanız için Bitcoin bağışlarını kabul ediyorsunuz ve adresi halka açık bir forumda yayınlıyorsunuz. Apple müşterilerinizden para kabul ettiğiniz adresle aynıdır. 7XybV3... bir.

Basit ama yıkıcı bir anonimleştirme saldırısı, Bitcoin adresinizi aramak için bir internet arama motoru kullanmak olacaktır. 7XybV3'ün adresini motora koymak iki farklı sonucu ortaya çıkarıyor. Elma işi ve l33tz0r. Bu, iki kimliği birbirine bağlamak ve l33tz0r'yi anonimlikten çıkarmak için yeterlidir; bu da güçlerin potansiyel olarak korkutucu sonuçlarıyla sonuçlanır.

Bu saldırının Monero ile AYRICA mümkün olduğunu unutmamak önemlidir. Monero zincirdeki verilerin çoğunu gizlese de bu saldırıda hiçbir veri kullanılmaz. Yalnızca ödeme alabilmek için paylaşılması gereken adresi kullanır. İsimsiz bağışlar durumunda kamuya açık olarak. Bu, Monero kullanıcılarının farkında olmadan mahremiyetlerine zarar vermelerinin olası bir yoludur ve aynı zamanda Monero'nun mahremiyetin korunması açısından en üst seviyede olmasına rağmen kurşun geçirmez olmadığının da bir örneğidir.

Bu sorunu aşmanın genel yolu birden fazla cüzdan sahibi olmaktı. Her kimlik (veya kullanım durumu) için farklı adreslerin yayınlanması nedeniyle bunlar birbirine bağlanamaz. Ancak bu gizlilik yalnızca kullanıcının bunları asla karıştırmaması durumunda geçerlidir. Yanlışlıkla yanlış adresi göndermek aynı bağlantı etkilerine sahip olacaktır. Ayrıca, her adresin çekirdeği güvenli bir şekilde saklanmalı ve yapılan her yeni cüzdanla gerekli bilgi güvenliği çalışması artırılmalıdır.

Monero'nun çözümü alt adreslerdi. Ana adresin altında, onu bir tür tohum olarak kullanarak kesinlikle çok sayıda adres oluşturma yeteneği. Oluşturulan her alt adres Monero'yu kabul edebilir ve hepsi aynı cüzdana gider. Bu yöntemi kullanarak, bilgi güvenliğinin çalışmasını minimumda tutarken, tek bir adres altında çalıştırılabilecek kimliklerin sayısı çok fazladır. Bu adresler aynı zamanda matematiksel olarak da ilişkilendirilebilir değildir, dolayısıyla kullanıcı dünyaya bağlantılarını bağırmadıkça, dışarıdan bir gözlemci bunları bağlamakta büyük zorluk çekecektir.

Ancak alt adreslerden başka bir ilginç kullanım durumu ortaya çıktı; evrensel olarak nefret edilen ödeme kimliklerinin yerine geçme seçeneği olarak.

Ödeme kimlikleri, satıcıların hangi müşterinin hangi ödemeyi gönderdiğini belirlemesinin bir yoluydu. Monero bilgileri zincir üzerinde gizlendiğinden, işlemin alıcısı işlemin hangi adresten gönderildiğini göremez. Bu, benzer fiyatlı ürünler ve birden fazla sipariş olması durumunda kimin neyi gönderdiğini tespit etmenin imkansız hale gelebileceği anlamına gelir. Ödeme kimlikleri, satıcı tarafından oluşturulan ve müşteriye verilen benzersiz, rastgele bir dizedir. Müşteri, işlemi gönderirken bunu ayrı bir alan olarak ekler. Bu rastgele dizi, işlemin bir parçası olarak blok zincirine yerleştirilir ve bu şekilde tüccar, gelen işlemleri tanımlayabilir ve sıralayabilir.

Bu yöntem birkaç açıdan kusurluydu. İlk olarak, zincir üstü verilerin tekdüzeliğini azaltır. Ek, benzersiz meta veriler, bazı işlemlerin diğerlerinden farklı olmasını sağlayarak buluşsal analize olanak tanır. Bu, özellikle bu meta verilerin herkes için zorunlu olarak zorunlu kılınmadığı durumlarda geçerlidir. Ancak bunun herkes için zorunlu hale getirilmesi, blockchain'e gereksiz alan eklenmesine yol açacaktı ve bu da takip edilmedi. Ayrıca, bir ödeme kimliğinin herhangi bir nedenle yeniden kullanılması halinde, iki işlemi bağlantılı olarak bağlamak önemsiz olacaktır. Bu genellikle döviz mevduatlarında meydana geliyordu ve herkes, hem bir borsadaki mevduat hem de belirli bir kişiden gelen işlemleri kolayca bağlayabilirdi.

İkinci olarak, UX perspektifinden bakıldığında, ödeme kimlikleri, diğer kripto paralardan gelen kripto para birimi kullanıcılarının alışık olmadığı ikinci bir adım oluşturur ve unutulmaları durumunda, bu işlemleri başka yollarla tanımlamak zorunda olan tüccar için büyük bir baş ağrısına neden olur. . Bu genellikle ödeme kimliğini girmeyi unutan her müşteriyle doğrudan konuşarak ve tutar, gönderilme tarihi ve işlem kimliğinin birleşimi gibi yalnızca kendilerinin bilebileceği diğer tanımlayıcı bilgileri doğrulayarak yapılıyordu.

Bu ekstra adım birçok kişi tarafından atlandı ve bazı borsaların, ödeme kimliğini unutmaları nedeniyle paralarının manuel olarak alınması gerektiğinde müşterilerden para talep etmeye başladığı noktaya geldi. Diğerleri dişlerini gıcırdatarak ekstra destek masraflarını yediler ama kimse bundan memnun değildi.

Bunun tek bir çözümü vardı; adresi ve ödeme kimliğini tek bir dizede birleştiren entegre adresler, böylece unutulması mümkün değildi, ancak satıcıların dahil edilmesinden elde edecekleri faydalara rağmen benimseme oldukça zayıftı. 

İlginç bir olay sonucu, günü kurtarmak için alt adresler devreye girdi. Ana adres başına büyük miktarlarda alt adres oluşturma ve hangi işlemlerin hangi alt adreslere geldiğini belirleme yeteneği, tüccarların yeni nesil Monero teknolojisini benimserken ödeme kimliklerinden zarif bir şekilde kurtulmalarına olanak sağladı. O zamandan bu yana çoğu borsa ve ticari araç, işlem tanımlamanın birincil yolu olarak alt adreslere geçti.

Bir gizlilik sorununa çözüm olarak başlayan şey, çok daha fazlasına dönüştü ve hem satıcılar hem de müşteriler için büyük bir kullanıcı deneyimi sorununu çözdü. Yenilik daha fazla yeniliği doğurur ve bu da çoğu zaman kartopu etkisi yaparak herkes için beklenmedik kazançlara dönüşebilir. Monero bunu defalarca gördü ve blockchain'de mümkün olan şeyleri yenilemek için büyük çaba harcıyor. Birlikte başka hangi şeylerin kilidini açabileceğimizi kim bilebilir?

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

  * [Monero'da Atomik Takaslar Nasıl Çalışacak?](/knowledge/monero-atomic-swaps)/

  * [Konu Ağ Oluşturmaya Geldiğinde Her Monero Kullanıcısının Bilmesi Gerekenler](/knowledge/monero-networking)/

  * [RingCT Monero İşlem Tutarlarını Nasıl Gizliyor?](/knowledge/monero-ringct)/

  * [Monero Gizli Adresleri Kimliğinizi Nasıl Korur?](/knowledge/monero-stealth-addresses)/

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