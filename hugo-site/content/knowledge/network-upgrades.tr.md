---
title: "Monero ağı yükseltmek için hard fork'ları nasıl kullanıyor?"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero'nun merkezi olmayan, gizliliği koruyan ve güvenli bir kripto para birimi oluşturma yaklaşımının en sık yanlış anlaşılan kısımlarından biri, hard fork'ların (veya ağ yükseltmelerinin) oynadığı roldür.

Bu yazıda hard forkların ne olduğunu, Monero için neden önemli olduklarını ve gelecekte bunlarda nasıl bir rol oynayabileceğinizi açıklayacağız.

## Monero'nun neden ağı yükseltmeye devam etmesi gerekiyor?

## Monero'nun neden ağı yükseltmeye devam etmesi gerekiyor?

Monero topluluğu, projeyi zaman içinde yinelemeye ve geliştirmeye kararlıdır ve görünen o ki bu bağlılık, topluluğun ahlakının iki temel yönüne indirgenmektedir:

  1. Monero projesi sonuçta insanlar tarafından yazılan bir yazılımdır (kod). Bu, hataları düzeltme, zaman içinde keşfedilen veya icat edilen iyileştirmeleri ekleme, protokolde modernizasyonlar uygulama veya yalnızca projeyi sürdürme ihtiyacına yol açabilir. Bu, birçok yönden, yeni özellikler eklemek ve hataları düzeltmek için sürekli olarak güncellenmesi gereken, kullandığınız diğer yazılımlara (bunu okuduğunuz tarayıcı gibi!) benzer.

  2. Monero projesi bir gizlilik aracıdır ve gizlilik sürekli ilerleyen bir silahlanma yarışıdır. Dünyanın mahremiyetini (hem finansal hem de kişisel) ortadan kaldırmaktan başka bir şey istemeyen insanlar ve gruplar, Monero'da kullanılanlar gibi, mahremiyetin korunmasına yönelik modern yaklaşımlara saldırmak için sürekli olarak gelişiyor, gelişiyor ve yeni yollar icat ediyor. Gizliliğin düşmanları bu yeni yaklaşımları keşfettikçe, Monero ağının buna uyum sağlaması ve iyileşmesi, mücadele etmesi ve finansal gizlilik hakkımızı savunması gerekiyor.

Monero projesi sonuçta insanlar tarafından yazılan bir yazılımdır (kod). Bu, hataları düzeltme, zaman içinde keşfedilen veya icat edilen iyileştirmeleri ekleme, protokolde modernizasyonlar uygulama veya yalnızca projeyi sürdürme ihtiyacına yol açabilir. Bu, birçok yönden, yeni özellikler eklemek ve hataları düzeltmek için sürekli olarak güncellenmesi gereken, kullandığınız diğer yazılımlara (bunu okuduğunuz tarayıcı gibi!) benzer.

Monero projesi bir gizlilik aracıdır ve gizlilik sürekli ilerleyen bir silahlanma yarışıdır. Dünyanın mahremiyetini (hem finansal hem de kişisel) ortadan kaldırmaktan başka bir şey istemeyen insanlar ve gruplar, Monero'da kullanılanlar gibi, mahremiyetin korunmasına yönelik modern yaklaşımlara saldırmak için sürekli olarak gelişiyor, gelişiyor ve yeni yollar icat ediyor. Gizliliğin düşmanları bu yeni yaklaşımları keşfettikçe, Monero ağının buna uyum sağlaması ve iyileşmesi, mücadele etmesi ve finansal gizlilik hakkımızı savunması gerekiyor.

## Sert çatal nedir?

## Sert çatal nedir?

Monero'yu yükseltmenin karmaşıklığı, bir kripto para birimini yükseltmenin tarayıcı gibi bir şeye yazılım güncellemesi göndermekten ne kadar farklı olduğunu anladığınızda devreye girer.

Kripto para birimlerinde, ağın kuralları (işlemlerin nasıl görünmesi gerektiği, madenciliğin nasıl çalıştığı ve her bloğun nasıl doğrulanacağı gibi şeyler) ağ tarafından üzerinde anlaşmaya varılmalıdır; buna "uzlaşma" adı verilir. Bu kurallardan herhangi birinin değiştirilmesi veya yükseltilmesi gerektiğinde, ağın yeni kurallar üzerinde anlaşması gerekir, bu da bir "hard fork"a neden olur; bu durum ağın aslında iki blok zincirine bölündüğü bir durumdur; biri eski kurallarda, diğeri ise eski kurallardadır. yeni kurallarla ilgili bir tane.

