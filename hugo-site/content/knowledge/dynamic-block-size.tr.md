---
title: "Monero, Bitcoin'i Saldıran Blok Boyutu Sorununu Nasıl Çözdü?"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Not:** Okuyucunun ["Monero'nun Neden Kuyruk Emisyonu Vardır"](/knowledge/monero-tail-emission) ve [“Monero Madenciliği: RandomX'i Ne Yapar? adlı makalelerimizi okuması önemle tavsiye edilir. çok Özel”](/knowledge/monero-mining-randomx). Bu makale burada sunulan kavramlardan yola çıkılarak oluşturulmuştur._

Ne zaman bireyler blockchain ile ilgili sorunları tartışsa, ortaya çıkan ilk kelimelerden biri "ölçeklendirme" olacaktır. Blockchainlerin iyi ölçeklenemediği bir sır değil ancak çoğu insan bunun nedenini bilmiyor.

Gerçek şu ki, ölçeklendirme aslında iki farklı kategoriyi kapsayan bir şemsiye terimdir: Protokol desteği ve belirli bir zamanda teknolojik destek. Bu makalede dikkatimizi bir tanesine yoğunlaştıracağız: Protokol desteği temel olarak protokolün belirli bir zamanda kaç işlemi gerçekleştirebileceğinin bir ölçüsüdür.

Bitcoin'in bir blok boyutu sınırı vardır; bu, bir bloğa yeterli sayıda işlem dahil edildiğinde, tüm ek işlemlerin bir sonraki blok için sırada beklemesi gerekeceği anlamına gelir. Yararlı bir benzetme, bir treni düşünmek olabilir. Bir tren istasyona yanaşıyor ve sırada bekleyenler sıraya giriyor. Tren dolduğunda, dışarıda kalan herkes bir sonraki treni beklemek zorunda kalacak.

Bitcoin, bloğa kimin girip girmeyeceğini belirlemek için ücretleri kullanır. Tren benzetmesine geri dönecek olursak, geride kalmak üzere olan potansiyel bir yolcunun, tren makinistine kendisine yer vermesi için beş dolar teklif ettiğini hayal edebiliriz. Diğer yolcular da aynısını yapar ve sonunda kimin hangi koltuğu alacağını görmek için bir açık artırma savaşı başlar. İlk gelen ilk alır politikasına uyup uymamak sürücüye kalmıştır, ancak en yüksek teklif verenleri araca alarak gelirini en üst düzeye çıkarmak onun mali çıkarınadır.

Bu benzetmede madenciler tren makinistleridir. İstedikleri işlemleri bloğa dahil edebilirler ancak genellikle en yüksek ücrete sahip olanları seçerler.

Alternatif olarak, bloklar çok dolu değilse, yedeklenecek çok sayıda boş koltuk olduğundan insanların yüksek ücret ödemeye teşviki olmaz.

2017'deki kripto para patlamasının zirvesinde, Bitcoin işlemlerle doluydu ve bir sonraki bloğa veya bu konuda yakın gelecekteki herhangi bir bloğa dahil olmak isteyenler için ücretler hızla arttı. Yüksek ücret ödemeye isteksiz olanlar, işlemlerinin saatlerce, günlerce ertelendiğini, hatta kuyruktan tamamen çekildiğini gördüler.

Bu, 'kitlesel benimseme'den sık sık bahsedilirse Bitcoin'in nasıl bir performans göstereceğine dair üzücü bir fikirdi. Eğer Bitcoin kitleler tarafından kullanılacak olsaydı, işler 2017'dekinden daha da kötü olurdu ve Bitcoin'e zenginler dışında kimse erişemez olurdu, çünkü sabit blok boyutu nedeniyle verim küçüktü ve ücret piyasasının kontrolü ele geçirmesine neden olurdu. .

Monero bunu öngördü ve farklı bir şey yapmak istedi. Böylece Monero geliştiricileri dinamik bir blok boyutu uyguladılar.

Temel olarak Monero'nun blok boyutunda bir üst sınırı vardır, ancak bu yumuşak bir üst sınırdır. Bekleme işlemlerinin sırası çok uzadığında madenciler blokların boyutunu artırabilir. Bizim tren benzetmemizle, ekstra yolculara sığacak şekilde daha fazla tren vagonu eklemeyi hayal edebilirsiniz. Sıra boşaldıktan sonra bloklar ileriye doğru orijinal boyutlarına geri döner.

Bu iyi bir fikir gibi görünüyorsa, Monero'nun neden bunu uygulayan tek kripto para birimi olduğunu sormak mantıklı görünüyor. Üretim sorunlarına bir son vermek için neden bunu Bitcoin'e eklemiyorsunuz?

Maalesef bu mümkün değil. Bunun birkaç nedeni var ve açıklamak için elimizden geleni yapacağız.

Büyük bloklara sahip olmak her zaman madencinin çıkarınadır. Büyük bloklarla daha fazla işleme sığabilirler ve blok ödüllerinin yanı sıra ücretlerden de daha fazla para kazanabilirler. Bunun, zinciri şişirmek için birisinin küçük ücretlerle çok sayıda küçük işlem gönderdiği spam saldırılarına yol açma potansiyeli vardır. Madenciler blok boyutunu yükseltir, hepsini içerir çünkü ne kadar küçük olursa olsun para paradır. Bu, çok az ekonomik fayda sağlayan sürekli olarak büyük bloklara yol açacaktır. Bitcoin bunu blok boyutunu yapay olarak kısıtlayarak ve böylece bir ücret piyasası oluşturarak çözer. Spam saldırganlarının diğer kullanıcılara ücret olarak daha fazla ödeme yapması gerekecek ve bu artık ucuz değil. Ancak bu, yukarıda belirtildiği gibi blokların dolması ve bazı işlemlerin beklemede kalması anlamına gelir.

Peki Monero nasıl dinamik blok boyutlarına sahip olabilir ama spam saldırılarından kaçınabilir? Cevap basit ama akıllıca. Bir blok normalden büyük olduğunda blok ödülüne ceza uygulanır. Bir madenci blok boyutunu artırmak isterse, o bloğu bulmaktan elde edeceği ödül, aksi takdirde alacağından daha az olacaktır. Dolayısıyla, yalnızca kullanıcıların ödediği işlem ücretleri, blok ödülünün kaybedilen kısmından daha ağır bastığında blok boyutunu artıracaklar. Örneğin, madenci blok boyutunu yükselterek 0,5 XMR kaybedecekse ve ödenen işlem ücretlerinin toplamı 0,4 XMR olacaksa, o zaman boyutu yükseltirse 0,1 XMR net kayıp olacaktır; yapma. Tersine, toplam işlem ücretlerinin toplamı 0,7 XMR'ye ulaşırsa, blok ödülü cezasından 0,5 XMR'yi kaybetmelerine rağmen 0,2 XMR'lik net kazanç olur, dolayısıyla madenci boyutu artıracaktır.

Bu dinamik bloklar, spam saldırılarından kaçınırken zorunlu bir ücret piyasası oluşturmak için blok boyutunu yapay olarak kısıtlamadan ağın organik olarak büyümesine olanak tanır. Bu fikre bakabileceğimiz birkaç bakış açısı ve bunun Bitcoin'e eklenmesinin mümkün olmamasının daha fazla nedeni var, ancak şimdilik okuyucunun Monero'nun Bitcoin'deki birçok sorunu nasıl atlattığını anladığını umuyoruz. türevleri ve verimini geleceğe nasıl ölçeklendirmeyi planladığı.

daha fazla okuma

  * [Monero döngüsel ekonomileri benzersiz bir şekilde nasıl mümkün kılıyor?](/knowledge/monero-circular-economies/)

  * [Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı](/knowledge/ring-signatures-vs-coinjoin/)

  * [Neden (ve nasıl!) kendi anahtarlarınızı tutmalısınız?](/knowledge/hold-your-keys/)

  * [Monero'ya geri katkıda bulunmak](/knowledge/contributing-to-monero/)

  * [Uzak düğümler Monero'nun gizliliğini nasıl etkiler?](/knowledge/remote-nodes-privacy/)

  * [Monero ağı yükseltmek için hard fork'ları nasıl kullanıyor?](/knowledge/network-upgrades/)

  * [Etiketleri görüntüle: Bir bayt, Monero cüzdan senkronizasyon sürelerini nasıl %40'tan fazla azaltır?](/knowledge/view-tags-reduce-monero-sync-time/)

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

  * [CLSAG Monero'nun Verimliliğini Nasıl Artıracak?](/knowledge/what-is-clsag/)

  * [Monero'nun Neden Kuyruk Emisyonu Var?](/knowledge/monero-tail-emission/)

  * [Monero'nun Kısa Tarihi](/knowledge/monero-history/)

  * [Wired Magazine Monero Konusunda Yanılıyor, İşte Nedeni](/knowledge/wired-article-debunked/)

  * [En Önemli 15 Monero Efsanesi ve Endişesi Çürütüldü](/knowledge/monero-myths-debunked/)

  * [Dandelion++ Monero'nun İşlem Kaynaklarını Nasıl Gizli Tutuyor?](/knowledge/monero-dandelion/)

  * [Monero Neden Açık Kaynaklı ve Merkezi Değildir?](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Monero Madenciliği: RandomX'i Bu Kadar Özel Kılan Nedir?](/knowledge/monero-mining-randomx/)

  * [Monero Neden Dash, Zcash, Zcoin (Lelantus ile Bile), Grin ve Wasabi Gibi Bitcoin Karıştırıcılarından Daha İyidir (Mayıs 2020'de Güncellendi)](/knowledge/why-monero-is-better/)