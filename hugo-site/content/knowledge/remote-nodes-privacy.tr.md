---
title: "Uzak düğümler Monero'nun gizliliğini nasıl etkiler?"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero'nun diğer kripto para birimlerine göre sahip olduğu en büyük avantajlardan biri zincir içi gizliliktir, ancak uzak bir düğüm kullandığınızda Monero'nun gizliliğinin nasıl dayandığını hiç merak ettiniz mi? MyMonero gibi bir "hafif cüzdan" sunucusu kullansanız nasıl olur?

Bu gönderide, Monero'nun uzak bir düğüm kullanırken bile nasıl olağanüstü zincir içi gizlilik sağladığının yanı sıra uzak düğümleri kullanırken nelere dikkat edilmesi gerektiğinin arkasındaki bazı ayrıntılara dalacağız.

## Monero'da düğümler hangi işlevi yerine getirir?

Monero'nun nasıl çalıştığına daha az aşina olanlar için, Monero ağındaki düğümler (veya sunucular) herkes tarafından çalıştırılabilir ve düğümün sahibinin veya seçtiği diğer kişilerin onu paylaşmalarına izin verilebilir! – Blockchain'in bir kopyasını senkronize etmek ve bu kopyayı ağdaki diğer kişilere sağlamak. Bu düğümler ayrıca ağda gerçekleşen tüm işlemlerin yanı sıra yayınlanan tüm blokları da doğrular ve hepsinin fikir birliğiyle belirlenen kurallara uymasını sağlar.

Monero'da düğümlerin hizmet ettiği diğer işlev, favori Monero cüzdanınızın size ait işlemleri doğru şekilde kontrol etmek ve yeni işlemler yapmak için ihtiyaç duyduğu tüm verileri sağlamanın bir yoludur. Bu veriler düğümler tarafından iki şekilde sağlanır:

  * Blockchain'deki her bloktaki veriler cüzdan tarafından talep edilir, size ait işlemler için taranır ve ardından cüzdan tarafından kontrol edildikten sonra atılır. 
    * Bu adım, [görüntüleme etiketleri](/knowledge/view-tags-reduce-monero-sync-time) sayesinde yakında büyük ölçüde iyileştirilecek.
  * İşlemleri gönderirken, kullandığınız düğüm, işlemi oluştururken kullanılabilecek olası tuzakların (veya sahte girişlerin) bir listesini sağlayarak Monero'yu her harcadığınızda saklanacak iyi bir kalabalığa sahip olmanızı sağlar. 
    * Bu tuzaklar, Monero'nun zincir içi gizliliğe yaklaşımının önemli bir parçası olan [halka imzalarının](/knowledge/ring-signatures) bir parçasıdır.

## Monero'yu kullanmanın en özel ve güvenli yolu nedir?

Uzak düğümleri kullanırken Monero tarafından sağlanan güçlü zincir içi gizlilikle bile yapılacak en iyi şey, Monero blok zincirinin bozulmamış bir kopyasının elinizin altında olduğundan ve IP adresinizin korunduğundan emin olmak için kendi Monero düğümünüzü çalıştırmaktır. iyi korunmaktadır. Kendi düğümünüzü çalıştırmanın diğer bir faydası da, diğer düğümlerin sizin düğümünüzden senkronizasyon yapmasına ve hatta diğer kullanıcıların cüzdanlarıyla düğümünüze bağlanmasına izin vererek ağa geri katkıda bulunabilmenizdir.

