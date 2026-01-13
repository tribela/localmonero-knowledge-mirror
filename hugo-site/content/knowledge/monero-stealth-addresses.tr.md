---
title: "Monero Gizli Adresleri Kimliğinizi Nasıl Korur?"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero gizliliğe üç yönlü bir yaklaşım uyguladı. Bu teknolojiler, gerçek çıktıyı (göndereni) gizleyen [halka imzaları](/knowledge/ring-signatures), miktarları gizleyen RingCT ve alıcıyı gizleyen gizli adreslerdir. Bugün bu bahsedilen teknolojilerin sonuncusunu tartışacağız: gizli adresler.

Bir kişinin kime gönderim yaptığını gizlemek istemesinin birçok nedeni vardır. Kimsenin bizi bu örneklerin hepsinin çirkin davranışlar olduğuna inandırmaya çalışmasına asla izin vermemeliyiz. Popüler olmayan bir siyasi partiye para göndermek, hayır kurumlarına bağış yapmak veya kültürün 'iptal edildiğini' düşündüğü şeyleri desteklemek gibi şeylerin tümü, bir kişinin, tepki korkusuyla harcama davranışlarını gizlemek isteyebileceği yerlere örnektir, ancak doğası gereği tamamen meşrudur.[X840X ] 

Şeffaf bir blok zincirinde, kişinin işlemlerinin gönderildiği adresler herkes tarafından görülebilir. Madencilerin paranın nereye gittiği konusunda anlaşamamaları durumunda, parayı bir bloğa ayırmamayı seçebileceklerini ve sansüre dirençli gibi görünen bir platformda bu işlemi etkili bir şekilde sansürleyebileceklerini dikkate almak önemlidir. Bunu sansürü imkansız hale getirmenin tek yolu, tüm zincir üstü meta veriler çeşitli yollarla gizlendiği için madencilerin işlemler arasında ayrım yapamamasıdır. Monero'nun meşhur olduğu bir şey.

Monero, bu şeffaf adres sorununu, aslında Bitcoin için 2011 yılında Bitcoin Talk forumu kullanıcısı ByteCoin tarafından geliştirilen bir teknoloji olan gizli adresleri uygulayarak çözmektedir (daha sonra gizli adresleri entegre edecek olan Bytecoin ile ilişkisi bilinmemektedir). Bununla birlikte, gizli adreslerin mevcut biçimi, ilk fikre göre bazı iyileştirmelere sahiptir. Ama önce nasıl çalıştıklarını görmek için tuşlardan bahsedelim.

Kripto para dünyasında olup da anahtarlar hakkında bir şey duymamak zor. 'Özel anahtarınızı yedekleyin' gibi ifadeler yaygındır, ancak ortalama bir Joe "genel anahtar" ve "özel anahtar" kelimelerini duyduğunda korkar ve bunun anlaşılamayacak kadar teknik ve kafa karıştırıcı olacağını düşünür. Ama endişelenme. Ağırdan alacağız ve bol miktarda örnek kullanacağız.

Kripto para birimlerinde kullanılan iki tür anahtar, daha önce de belirtildiği gibi, genel ve özeldir. Bu iki anahtar genellikle bir çift halinde gelir; bu, belirli bir genel ve özel anahtarın birbirine bağlı olduğu anlamına gelir. Aslında genel anahtar genellikle özel anahtardan türetilir; yani özel anahtarı biliyorsanız cüzdanınız bazı hesaplamalar yapabilir ve her seferinde doğru genel anahtarı bulabilir.

Artık adlarından da anlaşılacağı gibi, genel anahtar herhangi bir sonuç olmaksızın genel olabilir. Genellikle bu, kripto para cüzdanınıza para almak için paylaştığınız adresin bir parçasıdır. Ayrıca kendi adını taşıyan özel anahtar, paylaşılmaması gereken bir anahtardır. Bu, bir işlemi imzalamanıza ve harcamanıza olanak tanıyan şeydir; dolayısıyla çalınırsa veya paylaşılırsa, o zaman alçak üçüncü taraf paranızı genellikle kendilerine harcayabilir.