Topluluktaki herkes kural değişiklikleri üzerinde hemfikir olduğunda buna "tartışmasız hard fork" denir ve hala eski kurallara sahip olan zincir ölür ve hard fork sonrasında madencilik yapılmaz. Bu hemen hemen her Monero hard forku için geçerliydi ve eski kuralların devamı olan tek şey, hard fork'tan kar elde etmeye çalışan projelerdi.

Çekişmeli olmayan sert çatallar Monero ağının önemli yönlerini düzgün bir şekilde yükseltmenin tek yolu olsa da, bunların aynı zamanda sinir bozucu bir yan etkisi de var: Sert çatal planlanmadan önce piyasaya sürülen eski yazılım, yeniyi anlayamıyor ağın kuralları ve bu nedenle hard fork sonrasında çalışmaz! Bu, kullanıcıların fonların kaybolduğunu düşünmesine, Monero blok zincirinin durduğunu düşünmesine ve cüzdanlarını yükseltene kadar fonları taşıyamamalarına yol açabilir.

## Monero ağının ne zaman yükseltileceğine ve nelerin dahil edileceğine kim karar veriyor?

## Monero ağının ne zaman yükseltileceğine ve nelerin dahil edileceğine kim karar veriyor?

Monero'nun merkezi bir otoritesi, CEO'su veya başkanı olmadığından, ağın ne zaman yükseltileceğine, nelerin dahil edileceğine ve bunun nasıl yapılacağına karar verme işi _bizim_ 'e, yani bu kişilere düşüyor. Etkileşim kurmayı ve etkileşimde bulunmayı seçen Monero topluluğu! Bu, merkezi olmayan bir projenin hem son derece önemli bir parçasıdır, hem de proje için planlama ve karar alma süreci sonuçta merkezi olmayan bir yapıya sahiptir ve topluluktan kitle kaynaklıdır.

Monero'daki her ağ yükseltmesinde yer alan zamanlama ve özelliklerin planlanması iki ana yerde gerçekleşir:

  1. IRC ve Matrix'te, Monero topluluğunda en çok kullanılan sohbet platformları (birbirine köprülenmiştir). Bu platformlar büyük grup sohbetlerine izin verir ve planlanmış tüm Monero topluluk toplantılarının, geliştirme toplantılarının ve araştırma laboratuvarı toplantılarının yapıldığı yerdir. Bu toplantılar, Monero'daki ağ yükseltmeleriyle ilgili planlama ve tartışmayı dinlemeniz (veya katkıda bulunmanız!) için en iyi yoldur.

  2. Daha uzun süren Monero tartışmaları, planlaması ve organizasyonu için ana iletişim platformu olan Github'da. Monero topluluğu, Monero projesinin kodunu saklamanın yanı sıra toplantılar düzenlemek, yeni özellikleri ve fikirleri tartışmak ve ağ yükseltmelerinin planlanmasını koordine etmek için Github'u kullanıyor.

IRC ve Matrix'te, Monero topluluğunda en çok kullanılan sohbet platformları (birbirine köprülenmiştir). Bu platformlar büyük grup sohbetlerine izin verir ve planlanmış tüm Monero topluluk toplantılarının, geliştirme toplantılarının ve araştırma laboratuvarı toplantılarının yapıldığı yerdir. Bu toplantılar, Monero'daki ağ yükseltmeleriyle ilgili planlama ve tartışmayı dinlemeniz (veya katkıda bulunmanız!) için en iyi yoldur.

Daha uzun süren Monero tartışmaları, planlaması ve organizasyonu için ana iletişim platformu olan Github'da. Monero topluluğu, Monero projesinin kodunu saklamanın yanı sıra toplantılar düzenlemek, yeni özellikleri ve fikirleri tartışmak ve ağ yükseltmelerinin planlanmasını koordine etmek için Github'u kullanıyor.

Ağ yükseltmesi için önemli bir fikriniz varsa, benimsenen yaklaşımdan hoşlanmıyorsanız veya yükseltmenin zamanlaması konusunda endişeleriniz varsa, açıkça konuşmanız ve durumunuzu topluluğa açıkça sunmanız önemlidir![X1521X ]

## Ağ yükseltmelerine nasıl yardımcı olabilirim?

## Ağ yükseltmelerine nasıl yardımcı olabilirim?

