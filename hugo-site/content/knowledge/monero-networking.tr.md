---
title: "Konu Ağ Oluşturmaya Geldiğinde Her Monero Kullanıcısının Bilmesi Gerekenler"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero'nun ve aslında tüm kripto para birimlerinin internette çalışması hiç kimse için sürpriz olmamalı. Ancak bu ifade basit ve açık görünse de çoğu kişi bunun kendi mahremiyetleri açısından ne anlama geldiğini dikkate almıyor. Başka bir deyişle, Monero'nun internette çalışmanın doğası gereği koruyabileceği ve koruyamayacağı bazı şeyler var. Bu hususların bazıları yalnızca rahatsızlık verirken bazıları mutlak mahremiyetin gerekli olduğu bir senaryoda çok daha ciddidir. Monero kullanıcılarının ağda birbirleriyle nasıl etkileşim kurduğunu ve bunun gizlilik açısından ne anlama geldiğini öğrenmek için zaman ayıralım.

İşin önemsiz yönünden başlayarak, eğer bir kullanıcının internet erişimi yoksa, yeni bloklar indiremez, başkaları adına işlemleri yayamaz veya kendi işlemlerini gönderemez. Dikkat edilmesi gereken ilginç nokta, tam düğüme sahip, internet erişimi olmayan bir kullanıcının daha sonra gönderilebilecek bir işlemi çevrimdışı olarak oluşturabilmesidir. Bunun nedeni, bir halka imzasının saklanmak için yalnızca blok zincirinden gelen çıktılara ihtiyaç duymasıdır. [zil imzalarının nasıl çalıştığına dair kısa bir hatırlatma](/knowledge/ring-signatures), geçmişten seçilmiş, bağlantısız çıktılar koleksiyonu arasında bir kullanıcının gönderdiği gerçek çıktıyı gizler. Kullanıcının bu çıktılara tamamen indirilmiş bir blok zinciri (tam düğüm) biçiminde erişimi varsa, geçmiş çıktılardan halka imzasını oluşturabilir ve internet bağlantısı yeniden sağlandığında işlemi ağa yayabilir.

Uzak düğüm kullanan bir kullanıcı bunu yapamaz, çünkü kendi halka imzasını oluştururken, çıktıların halka imzasına dahil edilmesi için uzak tam düğümle iletişim kurar. İnternetin olmaması bu düğüme ulaşamayacakları anlamına gelir, dolayısıyla çevrimdışı işlem oluşturma yetenekleri yoktur.

Gizlilik hususlarından bazılarına devam etmeden önce, internetin bir bütün olarak nasıl çalıştığına dair kısa bir giriş yapalım. İnternetin tamamı diğer bilgisayarlara bağlanan bilgisayarlardan başka bir şey değildir. Bu kadar. Okumayı sevdiğiniz blog? Sadece başka birinin bilgisayarında barındırılan bazı dosyalar. Bu makaleyi okuduğunuz web sitesi (LocalMonero)? Bir bilgisayarda bir yerde barındırılan dosyalar ve kodlar. Büyük çılgın siteler bile bu şekilde çalışıyor. Örneğin YouTube'u ele alalım. Yalnızca Google'ın devasa bilgisayar sistemlerinde barındırılan video dosyaları ve siz onlara bağlanarak videoyu kendi bilgisayarınıza indirip izleyebilirsiniz.

Bu bilgisayarlar birbirlerini ayırt edebilirler çünkü internete bağlı her bilgisayara IP adresi adı verilen benzersiz bir kimlik numarası verilir. Bunlar tipik olarak noktalarla ayrılmış dört sayı kümesidir; örneğin: 172.66.35.7. Monero bilgilerinin internette nasıl taşındığını düşündüğümüzde bunu akılda tutmak önemlidir. Monero eşler arası bir ağdır (P2P), yani bilgisayarlar bir aracı kullanmak yerine doğrudan birbirine bağlanır. Yani bir kullanıcının tam düğümü yeni keşfedilen bir bloğu indirirken, bunu merkezi bir sunucudan değil, eşlerinden indiriyor. Bunun dezavantajı, kullanıcıların birbirlerine doğrudan bağlandıkları için birbirlerinin IP adreslerini bilmeleridir.