Buna kolay bir benzetme, bir asma kilit ve onu açmak için gereken anahtar olabilir. Açık asma kilit serbestçe paylaşılabilir ve aslında bu asma kilitle her şey kilitlenebilir, ancak asma kilidin kapalı olduğu herhangi bir şeyi yalnızca anahtara sahip olan kişi açabilir. Asma kilit kopyalanıp paylaşılabilir, anahtar olmamalıdır.

Bu anahtarlar genellikle kullanıcıdan soyutlanır, dolayısıyla onları hiçbir zaman gerçekten göremezsiniz. Monero'da bunlar hiç de korkutucu bir alfasayısal dizi olarak görünmüyor. Monero'da sıradan kullanıcı özel anahtarı kendi tohumu olarak bilir. Tohum (eğer yazmadıysanız yazmanız gerekir) aslında sadece insanlar tarafından okunabilen bir özel anahtardır. 

Gördün mü? Sonuçta o kadar da korkutucu değil. Gizli adreslere geri dön.

Daha önce de belirtildiği gibi, gizli adresler başlangıçta Monero için değil, Bitcoin için yapılmıştı. Çoğu acemi fikirde olduğu gibi, bu ilk yinelemenin de sorunları vardı. Bir sonraki girişim, CryptoNote'un Monero'nun öncüsü olan Bytecoin için Nicholas van Saberhagan tarafından yaratılmasıyla geldi ([Monero ve Bytecoin geçmişimizi buradan görebilirsiniz](/knowledge/monero-history)) ve orijinaline göre kesin bir gelişme olmasına rağmen, o bile bazı ince kusurlar.

Sonunda, artık kullanılmayan başka bir gizlilik kripto para biriminin geliştiricisinden son bir yineleme ortaya çıktı ve bu fikirle ilgili olağanüstü gizlilik ve güvenlik sorunlarını düzeltti. Bu, sonunda Monero'ya da girdi ve bugün kullanılan da budur.

Bu gizlilik ve güvenlik sorunları çözülmüş olsa da, gizli adresler blockchain teknolojilerine daha önce var olmayan farklı bir tuhaflık kattı. Tarama ihtiyacı. Alıcı adresler blockchain'de herkese açık olarak görüntülenmediğinden, alıcı herhangi bir işlemin kendisine ait olup olmadığını asla bilemez, dolayısıyla kendisine ait olup olmadığını görmek için gelen her işlemi kendi özel anahtarıyla taraması gerekir.

Şeffaf paralarla tek yapmaları gereken, adresinize bir işlem gönderilip gönderilmediğini kontrol etmektir. Kolay bir evet veya hayır sorusu. Ancak gizli adresler kullanıldığında, her işlem potansiyel olarak size gönderiliyor olabilir, bu nedenle açılıp açılmadığını görmek için her birinin kilidini özel anahtarınızla açmaya çalışmanız gerekir.

Bu, Bitcoin ve türevlerinin sahip olmadığı ekstra bir adımdır ve Bitcoin'den çok daha uzun bir süre açmadığınız bir cüzdanı senkronize etmenin yanı sıra, ilk cüzdan kurulumunu yapar. Ancak sahip olduğu gizlilik garantilerinin kilidini açmak için bu ödünleşim gereklidir. Gizlilik üçlüsünün en zayıf noktası olan halka imzaların aksine, gizli adreslerin buluşsal yöntemlere duyarlı olmadığı unutulmamalıdır. Tüm internetin güvendiği, denenmiş ve gerçek eliptik eğri kriptografisine dayanır; dolayısıyla bunun kırılması, yalnızca Monero'nun değil, genel olarak bilgisayar güvenliğinin sona ermesi anlamına gelir.

daha fazla okuma