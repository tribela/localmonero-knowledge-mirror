---
title: "Bagaimana Stealth Address Monero Melindungi Identitas Anda"
slug: "monero-stealth-addresses"
date: "2020-10-21"
image: "/images/stealth.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero telah menerapkan pendekatan tiga cabang untuk privasi. Teknologi ini adalah [ring signatures](/knowledge/ring-signatures), yang menyembunyikan output sebenarnya (pengirim), RingCT yang menyembunyikan jumlah, dan stealth address (alamat tersembunyi), yang menyembunyikan penerima. Hari ini, kita akan membahas teknologi terakhir yang disebutkan ini: stealth address.

Ada banyak alasan mengapa seseorang mungkin ingin menyembunyikan kepada siapa mereka mengirim. Kita tidak boleh membiarkan siapa pun mencoba meyakinkan kita bahwa semua contoh ini adalah perilaku yang tidak baik. Hal-hal seperti mengirim ke partai politik yang tidak populer, menyumbang ke badan amal, atau mendukung hal-hal yang dianggap 'cancelled' oleh budaya adalah contoh di mana seseorang mungkin ingin menyembunyikan perilaku belanja mereka karena takut akan dampaknya, tetapi pada dasarnya sah-sah saja.

Pada blockchain transparan, alamat tujuan pengiriman transaksi dapat dilihat oleh semua orang. Penting untuk dipertimbangkan bahwa jika penambang sendiri tidak setuju dengan ke mana uang itu pergi, mereka dapat memilih untuk tidak menambangnya menjadi blok, secara efektif menyensor transaksi ini pada platform yang tampaknya tahan sensor. Satu-satunya cara untuk membuat ini, diakui tidak mungkin, penyensoran tidak mungkin dilakukan adalah jika penambang tidak dapat membedakan antara transaksi karena semua metadata on-chain dikaburkan dengan berbagai cara. Sesuatu yang membuat Monero terkenal.

Monero memecahkan masalah alamat transparan ini dengan menerapkan stealth address, sebuah teknologi yang awalnya dibuat untuk Bitcoin pada tahun 2011 oleh pengguna forum Bitcoin Talk, ByteCoin (hubungannya dengan Bytecoin, yang nantinya akan mengintegrasikan stealth address, tidak diketahui). Bentuk dari stealth address saat ini sudah mendapatkan beberapa perbaikan dari ide awal. Namun pertama-tama, untuk melihat cara kerjanya, mari kita bicara tentang kunci.

Sulit berada di ruang kripto dan tidak mendengar tentang kunci. Ungkapan seperti 'cadangkan kunci pribadi Anda' sudah umum, tetapi ketika seorang average Joe mendengar kata "kunci publik" dan "kunci pribadi", mereka menjadi takut dan berpikir itu akan terlalu teknis dan membingungkan untuk dipahami. Tapi jangan khawatir. Kita akan melakukannya pelan-pelan, dan menggunakan banyak contoh.

Dua jenis kunci yang digunakan dalam mata uang kripto adalah, seperti yang baru saja disebutkan, publik dan pribadi. Kedua kunci ini biasanya berpasangan, artinya kunci publik dan privat tertentu saling terkait satu sama lain. Faktanya, biasanya kunci publik diturunkan dari kunci privat, artinya jika Anda mengetahui kunci privatnya, dompet Anda dapat melakukan perhitungan matematika yang bagus dan menghasilkan kunci publik yang benar setiap saat.

Sekarang, seperti namanya, kunci publik dapat bersifat publik tanpa konsekuensi. Biasanya itu adalah bagian dari alamat yang Anda bagikan untuk menerima uang ke dompet kripto Anda. Juga sesuai dengan namanya, kunci privat adalah satu hal yang tidak boleh dibagikan. Itu adalah hal yang memungkinkan Anda untuk menandatangani dan membelanjakan transaksi, jadi jika dicuri atau dibagikan, pihak ketiga pengecut dapat menghabiskan uang Anda, biasanya untuk diri mereka sendiri.

Analogi yang mudah untuk ini adalah gembok dan kunci yang diperlukan untuk membukanya. Gembok yang terbuka dapat dibagikan secara bebas, dan memang apa saja dapat dikunci dengan gembok ini, namun hanya orang yang memiliki kunci yang dapat membuka apapun yang tertutup gembok tersebut. Gembok dapat disalin dan dibagikan, kuncinya tidak boleh.

Kunci ini biasanya dipisahkan dari pengguna, sehingga Anda tidak pernah benar-benar melihatnya. Di Monero, kunci-kunci ini sama sekali tidak terlihat sebagai string alfanumerik yang menakutkan. Di Monero, pengguna umum mengetahui kunci privat sebagai seed mereka. Seed (yang harus Anda tulis jika belum), sebenarnya hanyalah kunci pribadi yang dapat dibaca manusia. 

Lihat? Lagipula tidak terlalu menakutkan. Kembali ke stealth address.

Seperti yang disebutkan sebelumnya, stealth address pada awalnya tidak dibuat untuk Monero, tetapi Bitcoin. Seperti kebanyakan ide pemula, iterasi pertama ini memiliki masalah. Upaya berikutnya datang ketika CryptoNote dibuat oleh Nicholas van Saberhagan untuk Bytecoin, pendahulu Monero ([ lihat sejarah Monero dan Bytecoin kami di sini ](/knowledge/monero-history)), dan meskipun itu merupakan peningkatan yang definitif dibandingkan aslinya, bahkan itu masih memiliki beberapa kelemahan halus. 

Akhirnya, satu iterasi terakhir muncul dari pengembang untuk mata uang kripto privasi lain yang sekarang sudah tidak berfungsi, yang memperbaiki masalah privasi dan keamanan yang luar biasa dengan ide tersebut. Iterasi ini akhirnya masuk ke Monero, dan digunakan saat ini.

Meskipun masalah privasi dan keamanan ini diselesaikan, stealth address itu sendiri menambahkan jenis kekhasan yang berbeda pada teknologi blockchain, yang sebelumnya tidak ada. Kebutuhan untuk memindai. Karena alamat penerima tidak ditampilkan secara publik di blockchain, penerima tidak pernah tahu apakah ada transaksi yang diberikan adalah milik mereka, jadi mereka harus memindai setiap transaksi yang masuk dengan kunci pribadi mereka untuk melihat apakah itu milik mereka.

Dengan koin transparansi, yang harus mereka lakukan hanyalah memeriksa apakah transaksi dikirim ke alamat Anda. Pertanyaan ya atau tidak yang mudah. Tetapi dengan alamat tersembunyi, setiap transaksi berpotensi menjadi salah satu yang dikirimkan kepada Anda, jadi Anda harus mencoba membuka setiap transaksi dengan kunci pribadi Anda untuk melihat apakah itu terbuka.

Ini adalah langkah ekstra yang tidak dimiliki Bitcoin dan turunannya, dan membuat pengaturan awal dompet, bersamaan dengan menyinkronkan dompet saat Anda belum membukanya untuk sementara waktu, jauh lebih lama daripada Bitcoin. Pengorbanan diperlukan, untuk membuka kunci jaminan privasi yang dimilikinya. Perlu dicatat bahwa, tidak seperti titik terlemah dari trifecta privasi, ring signature, stealth address tidak rentan terhadap heuristik. Itu bergantung pada kriptografi kurva eliptik yang dicoba dan benar, yang diandalkan oleh seluruh internet, jadi melanggarnya berarti mengakhiri keamanan komputer secara umum, bukan hanya Monero.

Bacaan lebih lanjut