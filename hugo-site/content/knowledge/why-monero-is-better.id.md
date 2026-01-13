---
title: "Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)"
slug: "why-monero-is-better"
date: "Sat Feb 01"
image: "/images/why-monero.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Tidak semua koin yang berpusat pada privasi dapat memberikan 100% privasi, tidak dapat dilacak, keamanan, dan fungibilitas dalam 100% koin terdesentralisasi dengan pengaturan tanpa kepercayaan. Inilah atribut-atribut tersebut dan mengapa atribut itu penting:

Pribadi
    Keuangan Anda tidak terlihat oleh publik. Seseorang yang melihat blockchain koin tidak akan dapat melihat berapa banyak uang yang Anda miliki.
Tidak dapat terlacak
    Koin tidak dapat dilacak melalui analisis blockchain atau pemantauan blockchain.
Aman
    Semua transaksi dienkripsi dan dompet yang menyimpan dana Anda dienkripsi.
Sepadan
    Semua koin setara dan memiliki nilai yang sama.
Terdesentralisasi
    Semua node (node adalah instance berjalan dari blockchain koin) dari jaringan adalah sama. Tidak ada node superclass yang memiliki pengaruh atau kontrol lebih besar atas transaksi atau sistem daripada node lainnya.

## Analisis koin

Berikut adalah analisis mata uang kripto terkenal yang mengklaim anonimitas dan/atau tidak dapat dilacak sebagai pembeda utama mereka. Bitcoin sendiri tidak termasuk dalam cakupan analisis ini karena tidak pernah mengklaim sebagai anonim.

Situs ini dibuat oleh para pengguna Monero. Ada saat ketika kami bukan pengguna Monero tetapi khawatir tentang privasi finansial. Kami meneliti koin yang diklaim sebagai pribadi dan halaman ini adalah hasil penelitian kami. Itu sebabnya kami memilih Monero daripada yang lain. Jadi, jika kami tampak bias, memang demikian, tetapi kami percaya bahwa bias didasarkan pada fakta yang dapat Anda baca di bawah dan verifikasi sendiri.

### Ringkasan

Pilih logo untuk menuju ke analisis koin tersebut.

| Pribadi| Tidak dapat terlacak| Aman| Sepadan| Terdesentralisasi  
---|---|---|---|---|---  
Monero| Ya| Ya| Ya| Ya| Ya  
DASH| Tidak| Tidak| Ya| Tidak| Tidak  
Zcash| Tidak| Tidak sepenuhnya| Ya| Tidak| Tidak  
| Ya| Ya| Ya| Ya| Tidak  
| Kadang-kadang| Tidak| Ya| Tidak yakin| Ya  
Bitcoin mixers| Tidak| Tidak| Ya| Tidak| Kadang-kadang  
  
### Monero

