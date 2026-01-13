---
title: "Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Bitcoin'in gizlilik araçları daha fazla ilgi ve kullanım kazandıkça, daha fazla düzenleyici incelemeye tabi tutuldu. Bu inceleme, bir Bitcoin gizlilik aracı olan Wasabi Cüzdan tarafından [yakın zamanda yapılan bir duyuruya](https://twitter.com/wasabiwallet/status/1503091503207432193) yol açtı; yasa dışı veya Hizmet Şartlarına aykırı olduğunu düşündükleri karışımlara gelen girdileri sansürlemeye ve reddetmeye başlayacaklar ve bir zincir analizi ödeyecekler şirket gelen mix katılımcılarını "inceleyecek".

Bitcoin'deki fonların kaynağını gizlemek için CoinJoin işlemlerinin kullanılması, uzun yıllardan beri Bitcoin gizliliğinin temelini oluşturmuştur ve kullanımının doğasında olan sorunlar ve riskler, Monero'nun halka imzalarının düzelttiği ve önlediği temel sorunlardan bazılarıdır. .

Bu blog yazısında, CoinJoin ve ring imzalarının karşılaştırmasına ve ayrıca Monero'da benimsenen yaklaşımın neden sansüre karşı daha fazla direnç, daha fazla gizlilik ve kullanıcılar için daha az soruna yol açtığına kısaca değineceğiz.

## CoinJoin işlemi nedir?

Bitcoin'de tüm işlemler tamamen şeffaf olduğundan (göndereni, alıcıyı ve tutarları ortaya çıkarır), kullanıcıların gizliliklerini önceki göndericilerden ve gelecekteki fon alıcılarından korumak veya sansür, gözetleme veya fon hırsızlığı riskiyle karşı karşıya kalmak için ekstra adımlar atması gerekir. fiziksel şiddet.

Bitcoin'de gizlilik için bugün en iyi çözüm, 2 veya daha fazla kullanıcının (genellikle merkezi bir koordinatör aracılığıyla) dışarıdakilerin işini zorlaştıran özel bir işlem oluşturmak için birlikte çalıştığı ["CoinJoin"](https://bitcoiner.guide/qna/coinjoin/) adlı bir araçtır. Girişleri çıkışlara bağlamak için gözlemciler. Her katılımcı, fonlarının velayetini vermeden işlemi ortaklaşa oluşturmak için iletişim kurar ve sonunda, önceki geçmişi artık dış gözlemciler için belirsiz (veya gizlenmiş) olan bir çıktı alır.

