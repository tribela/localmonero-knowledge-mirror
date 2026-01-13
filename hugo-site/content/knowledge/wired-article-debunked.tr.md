---
title: "Wired Magazine Monero Konusunda Yanılıyor, İşte Nedeni"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Hem gizlilik hem de kripto para alanında yanlış bilgi sıklıkla yaygınlaşıyor. Monero hakkında on beş yaygın yanlış veya güncelliğini kaybetmiş varsayımı özetleyen [bir makalemiz var](/knowledge/monero-myths-debunked), ancak Monero şüphecileri tarafından sıklıkla alıntı yapılan ve dağıtılan belirli bir makaleye değinmek için zaman ayırmak istiyoruz.

Wired yayını 27 Mart 2018'de [bir makale](https://www.wired.com/story/monero-privacy/) yayınladı; bu makalenin kendisi de çeşitli akademisyenler tarafından yeni basılan başka bir makaleye yanıt olarak yazılmıştır: "Deneysel Bir Analiz" Monero Blok Zincirinde İzlenebilirlik”.

Makale, açık çıkar çatışması olan kişiler tarafından ortak yazılmış olmasına rağmen (okuyun: onlar Zcash'in danışmanıdır ve Zcash'te hisseye sahiptir), makale Monero topluluğu tarafından topluluğun zaten bildiği şeyleri doğruladığı için orta derecede iyi karşılandı. ve en eskisi dört yıl önce yayınlanmış olan kendi Monero Araştırma Laboratuvarı makalelerinde ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) ve [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) yazılmıştır. Bununla birlikte, başta çıkar çatışması, sorunların zaten bilindiği, tartışıldığı ve bazı durumlarda düzeltildiği gerçeği ve Monero'nun gizlilik garantilerinin o dönemde büyük ölçüde yanlış tanımlanması gibi bazı hayal kırıklıkları da vardı. Topluluk, çalışmanın ön basımına yorum yaptı ve tavsiyelerinin çoğu, son makaleye kadar ulaştı.

Fakat tam olarak yanlış nitelendirilen şey neydi? Monero'nun bir yıldan fazla süredir makalede tartışılan kusurlara sahip olmadığı gerçeği. 2017 öncesi işlemler gerçekten de bir tür gizlilik sızıntısına karşı savunmasızdı, ancak yayınlandığı sırada Monero endişelerin çoğunu gidermişti. Yazarlara karşı adil olmak gerekirse, Monero'nun çözümlerini küçük bir dereceye kadar tartışıyorlar, ancak o zamanın kripto para birimi medya döngüsü üzerindeki etkisini etkilemeye yetmiyor. Dolayısıyla Wired makalesi.

Söz konusu Wired makalesini bir dönem yazısı olarak ve o dönemde ne kadar doğru ya da yanlış olduğunu inceleyebilirken, Monero'nun gizlilik garantilerinin neden zayıf olduğunun gerekçesi olarak bugün hala paylaşılıyor olması aslında bir analize davet ediyor parçanın günümüzde nasıl ayakta kaldığına dair. Bu daveti memnuniyetle kabul ediyoruz.

Makale hızlı bir şekilde okunduğunda, "[Bulgular] bugün Monero'yu gizlice harcamaya çalışan kimseyi endişelendirmemeli" gibi birkaç sansasyonel satır ve araştırmayı 'yeni' olarak öne süren makalenin tüm tonu görülüyor. büyük ölçüde yayına dayanmaktadır. Akademik makalenin kendisi, Monero kullanıcılarını, anonimliklerinin potansiyel olarak tehlikeye atılması konusunda uyarmak gibi tavsiyeler içeriyor; buna rağmen bu tartışmalar sadece 2014'ten beri sürmekle kalmıyor, aynı zamanda topluluğun toplanan çığlığı, insanların Monero'yu satın almamaları yönündeydi ve Monero'nun oldukça deneyseldi.

Peki ya eleştirilerin kendisi? Gerçek şu ki, Monero'nun bir mahremiyet parası olarak yaşadığı pek çok sorun ya Monero için artık geçerli değil ya da bir blockchain tabanlı kripto para kategorisi olarak mahremiyet koinleri ile ilgili ortak endişeler var. Bunları ele almaya başlayalım.

Monero'ya yönelik en sık alıntılanan eleştirilerden biri, blockchainin kalıcılığı ve değişmezliği nedeniyle, gelecekteki bir teknolojinin mahremiyeti ihlal etmesi durumunda Monero'nun tüm geçmiş işlemlerinin açığa çıkacağıdır. Başka bir deyişle, gizliliğinizin işleyen bir saati var.

