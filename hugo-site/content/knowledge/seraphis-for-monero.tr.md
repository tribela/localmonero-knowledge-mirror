---
title: "Seraphis: Monero İçin Ne Yapacak?"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: Monero işlemleri için modüler bir tasarım yükseltmesi

Bu yazı, Monero ekosistemi için araştırma katılımcısı [`koe`](https://github.com/UkoeHB) tarafından geliştirilen ve devam eden güvenlik analiziyle birlikte geliştirilen bir dizi işlem protokolü yapısı ve soyutlaması olan [Seraphis](https://github.com/UkoeHB/Seraphis)'i açıklamaktadır. takma adlı katılımcı tarafından [`coinstudent2048`](https://github.com/coinstudent2048).  
Anlaşılırlık adına bazı basitleştirmeler yapıyoruz ve bazı teknik detayları atlıyoruz; bu nedenle ve Seraphis'in tasarımı halen devam ettiğinden, ilgilenen okuyucular en güncel bilgiler için Seraphis belgelerine başvurmalıdır.

## Monero'daki işlemler

Bitcoin ve Monero gibi protokoller ve diğerleri, sözde "çıktı modeli"ne dayanır; burada bir _çıktı_ , aktarılabilecek değerin bir temsilidir.  
İşlemler, gönderen tarafından kontrol edilen bir veya daha fazla çıktıyı tüketir ve alıcılara (veya değişiklik olarak gönderene geri) yönlendirilen yeni çıktılar üretir; işlem, tüketilen çıktıların yeni çıktılardaki değere tam olarak eşit bir toplam değer içermesi (artı ağ tarafından uygulanan bir ücret) açısından dengelenmelidir.  
Bitcoin gibi birçok protokolde, bir çıktının içerdiği değer, alıcı gibi açık bir şekilde yazılır.  
Ayrıca, blockchaine bakarak bir çıktının harcanıp harcanmadığını ve ne zaman harcandığını (yani daha sonraki bir işlemde tüketilip tüketilmediğini ve bunu hangi işlemin harcadığını) görmek önemsizdir.

Buna karşılık, Monero gibi protokoller farklı bir tasarım sunar:

  * Çıktı değerleri gizlidir ve blok zincirinde görünmez
  * Alıcı adresleri, tek seferlik adresleme protokolü kullanılarak gizlenir
  * Bir çıktının harcanıp harcanmadığı, belirsiz imzaların kullanılmasıyla gizleniyor

Sonuç olarak, harici bilgi olmadığında belirli bir çıktının harcanıp harcanmadığını, değerinin ne olduğunu ve alıcısının kim olduğunu belirlemek zordur.

Mevcut Monero işlem protokolüne _RingCT_ adı verilir ve bu tasarım hedeflerine ulaşmak için çeşitli şifreleme yapı taşları kullanılır.

  * _Taahhütler_ tutarları matematiksel açıdan yararlı bir şekilde gizler
  * _Aralık provaları_ , kaynağı şişirebilecek taşmayı önler
  * _Bağlanabilir halka imzalar_ imzalayanın belirsizliğini sağlar ve çift harcama girişimlerini önler
  * _Taahhüt mahsupları_ işlemlerin bakiyesini belirtir

Bu yapı taşları, RingCT protokolünü oluşturmak için dikkatli bir şekilde iç içe geçmiştir.

RingCT protokolünün kullanışlı bir özelliği, bazı yapı taşlarının genel tasarımı ve özellikleri koruyacak, ancak verimlilik veya güvenlik iyileştirmeleri sağlayabilecek şekilde değiştirilebilmesi veya yükseltilebilmesidir. Aslında bu tür yükseltmeler Monero'nun tarihinde birkaç kez gerçekleşti (veya gerçekleşmesi planlanıyor). Orijinal RingCT protokolündeki aralık kanıtları hantal ve yavaştı; daha sonra, daha iyi güvenlik analiziyle işlemleri daha küçük ve daha hızlı hale getiren [Kurşun Geçirmezler](https://eprint.iacr.org/2017/1066) adlı bir yapıya güncellendiler ve daha da büyük verimlilik avantajları için [Kurşun Geçirmezler+](https://eprint.iacr.org/2020/735) adı verilen daha yeni bir yapıya güncellenmeleri planlandı. 

Bağlanabilir halka imza yapı bloğunda da benzer bir süreç uygulandı. Orijinal protokolde [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) adı verilen bir yapı kullanıldı. Bu daha sonra [CLSAG](https://eprint.iacr.org/2019/654) adı verilen daha hızlı, daha küçük işlemlerle sonuçlanan ve daha iyi güvenlik analizine sahip daha yeni bir yapıya güncellendi. [Triptych](https://eprint.iacr.org/2020/018)'i temel alan daha da yeni bir bağlanabilir halka imza yapısı önerildi, ancak bu, çoklu imza işlemleri üzerindeki etkilerinden dolayı dağıtım için seçilmedi.

## Serafis

Seraphis bu fikri bir adım daha ileri taşıyor.  
Mevcut RingCT işlem protokolünün ayrı ayrı yapı taşlarını güncellemek yerine, farklı yapı taşlarından yararlanabilen ve gelişmiş işlevsellik sunabilen farklı bir protokol sunar.

## Yapı taşları

Seraphis, tasarım hedeflerine ulaşmak için farklı bir dizi şifreleme yapı taşı kullanıyor.

  * _Taahhütler_ hâlâ tutarları gizliyor
  * _Menzil kanıtları_ yine de taşmayı ve arz enflasyonunu önler
  * _Üyelik kanıtları_ imzalayanın belirsizliğini sağlar
  * _Taahhüt denkleştirmeleri_ hala dengeyi koruyor
  * _Yetkilendirme kanıtları_ çift harcama girişimlerini önler

Buradaki değişikliğe dikkat edin: bağlanabilir halka imzalar, üyelik kanıtları ve yetkilendirme kanıtlarının bir kombinasyonuyla değiştirildi. Kabaca söylemek gerekirse, üyelik kanıtları, RingCT'de olduğu gibi, tüketilen bir çıktının daha büyük bir kümenin parçası olduğunu göstermektedir. Ancak RingCT'den farklı olarak üyelik kanıtları hiçbir şekilde bağlantı etiketini içermez! Yetkilendirme kanıtları, bağlantı etiketinin geçerli olduğunu ve son işlemi imzalamak için kullanıldığını gösterir.

RingCT bağlantı etiketini belirsiz imzaya dönüştürdüğü için imzalama (ve çoklu imza) işlemleri hesaplama açısından daha yoğundur ve etiketle ilgili diğer işlevlerin oluşturulması daha zor hale gelir. Ancak Seraphis'te üyelik kanıtlarının oluşturulması, son derece güvenilir cihazlardan (donanım cüzdanı gibi sınırlı bilgi işlem gücüne sahip olabilir) daha az güvenilen bir cihaza güvenli bir şekilde devredilebilir ve imzalama (ve çoklu imza) işlemleri, çok daha basit yetkilendirme kanıtı kullanılarak çok daha kolaydır. .

Neyse ki, Seraphis'in ihtiyaç duyduğu bazı yapı taşları zaten başka yerlerde mevcut ve sıfırdan tasarlanmalarına gerek yok. Hem Kurşun Geçirmez hem de Kurşun Geçirmez+ yapılar menzile dayanıklı olarak kullanılabilir. Kanıtların onaylanması için Schnorr tipi kanıtlama sistemlerinde yapılan değişiklikler kullanılabilir. Ayrıca halihazırda Triptych, [Lelantus](https://eprint.iacr.org/2019/373) ve [Spark](https://eprint.iacr.org/2021/1173)* için temel olarak kullanılan etkili bir [kanıtlama sistemi](https://eprint.iacr.org/2015/643), üyelik kanıtları için değiştirilebilir.[ X2127X] 

* Cypher Stack, Spark geliştirmesi için fon alıyor.

## Adresleme

Maalesef şu anda kullanımda olan Monero adresleri Seraphis ile uyumlu değil. Seraphis'in uygulanması durumunda kullanıcıların Monero'yu alabilmeleri için cüzdan anahtarlarından yeni adresler oluşturmaları gerekecek. Ancak bu ekosistem maliyeti birçok faydayı da beraberinde getiriyor.

Yukarıda tartışılan yapısal faydaların yanı sıra, Seraphis tasarımı birçok farklı adres oluşturma olasılığına uygundur ve bunların her biri ödünleşimlerle birlikte gelir. Seraphis'te kullanılacak son adres yapısına [hala karar verilirken](https://github.com/monero-project/research-lab/issues/92) (çok dikkat çeken şemalardan biri [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024) olarak adlandırılır), bazı ortak ve kullanışlı özellikleri tanımlayabiliriz.[X908X ] 

Monero adreslerinin, bir cihaza veya üçüncü tarafa bir görüntüleme anahtarı sağlayabileceğiniz ve harcamadan vazgeçmeden sizin adınıza gelen çıktıları izlemesine izin verebileceğiniz _görüntüleme anahtarı_ işlevselliği sunduğunu biliyor olabilirsiniz. yetki. Bu, harcama anahtarınızı güvenli bir şekilde kilitli tutarken güncel kalabilen cüzdanlar için kullanışlıdır. Ayrıca şeffaflık sunan kamuya açık bir hayır kurumu veya muhasebe departmanı olan bir şirket gibi harici görüntüleme erişimi istediğiniz durumlar için de kullanışlıdır.

Monero görünüm tuşlarının dezavantajı, tam veya ayrıntılı görünüm erişimi sağlamamalarıdır. Bir cüzdanın ne zaman para harcadığını güvenilir bir şekilde tespit etmek mümkün değildir; bu da, harcama anahtarı mevcut olmadığında cüzdan bakiyelerinin doğru şekilde hesaplanmasını zorlaştırır. Şu anda, bu çıktıların içerdiği değeri öğrenmeden gelen çıktıları tespit etmek de mümkün değildir (bu, gelen çıktıları bulmaktan sorumlu herhangi bir üçüncü tarafın tam olarak ne kadar Monero satın aldığınızı öğreneceği anlamına gelir).

Seraphis adresleme yapıları bunu çözebilir. Seraphis ile adresiniz farklı şeyler yapabilen farklı anahtarlarla donatılmış olarak gelir:

  * Gelen çıkışları izleyin ancak değerlerini gizleyin
  * Gelen çıkışları izleyin ancak değerlerini gösterin
  * Giden çıkışlara dikkat edin
  * İşlemleri oluşturmanıza yardımcı olur ancak imzalamanıza gerek kalmaz
  * Yeni adresler oluşturun (perakendeciler veya çok sayıda müşterisi olan borsalar için kullanışlıdır)

Adres sahibi olarak, diğer cihazlara veya üçüncü taraflara ne kadar yetki devredeceğinize siz karar verirsiniz.

## Büyük resim

Seraphis, Monero ekosisteminde büyük bir değişikliktir. Adreslerde ve işlem yapı taşlarında değişiklikler yapılmasına rağmen tasarımı, günümüzün RingCT protokolüyle mümkün olmayan esneklik ve kullanışlı işlevsellik sunar. Tasarımın büyük bir kısmı tamamlanmış ve [bir uygulamaya](https://github.com/UkoeHB/monero/tree/seraphis_lib) dönüştürülmüş olsa da, adres tasarımı ve güvenlik analizi devam etmektedir. Seraphis, Monero ekosistemini ileriye taşımak için mükemmel bir fırsat sunuyor!

daha fazla okuma