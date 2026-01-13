---
title: "Monero Çıktılarının Açıklaması"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, diğer kripto para birimleri gibi, fonları muhasebeleştirmek için çıktıları kullanır. Kripto konusunda bilgili birçok kullanıcı muhtemelen bu terimi daha önce duymuştur, ancak herkes bunların ne anlama geldiğini ve nasıl çalıştığını anlamıyor. [halka imzaları makalemizde](/knowledge/ring-signatures) incelendiği gibi, çıktılar, işlem yapan taraflar arasında blok zincirinde değiştirilen gerçek birimdir. Dolar banknotuna benzer ancak tutar sabit bir para biriminde değildir.

Bir iş için 16 dolar alırsanız, bir dolarlık banknot, beş dolarlık bir banknot ve on dolarlık bir banknot alabilirsiniz. 16 dolarınız var ama aynı zamanda cüzdanınızda üç farklı banknot var. Birisine 6 dolar ödemek istiyorsanız, 5 ve 1'lik banknotu kullanabilirsiniz, ancak birine 8 dolar ödemek istiyorsanız yalnızca 10 doları kullanabilir ve para üstü olarak 2 doları geri alabilirsiniz. Son olarak, eğer birine 14$ ödemek istiyorsanız, üç banknotun hepsini kullanmak zorunda kalacaksınız ve 2$'ı da para üstü olarak geri alacaksınız, ancak bir an için, üç banknotu da teslim ettiğinizde, parayı alana kadar cüzdanınızda hiç para kalmaz. geri değiştirin.

Monero benzer şekilde çalışır. Bir mağaza işlettiğinizi ve üç farklı üründen üç satış yaptığınızı varsayalım. Toplam 9 XMR karşılığında 1,5 XMR, 2,25 XMR ve 5,25 XMR alabilirsiniz, ancak cüzdanınızda daha önce belirtilen değerlerden üç farklı çıktı da bulunur. Tıpkı dolarlarda olduğu gibi birine 3 XMR ödemek isteyebilirsiniz. Yalnızca 5,25 XMR çıkışını kullanabilir ve değişim olarak 2,25 XMR geri alabilirsiniz veya 1,5 ve 2,25 XMR çıkışlarını birleştirip değişim olarak 0,75 XMR geri alabilirsiniz.

Ancak, işlemi gönderdiğiniz anda, kullandığınız çıkışlar "kilitli" duruma getirilir; bu, siz değişikliği geri alana kadar bunlara erişilemeyeceği anlamına gelir. Protokol, 10 onaydan sonra veya yaklaşık 20 dakika sonra fonların kilidini açar (yani parayı size geri verir). Tıpkı cüzdanınızdan dolar banknotlarını teslim ettiğinizde, kasadan para üstünü alana kadar parayı tekrar kullanamayacağınız gibi, para üstünü geri alana kadar da Monero'nuza erişemezsiniz.

Birine 3 XMR gönderme örneğine geri dönelim ve siz 5,25 XMR çıkışını kullanıyorsunuz. Artık 1,75 XMR'nin para üstü olarak geri dönmesini beklerken onu kullanamazsınız. Bu 1,75 XMR'ye erişemezsiniz. Ancak bunlar harcanmadığı için yine de 1,5 XMR ve 2,25 XMR çıkışlarını kullanabilirsiniz. Dolar örneğine dönecek olursak, eğer birine önceki örnekte olduğu gibi 8$ ödediyseniz, bozuk para olarak geri almayı beklediğiniz 2$'ı size verilene kadar kullanamazsınız, ancak bu örnekte hala elinizde bir dolar var. Cüzdanınızda kullanılmayan 10 dolarlık banknot. Bu, değişikliği beklerken istediğiniz her şeyi satın almak için hala kullanılabilir. Monero için de aynısı.

Bu genellikle yeni Monero kullanıcıları için bir kafa karışıklığı noktasıdır. Çoğu zaman, bir kullanıcının cüzdanında bir borsadan veya bir arkadaşından alınan tek bir çıktı bulunabilir. Bu çıktının 20 XMR olduğunu varsayalım. Cüzdanlarında başka çıktıları yok. Şimdi en sevdikleri iki hayır kurumuna bağışta bulunmak istiyorlar. İlk hayır kurumuna 5 XMR gönderiyorlar ve sonra kafaları karışıyor çünkü ellerinde 15 XMR kalması gerekirken bir sonraki bağışı hemen ikinci hayır kurumuna gönderemiyorlar. Tahmin edebileceğiniz gibi bunun nedeni 15 XMR'nin kilitli olmasıdır. Para üstü olarak iade edilene kadar (10 onay veya yaklaşık 20 dakika) harcanamaz. Fonlarının kilidi açıldıktan sonra ikinci bağışlarını gönderebilecekler.

Meseleyi tekrarlamak gerekirse, bunun yerine iki adet 10 XMR çıkışı veya benzeri gibi birden fazla çıkışa sahip olsalardı bu sorunu yaşamazlardı. Her iki bağışı da arka arkaya gönderebilecekler çünkü ilk bağışta 10 XMR çıktısından biri kullanılacak (ve değişim olarak 5 XMR'yi geri almak için 10 onay beklenecek) ve ikinci bağışta diğer 10 XMR kullanılacaktı. çıktı.

Bazı kripto para cüzdanlarında 'çıktı yönetimi' adı verilen bir özellik bulunur; bu özellik, kullanıcıya o anda hangi çıktılara sahip olduğunu (toplam toplamlarına ek olarak) gösterir ve harcama yaparken hangilerini kullanmak istediklerini seçmelerine olanak tanır. onların kripto para birimi.

Şu an itibariyle Monero GUI, kullanıcılar için çıktı seçimini otomatik olarak yapıyor; çünkü kullanıcıların kendi çıktılarını seçmesi genellikle kafa karışıklığına yol açıyor veya bazı durumlarda gizliliğe zarar veriyor. Ancak yeni Feather cüzdan projesi gibi bu çıktı yönetimi özelliklerini içerecek olan cüzdanlar yapım aşamasındadır.

Gönderme kısmı hakkında çok konuştuk ama alıcı tarafta büyüleyici bir şey oluyor. Birine 3 XMR gönderme örneğimize dönersek ve işlemde 1,5 XMR ve 2,25 XMR çıkışlarınızı kullanırsak (değişimde 0,75 XMR beklerken), alıcı 1,5 XMR ve 2,25 XMR'lik iki çıkışı ALMAZ. Bunun yerine ONE 3 XMR çıkışı alırlar.

Arka planda, protokol harcama için kullanılan tüm çıktıları birleştirir ve alıcıya ödenen tutarın bir çıktısını verir ve bir değişiklik çıktısını göndericiye geri gönderir. Böylece gönderen, işlemi göndermek için iki, üç veya on çıktı kullanmış olmasına bakılmaksızın değişiklik olarak bir çıktıyı da geri alacaktır.

Bunun, çıktılar ve protokolün dahili muhasebesinin nasıl çalıştığına ilişkin bazı kafa karışıklıklarının yanı sıra, kilitli fonlarla karşılaştığında yaygın kullanıcıların karşılaştığı kafa karışıklığı sorununu giderdiğini umuyoruz. Başka bir makalede, gelecekteki işlemleri göndermeden önce kilidi açılmış fonları beklemek zorunda kalma olasılığını en aza indirecek şekilde çıktılarınızı yönetmeyi inceleyeceğiz.

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

  * [Monero Alt Adresleri Kimlik Bağlantısını Nasıl Önler?](/knowledge/monero-subaddresses)/

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