Pribadi
    Monero menggunakan sistem suara kriptografis yang memungkinkan Anda mengirim dan menerima dana tanpa transaksi Anda terlihat secara publik di blockchain (buku besar transaksi yang didistribusikan). Hal ini memastikan bahwa pembelian, tanda terima, dan transfer lainnya tetap **pribadi secara default**. Pengirim, penerima, dan jumlah transaksi semuanya bersifat pribadi. Beberapa koin memiliki "daftar kaya" yang memungkinkan siapa saja melihat akun mana yang memiliki koin paling banyak. Karena Monero bersifat pribadi, daftar kaya [ Monero ](http://moneroblocks.info/richlist) tidak akan ada.
Tidak dapat terlacak
    Dengan memanfaatkan ring signature (properti khusus dari jenis kriptografi tertentu), Monero memungkinkan transaksi yang tidak dapat dilacak. Ini berarti tidak jelas dana mana yang telah dibelanjakan, dan dengan demikian sangat tidak mungkin sebuah transaksi dapat dikaitkan dengan pengguna tertentu.
Aman
    Menggunakan jaringan konsensus peer-to-peer terdistribusi, setiap transaksi diamankan secara kriptografis. Akun individu memiliki mnemonic seed 25 kata yang ditampilkan saat dibuat, yang dapat ditulis untuk mencadangkan akun. Kata sandi wajib saat membuat dompet, dan file akun dienkripsi dengan frasa sandi untuk memastikannya jadi tidak berharga jika dicuri.
Sepadan
    Semua koin setara dan memiliki nilai yang sama. Pengguna, vendor, atau entitas lainnya tidak dapat memblokir atau memasukkan koin Monero tertentu ke dalam daftar hitam karena riwayat transaksi koin Monero ambigu.
Terdesentralisasi
    Semua node Monero adalah setara. Tidak ada node superclass yang memiliki pengaruh atau kontrol lebih besar atas transaksi daripada node lainnya. Tidak ada orang atau entitas yang dapat melacak transaksi dengan memiliki banyak node. Selain itu, tidak ada setup tepercaya. Artinya, kebutuhan untuk memercayai seseorang atau entitas bukanlah faktor. Satu-satunya hal yang perlu dipercaya adalah source code (yang dapat diverifikasi oleh siapa saja) dan matematika.

Monero telah 100% open source sejak awal, artinya siapa pun dapat melihat [ source code ](https://github.com/monero-project/bitmonero) perangkat lunak untuk memverifikasi bahwa tidak ada pintu belakang dan bahwa perangkat lunak tersebut aman.

Monero juga memiliki [ makalah penelitian peer-review ](https://lab.getmonero.org/) yang secara matematis dan sistematis memverifikasi semua propertinya yang tercantum di atas.

### DASH

Pribadi
    

DASH memiliki daftar kaya [ ](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), jadi ini bukan koin pribadi. Detail keuangan alamat koin dapat dilihat oleh siapa saja yang memeriksa blockchain.

> DASH sama sekali tidak bersifat pribadi secara kriptografis. Sebenarnya saya memiliki seluncuran di geladak yang seperti 'DASH, LOL,' dan tidak seperti yang lain ... itu adalah minyak ular dan saya agak gila tentang hal itu, secara pribadi. 
> 
> **Gregory Maxwell** , pengembang dan kriptografer Bitcoin Core, dalam presentasi [ ke Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , pengembang dan kriptografer Bitcoin Core lainnya, telah membuat pernyataan serupa [](https://twitter.com/petertoddbtc/status/622022840330682368).

Tidak dapat terlacak
    Transaksi dialihkan melalui serangkaian [ Masternode ](https://www.dash.org/masternodes/) agar tidak dapat dilacak. Praktik ini mungkin berhasil jika semua operator masternode hanya memiliki motif murni. Namun, jika pemerintah, kelompok peretas, entitas lain, atau bahkan individu membeli banyak masternode (tidak akan ada cara untuk mengetahui apakah ini terjadi) dan jika transaksi melewati rute di mana semua masternode dimiliki oleh entitas tersebut. , maka transaksi dapat dilacak oleh entitas tersebut. Mengingat biaya masternode yang relatif rendah dan anggaran pemerintah dan beberapa organisasi yang sangat besar, kemungkinan koin dapat dilacak adalah nyata.
Aman
    Transaksi aman secara kriptografis.
Sepadan
    Karena transaksi tidak bersifat pribadi, ada potensi bagi suatu entitas untuk memblokir atau memasukkan koin tertentu ke dalam daftar hitam, menjadikannya kurang berharga daripada yang lain. Lihat catatan tentang kurangnya fungibilitas Bitcoin di bawah karena prinsip yang sama berlaku untuk DASH.
Terdesentralisasi
    Tidak semua node DASH setara. Ada superclass node, yang disebut _Masternodes_ yang pemiliknya memiliki pengaruh lebih besar terhadap sistem dibandingkan operator node biasa. Ini membuat DASH semi-terpusat, bukan sistem desentralisasi 100% yang ideal.

### Zcash

Pribadi
    

Transaksi Zcash terlihat di blockchain mereka. Mereka mengaktifkan transaksi tersembunyi, tetapi [ kurang dari 1% dari transaksi sepenuhnya terlindung ](http://stat.bloxy.info/superset/dashboard/zcash/) . Karena transaksi tersembunyi adalah opsional dan bukan default (belum lagi jarang digunakan), [ transaksi tersembunyi yang menonjol di blockchain mereka ](http://weuse.cash/2016/06/09/btc-xmr-zcash/), menarik perhatian pada diri mereka sendiri.

> Dan omong-omong, saya pikir kami dapat berhasil membuat Zcash terlalu dapat dilacak untuk penjahat seperti WannaCry, tetapi sepenuhnya pribadi & fungible. 
> 
> **Zooko Wilcox** , CEO Zcash, dalam tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Jika Zcash dapat "terlalu dilacak", maka Zcash tidak dapat sepenuhnya bersifat pribadi atau fungible. 

Tidak dapat terlacak
    

Transaksi reguler transparan. Transaksi tersembunyi menggunakan zk-SNARKS, yang diakui memiliki jaminan privasi yang kuat dalam kondisi tertentu. Pertanyaannya adalah apakah kondisi ini terpenuhi, dan melihat sedikitnya jumlah orang yang menggunakan kapabilitas terlindungi, hal ini masih tetap dipertanyakan.

Aman
    Transaksi aman secara kriptografis.
Sepadan
    Karena semua transaksi tidak bersifat pribadi, ada potensi bagi suatu entitas untuk memblokir atau memasukkan koin tertentu ke dalam daftar hitam, menjadikannya kurang berharga daripada yang lain. Lihat catatan tentang kurangnya fungibilitas Bitcoin di bawah karena prinsip yang sama berlaku untuk Zcash.
Terdesentralisasi
    

Zcash adalah sebuah perusahaan dan saat ini [ mengambil 20% dari semua ZEC yang ditambang sebagai hadiah pendiri ](https://z.cash/blog/funding.html). 

Zcash memerlukan **Pengaturan Tepercaya**. Ini berarti Anda harus percaya bahwa sistem itu dibuat dengan jujur. Jika tidak diatur dengan jujur, [ jumlah ZEC yang tidak terbatas dapat dibuat tanpa diketahui siapa pun ](https://blog.okturtles.com/2016/03/the-zcash-catch/). Ini akan membuat peretas kaya dan menurunkan nilai ZEC. Tidak ada cara untuk mengetahui apakah Setup Tepercaya dijalankan dengan jujur. Kita harus mengambil kata-kata mereka. Ini memperkenalkan titik kegagalan manusia ke dalam sistem yang bertentangan dengan hampir semua mata uang kripto lainnya. Anda seharusnya hanya mempercayai matematika dan source code yang dapat diverifikasi dalam mata uang kripto, bukan manusia. Seperti yang telah kita lihat dengan hampir semua perusahaan perangkat lunak besar, seperti [ Microsoft ](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple ](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), dan bahkan pemerintah, mereka tidak boleh dipercaya. 

Peter Todd, pengembang Bitcoin Core yang [ berpartisipasi ](https://github.com/zcash/mpc/blob/master/README.md) dalam Zcash Trusted Setup, menyebutnya sebagai backdoor " [ ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash tidak terdengar tanpa syarat, tidak bisa dengan teknologi saat ini...memerlukan setup tepercaya… perlu mengulangi prosedur [Setup Tepercaya] untuk memutakhirkan kripto dari waktu ke waktu sehingga menjadi kerentanan. 
> 
> Gregory Maxwell, pengembang dan kriptografer Bitcoin Core, dalam presentasi [ kepada Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Catatan:** Zcoin sedang beralih dari skema Sigma saat ini ke protokol baru yang bergantung pada pekerjaan barunya, Lelantus. Lelantus akan diimplementasikan secara bertahap, dan artikel ini akan menganggap semua tahapan selesai dan diimplementasikan untuk perbandingan yang tepat bersamaan dengan waktu implementasi yang diproyeksikan.

Alasan Zcoin diberikan kemewahan untuk dinilai berdasarkan protokolnya di masa depan, dan bukan Zcash, adalah karena Zcoin memiliki roadmap dengan pengaturan waktu umum untuk aktivasi, sedangkan rencana 'privasi secara default' Zcash terasa dan terus samar-samar.

Pribadi
    

Zcoin (XZC) tidak akan memiliki daftar kaya, sehingga akan bersifat pribadi. Secara default, privasi wajib diharapkan untuk aktif pada tahun 2021. Setelah diterapkan, daftar kaya tidak akan dapat dibuat (meskipun saat ini [mereka memilikinya](https://www.coinexplorer.net/XZC/richlist)).

Tidak dapat terlacak
    Dengan tahap akhir Lelantus yang diimplementasikan pada tahun 2021, Zcoin seharusnya tidak dapat dilacak, meskipun serangan teoretis belum dieksplorasi karena belum dirilis atau sudah habis di alam liar. Saat ini Zcoin dapat dilacak jika seseorang memasukkan [ alamat Zcoin ](https://explorer.zcoin.io/) di penjelajah blockchain dan Anda dapat melihat saldo dan transaksi terkait.
Aman
    Transaksi aman secara kriptografis.
Sepadan
    Setelah tahap akhir Lelantus mengudara pada tahun 2021, diasumsikan bahwa Zcoin akan jadi fungible karena penegakan privasi wajib. Dalam hal ini, mereka akan menjadi pesaing sejati Monero. Namun...
Terdesentralisasi
    Zcoin telah mengimplementasikan Znodes, yang bertindak mirip dengan masternode Dash, dan memiliki kekuatan lebih besar daripada node lain di jaringan. Karena semua node tidak dibuat setara, dan faktor pembeda di antara mereka adalah jumlah uang yang dimiliki seseorang (biaya Znodes 1000 XZC), jaringan menjadi semi-terpusat.

Pribadi
    Grin tidak memiliki daftar kaya, yang mengindikasikan suatu bentuk privasi. Memang, penyerang pasif yang memindai chain tidak dapat melihat alamat mana yang memiliki berapa banyak uang di dalamnya, sebagian karena jumlahnya dikaburkan melalui transaksi rahasia, sebagian karena data alamat tidak disimpan dalam chain, dan sebagian karena teknologi cut-through Mimblewimble, di mana transaksi perantara dapat dihapus dari chain, menyisakan sedikit metadata dari transaksi sebelumnya.
Tidak dapat terlacak
    Grin tidak bertahan melawan penyerang aktif yang membangun grafik transaksi. Sangat mungkin bagi penambang dan node yang sedikit dimodifikasi dapat menonton setiap transaksi, menyimpannya sebelum teknologi cut-through masuk, dan membuat grafik transaksi lengkap dari sini, bersamaan dengan menyimpan semua data 'cut-through'. Mereka tidak akan dapat membedakan informasi apa pun sebelum mereka mulai, tetapi semuanya setelah mereka mulai akan menjadi metadata berharga yang berpotensi menghubungkan transaksi.
Aman
    Transaksi aman secara kriptografis.
Sepadan
    Karena semua transaksi diragukan bersifat pribadi, dan berpotensi dapat dilacak, ada kemungkinan untuk membuat grafik transaksi, yang darinya dapat diperoleh informasi berharga yang dapat digunakan terhadap individu terkait kebiasaan belanja mereka. Output kemudian dapat ditautkan dengan identitas, dan, meskipun jumlahnya tidak terlihat, fakta bahwa suatu output dapat ditautkan dengan identitas berarti output tersebut dapat dinodai, hanya berdasarkan siapa yang memegangnya. Kami pikir ini berarti bahwa Grin tidak fungible, karena beberapa output mungkin ternoda sementara yang lain tidak.
Terdesentralisasi
    Grin tidak memiliki premine, hadiah pendiri, masternode, atau perbendaharaan. Mereka tidak memiliki ICO, dan dijalankan dengan cara yang sesuai dengan komunitas terdesentralisasi. Grin terdesentralisasi.

### Bitcoin Mixers

Pribadi
    

Semua transaksi Bitcoin terlihat di blockchain dan ada daftar kaya Bitcoin [ ](http://www.bitcoinrichlist.com/top100), jadi Bitcoin tidak bersifat pribadi. Bitcoin adalah [ pseudonononymous ](https://bitcoin.org/en/you-need-to-know), bukan anonim. 

Untuk **Bitcoin mixers** , Anda harus percaya bahwa mereka dapat menjaga keamanan datanya dan tidak dimiliki oleh atau bekerja sama dengan pemerintah, peretas, atau entitas lain. 

Pada bulan Juli 2017, pendiri layanan mixing Bitcoin terbesar, BITMIXER.IO, mengumumkan bahwa mereka akan ditutup dan memberikan alasan berikut: 

> … Sekarang saya memahami bahwa Bitcoin adalah sistem non-anonim transparan **dengan desain**. Blockchain adalah buku terbuka yang bagus… 
> 
> BITMIXER.IO, dalam pengumuman penutupan pada [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (penekanan pada aslinya). 

Beberapa minggu kemudian, setelah mempertimbangkan berbagai koin privasi-sentris, dia mengatakan ini: 

> Setelah penyelidikan mendalam, saya mengonfirmasi bahwa MONERO adalah mata uang privasi terbaik. Jadi saya sangat merekomendasikan MONERO untuk semua orang yang membutuhkan privasi ekstra. 
> 
> BITMIXER.IO, dalam postingan lanjutan [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Tidak dapat terlacak
    

Karena semua transaksi Bitcoin terlihat di blockchain, SEMUA transaksi Bitcoin dapat dilacak. Mixer Bitcoin dapat sangat mengaburkan transaksi, membuatnya jauh lebih sulit bagi seseorang untuk melacak Bitcoin, tetapi bukan tidak mungkin. Seiring kemajuan teknologi dan perusahaan yang berspesialisasi dalam melacak transaksi Bitcoin menjadi lebih umum, setelah transaksi yang sangat kabur akan menjadi relatif mudah dilacak: 

  * [ Penegakan Hukum Terus Berinvestasi dalam Layanan Pelacakan Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoin Lebih Mudah Dilacak Daripada Yang Anda Pikirkan ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: Perusahaan yang Berspesialisasi dalam Melacak Bitcoin untuk Penegakan Hukum ](https://www.elliptic.co/)

Pencarian Google akan mengungkapkan puluhan artikel seperti di atas. Dan ingat, setiap transaksi yang terjadi kapan saja di masa lalu ada di blockchain dan berpotensi dilacak, bahkan jika layanan mixing digunakan. Faktanya, penggunaan layanan mixing cenderung menarik perhatian pada transaksi tersebut. 

Aman
    Transaksi aman secara kriptografis.
Sepadan
    

Tidak semua Bitcoin setara dan memiliki nilai yang sama. Beberapa Bitcoin telah masuk daftar hitam dan diblokir oleh beberapa entitas, membuat koin-koin tersebut menjadi kurang berharga dibandingkan koin lainnya. Jika Anda menerima Bitcoin yang sebelumnya digunakan untuk tujuan ilegal, Bitcoin Anda dapat masuk daftar hitam meskipun Anda tidak ada hubungannya dengan aktivitas ilegal tersebut. Atau, katakanlah pemerintah, pemberi kerja, atau entitas lain memutuskan untuk memasukkan Bitcoin Anda ke daftar hitam di masa mendatang, seperti yang mereka lakukan dengan pembekuan atau penyitaan aset. Tidak akan ada yang bisa Anda lakukan. Karena mixer hanya mempersulit pelacakan Bitcoin Anda, kategori ini telah ditandai sebagai "tidak fungible." 

  * Andreas Antonopoulos, mantan pengembang Bitcoin Core yang dihormati di komunitas Bitcoin dan mata uang kripto lainnya, mengakui masalah fungibilitas Bitcoin dalam [ video YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Diskusi tentang masalah fungibilitas Bitcoin di [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

Terdesentralisasi
    Bitcoin sendiri terdesentralisasi, tetapi sebagian besar layanan pencampuran adalah tersentralisasi. Ini berarti Anda harus memercayai mereka. Namun, beberapa yang lebih baru, seperti dompet Wasabi, tidak.

## Ringkasan

Menurut pendapat kami, Monero adalah pilihan yang jelas jika Anda mencari mata uang kripto yang pribadi, aman, tidak dapat dilacak, fungible, dan terdesentralisasi tanpa memerlukan setup tepercaya. Ada hal lain yang membahayakan privasi dan keamanan Anda. Tapi jangan hanya mengambil pendapat kami. Lakukan penelitian Anda sendiri dan lihat sendiri. Pertimbangkan bahwa Monero didukung dan digunakan oleh entitas yang bergantung pada privasi dan tidak dapat dilacak, seperti: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purisme ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) ditutup pada Juli 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) terhadap AB menunjukkan bahwa: 
    * **Monero adalah satu-satunya mata uang kripto pribadi dan tidak dapat dilacak:**   
"Secara total, dari dompet CAZES dan agen komputer menguasai sekitar $8.800.000 dalam Bitcoin, Ethereum, Moreno [sic], dan Zcash, yang diuraikan sebagai berikut: 1.605,0503851 Bitcoin, 8.309,271639 Ethereum, 3.691,98 Zcash, _dan jumlah Monero yang tidak diketahui._ "(bagian bawah dari hal.20 dan bagian atas dari hal.21, penekanan ditambahkan)
    * **Transaksi Bitcoin tidak bersifat pribadi dan dapat dilacak:**   
"Agen federal memperoleh surat perintah setelah melacak sejumlah transaksi Bitcoin yang berasal dari AlphaBay ke rekening mata uang digital, dan akhirnya rekening bank dan aset berwujud lainnya, yang dipegang oleh CAZES dan istrinya." (hal. 17, baris 24- 26) 

LocalMonero tidak menganjurkan atau mendorong aktivitas ilegal apa pun. 

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies)/

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys)/

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero)/

  * [Bagaimana node jarak jauh memengaruhi privasi Monero](/knowledge/remote-nodes-privacy)/

  * [Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan](/knowledge/network-upgrades)/

  * [Lihat tag: Bagaimana satu byte akan mengurangi waktu sinkronisasi dompet Monero hingga 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool dan Perannya dalam Desentralisasi Penambangan Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Apa yang Akan Dilakukannya untuk Monero](/knowledge/seraphis-for-monero)/

  * [Apakah Mengonversi Bitcoin ke Monero Sama Privatnya dengan Membeli Monero Secara Langsung?](/knowledge/most-private-way-to-buy-monero)/

  * [Mengapa Monero Menggunakan Pengaturan Tanpa Kepercayaan Tidak Seperti Zcash](/knowledge/monero-trustless-setup)/

  * [Mengapa Monero Adalah Penyimpan Nilai Yang Lebih Baik Dibandingkan Dengan Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Bagaimana Monero Dapat Mengatasi Efek Jaringan Bitcoin](/knowledge/network-effect)/

  * [Mengapa Monero Memiliki Komunitas Dengan Pemikiran Paling Kritis](/knowledge/critical-thinking)/

  * [Penipuan yang Harus Diwaspadai Saat Menggunakan Monero](/knowledge/monero-scams)/

  * [Bagaimana Atomic Swap Akan Bekerja di Monero](/knowledge/monero-atomic-swaps)/

  * [Apa yang Perlu Diketahui Setiap Pengguna Monero Saat Berbicara tentang Jaringan](/knowledge/monero-networking)/

  * [Bagaimana RingCT Menyembunyikan Jumlah Transaksi Monero](/knowledge/monero-ringct)/

  * [Bagaimana Stealth Address Monero Melindungi Identitas Anda](/knowledge/monero-stealth-addresses)/

  * [Bagaimana Sub Alamat Monero Mencegah Penautan Identitas](/knowledge/monero-subaddresses)/

  * [Output Monero Dijelaskan](/knowledge/monero-outputs)/

  * [Praktik Terbaik Monero untuk Pemula](/knowledge/monero-best-practices)/

  * [Bagaimana Ring Signature Mengaburkan Output Monero](/knowledge/ring-signatures)/

  * [Bagaimana Monero Memecahkan Masalah Ukuran Blok Yang Mengganggu Bitcoin](/knowledge/dynamic-block-size)/

  * [Bagaimana CLSAG Akan Meningkatkan Efisiensi Monero](/knowledge/what-is-clsag)/

  * [Mengapa Monero Memiliki Tail Emission](/knowledge/monero-tail-emission)/

  * [Sejarah Singkat Monero](/knowledge/monero-history)/

  * [Majalah Wired Salah Tentang Monero, Ini Alasannya](/knowledge/wired-article-debunked)/

  * [Top 15 Mitos dan Kekhawatiran Monero Terbantahkan](/knowledge/monero-myths-debunked)/

  * [Bagaimana Dandelion++ Menjaga Kerahasiaan Asal Transaksi Monero](/knowledge/monero-dandelion)/

  * [Mengapa Monero Open Source Dan Terdesentralisasi](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa](/knowledge/monero-mining-randomx)/

Tidak semua koin yang berpusat pada privasi dapat memberikan 100% privasi, tidak dapat dilacak, keamanan, dan fungibilitas dalam 100% koin terdesentralisasi dengan pengaturan tanpa kepercayaan. Inilah atribut-atribut tersebut dan mengapa atribut itu penting:

## Analisis koin

Berikut adalah analisis mata uang kripto terkenal yang mengklaim anonimitas dan/atau tidak dapat dilacak sebagai pembeda utama mereka. Bitcoin sendiri tidak termasuk dalam cakupan analisis ini karena tidak pernah mengklaim sebagai anonim.

Situs ini dibuat oleh para pengguna Monero. Ada saat ketika kami bukan pengguna Monero tetapi khawatir tentang privasi finansial. Kami meneliti koin yang diklaim sebagai pribadi dan halaman ini adalah hasil penelitian kami. Itu sebabnya kami memilih Monero daripada yang lain. Jadi, jika kami tampak bias, memang demikian, tetapi kami percaya bahwa bias didasarkan pada fakta yang dapat Anda baca di bawah dan verifikasi sendiri.

Situs ini dibuat oleh para pengguna Monero. Ada saat ketika kami bukan pengguna Monero tetapi khawatir tentang privasi finansial. Kami meneliti koin yang diklaim sebagai pribadi dan halaman ini adalah hasil penelitian kami. Itu sebabnya kami memilih Monero daripada yang lain. Jadi, jika kami tampak bias, memang demikian, tetapi kami percaya bahwa bias didasarkan pada fakta yang dapat Anda baca di bawah dan verifikasi sendiri.

### Ringkasan

Pilih logo untuk menuju ke analisis koin tersebut.

### Monero

Monero telah 100% open source sejak awal, artinya siapa pun dapat melihat [ source code ](https://github.com/monero-project/bitmonero) perangkat lunak untuk memverifikasi bahwa tidak ada pintu belakang dan bahwa perangkat lunak tersebut aman.

Monero juga memiliki [ makalah penelitian peer-review ](https://lab.getmonero.org/) yang secara matematis dan sistematis memverifikasi semua propertinya yang tercantum di atas.

### DASH

DASH memiliki daftar kaya [ ](https://bitinfocharts.com/top-100-richest-darkcoin-addresses.html), jadi ini bukan koin pribadi. Detail keuangan alamat koin dapat dilihat oleh siapa saja yang memeriksa blockchain.

> DASH sama sekali tidak bersifat pribadi secara kriptografis. Sebenarnya saya memiliki seluncuran di geladak yang seperti 'DASH, LOL,' dan tidak seperti yang lain ... itu adalah minyak ular dan saya agak gila tentang hal itu, secara pribadi. 
> 
> **Gregory Maxwell** , pengembang dan kriptografer Bitcoin Core, dalam presentasi [ ke Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

DASH sama sekali tidak bersifat pribadi secara kriptografis. Sebenarnya saya memiliki seluncuran di geladak yang seperti 'DASH, LOL,' dan tidak seperti yang lain ... itu adalah minyak ular dan saya agak gila tentang hal itu, secara pribadi. 

DASH sama sekali tidak bersifat pribadi secara kriptografis. Sebenarnya saya memiliki seluncuran di geladak yang seperti 'DASH, LOL,' dan tidak seperti yang lain ... itu adalah minyak ular dan saya agak gila tentang hal itu, secara pribadi. 

**Gregory Maxwell** , pengembang dan kriptografer Bitcoin Core, dalam presentasi [ ke Coinbase ](https://archive.21mil.com/blockstream-cto-greg-maxwell-discusses-monero-zcash-privacy-focused-altcoins/). 

**Peter Todd** , pengembang dan kriptografer Bitcoin Core lainnya, telah membuat pernyataan serupa [](https://twitter.com/petertoddbtc/status/622022840330682368).

### Zcash

Transaksi Zcash terlihat di blockchain mereka. Mereka mengaktifkan transaksi tersembunyi, tetapi [ kurang dari 1% dari transaksi sepenuhnya terlindung ](http://stat.bloxy.info/superset/dashboard/zcash/) . Karena transaksi tersembunyi adalah opsional dan bukan default (belum lagi jarang digunakan), [ transaksi tersembunyi yang menonjol di blockchain mereka ](http://weuse.cash/2016/06/09/btc-xmr-zcash/), menarik perhatian pada diri mereka sendiri.

> Dan omong-omong, saya pikir kami dapat berhasil membuat Zcash terlalu dapat dilacak untuk penjahat seperti WannaCry, tetapi sepenuhnya pribadi & fungible. 
> 
> **Zooko Wilcox** , CEO Zcash, dalam tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Dan omong-omong, saya pikir kami dapat berhasil membuat Zcash terlalu dapat dilacak untuk penjahat seperti WannaCry, tetapi sepenuhnya pribadi & fungible. 

Dan omong-omong, saya pikir kami dapat berhasil membuat Zcash terlalu dapat dilacak untuk penjahat seperti WannaCry, tetapi sepenuhnya pribadi & fungible. 

**Zooko Wilcox** , CEO Zcash, dalam tweet [ ](https://twitter.com/zooko/status/863202798883577856)

Jika Zcash dapat "terlalu dilacak", maka Zcash tidak dapat sepenuhnya bersifat pribadi atau fungible. 

Transaksi reguler transparan. Transaksi tersembunyi menggunakan zk-SNARKS, yang diakui memiliki jaminan privasi yang kuat dalam kondisi tertentu. Pertanyaannya adalah apakah kondisi ini terpenuhi, dan melihat sedikitnya jumlah orang yang menggunakan kapabilitas terlindungi, hal ini masih tetap dipertanyakan.

Zcash adalah sebuah perusahaan dan saat ini [ mengambil 20% dari semua ZEC yang ditambang sebagai hadiah pendiri ](https://z.cash/blog/funding.html). 

Zcash memerlukan **Pengaturan Tepercaya**. Ini berarti Anda harus percaya bahwa sistem itu dibuat dengan jujur. Jika tidak diatur dengan jujur, [ jumlah ZEC yang tidak terbatas dapat dibuat tanpa diketahui siapa pun ](https://blog.okturtles.com/2016/03/the-zcash-catch/). Ini akan membuat peretas kaya dan menurunkan nilai ZEC. Tidak ada cara untuk mengetahui apakah Setup Tepercaya dijalankan dengan jujur. Kita harus mengambil kata-kata mereka. Ini memperkenalkan titik kegagalan manusia ke dalam sistem yang bertentangan dengan hampir semua mata uang kripto lainnya. Anda seharusnya hanya mempercayai matematika dan source code yang dapat diverifikasi dalam mata uang kripto, bukan manusia. Seperti yang telah kita lihat dengan hampir semua perusahaan perangkat lunak besar, seperti [ Microsoft ](https://www.gnu.org/proprietary/proprietary-back-doors.en.html), [ Apple ](http://www.digitaltrends.com/computing/apple-vs-fbi-backdoor-to-data-already-exists/), dan bahkan pemerintah, mereka tidak boleh dipercaya. 

Peter Todd, pengembang Bitcoin Core yang [ berpartisipasi ](https://github.com/zcash/mpc/blob/master/README.md) dalam Zcash Trusted Setup, menyebutnya sebagai backdoor " [ ](https://twitter.com/petertoddbtc/status/793584540891643906) ". 

> Zcash tidak terdengar tanpa syarat, tidak bisa dengan teknologi saat ini...memerlukan setup tepercaya… perlu mengulangi prosedur [Setup Tepercaya] untuk memutakhirkan kripto dari waktu ke waktu sehingga menjadi kerentanan. 
> 
> Gregory Maxwell, pengembang dan kriptografer Bitcoin Core, dalam presentasi [ kepada Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

Zcash tidak terdengar tanpa syarat, tidak bisa dengan teknologi saat ini...memerlukan setup tepercaya… perlu mengulangi prosedur [Setup Tepercaya] untuk memutakhirkan kripto dari waktu ke waktu sehingga menjadi kerentanan. 

Zcash tidak terdengar tanpa syarat, tidak bisa dengan teknologi saat ini...memerlukan setup tepercaya… perlu mengulangi prosedur [Setup Tepercaya] untuk memutakhirkan kripto dari waktu ke waktu sehingga menjadi kerentanan. 

Gregory Maxwell, pengembang dan kriptografer Bitcoin Core, dalam presentasi [ kepada Coinbase](https://youtu.be/LHPYNZ8i1cU#t=29m30s). 

**Catatan:** Zcoin sedang beralih dari skema Sigma saat ini ke protokol baru yang bergantung pada pekerjaan barunya, Lelantus. Lelantus akan diimplementasikan secara bertahap, dan artikel ini akan menganggap semua tahapan selesai dan diimplementasikan untuk perbandingan yang tepat bersamaan dengan waktu implementasi yang diproyeksikan.

Alasan Zcoin diberikan kemewahan untuk dinilai berdasarkan protokolnya di masa depan, dan bukan Zcash, adalah karena Zcoin memiliki roadmap dengan pengaturan waktu umum untuk aktivasi, sedangkan rencana 'privasi secara default' Zcash terasa dan terus samar-samar.

Zcoin (XZC) tidak akan memiliki daftar kaya, sehingga akan bersifat pribadi. Secara default, privasi wajib diharapkan untuk aktif pada tahun 2021. Setelah diterapkan, daftar kaya tidak akan dapat dibuat (meskipun saat ini [mereka memilikinya](https://www.coinexplorer.net/XZC/richlist)).

### Bitcoin Mixers

Semua transaksi Bitcoin terlihat di blockchain dan ada daftar kaya Bitcoin [ ](http://www.bitcoinrichlist.com/top100), jadi Bitcoin tidak bersifat pribadi. Bitcoin adalah [ pseudonononymous ](https://bitcoin.org/en/you-need-to-know), bukan anonim. 

Untuk **Bitcoin mixers** , Anda harus percaya bahwa mereka dapat menjaga keamanan datanya dan tidak dimiliki oleh atau bekerja sama dengan pemerintah, peretas, atau entitas lain. 

Pada bulan Juli 2017, pendiri layanan mixing Bitcoin terbesar, BITMIXER.IO, mengumumkan bahwa mereka akan ditutup dan memberikan alasan berikut: 

> … Sekarang saya memahami bahwa Bitcoin adalah sistem non-anonim transparan **dengan desain**. Blockchain adalah buku terbuka yang bagus… 
> 
> BITMIXER.IO, dalam pengumuman penutupan pada [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (penekanan pada aslinya). 

… Sekarang saya memahami bahwa Bitcoin adalah sistem non-anonim transparan **dengan desain**. Blockchain adalah buku terbuka yang bagus… 

… Sekarang saya memahami bahwa Bitcoin adalah sistem non-anonim transparan **dengan desain**. Blockchain adalah buku terbuka yang bagus… 

BITMIXER.IO, dalam pengumuman penutupan pada [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=2042470.msg20357093#msg20357093) (penekanan pada aslinya). 

Beberapa minggu kemudian, setelah mempertimbangkan berbagai koin privasi-sentris, dia mengatakan ini: 

> Setelah penyelidikan mendalam, saya mengonfirmasi bahwa MONERO adalah mata uang privasi terbaik. Jadi saya sangat merekomendasikan MONERO untuk semua orang yang membutuhkan privasi ekstra. 
> 
> BITMIXER.IO, dalam postingan lanjutan [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Setelah penyelidikan mendalam, saya mengonfirmasi bahwa MONERO adalah mata uang privasi terbaik. Jadi saya sangat merekomendasikan MONERO untuk semua orang yang membutuhkan privasi ekstra. 

Setelah penyelidikan mendalam, saya mengonfirmasi bahwa MONERO adalah mata uang privasi terbaik. Jadi saya sangat merekomendasikan MONERO untuk semua orang yang membutuhkan privasi ekstra. 

BITMIXER.IO, dalam postingan lanjutan [ ](https://bitcointalk.org/index.php?topic=2042470.msg21113378#msg21113378). 

Karena semua transaksi Bitcoin terlihat di blockchain, SEMUA transaksi Bitcoin dapat dilacak. Mixer Bitcoin dapat sangat mengaburkan transaksi, membuatnya jauh lebih sulit bagi seseorang untuk melacak Bitcoin, tetapi bukan tidak mungkin. Seiring kemajuan teknologi dan perusahaan yang berspesialisasi dalam melacak transaksi Bitcoin menjadi lebih umum, setelah transaksi yang sangat kabur akan menjadi relatif mudah dilacak: 

  * [ Penegakan Hukum Terus Berinvestasi dalam Layanan Pelacakan Bitcoin ](https://news.bitcoin.com/law-enforcement-continues-invest-bitcoin-tracking-services/)
  * [ Time.com: Bitcoin Lebih Mudah Dilacak Daripada Yang Anda Pikirkan ](http://time.com/3689359/bitcoins-track-anonymous/)
  * [ Elliptic: Perusahaan yang Berspesialisasi dalam Melacak Bitcoin untuk Penegakan Hukum ](https://www.elliptic.co/)

Pencarian Google akan mengungkapkan puluhan artikel seperti di atas. Dan ingat, setiap transaksi yang terjadi kapan saja di masa lalu ada di blockchain dan berpotensi dilacak, bahkan jika layanan mixing digunakan. Faktanya, penggunaan layanan mixing cenderung menarik perhatian pada transaksi tersebut. 

Tidak semua Bitcoin setara dan memiliki nilai yang sama. Beberapa Bitcoin telah masuk daftar hitam dan diblokir oleh beberapa entitas, membuat koin-koin tersebut menjadi kurang berharga dibandingkan koin lainnya. Jika Anda menerima Bitcoin yang sebelumnya digunakan untuk tujuan ilegal, Bitcoin Anda dapat masuk daftar hitam meskipun Anda tidak ada hubungannya dengan aktivitas ilegal tersebut. Atau, katakanlah pemerintah, pemberi kerja, atau entitas lain memutuskan untuk memasukkan Bitcoin Anda ke daftar hitam di masa mendatang, seperti yang mereka lakukan dengan pembekuan atau penyitaan aset. Tidak akan ada yang bisa Anda lakukan. Karena mixer hanya mempersulit pelacakan Bitcoin Anda, kategori ini telah ditandai sebagai "tidak fungible." 

  * Andreas Antonopoulos, mantan pengembang Bitcoin Core yang dihormati di komunitas Bitcoin dan mata uang kripto lainnya, mengakui masalah fungibilitas Bitcoin dalam [ video YouTube](https://www.youtube.com/watch?v=ak1iojpiHpM&feature=youtu .be&t=33m9s). 
  * Diskusi tentang masalah fungibilitas Bitcoin di [ Bitcointalk.org ](https://bitcointalk.org/index.php?topic=1190707.0)

## Ringkasan

Menurut pendapat kami, Monero adalah pilihan yang jelas jika Anda mencari mata uang kripto yang pribadi, aman, tidak dapat dilacak, fungible, dan terdesentralisasi tanpa memerlukan setup tepercaya. Ada hal lain yang membahayakan privasi dan keamanan Anda. Tapi jangan hanya mengambil pendapat kami. Lakukan penelitian Anda sendiri dan lihat sendiri. Pertimbangkan bahwa Monero didukung dan digunakan oleh entitas yang bergantung pada privasi dan tidak dapat dilacak, seperti: 

  * [ SIGAINT ](https://www.reddit.com/r/Monero/comments/4xqrzd/sigaint_launches_tor_monero_node_as_its_operators/)
  * [ Purisme ](https://puri.sm/posts/purism-collaborates-with-cryptocurrency-monero-to-enable-mobile-payments/)
  * [ Wikileaks ](https://shop.wikileaks.org/donate#db9)
  * AlphaBay Market (AB) ditutup pada Juli 2017. [ Federal Forfeiture Complaint ](https://assets.documentcloud.org/documents/3898109/AlphaBay-Cazes-Forfeiture-Complaint.pdf) terhadap AB menunjukkan bahwa: 
    * **Monero adalah satu-satunya mata uang kripto pribadi dan tidak dapat dilacak:**   
"Secara total, dari dompet CAZES dan agen komputer menguasai sekitar $8.800.000 dalam Bitcoin, Ethereum, Moreno [sic], dan Zcash, yang diuraikan sebagai berikut: 1.605,0503851 Bitcoin, 8.309,271639 Ethereum, 3.691,98 Zcash, _dan jumlah Monero yang tidak diketahui._ "(bagian bawah dari hal.20 dan bagian atas dari hal.21, penekanan ditambahkan)
    * **Transaksi Bitcoin tidak bersifat pribadi dan dapat dilacak:**   
"Agen federal memperoleh surat perintah setelah melacak sejumlah transaksi Bitcoin yang berasal dari AlphaBay ke rekening mata uang digital, dan akhirnya rekening bank dan aset berwujud lainnya, yang dipegang oleh CAZES dan istrinya." (hal. 17, baris 24- 26) 

  * **Monero adalah satu-satunya mata uang kripto pribadi dan tidak dapat dilacak:**   
"Secara total, dari dompet CAZES dan agen komputer menguasai sekitar $8.800.000 dalam Bitcoin, Ethereum, Moreno [sic], dan Zcash, yang diuraikan sebagai berikut: 1.605,0503851 Bitcoin, 8.309,271639 Ethereum, 3.691,98 Zcash, _dan jumlah Monero yang tidak diketahui._ "(bagian bawah dari hal.20 dan bagian atas dari hal.21, penekanan ditambahkan)
  * **Transaksi Bitcoin tidak bersifat pribadi dan dapat dilacak:**   
"Agen federal memperoleh surat perintah setelah melacak sejumlah transaksi Bitcoin yang berasal dari AlphaBay ke rekening mata uang digital, dan akhirnya rekening bank dan aset berwujud lainnya, yang dipegang oleh CAZES dan istrinya." (hal. 17, baris 24- 26) 

LocalMonero tidak menganjurkan atau mendorong aktivitas ilegal apa pun. 

LocalMonero tidak menganjurkan atau mendorong aktivitas ilegal apa pun. 

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies)/

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys)/

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero)/

  * [Bagaimana node jarak jauh memengaruhi privasi Monero](/knowledge/remote-nodes-privacy)/

  * [Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan](/knowledge/network-upgrades)/

  * [Lihat tag: Bagaimana satu byte akan mengurangi waktu sinkronisasi dompet Monero hingga 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

  * [P2Pool dan Perannya dalam Desentralisasi Penambangan Monero](/knowledge/p2pool-decentralizing-monero-mining)/

  * [Seraphis: Apa yang Akan Dilakukannya untuk Monero](/knowledge/seraphis-for-monero)/

  * [Apakah Mengonversi Bitcoin ke Monero Sama Privatnya dengan Membeli Monero Secara Langsung?](/knowledge/most-private-way-to-buy-monero)/

  * [Mengapa Monero Menggunakan Pengaturan Tanpa Kepercayaan Tidak Seperti Zcash](/knowledge/monero-trustless-setup)/

  * [Mengapa Monero Adalah Penyimpan Nilai Yang Lebih Baik Dibandingkan Dengan Bitcoin](/knowledge/monero-better-store-of-value)/

  * [Bagaimana Monero Dapat Mengatasi Efek Jaringan Bitcoin](/knowledge/network-effect)/

  * [Mengapa Monero Memiliki Komunitas Dengan Pemikiran Paling Kritis](/knowledge/critical-thinking)/

  * [Penipuan yang Harus Diwaspadai Saat Menggunakan Monero](/knowledge/monero-scams)/

  * [Bagaimana Atomic Swap Akan Bekerja di Monero](/knowledge/monero-atomic-swaps)/

  * [Apa yang Perlu Diketahui Setiap Pengguna Monero Saat Berbicara tentang Jaringan](/knowledge/monero-networking)/

  * [Bagaimana RingCT Menyembunyikan Jumlah Transaksi Monero](/knowledge/monero-ringct)/

  * [Bagaimana Stealth Address Monero Melindungi Identitas Anda](/knowledge/monero-stealth-addresses)/

  * [Bagaimana Sub Alamat Monero Mencegah Penautan Identitas](/knowledge/monero-subaddresses)/

  * [Output Monero Dijelaskan](/knowledge/monero-outputs)/

  * [Praktik Terbaik Monero untuk Pemula](/knowledge/monero-best-practices)/

  * [Bagaimana Ring Signature Mengaburkan Output Monero](/knowledge/ring-signatures)/

  * [Bagaimana Monero Memecahkan Masalah Ukuran Blok Yang Mengganggu Bitcoin](/knowledge/dynamic-block-size)/

  * [Bagaimana CLSAG Akan Meningkatkan Efisiensi Monero](/knowledge/what-is-clsag)/

  * [Mengapa Monero Memiliki Tail Emission](/knowledge/monero-tail-emission)/

  * [Sejarah Singkat Monero](/knowledge/monero-history)/

  * [Majalah Wired Salah Tentang Monero, Ini Alasannya](/knowledge/wired-article-debunked)/

  * [Top 15 Mitos dan Kekhawatiran Monero Terbantahkan](/knowledge/monero-myths-debunked)/

  * [Bagaimana Dandelion++ Menjaga Kerahasiaan Asal Transaksi Monero](/knowledge/monero-dandelion)/

  * [Mengapa Monero Open Source Dan Terdesentralisasi](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa](/knowledge/monero-mining-randomx)/

Bacaan lebih lanjut