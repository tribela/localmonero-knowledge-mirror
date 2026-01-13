---
title: "RingCT Monero İşlem Tutarlarını Nasıl Gizliyor?"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero'nun gizliliği, bozulduğu takdirde işlemlerin tamamını ortaya çıkaracak tek bir mekanizmaya değil, diğer parçaların zayıf yönlerini telafi ederken bütünsel gizlilik sağlamak için birlikte çalışan üç farklı teknolojiye bağlıdır. Bu üç aşamalı yaklaşım, [halka imzaları](/knowledge/ring-signatures), RingCT ve [gizli adreslerden](/knowledge/monero-stealth-addresses) oluşur. Bu üç teknoloji sırasıyla gerçek çıktıyı (gönderen), miktarı ve alıcıyı gizler. Bugün RingCT'den bahsedeceğiz.

RingCT muhtemelen üçü arasında en teknik olanıdır ve anlaşılması zor olabilir, bu nedenle tam olarak nasıl çalıştığını anlatmayacağız, bunun yerine bir miktarı bilmemenin ve yine de bununla ilgili şeyleri onaylamanın nasıl mümkün olduğunu göstereceğiz. . Ve endişelenmeyin, her zaman olduğu gibi birçok örnek kullanacağız.

Önce miktarlarla ilgili herhangi bir şeyi doğrulamanın neden önemli olduğunu keşfedelim. Neden onları tamamen gizli tutamıyoruz? Cevap şu: Fırsat verilirse insanların yoktan para yaratmasının akıllıca yolları var. Böyle bir şey nasıl işe yarayabilir? Bir örneğe bakalım.

Arkadaşınızdan bir ürün satın almak istiyorsanız ve o bunun için on dolar istiyorsa, o zaman siz on dolarla başlarsınız ve o da sıfırla başlar. Ona on doları verdikten sonra onun on doları var, senin ise sıfır. Sen onla başladın, şimdi onda var. Bu işlemde hiçbir para yaratılmadı veya yok edilmedi.

Kripto para birimleriyle akıllı bir kişi, ürün için on dolar verebilir ve bozuk para olarak sıfır dolar almak yerine iki doları geri alabilir. 0 ve 10'un 10 ve 0'a (veya 10=10) götürmesi yerine, artık 0 ve 10'un sonucu 10 ve 2'dir (veya 10=12). İki Monero yoktan var edildi. Bireyin bunu kendisine birkaç kez yapması durumunda kısa sürede devasa bir servete sahip olabileceğini tahmin edebilirsiniz.

Bitcoin ve diğerleriyle bunu görmek kolay olurdu. Bir işleme giren girdilere ve çıkan çıktılara bakarsınız ve gönderilenin alınana eşit olduğundan emin olursunuz. Bu miktarlar şifrelenmişse ve görünmüyorsa, kullanıcının gönderilen ve alınanın aynı olduğunu doğrulamasının hiçbir yolu yoktur.

Bitcoin gizliliğini artırmak amacıyla Gregory Maxwell, şifrelenmiş miktarlara izin veren ve bu süreçte hiçbir şeyin yaratılmadığını veya yok edilmediğini kanıtlayan yeni bir teknoloji olan Gizli İşlemleri (CT) yarattı. Çoğu gizlilik teknolojisinde olduğu gibi Bitcoin'e girmedi ancak Monero onu benimsemeye istekliydi. Sadece bir problem vardı. Halihazırda uygulanan halka imza teknolojisi, önerilen fikirle uyumsuzdu. Böylece, o zamanki MRL araştırmacılarından biri olan Shen Noether, CT'yi, CT'nin halka imzalarıyla uyumlu bir versiyonu olan RingCT'ye dönüştürdü.

Bir kez daha, bunun çalışma şekli oldukça tekniktir ve bir giriş makalesinde açıklanması zor olacaktır. Sadece bilmesi gereken kriptografi meraklıları için internette CT'nin iç işleyişi hakkında yazılmış çok sayıda derinlemesine makale var. Geri kalanımız için bu makale, miktarları gizlemenin nasıl mümkün olabileceğini gösterecek, ancak yine de hiçbir şeyin yaratılmadığını veya yok edilmediğini kanıtlayacaktır.

Diyelim ki Alice, Bob'a para göndermek istedi. Alice, 10 XMR alacak olan Bob'a 10 XMR gönderecek. 10=10 yani burada yanlış bir şey yok. Ancak Alice kimsenin ne kadar gönderdiğini bilmesini istemiyor. Böylece o ve Bob ortak bir sır yaratırlar. Temelde sadece ikisinin bildiği bir sayı. Diyelim ki bu sayı 22. Şimdi Alice 10'u (gerçekte gönderdiği şeyi) 22 ile çarparak 220'yi buluyor. Bu onun ağla paylaştığı sayıdır.

Madenciler gizli numarayı bilmiyorlar. Eğer öyle olsaydı, kendilerine gösterilen sayıyı gizli numaraya bölerek gönderilen gerçek tutarı elde edebilirlerdi. Ama bunu yapmadıkları için yapamazlar. Ancak Bob'un 220 alacağını görüyorlar. 220 gönderildi. 220 alındı. 220 = 220. Bu şekilde ağ, Alice'in Bob'a gönderdiği gerçek miktarı bilmeden hiçbir Monero'nun yaratılmadığını veya yok edilmediğini doğrulayabilir.

Bob paylaşılan gizli numarayı bildiğinden, parayı aldığında Alice'in gönderdiği gerçek tutarı (10) bulmak için sadece 22'ye böler. Hem Alice hem de Bob ne kadar gönderildiğini ve ne kadar alındığını bilir. herkese sahte bir numara veriliyor.

Bir kez daha söylüyorum ki CT'nin çalışma şekli bu değil ama böyle bir şeyin nasıl mümkün olabileceğine dair bir fikir veriyor. Gerçek yol, Pedersen taahhütleri, gönderilen iki miktar (alıcıya şifrelenmiş bir miktar ve ağa bir taahhüt tutarı) gibi şeyleri içerir ve… evet, insanın tüm bunların içinde nasıl kaybolabileceğini görmek zaten kolaydır.

Ancak dikkat edilmesi gereken nokta, RingCT'nin bir işlemde iki taraf arasında gerçekleştirilen tutarı gizlerken diğer iki sayı kümesini gizlememesidir.

Birincisi coinbase işlemleridir. Bu terim size tanıdık gelmiyorsa temel olarak madencilerin bir sonraki bloğu buldukları için aldıkları ödül anlamına gelir. Bu numara gizli değil. Protokolün bir madenciye hizmetleri karşılığında ne kadar ödül verdiğini herkes görebilir. Bu sayede tüm coinbase işlemlerinin toplanmasıyla mevcut Monero miktarı bilinebilecek. Toplamları dolaşımdaki mevcut Monero'ya eşit olacaktır.

Gizlenmeyen ikinci sayı, bir kullanıcı işlem gönderdiğinde madencilere ödenen ücrettir. Madencilerin kime öncelik vereceğini bilmesi için ücretlerin açık olması gerekir. Bu, kullanıcıların gizliliklerine zarar vermelerinin bir yoludur, ancak sanki birisi her işlem gönderdiğinde (0,12345 gibi) benzersiz bir madencilik ücreti kullanıyormuş gibi, o zaman işlemleri bağlanabilir.

Bu vakaların dışında, RingCT 2017'den beri Monero tutarlarını saklıyor ve bu nedenle kolektif gizliliğimiz daha da güçlü.

daha fazla okuma