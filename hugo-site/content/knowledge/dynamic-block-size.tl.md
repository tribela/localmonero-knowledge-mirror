---
title: "Paano Nalutas ni Monero ang Problema sa Laki ng Bloke na Sinasalot ang Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Tandaan:** Lubos na inirerekomenda na basahin ng mambabasa ang aming mga artikulo ["Bakit May Tail Emission ang Monero"](/knowledge/monero-tail-emission) at [“Monero Mining: What Makes RandomX napaka Espesyal”](/knowledge/monero-mining-randomx). Binubuo ng artikulong ito ang mga konseptong ipinakita doon._

Sa tuwing tinatalakay ng mga indibidwal ang mga problema sa blockchain, ang isa sa mga unang salitang lalabas ay ang 'scaling'. Hindi lihim na ang mga blockchain ay hindi maganda ang sukat, ngunit karamihan sa mga tao ay hindi alam kung bakit.

Ang totoo, ang pag-scale ay talagang isang umbrella term na sumasaklaw sa dalawang magkaibang kategorya: Protocol support at technological support sa isang partikular na punto ng oras. Sa artikulong ito, itutuon namin ang aming pansin sa isa, ang suporta sa Protocol ay karaniwang sukatan kung gaano karaming mga transaksyon ang maaaring pangasiwaan ng protocol sa isang partikular na oras.

Ang Bitcoin ay may limitasyon sa laki ng block, na nangangahulugang kapag sapat na ang mga transaksyon na naisama sa isang bloke, anumang karagdagang transaksyon ay kailangang maghintay sa linya para sa susunod na block. Ang isang kapaki-pakinabang na pagkakatulad ay pag-iisip tungkol sa isang tren. Isang tren ang humihinto sa istasyon, at ang mga nasa linya ay pumasok. Kapag puno na ang tren, sinumang maiiwan sa labas ay kailangang maghintay para sa susunod.

Gumagamit ang Bitcoin ng mga bayarin upang matukoy kung sino ang papasok sa block o hindi. Sa pagbabalik sa analogy ng tren, maiisip ng isang tao ang isang potensyal na pasahero, na malapit nang maiwan, ay nag-aalok sa engineer ng tren ng limang dolyar upang bigyan siya ng upuan. Sumunod din ang ibang mga pasahero, at kalaunan ay may bidding war upang makita kung sino ang makakakuha ng mga upuan. Nasa driver ang pagpapasya kung gusto niyang igalang ang patakarang first-come-first-serve, ngunit nasa kanyang pinakamahusay na pinansiyal na interes na i-maximize ang kanyang kita sa pamamagitan ng pagkuha ng pinakamataas na bidder.

Sa pagkakatulad na ito, ang mga minero ay ang mga tsuper ng tren. Maaari nilang isama ang anumang mga transaksyon na gusto nila sa block, ngunit karaniwang pipiliin nila ang mga may pinakamataas na bayad na bayarin.

O kaya, kung hindi masyadong puno ang mga bloke, walang insentibo ang mga tao na magbayad ng mataas na bayarin dahil maraming libreng upuan na matitira.

Sa kasagsagan ng 2017 cryptocurrency boom, binaha ang Bitcoin ng mga transaksyon, at ang mga bayarin ay tumaas para sa mga gustong mapabilang sa susunod na block, o anumang malapit na hinaharap na block sa bagay na iyon. Nakita ng mga ayaw magbayad ng mataas na bayarin ang kanilang mga transaksyon na itinulak pabalik sa loob ng maraming oras, araw, o kahit na tuluyang umalis sa pila.

Ito ay isang nakakatakot na insight sa kung ano ang mangyayari sa Bitcoin kung ang madalas na pinag-uusapan tungkol sa 'mass adoption' ay mangyayari. Kung ang Bitcoin ay gagamitin ng masa, ang mga bagay ay magiging mas masahol pa kaysa sa 2017, at ang Bitcoin ay hindi naa-access ng sinuman maliban sa mga mayayaman, dahil lamang sa maliit na throughput dahil sa isang nakapirming laki ng bloke, na nagiging sanhi ng pagsakop sa merkado ng bayad. .

Nakita ito ni Monero at gustong gumawa ng kakaiba. Kaya nagpatupad ang mga developer ng Monero ng dynamic na blocksize.