Bunu yeterince vurgulayamayız. Kelimenin tam anlamıyla, gizleme ve mahremiyet için zincir üstü yöntemler kullanan her mahremiyet koini bu kusura sahiptir ve yine de sıklıkla Monero'ya karşı kullanılır (ironik bir şekilde, birçok kez mahremiyet koinleriyle aynı sorunla rekabet ederek) ve bu makalede de kullanılır. Bu eleştiriye verilen yanıt bazıları için şaşırtıcı olabilir ancak Monero, gizliliğe çok yönlü bir yaklaşıma sahip olması nedeniyle aslında diğer gizlilik koinlerine göre bu konuda daha az savunmasız olabilir.

Monero, sırasıyla halka imzalar, RingCT ve gizli adresler olmak üzere üç farklı teknoloji aracılığıyla çıkışları (göndericileri), tutarları ve alıcıları gizler. Bunlardan halka imzalar en zayıf olanıdır ve hem modern buluşsal yöntemlere hem de teorik, geleceğin mahremiyetini bozan teknolojilere karşı en duyarlı olanıdır. Bu, Monero topluluğu tarafından yıllardır biliniyor ve halka imza şemasını tamamen iyileştirmek veya değiştirmek için aktif araştırmalar sürüyor.

Ancak halka imzası tamamen bozulsa bile yalnızca gerçek çıktı ortaya çıkacaktı. Gönderen DEĞİL (bireysel olarak olduğu gibi), ancak çıktı. Bir çıktıyı bir kimlikle eşleştirmek imkansız değildir ancak daha fazla meta veri ve kaynak gerektirir. RingCT ve gizli adresin açığa çıkmayacağı gerçeğiyle birleştiğinde etki daha da azalır.

Wired makalesinin, yorum yapmak için Riccardo 'fluffypony' Spagni'ye ulaştığı bölümde yukarıdaki bilgileri hafifçe tartıştığına dikkat edilmelidir, ancak bu makaleye verilen süre kısadır ve neredeyse el sallayarak uzaklaşmış gibi görünmektedir. bu çok önemli bilgi. Anlayış eksikliği, özellikle günümüzde makaleyi ister istemez paylaşan insanlarla bu konuları tartışmaya çalışırken açıkça görülüyor.

Ele alınması çok daha zor olan bir diğer eleştiri ise dış dünyanın Monero'ya nasıl baktığı ve bunun Monero çevresindeki topluluğun koine nasıl baktığıyla nasıl bağlantılı olduğudur. Bunun bir örneği olarak okuyucuların makalenin başlığından öteye bakmalarına gerek yok: "Dark Web'in Favori Para Birimi Göründüğünden Daha Az Takip Edilemez".

Monero topluluğunda önemli miktarda zaman harcayan herhangi bir kişi, Monero topluluğunun, pazarlama veya benimseme çabalarına zarar verse bile, gerçek gizliliği elde etmenin ne kadar zor olduğunu göstermek için büyük çaba harcadığını doğrulayabilir. Topluluk, coini ve eksikliklerini doğru bir şekilde tartışan bol miktarda kaynak sağlarsa, bir noktada bu bilgisizlik, coinin %100 gizli olması için ihtiyaç duyduğu tek şeyin bu olduğuna inanan kullanıcının hatası haline gelir.

Bu noktaya gelindiğinde, Monero topluluğunun hem gizliliğini hem de buradaki zayıflıklar ve sonraki iyileştirmeler konusundaki dürüstlüğünü ciddiye aldığı açık olmalıdır. Söz konusu makale gibi makaleler Monero'daki bu yenilik ruhunu tamamen gözden kaçırıyor. Monero'yu, sadece kâr amaçlı ve eğitimsiz yatırımcı özentilerini avlayan, büyük iddialarda bulunan diğer kripto para birimlerine benzetiyor.

Gerçek bundan daha farklı olamazdı. Monero, zayıf yönlerinin son derece farkındadır; bunları geliştirmek, gevşek bağlantıları sıkılaştırmak ve dünyaya herkes tarafından kullanılabilecek özel, takas edilebilir bir kripto para birimi vermek gibi çok gerçek ama çok zor bir hedefe ulaşmak için inşa etmeye devam etmeyi amaçlamaktadır ve hepsini adil, merkezi olmayan ve topluluk odaklı bir şekilde yapın. Belki de sansasyon yaratmayı ve makale paylaşmayı bir kenara bırakıp rakipleri tanıtmanın zamanı gelmiştir. Belki başka bir hikaye anlatmanın zamanı gelmiştir.

daha fazla okuma