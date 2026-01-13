---
title: "Bagaimana CLSAG Akan Meningkatkan Efisiensi Monero"
slug: "what-is-clsag"
date: "2020-08-05"
image: "/images/clsag.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Sebagai sebuah protokol, Monero saat ini terus berinovasi. Memanfaatkan penelitian dalam solusi on-chain dan off-chain, komunitas Monero mencari area untuk ditingkatkan agar Monero lebih privat, lebih dapat diskalakan, dan lebih mudah diakses oleh semua orang. Salah satu inovasi terbaru adalah penggantian skema ring signature yang dapat ditautkan, MLSAG, dengan pengganti drop-in CLSAG, yang merupakan singkatan dari Concise Linkable Spontaneous Anonymous Group.

Pada tingkat permukaan, implementasi CLSAG akan menurunkan 2 input paling umum, 2 transaksi output sebesar 25%. Kami juga akan melihat penurunan waktu verifikasi sebesar 10%. 

Tapi apa sebenarnya CLSAG itu? Apa fungsinya, dan apa yang membedakannya dengan versi lama, MLSAG? Mari luangkan waktu sejenak untuk mengingatkan diri kita tentang mengapa dan bagaimana ring signature itu sehingga kita dapat lebih memahami konsep ini. Ring signature memungkinkan input yang bersifat non-interaktif dan yang tidak dapat dibedakan oleh saksi melalui penggunaan kumpulan anonimitas yang dipilih oleh penanda tangan dari output sebelumnya. Dalam istilah awam, ini memungkinkan pengguna untuk menyembunyikan luaran mereka yang digunakan dalam transaksi bersama keluaran yang tidak terkait, dan mereka dapat melakukan semua ini tanpa memerlukan orang lain untuk ambil bagian. Yang Anda butuhkan hanyalah salinan blockchain. Masing-masing luaran ini sebagian besar tampaknya memiliki kemungkinan yang sama untuk dikirim, sehingga menyembunyikan metadata tentang pengirim.

Namun, ini menimbulkan sedikit masalah. Bagaimana jika pengguna membuat ring signature dengan semua luaran pengecoh? Bagaimana orang tahu bahwa pengirim yang tidak dikenal tersebut tidak memiliki wewenang untuk mengirim hal-hal itu? Akankah pengguna ini dapat membelanjakan uang palsu? Jawabannya adalah tidak. Ring signature mencakup metode untuk membuktikan bahwa setidaknya salah satu luaran dimiliki oleh pengirim yang tidak dikenal, tanpa mengungkapkan yang mana. Faktanya, CLSAG dan MLSAG (selanjutnya dikenal sebagai SAG) adalah bagian dari ring signature yang membuktikan hal ini. Menariknya, pada waktu yang sama, juga membuktikan bahwa jumlah transaksi berimbang, meski tersembunyi di balik transaksi rahasia (RingCT). Bahwa SAG membuktikan dua hal, bahwa satu luaran dimiliki oleh seseorang di ring, dan bahwa transaksi berimbang, itu penting, dan sebenarnya di mana ukuran dan verifikasi tabungan itu berada. Jika ini semakin membingungkan, jangan khawatir, kita akan segera mendapatkan analogi yang menyenangkan dan mudah dipahami.

Skema signature lama, MLSAG (Multilayered Linkable Spontaneous Anonymous Group) membuktikan dua hal yang disebutkan di atas dalam ring signature, tetapi masing-masing melakukannya secara terpisah. Penggunaan komputasi terpisah untuk penandatanganan dan kunci komitmen berarti pengoperasian akan lebih lambat. Komputer modern dapat melakukan komputasi ini dalam hitungan milidetik, yang terlihat seperti tidak banyak, dan memang, tidak banyak untuk satu transaksi. Tetapi ketika kami mempertimbangkan banyaknya transaksi pada blockchain Monero, dan bahwa sebuah node yang disinkronkan dari awal harus mengunduh dan memverifikasi masing-masing transaksi, byte dan milidetik mulai menumpuk dengan cepat.