Sa pangkalahatan, mayroon ding block size na takip ang Monero, ngunit ito ay malambot na takip. Kapag ang linya ng naghihintay na mga transaksyon ay masyadong mahaba, maaaring dagdagan ng mga minero ang laki ng mga bloke. Sa aming pagkakatulad ng tren, maaari mong isipin na magdagdag ng higit pang mga kotse ng tren upang magkasya sa mga dagdag na pasahero. Matapos mawalan ng laman ang pila, ang mga bloke ay lumiliit pabalik sa kanilang orihinal na laki pasulong.

Kung ito ay tila isang maayos na ideya, tila makatwirang itanong kung bakit ang Monero ang tanging cryptocurrency na nagpatupad nito. Bakit hindi ito idagdag sa Bitcoin para matigil ang mga isyu sa throughput?

Sa kasamaang palad, hindi ito posible. Mayroong ilang mga dahilan kung bakit, at gagawin namin ang aming makakaya upang ipaliwanag.

Palaging nasa pinakamahusay na interes ng isang minero ang magkaroon ng malalaking bloke. Sa malalaking bloke maaari silang magkasya sa mas maraming transaksyon, at kumita ng mas maraming pera mula sa mga bayarin, pati na rin ang mga reward sa block. Ito ay may potensyal na humantong sa mga pag-atake ng spam, kung saan ang isang tao ay nagpapadala ng maraming maliliit na transaksyon, na may maliliit na bayad, upang palakihin ang kadena. Itataas lang ng Miner ang block size isama silang lahat dahil pera ay pera, gaano man kaliit. Ito ay hahantong sa tuluy-tuloy na malalaking bloke na may kaunting pakinabang sa ekonomiya. Niresolba ito ng Bitcoin sa pamamagitan ng artipisyal na paghihigpit sa laki ng block, sa gayon ay bumubuo ng isang market ng bayad. Kailangang bayaran ng mga spam attacker ang iba pang mga user sa mga bayarin, at hindi na ito mura. Ngunit ito ay nangangahulugan na ang mga bloke ay napuno na iniiwan ang ilang mga transaksyon na naghihintay tulad ng nabanggit sa itaas.

Kaya paano magkakaroon ng mga dynamic na blocksize ang Monero ngunit maiiwasan ang mga pag-atake ng spam? Ang sagot ay simple, ngunit matalino. Ang isang parusa sa block reward ay ipinakilala kapag ang isang block ay mas malaki kaysa sa normal. Kung gusto ng isang minero na pataasin ang blocksize, ang reward na makukuha nila sa paghahanap sa block na iyon ay magiging mas mababa kaysa sa kung hindi man ay matatanggap nila. Kaya't tataas lamang nila ang blocksize kapag ang mga binayarang bayarin sa transaksyon ng mga user ay lumampas sa nawalang bahagi ng block reward. Halimbawa, kung mawawalan ng 0.5 XMR ang minero sa pamamagitan ng pagpapataas sa laki ng block, at ang kabuuan ng mga binabayarang bayarin sa transaksyon ay magiging 0.4 XMR, magkakaroon ng netong pagkawala ng 0.1 XMR kung tataasan nila ang laki, kaya tataas sila. huwag gawin ito. Sa kabaligtaran, kung ang kabuuang bayarin sa transaksyon ay idinagdag ng hanggang 0.7 XMR, magkakaroon ng netong pakinabang na 0.2 XMR, kahit na mawala sa kanila ang 0.5 XMR mula sa parusa sa block reward, kaya tataas ang laki ng minero.

Ang mga dynamic na bloke na ito, ay nagbibigay-daan sa network na lumago nang organiko, nang hindi pinaghihigpitan ang laki ng block upang makagawa ng market ng sapilitang bayad, habang iniiwasan pa rin ang mga pag-atake ng spam. Mayroong ilang higit pang mga anggulo na maaari naming tingnan ang ideyang ito, at higit pang mga dahilan kung bakit hindi ito posibleng idagdag sa Bitcoin, ngunit sa ngayon, umaasa kami na ang mambabasa ay may pag-unawa kung paano iniiwasan ni Monero ang ilang mga problema sa Bitcoin at ang mga derivative nito, at kung paano nito pinaplano na i-scale ang throughput nito sa hinaharap.

Karagdagang pagbabasa