Peki? Problem ne? Bu sadece bir sayı, değil mi? Tam olarak değil. IP adreslerinin kendisi, kaynak ülke ve ağ sağlayıcısı gibi kullanıcı hakkında bilgiler içerir; ancak daha da kötüsü, internet servis sağlayıcıları (ISP'ler), hizmetlerini kullanan her kişinin IP adresini bilir. Bu, bu ISP'lerin ve birlikte çalıştıkları kişilerin bir kullanıcının internet trafiğini izleyebileceği ve bazı akıllı taktikler kullanarak Monero kullandığını keşfedebileceği anlamına gelir. Şimdi korkmadan önce oradaki ifadelere dikkat edin. Bu meraklıların yapabileceği tek şey, bir kişinin Monero ağındaki diğer düğümlere bağlandığını görmektir. Monero'nun gizlilik teknolojisi sayesinde kişi hakkında başka hiçbir şey sızdırılmıyor. Bir düğümü çalıştırıp çalıştırmadıkları ya da işlem gönderip göndermedikleri/ne zaman gönderdikleri ve bir işlemin gönderilip gönderilmediğine dair hiçbir bilgi bilinmiyor. Bu İSS'lerin görebildiği tek şey, kullanıcılarından birinin Monero ağına bağlandığıdır.

Şimdi, bazı yerlerdeki bazı insanlar için bu bilgi tek başına itibara veya özgürlüğe zarar vermeye yeterli olabilir. Veya herhangi birinin herhangi bir nedenle mahremiyetinizi ve internette yaptıklarınızı ihlal etmesi fikri sizin için kabul edilebilir değildir. Bu kişilerin Monero ağına yalnızca VPN, Tor veya I2P kullanarak bağlanmaları teşvik edilir; bunların tümü, kullanıcının IP adresini diğerlerinden gizleyen ve aynı zamanda kullanıcının İSS'sinden ne yaptığını gizleyen hizmetlerdir. Bu hizmetler arasındaki farklar bu makalenin kapsamı dışındadır, ancak konuyla ilgili yazılmış çok sayıda yüksek kaliteli makale vardır, bu nedenle ilgili kullanıcıların incelemesini öneririz!

Geri kalanımız için, Monero ağına bağlı olduğumuzu başkalarının bilmesinin o kadar da önemli olmadığını düşünebiliriz. Sonuçta, işlemlerimizin gerçek içeriği veya gönderiyorsak bile kamuya gizlidir, peki bunun ne zararı var? Bu doğru olsa da, kullanıcıların kripto para birimlerinin asıl çekiciliğinin kendi bankaları olduğu gerçeğini dikkate almaları teşvik ediliyor. Özel anahtarınızı elinizde tuttuğunuzda ve ona bir şey olursa, kimse kaybettiğiniz parayı geri kazanmanıza yardımcı olamaz.

Kendi bankanız olmak, yalnızca dijital güvenliğinizi değil, fiziksel güvenliğinizi de dikkate almak anlamına gelir. Monero ağına bağlanan bir bireyin bilgisi, ulus devletler gibi büyük ölçekli aktörlerin değil, kolay para kazanmak isteyen bilgisayar korsanları gibi bencil çıkarları olan daha küçük aktörlerin istenmeyen ilgisini çekebilir. Gerçekten de kripto dünyasının her yerinde bu tür senaryoların gerçekten gerçekleştiğine dair sayısız hikaye var.

Bu makalenin amacı korku çığırtkanlığı yapmak veya korkutmak değildir; bunun yerine kullanıcıları, web'de gezinme korumasının hangi yöntemlerinin kendileri için uygun olduğu konusunda araştırma yapmaya teşvik etme amacındadır. İyi haber şu ki, bu beceriler sadece Monero kullanımına değil, genel internet kullanımına da aktarılacak ve bu nedenle, internete giderek daha fazla bağlanan dünyamızda, bilgili bir kullanıcı güvende kalmak için gerekli bilgi ve becerileri biriktirmede hata yapamaz. ve gerçekten kendi bankaları olacaklar.

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