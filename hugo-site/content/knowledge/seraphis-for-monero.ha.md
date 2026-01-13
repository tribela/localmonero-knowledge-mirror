---
title: "Seraphis: Abin da Zai Yi wa Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: haɓaka ƙirar ƙirar ƙira don ma'amalar Monero

Wannan sakon yana bayyana [ Seraphis ](https://github.com/UkoeHB/Seraphis), saitin tsarin tsarin ma'amala da abstractions wanda mai ba da gudummawar bincike na bogi [ ` koe ` ](https://github.com/UkoeHB) don yanayin yanayin Monero, kuma tare da ci gaba da binciken tsaro. ta mai ba da gudummawa mara suna [ ` coinstudent2048` ](https://github.com/coinstudent2048).  
Muna yin wasu sauƙaƙawa kuma muna barin wasu cikakkun bayanai na fasaha don tabbatar da tsabta; saboda wannan dalili, kuma saboda ƙirar Seraphis har yanzu yana ci gaba, masu karatu masu sha'awar ya kamata su koma ga takaddun Seraphis don ƙarin sabbin bayanai.

## Ma'amaloli a Monero

Lambobi kamar Bitcoin da Monero da sauransu sun dogara da abin da ake kira "samfurin fitarwa" na aiki, inda wani _fitarwa_ wakiltar darajar da za a iya canjawa wuri.  
Ma'amaloli suna cinye abubuwa ɗaya ko fiye da mai aikawa ke sarrafawa, kuma suna haifar da sabbin abubuwan da aka kai ga masu karɓa (ko komawa ga mai aikawa azaman canji); Dole ne ma'amala ta daidaita a cikin abin da ake cinyewa dole ne ya ƙunshi jimlar ƙimar daidai daidai da ƙima a cikin sabbin abubuwan fitarwa (da kuɗin da aka sanya hanyar sadarwa).  
A cikin ka'idoji da yawa kamar Bitcoin, ana rubuta ƙimar da ke cikin abin fitarwa a bayyane, kamar yadda mai karɓa yake.  
Bugu da ƙari kuma, ta hanyar kallon blockchain, yana da mahimmanci don ganin ko kuma lokacin da aka kashe kayan aiki (wato, idan an cinye shi a cikin ciniki na baya, da kuma wace ciniki ya kashe shi).

Sabanin haka, ka'idoji kamar Monero suna gabatar da wani tsari na daban: 

  * Ana ɓoye ƙimar fitarwa kuma ba a bayyane akan toshewar
  * Ana ɓoye adiresoshin masu karɓa ta amfani da ka'idar yin jawabi na lokaci ɗaya
  * Ko an kashe wani fitarwa ko a'a an rufe shi ta hanyar amfani da sa hannu marasa ma'ana

Sakamakon shi ne, rashin bayanan waje, yana da wuya a tantance ko an kashe abin da aka bayar, menene ƙimarsa, da kuma wanda yake karɓa.

Ana kiran ka'idar ma'amala ta Monero na yanzu _RingCT_ , kuma yana amfani da tubalan gine-gine da yawa don cimma waɗannan manufofin ƙira.

  * _Ƙaddamarwa_ yana ɓoye adadin ta hanyar lissafi-mai amfani
  * _Tabbatattun Range_ suna hana ambaliya wanda zai iya haifar da wadata
  * _Sa hannu na zobe masu iya haɗawa_ suna ba da rashin fahimta da hana yunƙurin kashe kuɗi sau biyu
  * _Rarraba ƙaddamarwa_ yana tabbatar da ma'auni na ma'amaloli
[X1785] 

Waɗannan tubalan ginin an haɗa su a hankali don gina ka'idar RingCT.

Kadari mai amfani na ka'idar RingCT ita ce ana iya canza wasu tubalan gini ko haɓaka ta hanyar da za ta ci gaba da ƙira da kaddarorin gaba ɗaya, amma hakan na iya samar da inganci ko haɓaka tsaro. A haƙiƙa, waɗannan nau'ikan haɓakawa sun faru (ko an tsara su faruwa) sau da yawa a cikin tarihin Monero. Tabbacin iyaka a cikin ainihin yarjejeniyar RingCT sun kasance masu girma da jinkiri; Daga baya an sabunta su zuwa wani gini mai suna [ Bulletproofs ](https://eprint.iacr.org/2017/1066) wanda ke yin ma'amala da ƙanƙanta da sauri tare da ingantaccen bincike na tsaro, kuma ana shirin sabunta su zuwa sabon ginin da ake kira [ Bulletproofs + ](https://eprint.iacr.org/2020/735) don ƙarin fa'idodin inganci. 

An gudanar da irin wannan tsari tare da haɗin ginin sa hannu na zobe. A cikin ƙa'idar asali, an yi amfani da gini mai suna [ MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Daga baya aka sabunta wannan zuwa sabon gini mai suna [ CLSAG](https://eprint.iacr.org/2019/654) wanda yake da sauri, yana haifar da ƙarami, kuma yana da ingantaccen bincike na tsaro. Wani sabon ginin sa hannu na zobe mai alaƙa wanda ya dogara da [ Triptych](https://eprint.iacr.org/2020/018) an ƙaddamar da shi, amma ba a zaɓi wannan don turawa ba saboda tasirin sa akan ayyukan sa hannu da yawa.

Waɗannan tubalan ginin an haɗa su a hankali don gina ka'idar RingCT.

Kadari mai amfani na ka'idar RingCT ita ce ana iya canza wasu tubalan gini ko haɓaka ta hanyar da za ta ci gaba da ƙira da kaddarorin gaba ɗaya, amma hakan na iya samar da inganci ko haɓaka tsaro. A haƙiƙa, waɗannan nau'ikan haɓakawa sun faru (ko an tsara su faruwa) sau da yawa a cikin tarihin Monero. Tabbacin iyaka a cikin ainihin yarjejeniyar RingCT sun kasance masu girma da jinkiri; Daga baya an sabunta su zuwa wani gini mai suna [ Bulletproofs ](https://eprint.iacr.org/2017/1066) wanda ke yin ma'amala da ƙanƙanta da sauri tare da ingantaccen bincike na tsaro, kuma ana shirin sabunta su zuwa sabon ginin da ake kira [ Bulletproofs + ](https://eprint.iacr.org/2020/735) don ƙarin fa'idodin inganci. 

An gudanar da irin wannan tsari tare da haɗin ginin sa hannu na zobe. A cikin ƙa'idar asali, an yi amfani da gini mai suna [ MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34). Daga baya aka sabunta wannan zuwa sabon gini mai suna [ CLSAG](https://eprint.iacr.org/2019/654) wanda yake da sauri, yana haifar da ƙarami, kuma yana da ingantaccen bincike na tsaro. Wani sabon ginin sa hannu na zobe mai alaƙa wanda ya dogara da [ Triptych](https://eprint.iacr.org/2020/018) an ƙaddamar da shi, amma ba a zaɓi wannan don turawa ba saboda tasirin sa akan ayyukan sa hannu da yawa.

## Serafis

Seraphis yana ɗaukar wannan matakin gaba.  
Maimakon sabunta tubalan ginin mutum ɗaya na ƙa'idar ciniki ta RingCT, tana gabatar da wata yarjejeniya ta daban wacce za ta iya cin gajiyar tubalan gini daban-daban da bayar da ingantattun ayyuka.

## Tubalan gini

Seraphis yana amfani da nau'ikan tubalan gini daban-daban don cimma burin ƙirar sa.

  * _Alƙawari_ har yanzu yana ɓoye adadin
  * _Tabbatattun Range_ har yanzu suna hana ambaliya da wadatar hauhawar farashi
  * _Hujjojin Membobi_ suna ba da rashin fahimta 
  * _Rarraba ƙaddamarwa_ har yanzu yana tabbatar da ma'auni
  * _Bada izini_ yana hana yunƙurin kashe kuɗi biyu

Lura da canjin anan: ana maye gurbin sa hannun zobe masu alaƙa tare da haɗakar hujjojin zama memba da hujjoji masu ba da izini. Kusan magana, hujjojin membobin sun nuna cewa fitarwar da aka cinye wani yanki ne na babban saiti, kama da abin da ke faruwa a cikin RingCT. Amma ba kamar RingCT ba, hujjojin membobin ba su ƙunshi alamar haɗin gwiwa kwata-kwata! Hujjoji masu izini sun nuna cewa alamar haɗin gwiwa tana aiki kuma ana amfani da ita don sanya hannu kan ciniki na ƙarshe.

Saboda RingCT yana gasa alamar haɗin kai cikin sa hannu mara kyau, sa hannu (da sa hannu da yawa) ayyuka sun fi ƙarfin lissafi, kuma yana zama mafi ƙalubale don gina wasu ayyukan da ke da alaƙa. Amma a cikin Seraphis, ana iya ba da tabbaci na kasancewa memba cikin aminci daga na'urori da aka aminta da su sosai (waɗanda ƙila suna da iyakacin ikon sarrafa kwamfuta, kamar walat ɗin kayan masarufi) zuwa na'urar da ba ta da aminci, da sanya hannu (da sa hannu da yawa) ayyuka sun fi sauƙi ta amfani da mafi sauƙaƙan hujjar ba da izini. 

Abin farin ciki, wasu tubalan ginin da Seraphis ke buƙata sun riga sun wanzu a wani wuri, kuma ba sa buƙatar ƙira daga karce. Dukkanin gine-ginen harsashi da abubuwan hana harsashi+ ana iya amfani da su azaman tabbacin kewayo. Ana iya amfani da gyare-gyare zuwa tsarin tabbatar da nau'in Schnorr don ba da izini. Kuma ingantaccen tsarin tabbatarwa [ ](https://eprint.iacr.org/2015/643) da aka riga aka yi amfani dashi azaman tushen Triptych, [ Lelantus ](https://eprint.iacr.org/2019/373), da [ Spark](https://eprint.iacr.org/2021/1173) * ana iya canza shi don zama memba. X2127X] 

* Cypher Stack yana karɓar kuɗi don haɓaka Spark.

## Yin jawabi

Abin takaici, adiresoshin Monero a halin yanzu da ake amfani da su ba su dace da Seraphis ba. Masu amfani za su buƙaci samar da sababbin adireshi daga maɓallan walat ɗin su don karɓar Monero idan an aiwatar da Seraphis. Koyaya, wannan farashin yanayin muhalli yana zuwa tare da fa'idodi masu yawa.

Baya ga fa'idodin tsarin da aka tattauna a sama, ƙirar Seraphis yana dacewa da damar ginin adireshin daban-daban, kowannensu yana zuwa tare da ciniki. Yayin da ginin adireshin ƙarshe da za a yi amfani da shi a cikin Seraphis [ har yanzu ana yanke shawarar](https://github.com/monero-project/research-lab/issues/92) (makircin da ke karɓar kulawa mai yawa ana kiransa [ JAMTIS ](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), zamu iya kwatanta wasu abubuwan gama gari da amfani.

Kuna iya sanin cewa adiresoshin Monero suna ba da ayyuka na __ , inda zaku iya ba da maɓallin gani ga na'ura ko ɓangare na uku kuma ku ba shi damar kallon abubuwan da ke shigowa a madadin ku, amma ba tare da daina kashewa ba. hukuma. Wannan yana da amfani ga wallets, waɗanda za su iya kasancewa a sabunta su yayin da ake kiyaye maɓallin kashe kuɗin ku cikin aminci. Hakanan yana da amfani ga shari'o'in da kuke son samun damar kallon waje, kamar sadaka ta jama'a da ke ba da gaskiya ko kamfani mai sashen lissafin kuɗi.

Babban maɓallan kallon Monero shine cewa basa samar da cikakkiyar dama ga gani mai kyau. Ba zai yiwu a iya dogara da gaske lokacin da walat ɗin ke kashe kuɗi ba, wanda ke sa yana da wahala a ƙididdige ma'auni na walat daidai lokacin da maɓallin kashewa ba ya samuwa. Har ila yau, a halin yanzu ba zai yiwu a gano abubuwan da ke shigowa ba tare da koyon ƙimar da ke cikin waɗannan abubuwan ba (wanda ke nufin duk wani ɓangare na uku da ke da alhakin gano abubuwan da ke shigowa za su koyi daidai adadin Monero da kuke samu).

Abubuwan da ke magana da Seraphis na iya magance wannan. Tare da Seraphis, adireshin ku yana zuwa sanye take da maɓallai daban-daban waɗanda zasu iya yin abubuwa daban-daban:

  * Duba abubuwan da ke shigowa, amma ɓoye ƙimar su
  * Kalli abubuwan da ke shigowa, amma suna nuna ƙimar su
  * Duba abubuwan da ake fitarwa 
  * Taimaka muku don samar da ma'amaloli, amma kar a sanya hannu akan su
  * Ƙirƙirar sabbin adireshi (mai amfani ga dillalai ko musanya tare da abokan ciniki da yawa)

A matsayin mai riƙe adreshin, za ku yanke shawarar yawan ikon da kuka ba wa wasu na'urori ko wasu na uku.

## Babban hoto

Seraphis babban canji ne ga yanayin yanayin Monero. Yayin da ya ƙunshi gyare-gyare ga adireshi da tubalan ginin ma'amala, ƙirar sa tana ba da sassauci da ayyuka masu amfani waɗanda ba su yiwuwa tare da ka'idar RingCT ta yau. Yayin da aka kammala yawancin ƙira kuma ana haɓaka su zuwa [ aiwatarwa ](https://github.com/UkoeHB/monero/tree/seraphis_lib), ƙirar adireshin da bincike na tsaro suna gudana. Seraphis yana ba da kyakkyawar dama don ciyar da yanayin yanayin Monero gaba!

Kara karantawa