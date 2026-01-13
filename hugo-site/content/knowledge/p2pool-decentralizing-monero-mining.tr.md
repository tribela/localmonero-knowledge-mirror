---
title: "P2Pool ve Monero Madenciliğinin Merkezi Olmamasındaki Rolü"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero projesinin temel amaçlarından biri, günümüzde kripto para ağlarının güvenliğinin sağlanmasının ana yolu olan iş kanıtı (PoW) madenciliğine yeni ve yenilikçi yaklaşımlar aracılığıyla adil, merkezi olmayan ve güvenli bir ağ sağlamaktır.[ X230X] 

RandomX gibi benzersiz bir madencilik algoritması [bu amaç için son derece önemli olsa da, bilgisayarı olan herkesin ağın güvenliğine makul miktarda katkıda bulunabilmesini sağlamaya yardımcı olurken, RandomX sorunları çözmez havuz madenciliği nedeniyle meydana gelebilir. Havuz madenciliği, Monero da dahil olmak üzere günümüzde kripto para madenciliği yapmanın açık ara en yaygın yoludur, ancak şükürler olsun ki p2pool madenciliğinin ortaya çıkışı bunu hızla değiştiriyor.](/knowledge/monero-mining-randomx)

## Havuz madenciliği nedir?

Havuz madenciliği, madencilerin ağdaki bir bloğu çözme girişimi görevini paylaşmalarının ve ardından havuzun bulduğu tüm bloklar için ödülleri eşit olarak paylaşmalarının bir yoludur. Bu, madencilere ödeme sıklığının Monero madenciliği ile karşılaştırıldığında eşitlenmesine son derece yardımcı olsa da, ciddi merkezileştirme sorunları da yok değil.

Her madenci havuza iş katkısında bulunurken, yaptıkları her işin kontrolünü bırakır ve buldukları havuzun kendisine bloke eder, havuzun ödülleri tüm madenciler arasında ödül miktarına göre dürüst ve adil bir şekilde paylaşacağına güvenir. her birinin yaptığı iş. Her şey yolunda giderse, havuz operatörü tüm madencilerin çalışmalarını toplar, ağa gönderir ve ödülleri eşit olarak paylaşır.

## Havuz madenciliğindeki sorun nedir?

Maalesef bu tamamen güvene dayanıyor ve havuz operatörünün madencilerin yaptığı işlerle ilgili kötü şeyler yapmasına izin veriyor. Havuz operatörü, yapılan işi ağa saldırmak için kullanabilir, fonları iki katına çıkarmaya çalışabilir (eğer havuz yeterince büyükse) veya madenciler tarafından yapılan işi kendilerine ödeme yapmak için kullanabilir ve madencileri çalışmaları için asla uygun şekilde ödüllendirmez. .

Ağa yönelik en büyük risk, ağın hashrate'inin %51'den fazlasının kendi kontrolü altında olduğu bir havuzun (veya birlikte çalışan birden fazla havuzun) riskidir; çünkü bunu hile yapmak ve parayı iki kez harcamak için kullanabilirler (çift harcama) saldırı) veya ağın kurallarını değiştirme girişiminde bulunmak.

## p2pool nedir?

p2pool, ilk olarak 2011 yılında Bitcoin madenciliği için yaratılmış bir kavramdır, ancak hiçbir zaman geniş çapta benimsenmemiştir ve Bitcoin'de pratik olarak kullanılmamıştır. Neyse ki, RandomX'in arkasındaki kilit geliştiricilerden biri olan SChernykh, tatilini p2pool'un Bitcoin uygulamasıyla ilgili bazı sorunlara çözümler üreterek ve tüm yazılımı sıfırdan yeniden yazarak geçirdi.

Monero'daki p2pool, madencilerin blokları çözmek ve işi paylaşmak amacıyla p2pool için özel düğüm yazılımı kullanarak Monero ağını güvence altına almak için birlikte çalışmasına tamamen güvensiz bir yol sağlar.

Bu, her madencinin gerçekleştirdiği işin, cüzdan adresinin ve ne kadar Monero kazandıklarının kaydını tutan ve ardından ödülü bir güven içinde ödeyen yeni bir blockchain ("yan zincir") kullanılarak yapılır. -daha az ve merkezi olmayan bir yol. Bu yan zincirde çok daha az madenci olduğundan, blokları bulmak ve göndermek ana Monero ağına göre çok daha kolaydır, bu da madencilerin tek başına Monero madenciliği yapmaya kıyasla tutarlı ödemeler almasını kolaylaştırır.