Bu, belirli UTXO'ların geçmişini kırarak Bitcoin kullanıcılarının işlem yaparken bir miktar ileri gizlilik elde etmesine olanak tanır. Ancak CoinJoin'in (Bitcoin için en çok kullanılan iki CoinJoin aracı olan Wasabi Wallet ve Samourai Wallet'ta uygulandığı şekliyle) birkaç önemli dezavantajı vardır:

  * CoinJoin işlemleri tamamen isteğe bağlı olduğundan ve aktif katılım gerektirdiğinden, herhangi bir katılımcı mutlaka "normal" Bitcoin kullanıcılarından daha fazla gizlilik aradıklarını gösterir, bu da onları potansiyel olarak diğerlerinden ayırır ve birçok düzenlemeye tabi borsa veya kuruluşta fon harcama sorunlarına neden olur. Her kullanıcı CoinJoin işlemine katıldığını inkar edemez.
  * CoinJoin'e başkalarını bulmak için CoinJoin'e yönelik çoğu yaklaşım (Wasabi Wallet dahil), katılımcıları birbirine bağlayan ve iletişim kurmalarına ve uygun bir CoinJoin işlemi oluşturmalarına yardımcı olan merkezi bir koordinatör kullanır. Bu merkezi koordinatör hiçbir zaman kullanıcının fonlarını saklamaz ancak koordine ettiği işlemler hakkında kapsamlı bilgi sahibi olur, gelen girdileri sansürleyebilir (Wasabi Cüzdanında olduğu gibi) ve CoinJoin katılımcıları hakkında bilgi toplama veya paylaşma konusunda baskı altında kalabilir.[X2068X ] 
  * CoinJoin'e büyük miktarlarda para yatıran kullanıcılar, CoinJoin'e yetecek sayıda katılımcı bulmak için genellikle saatlerce (hatta günler!) beklemek zorunda kalabilir, bu da kullanıcının parayı aldığı andan bu parayı özel olarak harcayabileceği zamana kadar büyük gecikmelere yol açar. 
  * CoinJoin işlemi tarafından sağlanan gizlilik, diğer katılımcılar para harcadıkça veya çıktılarını KYC değişimleri, kimlik gerektiren tüccarlar vb. aracılığıyla kendi kimliklerine bağladıkça zamanla bozulur. Bu, kullanıcıların ideal olarak fonlarını CoinJoin işlemlerinde sürekli olarak çalkalayarak sürdürmeleri anlamına gelir. anonimlikleri (“saklanacak kalabalık”) mümkün olduğunca taze.
  * CoinJoin'e yönelik çoğu yaklaşımda, katılımcıların CoinJoin işlemlerinin giriş ve çıkışlarını bağlamayı zorlaştırmak için sabit boyutlu bir UTXO (yani 0,1 BTC) kullanması gerekir. Bu, daha yüksek ücretlere (büyük girdi başına daha fazla ayrı işlemin gerekli olması), daha fazla "toksik değişime" (gizlilik açısından ciddi riskler oluşturmadan harcanamayan fonlar) yol açar ve küçük kullanıcıların, eğer ellerinde bir para yoksa, bunları karıştırma olanağını tamamen ortadan kaldırabilir. gereken minimum bakiye.

## Halka imzalar bu sorunları nasıl çözer?

Geçmişte zil seslerinin ne olduğunu [derinlemesine incelemiş olduğumuzdan](/knowledge/ring-signatures), bu blog yazısında bunların nasıl çalıştıklarının teknik yönleri hakkında çok fazla ayrıntıya girmeyeceğim. Bunun yerine Monero'da benimsenen yaklaşımların CoinJoin ile yukarıda tartışılan sorunları nasıl çözdüğüne bakacağız.

> CoinJoin isteğe bağlıdır ve katılım gerektirir

Monero'nun halka imzaları, gizlilik protokolünün temel bir özelliğidir ve ağdaki _her_ işlemde bunları kullanır. Bu, hiçbir kullanıcının işlemlerinin "normal" Monero kullanıcılarından daha fazla gizlilik arayışında olmadığı ve tüm kullanıcıların herhangi bir işlemde para harcadıkları konusunda makul bir inkar elde ettiği anlamına gelir. Para harcayan bir kullanıcı, bir işlemdeki sahte girdileri koordine etmediğinden veya bunlara katılmadığından, tuzak olarak seçilen girdilere sahip olan kullanıcılar, bu işleme katılmadıklarını dürüstçe söyleyebilir ve bu da gizliliklerini güçlendirir.

> Merkezi bir koordinatörün kullanımı

Monero'nun halka imzaları tamamen koordine olmadığından ve işlemi oluşturmak için yalnızca fonları gerçek harcayan kişiye ihtiyaç duyduğundan, Monero'da merkezi bir koordinatöre ihtiyaç yoktur. Bu, _hiç kimsenin_ Monero'da gizliliğe erişiminizi engelleyememesini ve baskı altına alınabilecek hiçbir merkezi varlığın, likiditeye yönelik kolay Sybil saldırılarının olmamasını vb. sağlar. İşleminiz uygun ücretleri ödediği sürece, Monero'da gizliliğe, güvenliğe ve anonimliğe sansürlenemez erişim elde edersiniz.

> CoinJoin likidite gerektirir

Monero'yu tuzak olarak kullanmak üzere harcayan herkesin kullanabileceği "likidite" her zaman zincirdeki toplam çıktı kümesidir, dolayısıyla Monero'da saklanacak tuzak sıkıntısı asla yaşanmaz. Monero harcamak isteyen biri, parayı aldıktan yaklaşık 20 dakika sonra bunu yapabilir ve Monero'da güçlü bir gizlilik elde etmek için herhangi bir ek adım atması gerekmez.

> CoinJoin gizliliği zamanla bozulur

Monero'nun çıktıları hiçbir zaman ağ tarafından bilinmediğinden ve harcanmadığından, halka imzalarının sağladığı gizliliğin zaman içinde bozulmaya karşı duyarlılığı çok daha azdır. Kullanıcının Monero'da çıktıları sürekli olarak değiştirmesi gerekmez ve son derece nadir durumlar dışında zaman geçtikçe gizlilik kaybı olmaz.

Bir kullanıcı bir çıktıyla kullanılan tuzakları "yenilemek" isterse, parayı yalnızca kendisine geri gönderebilir ve her zamanki gibi ~20 dakika sonra harcayabilir.

> CoinJoin genellikle sabit boyutlu girişler gerektirir

Tutarlar, [“Gizli İşlemler”](/knowledge/monero-ringct) ("RingCT"nin bir parçası) kullanılarak her işlemde gizlendiğinden, herhangi bir işlemde kullanılan tuzaklar herhangi bir boyutta olabilir. Monero'da miktara dayalı buluşsal yöntemler konusunda endişelenmenize gerek yok ve bu nedenle işlemlerin oluşturulması çok daha kolaydır ve Monero blok zincirindeki herhangi bir zamanda ve herhangi bir miktardaki tuzaklardan yararlanılabilir.

## Daha fazlasını nasıl öğrenebilirim?

Merak ediyorsanız ve zil imzalarını veya CoinJoin işlemlerini daha iyi anlamak istiyorsanız, başlamak için harika yerler için aşağıdaki bağlantılara bakın:

  * [Halka İmzaları Monero'nun Çıktılarını Nasıl Gizliyor?](/knowledge/ring-signatures)
  * [Yüzük İmzası - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Para Birleştirme Soru+Cevap](https://bitcoiner.guide/qna/coinjoin/)
  * [CoinJoin'e Genel Bakış](https://6102bitcoin.com/coinjoin-overview/)

daha fazla okuma