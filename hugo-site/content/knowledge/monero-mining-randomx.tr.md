---
title: "Monero Madenciliği: RandomX'i Bu Kadar Özel Kılan Nedir?"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
30 Kasım 2019'da Monero altı ayda bir hard fork'unu gerçekleştirdi; en çok beklenen değişiklik eski PoW algoritması cryptonight'tan tamamen yeni, dahili olarak geliştirilen RandomX'e geçişti. Monero topluluğu RandomX'in eşitlikçi madenciliğe doğru büyük bir adım olduğuna inanıyor, ancak durumun böyle olup olmadığını görmek için daha derine inelim.

## Amaç

RandomX'in bir gelişme olup olmadığına karar vermek için öncelikle madenciliğin amacının ne olduğunu anlamalıyız. Madencilik, Nakamoto Konsensüsü aracılığıyla bir blockchain'i çifte harcamalardan korur. Bunu nasıl yaptığının tam incelikleri bu makalenin kapsamı dışındadır ancak bunlar internetteki birçok farklı kaynaktan öğrenilebilir. Önemli olan, güvenliğin, başka bir blok oluşturmak için gerekli matematiksel çözümü bulmak üzere birbirleriyle rekabet eden bilgisayarlar (madenciler) tarafından üretilen karmalardan gelmesidir. Bunu yaparken blok zincirine yeni işlemler eklerler. Çalışmalarının (hash) karşılığında yeni basılan paralarla telafi edilirler.   
  
Bu kurulumda ortaya çıkabilecek çok sayıda sorun var ve bunların doğru çalışması için uygun teşvikler gerekiyor, ancak biz ortaya çıkabilecek belirli bir soruna odaklanacağız. Madenciliğin bir rekabet olması gerekiyorsa, bir madenci avantaj elde ettiğinde ne olur?

## Arka plan

Bağlam açısından, madencilik donanımı hakkında biraz konuşalım. Madenciler işi yapmak için bilgisayarları kullanıyor ancak hepimiz her bilgisayarın eşit şekilde üretilmediğini biliyoruz. Bazı bilgisayarlar yapay zeka ağlarını veya yoğun oyunları çalıştıracak kadar güçlüyken bazıları basit görevlerle bile mücadele ediyor. Bilgi işlem gücündeki bu farklılıklar aynı zamanda hash oranını veya blok çözümleri arama hızını da etkiler.   
  