Bununla birlikte Monero, uzak bir düğüm kullanılırken hâlâ mükemmel gizlilik sağlıyor. Kendi Monero düğümünüzü çalıştırmakla ilgileniyorsanız, bunu yapmak için takip edilmesi kolay bir kılavuzu burada bulabilirsiniz:

  * [Monero Düğümünü Çalıştırın](https://sethforprivacy.com/guides/run-a-monero-node/)

## Uzak bir düğüm benim hakkımda ne öğrenebilir?

Uzak bir düğüm kullanırken, uzak bir düğüme maruz kalan birkaç önemli bilgi parçası vardır ve düğümün size saldırabileceği, işlem yapmanızı engelleyebileceği ve daha pek çok önemli yol vardır.

Uzak bir düğümün sizin hakkınızda öğrenebileceği ilk şey genel IP adresinizdir. Bunun bir VPN veya Tor aracılığıyla gizleneceği umulsa da uzak düğüm, genel IP adresinizi işlemle ilişkilendirebilir ve işlem yaptığınız yeri daraltmalarına yardımcı olabilir. Uzak düğüm aynı zamanda cüzdanınızın senkronize ettiği son bloğu da öğrenebilir ve bunu normalde Monero'yu ne zaman kullandığınız ve Monero'yu en son ne zaman harcadığınız gibi sizin hakkınızda bilinçli tahminler yapmak için kullanabilir. Bu özellikle her zaman aynı IP adresinden (eviniz gibi) geliyorsanız geçerlidir. Uzak bir düğümün sizin hakkınızda öğrenebileceği son önemli şey, onun aracılığıyla gönderdiğiniz işlemlerle ilgili temel bilgilerdir. Bu, uzak düğüm operatörünün sizin hakkınızda elde ettiği en belirgin veriler olsa da, bu bilgilerin diğer zincir dışı verilerle birleştirildiğinde işlemi gönderenin izini sürmeye yardımcı olmak için kullanılabileceğini anlamak önemlidir. Uzak düğümün kötü niyetli bir varlık, bir blockchain analiz şirketi veya baskıcı bir ulus devlet tarafından çalıştırılması durumunda bu özellikle tehlikeli olabilir.

Uzak bir düğüm ayrıca blokları sizden gizleyerek, cüzdanınızın senkronize olmadığı halde senkronize edildiğini düşünmesini sağlayarak size sorun çıkarmaya çalışabilir. Bu, paranızın kaybolduğunu düşünmenize neden olabilir veya başka bir düğüme bağlanana kadar para harcamanızı engelleyebilir. Uzak bir düğümün yapabileceği son önemli şey, cüzdanınızı manipüle edilmiş bir tuzak listesiyle beslemektir. Bu, cüzdanınızın işlem oluşturmada tamamen başarısız olmasına neden olabilir (para harcayamamanıza neden olabilir) veya uzaktaki düğümün, her işlemde aldığınız anonimliği azaltmak için harcandığını bildiği tuzakları denemesine ve sağlamasına izin verebilir.

## Uzak bir düğüm kullanıldığında hangi gizlilik garantileri hala mevcuttur?

Bu makale sizi biraz korkutmuş olsa da, Monero'nun sağladığı gizliliğin uzak bir düğüm kullanıldığında bile mükemmel olduğunu ve bu şekilde kullanıldığında diğer kripto para birimlerini çok geride bıraktığını fark etmek önemlidir. Uzak düğüm gerçek girdiyi (hangi paraları harcadığınızı), işlemde harcanan Monero miktarını veya işlemin alıcısının adresini asla bilemeyeceğinden, Monero tarafından sağlanan güçlü zincir içi gizliliği elde etmeye devam edersiniz. Dışarıdaki gözlemciler aynı zamanda gerçek girdiyi, miktarı veya ilgili adresleri göremez (hangi düğüm türünü kullanmayı seçerseniz seçin!), böylece uzak düğümün dışında IP adresinizin, cüzdan senkronizasyon bilgilerinizin ve işlemlerinizin bile güçlü gizlilik garantilerine sahip olması sağlanır. .

Uzak düğüm ayrıca gönderdiğiniz veya aldığınız önceki işlemlere veya şu anda cüzdanınızda bulunan Monero miktarına hiçbir zaman erişemez ve başka bir düğümü kullanmaya başladığınız anda işlemlerinizin tüm görünürlüğünü kaybeder. Uzak düğüme hiçbir özel anahtar (harcama veya görüntüleme anahtarları) sağlanmaz ve böylece cüzdanınız özel, güvenli ve kullanılabilir kalır. Uzak düğüm ne olursa olsun, Monero'yu kaybetme veya çalınma riskiyle karşı karşıya kalmazsınız çünkü düğüm alıcı adresini düzenleyemez, cüzdanınızın özel anahtarlarına hiçbir zaman erişemez ve Monero'nuza hiçbir şekilde el koyamaz.

## MyMonero gibi "hafif cüzdanlara" ne dersiniz?

Konu bu makalenin kapsamının biraz dışında olsa da, Monero'daki benzersiz bir cüzdan türüne, yani hafif cüzdanlara değinmek istedim. Hafif cüzdan adı, cüzdanınızın (telefonunuzda veya bilgisayarınızda) herhangi bir blockchain senkronizasyonu gerçekleştirmesine gerek olmamasından gelir ve bu da deneyimi daha hızlı ve daha akıcı hale getirir.

Ancak bunun gibi cüzdanlar şimdilik ciddi bir gizlilik ödünleşimiyle birlikte geliyor; cüzdanınız, özel görüntüleme anahtarını kullandığınız uzak sunucuya göndererek (MyMonero'daki varsayılan gibi), uzak sunucunun alınan tüm fonlar için tam görünürlük sağlamasına olanak tanır. Cüzdanınızın oluşturulmasından bu yana (ve o cüzdanı veya tohumu kullanmayı bırakana kadar). Bu, düğüm operatöründen aldığınız gizliliği büyük ölçüde azaltır ve bu duruma dikkatle yaklaşılmalıdır.

Neyse ki Monero topluluğu, kendi hafif cüzdan sunucunuzu (LWS) barındırmak için kullanabileceğiniz yazılımı geliştirmek için çalışıyor; bu, sizin gibi özel görünüm anahtarlarınız konusunda bir üçüncü tarafa güvenmeden hızlı senkronizasyon yapmanıza olanak tanıyacak. cüzdanınızın özel görünüm anahtarlarını gönderdiği yazılımı çalıştıracak!

Özel hafif cüzdan sunucusu hakkında daha fazla bilgi için aşağıdaki Github deposuna bakın:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Daha fazlasını nasıl öğrenebilirim?

Merak ediyorsanız ve Monero'daki düğümleri daha iyi anlamak istiyorsanız ve uzak bir düğüm kullanmayı veya kendi düğümünüzü çalıştırmayı düşünüyorsanız, başlamak için harika yerler için aşağıdaki bağlantılara bakın:

  * [Monero World, topluluk tarafından çalıştırılan uzak düğümlerin bir listesidir. kullanılabilir](https://moneroworld.com/#nodes)
  * [Monero düğümleri tarafından çalıştırılır Seth For Privacy, bu makalenin yazarı](https://sethforprivacy.com/about/#high- Performance-monero-nodes)
  * [monero.fail, sık sık kontrol edilen durumu olan uzak düğümlerin listesi< /a>](https://monero.fail/)
  * [Nasıl bağlanılır? GUI cüzdanındaki uzak bir düğüme](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Uzaktan Kumanda Düğüm](https://www.getmonero.org/resources/moneropedia/remote-node.html)

daha fazla okuma

  * [Monero döngüsel ekonomileri benzersiz bir şekilde nasıl mümkün kılıyor?](/knowledge/monero-circular-economies/)

  * [Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı](/knowledge/ring-signatures-vs-coinjoin/)

  * [Neden (ve nasıl!) kendi anahtarlarınızı tutmalısınız?](/knowledge/hold-your-keys/)

  * [Monero'ya geri katkıda bulunmak](/knowledge/contributing-to-monero/)

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