## p2pool havuz madenciliği sorunlarını nasıl çözüyor?

p2pool'da merkezi bir havuz, merkezi bir havuz operatörü veya fonları elinde tutan ve ödemeleri dağıtan tek bir kişi yoktur. Bu madencilik tarafından p2pool aracılığıyla kolektif olarak yapılan tüm işler, meşru olduğundan emin olmak için p2pool blok zinciri ve diğer düğüm operatörleri tarafından kontrol edilir ve tüm madencilere, doğrudan bir blok bulunduğunda anında yaptıkları işe göre ödeme yapılır. bulunan bloktaki ödüller.

Madenciler merkezi bir havuz yerine p2pool'u kullanmayı seçtiklerinde, havuz operatörlerinin tüm gücünü ve güvenini ortadan kaldırır ve çalışmalarının ağın iyiliğine ve kendi ödüllerine katkıda bulunmasını sağlar, ağ saldırıları, kötüye kullanım riskini azaltır yaptıkları işin ya da borçlu oldukları ödüllerin çalınmasının.

Bu sadece onların kendi çıkarlarını korumalarına yardımcı olmakla kalmıyor, aynı zamanda merkezi havuzların bir bütün olarak Monero ağı için oluşturabileceği riski de azaltıyor. P2pool kullanımı aynı zamanda ulus devletlerin veya düzenleyicilerin ağın sağlığına yönelik oluşturabileceği risklerin azaltılmasına da büyük ölçüde yardımcı olur; zira baskı uygulayacak merkezi havuz operatörleri, dayanılacak coğrafi havuz yoğunluğu veya başka herhangi bir kolay baskı noktası yoktur. Monero'ya karşı kullanmaları için.

## Dezavantajları nelerdir?

Şükür ki Monero'daki p2pool iyi tasarlanmış, iyi oluşturulmuş ve son derece iyi çalışıyor! Ancak p2pool madenciliğinin ana dezavantajı, p2pool'u kullanmak isteyen her madencinin kendi Monero düğümünü çalıştırmak zorunda olmasıdır, bu da başlangıç sürecinin biraz daha karmaşık olmasına neden olur. Ancak bu düğüm daha sonra blokların inşası ve kontrolü için gerekli tüm bilgileri hesaplamak için kullanılır ve madencinin yapılan iş üzerinde tam kontrole sahip olmasını sağlar. Düğüm aynı zamanda madencilerin kendi cüzdanları için uzak bir düğüm olarak da işlev görebilir, ağa katkıda bulunabilir ve çok daha fazlasını yapabilir.

Merkezi madencilikten diğer önemli fark, p2pool kullanan küçük madencilerin büyük bir merkezi havuza göre biraz daha fazla "varyansa" veya ödemeler arasındaki süreye sahip olmasıdır - ancak's _Bunun zamanla daha az Monero kazanmanıza yol açmayacağını belirtmek son derece önemli! p2pool zamanla küçük madenciler için bile merkezi havuzlar kadar karlı olacaktır. Bu farklılığın bir kısmı, hizmetleri için ödeme yapacak merkezi bir havuz operatörü olmadığından, p2pool'un yerel olarak %0 ücrete sahip olmasıyla da dengeleniyor!_

##  Nasıl başlayabilirim?

Neyse ki, Monero''in p2pool uygulamasının mükemmel tasarımı ve toplulukta p2pool yoluyla madencilik sürecini basitleştirmeye yardımcı olmak için zaman ayıran çok sayıda insan nedeniyle, başlamak zamanla daha da kolaylaşıyor. p2pool ile madenciliğe başlamanın birkaç yolu vardır, ancak teknik ayrıntılar bu makalenin kapsamı dışında olduğundan, işletim sisteminize bağlı olarak aşağıdaki bağlantıya geçmekten çekinmeyin:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Daha fazlasını nasıl öğrenebilirim?

Bu, p2pool madenciliği konusunda merakınızı artırdıysa, p2pool ile ilgili bazı ek bağlantılar ve açıklayıcılar, nasıl çalıştığı ve Monero için ne anlama geldiği için aşağıya göz atın:

  * [p2pool için resmi Github](https://github.com/SChernykh/p2pool)
  * [p2pool kullanımına ilişkin resmi belgeler](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool artık yayında](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, p2pool](https://p2pool.observer/)
için bir tür "blok gezgini" 
  * [Monero p2pool docker-oluşturma](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Merkezi Olmayan XMR Madencilik Havuzu P2Pool'u geliştirmesi üzerine](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

daha fazla okuma