Ancak bilgisayarlar arasındaki bu farklar bile, normal bilgisayarları birkaç kat geride bırakan, Uygulamaya Özel Entegre Devreler (ASIC'ler) olarak da bilinen özel donanımların hash oranlarıyla karşılaştırıldığında sönük kalır.  
  
ASIC'leri bu kadar güçlü kılan şeyin ne olduğunu keşfetmeye biraz zaman ayıralım. Tüm bilgisayarların, birçok şeyi yapabilmesinden ama hiçbir şeyi iyi yapmamasından tek bir şeyi yapmasına ama onu çok iyi yapmasına kadar uzanan bir spektrumda bir yere düştüğünü hayal edin. CPU'lar ve ASIC'ler bu spektrumun zıt uçlarında yer alır.  
  
Tüm standart bilgisayarlarda bulunan CPU'lar ilk uçtadır. Web'de gezinmek, oyun oynamak veya video işlemek gibi pek çok şeyi yapabilirler, ancak bunların hiçbirini özellikle iyi yapamazlar. Ancak bu esneklik, verimlilik pahasına gelir.  
  
ASIC'ler diğer tarafta, tek bir şeyi yapabiliyorlar ama bunu inanılmaz bir hızla yapıyorlar. Yalnızca tek bir matematiksel işlevi gerçekleştirebilirler, ancak diğer her şeyi göz ardı edebildikleri için performans kazanımları astronomiktir. Ancak bu verimlilik esneklikten ödün verilmesine neden olur; dolayısıyla eğer fonksiyon çok az da olsa değişirse (örneğin, x + y = z, 2x + y = z olarak değişirse), o zaman ASIC tamamen çalışmayı bırakacaktır.   
  
Herkes bir ASIC'e sahip değildir, ancak herkesin kendi bilgisayarı vardır. Bu durum haksız avantaja yol açabilir.

## Eğlenceli bir benzetme

Eğer bu hala kafa karıştırıcıysa, belki aşağıdaki benzetme yardımcı olabilir. Her saat başı bin doların verildiği bir piyango hayal edin ve bu piyango, kendi biletlerinizi basabilmenizi sağlıyor! Saniyede bir bilet basabilen ev yazıcınızda basabildiğiniz kadar bilet basmaya başlıyorsunuz. Elektrik ve mürekkep masraflarını çıkardıktan sonra, piyangoyu yalnızca birkaç haftada bir kazansanız bile hâlâ kâr elde edebileceğinizi görüyorsunuz.  
  
Zamanla, yazıcılara ayrılmış bir oda elde edene kadar operasyonunuzu genişletirsiniz. Toplam 20. Her şey yolunda... ta ki önemli bir güne kadar.  
  
Büyük haberler var. Birisi yeni bir tür yazıcı icat etti. Yalnızca piyango bileti basabilir. Resimleri veya ofis belgelerini basamaz veya çift taraflı baskı yapamaz. Sadece piyango biletleri. Ancak bunları saniyede 1000 bilet hızında basabiliyor. Küçük yazıcı odanıza bakıyorsunuz. 20 yazıcı. Bu canavar yazıcılardan BİRİNE ayak uydurmak için 980 yazıcıya daha ihtiyacınız var ve eğer birinin iki tane varsa…?  
  
Artık elektrik ve mürekkep maliyetlerini karşılayamayacağınız için ne yazık ki piyango oyunundan çıkıyorsunuz.  
  
Fakat bekle! Birkaç hafta sonra yeni haberler var! Biletin tasarımı değişti. Eskiden üstte olan rakamlar artık altta. Yeni canavar yazıcılar o kadar esnek değil ki bunu yapamıyorlar. Sadece önceki tasarımı yapabildiler. Bir kez daha mutlu bir şekilde baskı almanız çok uzun sürmez. En azından birisi yeni tasarım için yeni bir canavar yazıcı yapana kadar.

## RastgeleX

RandomX tüm bunların neresine uyuyor? ASIC'lerin yapımını çok zorlaştırarak ASIC'lerin avantajını eşitlemeye çalışıyor. Bunu, madencilerin bir algoritmaya dayalı karma işlemi yerine rastgele kod oluşturmasını ve yürütmesini gerektirerek yapar.  
  
Bunun aslında herhangi bir şeye nasıl yardımcı olduğu kafa karıştırıcı olabilir, bu yüzden yazıcı benzetmemize geri dönelim. Tasarım değiştiğinde ne olduğunu hatırlıyor musunuz? Eski canavar yazıcılar her gece demode oluyor ve yenilerinin, yeni tasarım göz önünde bulundurularak geliştirilmesi gerekiyordu. Her yeni piyango ödülü bileti, her yeni ikramiye için yeni bir tasarım standardına uymak zorunda olsaydı ne olurdu?   
  
Yeni bir canavar yazıcı yaratmak inanılmaz derecede zorlaşırdı. Artık tek bir bilet tasarımı üzerinde plan yapamazsınız. Tasarım rastgele olduğundan, canavar yazıcı üreticilerinin renk yetenekleri, farklı harfler, kenarlıklar ve şekiller yazdırma yolları ve daha fazlasını eklemesi gerekecekti. Kısacası, icat ettikleri makine standart, normal bir yazıcı olacaktı. Tıpkı herkesin yaptığı gibi.  
  
Bu rastgeleliği bilet tasarımına basitçe uygulayarak, özel donanımdan elde edilen büyük avantajı önemli ölçüde azalttık. RandomX de aynısını yapar ancak madencilikle yapar.  
  
Bu şekilde, seçilmiş birkaç varlıklı kişinin elde ettiği avantajlar en aza indirilir; sanki RandomX madenciliği için "ASIC'ler" oluşturmaya yatırım yapıyorlarmış gibi, aslında sadece daha güçlü, daha iyi CPU'lar icat edecekler ve bu da tüm dünyaya fayda sağlayacaktır.  
[ X1455X] Bu, 20 bilet yazıcısı olan küçük adamın oyuna geri döndüğü anlamına geliyor. Bu zengin bireyler hâlâ ondan daha fazla yazıcı satın alabildiği için hâlâ zor zamanlar geçirebilir, ancak en azından artık yalnızca tek bir makineden elde edilen büyüklük sıralamasında geride kalmış değil. Kendi küçük haliyle rekabetçidir.  
  
Küçük bir adamın bile Monero madenciliği konusunda rekabetçi olabileceğini bildiğimizden, herkesi solo madencilik desteğine sahip Monero GUI cüzdanını kullanarak veya topluluk tarafından sağlanan yazılımı indirerek denemeye teşvik ediyoruz. Kolaydır, rekabetçidir ve herkese açıktır.

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

  * [Monero Neden Dash, Zcash, Zcoin (Lelantus ile Bile), Grin ve Wasabi Gibi Bitcoin Karıştırıcılarından Daha İyidir (Mayıs 2020'de Güncellendi)](/knowledge/why-monero-is-better)/