CLSAG menggabungkan matematika yang diperlukan untuk membuktikan keduanya menjadi satu, serta menghitung keduanya sekaligus, dan melakukannya dengan cara yang aman. Apa artinya dengan cara yang aman? Nah, untuk memperjelas hal ini, dan semoga semuanya menjadi lebih masuk akal, mari jelajahi analogi menyenangkan yang dijanjikan di atas tadi.

Katakanlah Anda harus pergi ke toko kelontong dan toko perangkat keras, untuk membeli dua hal yang berbeda: makanan dan bahan kimia pembersih beracun. Anda tidak ingin mereka bercampur, seolah-olah terjadi kecelakaan, bahan kimia akan tumpah ke makanan, membuatnya tidak bisa dimakan. Anda memutuskan untuk menjadi seseorang yang sangat aman dan berkendara dari rumah Anda ke toko kelontong, membeli makanan, dan kemudian kembali ke rumah Anda. Hanya setelah Anda menurunkan makanan Anda kembali ke mobil, pergi ke toko perangkat keras, dan kembali ke rumah Anda dengan bahan kimia. Anda telah melakukan dua perjalanan terpisah untuk memastikan keamanan semua pembelian. Meskipun memang aman, itu tidak efisien. Ini mewakili MLSAG, di mana dua set matematika yang berbeda disimpan dan dua 'perjalanan' yang berbeda dilakukan agar dapat menghitungnya.

Namun, Anda memutuskan ingin cara yang lebih cepat untuk melakukan ini. Terlalu banyak membuang waktu. Tentu melakukannya sekali atau dua kali tidak akan mencuri hidup Anda, tetapi harus melakukan ini berulang kali, jam akan mulai bertambah. Anda mulai bertanya-tanya apakah Anda dapat melakukan satu perjalanan saja. Dari rumah Anda, ke toko kelontong, ke toko perangkat keras, dan kembali ke rumah. Anda tidak bisa begitu saja pergi dan membuang semua yang ada di mobil Anda sembarangan. Itu tidak aman. Sebaliknya, Anda menempatkan titik yang berbeda di mobil Anda untuk barang yang berbeda, dan memastikan semuanya terpasang dengan rapi pada tempatnya. Dengan demikian, Anda dapat dengan aman melakukan satu perjalanan ke kedua toko, dan menjauhkan barang dari satu sama lain. Ini mewakili CLSAG. Sekarang hanya ada satu set matematika yang disimpan dalam transaksi ini untuk membuktikan kedua hal tersebut, dan itu dilakukan agar tidak saling mengganggu satu sama lain. Perjalanan harus tetap dilakukan, tetapi Anda telah mengurangi jumlahnya secara drastis.

Semua ini terdengar cukup menarik. Mungkinkah kita dapat menemukan jalan pintas lain, atau cara lain untuk menghemat ruang dan waktu? Jawabannya adalah ya dan tidak. Menurut peneliti MRL saat ini, sepertinya tidak mungkin untuk memodifikasi konstruksi tipe SAG lebih lanjut untuk ukuran atau kecepatan yang lebih baik; namun konstruksi lain seperti Arcturus, Omniring, RCT3, atau Triptych menghasilkan penskalaan ukuran dan manfaat verifikasi yang jauh lebih baik menggunakan metode matematika yang berbeda. Namun, masing-masing pendekatan 'next-gen' untuk protokol penanda tangan yang ambigu hadir dengan pengorbanannya sendiri dalam detail implementasi, dan sedang menjalani penelitian dan investigasi aktif. 

Lagipula, Monero selalu berinovasi.

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

  * [Mengapa Monero Memiliki Tail Emission](/knowledge/monero-tail-emission)/

  * [Sejarah Singkat Monero](/knowledge/monero-history)/

  * [Majalah Wired Salah Tentang Monero, Ini Alasannya](/knowledge/wired-article-debunked)/

  * [Top 15 Mitos dan Kekhawatiran Monero Terbantahkan](/knowledge/monero-myths-debunked)/

  * [Bagaimana Dandelion++ Menjaga Kerahasiaan Asal Transaksi Monero](/knowledge/monero-dandelion)/

  * [Mengapa Monero Open Source Dan Terdesentralisasi](/knowledge/why-monero-is-open-source-and-decentralized)/

  * [Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa](/knowledge/monero-mining-randomx)/

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better)/

Bacaan lebih lanjut