Monero ağına yapılan yükseltmeler, yazılım güncellemelerinin yanı sıra topluluk koordinasyonu ve onayı gerektirdiğinden, ağ yükseltmelerinin planlama, test etme ve iletişim sürecine mümkün olduğunca çok kişinin dahil olması son derece önemlidir.

Ağ yükseltme işlemiyle ilgili sorunları gidermeye yardımcı olabileceğiniz birkaç kolay yol:

  1. Github'da yayınlanan [planlama toplantılarına katılın](https://github.com/monero-project/meta/issues), dinleyin ve gündeme getirmek istediğiniz konuyla ilgili bir konu varsa katkıda bulunun.
  2. Ağ yükseltme zamanlaması hakkındaki ayrıntıları (karar verildikten sonra!) favori borsanıza, cüzdanınıza veya madencilik havuzunuza iletin. Tüm Monero kullanıcılarını bir yükseltme konusunda düzgün bir şekilde bilgilendirmek zor olabilir, bu nedenle bu haberi duyurmak için elimizden gelen yardımı yapmamız önemlidir.
  3. Ağ yükseltmesinden önce yazılımı test edin. Yükseltmenin her yönünün yazılıma uygun şekilde planlandığından ve uygulandığından emin olmak için ağ yükseltmesinden önce hem test ağında hem de sahne ağında test uzmanlarına bir çağrı yapılacaktır. Ne kadar çok kişi dahil olur ve yeni sürümleri kapsamlı bir şekilde test ederse, ağ yükseltme işleminin sorunsuz ilerleme olasılığı da o kadar artar!
  4. Ağ yükseltmesiyle uyumlu sürümler yayınlandıktan sonra hemen yükseltme yaptığınızdan emin olun! Ne kadar çok kişi yükseltilirse ve ağ yükseltmesine hazır olursa, ağ bunu o kadar sorunsuz halleder ve kullanıcılar o kadar az baş ağrısı yaşar.

## Bir sonraki Monero ağ yükseltmesinden ne bekleyebilirim?

## Bir sonraki Monero ağ yükseltmesinden ne bekleyebilirim?

Henüz kesin bir tarih belirlenmemiş olsa da, Monero'da birkaç önemli yükseltmeyi ve özelliği uygulamak için yakında bir ağ yükseltmesi yapılacak:

  1. Ağdaki her işlemin temel anonimlik kümesini (okunur: makul inkar edilebilirlik veya temel gizlilik) artıran halka boyutunun 11'den 16'ya yükseltilmesi
  2. [Cüzdan senkronizasyon sürelerini %30-40 oranında azaltmanın harika bir yolu olan etiketleri görüntüleyin](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Ücret değişiklikleri, ücret piyasasındaki hızlı değişikliklere veya kötü niyetli kuruluşların saldırılarına karşı ağın güvenliğini ve esnekliğini artırır
  4. [Kurşun Geçirmezlik+, Monero işlemlerinin verimliliğinde daha fazla iyileştirme](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Bu değişiklikler ağın gizliliğini, verimliliğini ve güvenliğini artırmada uzun bir yol kat edecek ve aynı zamanda Monero için yeni nesil işlem protokolü olan [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero)'in önünü açacak.

## Daha fazlasını nasıl öğrenebilirim?

## Daha fazlasını nasıl öğrenebilirim?

Sert çatallanmalar ve ağ yükseltmeleri konusu çok geniştir ve bunların Monero'da uzun ve hikayeli bir geçmişi vardır; bu nedenle, hakkında daha fazla bilgi edinmek istiyorsanız aşağıdaki bağlantılardan bazılarına göz atmayı unutmayın. yaklaşan ağ yükseltmesi için devam eden geçmiş, süreç veya planlama!

  * [Monero v15 sert çatal planlaması](https://github.com/monero-project/meta/issues/630)
  * [Planlanmış yazılım yükseltmeleri (Monero'da)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Planlanmış protokol yükseltmeleri hakkında bir not](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

daha fazla okuma

  * [Monero döngüsel ekonomileri benzersiz bir şekilde nasıl mümkün kılıyor?](/knowledge/monero-circular-economies)/

  * [Monero'nun halka imzaları Wasabi'deki gibi CoinJoin'e karşı](/knowledge/ring-signatures-vs-coinjoin)/

  * [Neden (ve nasıl!) kendi anahtarlarınızı tutmalısınız?](/knowledge/hold-your-keys)/

  * [Monero'ya geri katkıda bulunmak](/knowledge/contributing-to-monero)/

  * [Uzak düğümler Monero'nun gizliliğini nasıl etkiler?](/knowledge/remote-nodes-privacy)/

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