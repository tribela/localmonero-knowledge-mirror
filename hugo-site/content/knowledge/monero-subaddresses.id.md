---
title: "Bagaimana Sub Alamat Monero Mencegah Penautan Identitas"
slug: "monero-subaddresses"
date: "2020-10-13"
image: "/images/subaddresses.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero selalu menemukan cara inovatif untuk memecahkan masalah privasi yang sulit. Seringkali inovasi ini mengarah pada inovasi lain, dan terkadang teknologi yang dihasilkan ini bahkan dapat digunakan untuk kasus penggunaan yang sebelumnya tidak dipertimbangkan. Tidak ada yang lebih dapat dijadikan contoh daripada dalam kasus teknologi subaddress Monero. 

Pertimbangkan masalah privasi hipotetis, di mana penggunaan satu alamat di berbagai platform dari orang yang tampaknya tidak terkait dapat menyebabkan keterkaitan dan deanonimisasi orang tersebut. Sederhananya, jika Anda adalah seseorang bernama Billy Joe Bob dan Anda menjual apel untuk mendapatkan Bitcoin, Anda dapat memposting alamat Bitcoin Anda di tempat umum agar pelanggan dapat membayar Anda. Katakanlah alamatnya dimulai dengan string alfanumerik 7XybV3... Namun mengesampingkan risiko privasi yang jelas dari siapa pun yang dapat memeriksa saldo Bitcoin Anda dan melihat berapa banyak yang telah Anda jual, ada hal kedua, yang jarang dibicarakan tentang risiko privasi. Katakanlah Anda juga seorang peretas bawah tanah dengan nama l33tz0r. Anda melakukan pekerjaan whistle-blowing, memberi tahu masyarakat yang tidak menaruh curiga tentang korupsi pemerintah, dan sangat penting bagi Anda untuk merahasiakan identitas Anda. Anda menerima sumbangan Bitcoin untuk pekerjaan Anda, dan memposting alamatnya di forum publik. Itu alamat yang sama dengan yang Anda gunakan untuk menerima uang dari pelanggan apel Anda. 7XybV3... satu.

Serangan deanonimisasi yang sederhana namun menghancurkan adalah menggunakan mesin pencari internet untuk mencari alamat Bitcoin Anda. Menempatkan alamat 7XybV3... di mesin menampilkan dua hasil berbeda. Bisnis apel, dan l33tz0r. Ini cukup untuk menghubungkan dua identitas dan mendeanonimkan l33tz0r, dengan konsekuensi yang berpotensi menakutkan dari kekuatan yang ada.

Penting untuk dicatat bahwa serangan ini JUGA dimungkinkan dengan Monero. Meskipun Monero menyembunyikan sebagian besar data on-chain, serangan ini tidak menggunakan data tersebut. Serangan itu hanya menggunakan alamat, yang harus dibagikan untuk menerima pembayaran. Secara publik dalam kasus sumbangan anonim. Ini adalah salah satu cara potensial di mana pengguna Monero tanpa disadari dapat merusak privasi mereka, dan juga merupakan contoh bagaimana, meskipun Monero adalah tingkat teratas dalam hal retensi privasi, itu tidak anti peluru. 

Cara biasa untuk mengatasi masalah ini adalah memiliki banyak dompet. Dengan alamat berbeda yang diposting untuk setiap identitas (atau usecase), mereka tidak dapat ditautkan. Tetapi privasi ini hanya berlaku jika pengguna tidak pernah mencampuradukkannya. Secara tidak sengaja memposting alamat yang salah akan memiliki efek tautan yang sama. Selain itu, seed dari setiap alamat harus dijaga keamanannya, meningkatkan kerja infosec yang diperlukan dengan setiap dompet baru yang dibuat.

Solusi Monero adalah subaddress. Kemampuan untuk membuat sejumlah besar alamat di bawah alamat utama, menggunakannya sebagai semacam seed. Setiap subaddress yang dihasilkan dapat menerima Monero, dan semuanya masuk ke dompet yang sama. Dengan menggunakan metode ini, jumlah identitas yang dapat dioperasikan di bawah satu alamat sangat besar sambil menjaga agar infosec tetap berfungsi seminimal mungkin. Alamat-alamat ini juga tidak dapat ditautkan secara matematis, jadi kecuali pengguna meneriakkan koneksi mereka ke dunia luar, observer dari luar akan mengalami kesulitan besar untuk menautkannya.

Tapi usecase lain yang menarik muncul dari subaddress; sebagai opsi pengganti ID pembayaran yang dibenci secara universal.

ID pembayaran adalah cara bagi pedagang untuk mengidentifikasi pelanggan yang mengirimkan pembayaran yang mana. Karena informasi Monero dikaburkan dalam chain, penerima transaksi tidak dapat melihat alamat mana yang mengirimkannya. Ini berarti bahwa jika ada item dengan harga yang sama dan beberapa pesanan, tidak mungkin untuk mengidentifikasi siapa yang mengirim apa. ID Pembayaran adalah string acak unik yang dihasilkan oleh pedagang dan diberikan kepada pelanggan. Pelanggan menambahkan ini sebagai bidang terpisah saat mengirim transaksi. String acak ini ditempatkan di blockchain sebagai bagian dari transaksi, dan dengan cara ini, pedagang dapat mengidentifikasi dan menyortir transaksi yang masuk.

Metode ini cacat dalam beberapa hal. Pertama, ini mengurangi keseragaman data on-chain. Tambahan, metadata unik dapat membuat beberapa transaksi berbeda dari yang lain, sehingga memungkinkan analisis heuristik. Ini terutama benar ketika metadata ini tidak diberlakukan sebagai kewajiban untuk semua. Membuat ini wajib untuk semua orang akan menambah ruang yang tidak perlu ke blockchain, dan hal ini tidak dikejar. Selain itu, jika ID pembayaran pernah digunakan kembali untuk alasan apa pun, akan sangat mudah untuk menautkan bahwa dua transaksi tersebut memiliki hubungan. Ini biasanya terjadi dengan setoran pada exchange, dan siapa pun dapat dengan mudah menautkan transaksi sebagai setoran di exchange, dan dari satu individu tertentu.

Kedua, dari perspektif UX, ID pembayaran membuat langkah kedua yang tidak biasa dilakukan oleh pengguna mata uang kripto yang berasal dari koin lain, dan jika langkah-langkah itu dilupakan maka hal itu akan menyebabkan sakit kepala besar bagi pedagang yang harus mengidentifikasi transaksi ini melalui cara lain . Hal ini biasanya diselesaikan dengan berbicara langsung dengan setiap pelanggan yang lupa mencantumkan ID pembayaran dan mengonfirmasi informasi pengenal lain yang hanya diketahui oleh mereka, seperti kombinasi jumlah, tanggal pengiriman, dan ID transaksi.

Langkah ekstra ini dilewatkan oleh banyak orang, dan sampai pada titik di mana beberapa exchange mulai membebankan biaya kepada pelanggan jika uang mereka harus diambil secara manual karena lupa ID pembayaran. Yang lain mengertakkan gigi dan menerima jika mereka harus membayar biaya dukungan tambahan, tetapi tidak ada yang senang karenanya. 

Ada satu solusi untuk ini, alamat terintegrasi, yang menggabungkan alamat dan ID pembayaran menjadi satu string, sehingga tidak dapat dilupakan, tetapi adopsi cukup lemah, meskipun pedagang akan menerima manfaat dari memasukkannya. 

Dalam pergantian peristiwa yang menarik, subaddress datang untuk menyelamatkan hari. Kemampuan untuk menghasilkan subaddress dalam jumlah besar per alamat utama, dan mengidentifikasi transaksi mana yang masuk ke subaddress mana, memungkinkan pedagang untuk melepaskan diri dari ID pembayaran dengan cara yang elegan, sambil mengadopsi teknologi Monero generasi berikutnya. Sejak saat itu, sebagian besar exchange dan pedagang telah beralih ke subaddress sebagai cara utama identifikasi transaksi.

Apa yang dimulai sebagai solusi untuk masalah privasi berubah menjadi sesuatu yang lebih, yang memecahkan masalah UX utama bagi pedagang dan pelanggan. Inovasi melahirkan lebih banyak inovasi, yang seringkali dapat bergulir menjadi kemenangan tak terduga bagi semua orang. Monero telah melihat ini berkali-kali, dan berusaha keras untuk berinovasi apa yang mungkin dilakukan di blockchain. Siapa yang tahu hal lain apa yang bisa kita buka bersama?

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies/)

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys/)

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero/)

  * [Bagaimana node jarak jauh memengaruhi privasi Monero](/knowledge/remote-nodes-privacy/)

  * [Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan](/knowledge/network-upgrades/)

  * [Lihat tag: Bagaimana satu byte akan mengurangi waktu sinkronisasi dompet Monero hingga 40%+](/knowledge/view-tags-reduce-monero-sync-time/)

  * [P2Pool dan Perannya dalam Desentralisasi Penambangan Monero](/knowledge/p2pool-decentralizing-monero-mining/)

  * [Seraphis: Apa yang Akan Dilakukannya untuk Monero](/knowledge/seraphis-for-monero/)

  * [Apakah Mengonversi Bitcoin ke Monero Sama Privatnya dengan Membeli Monero Secara Langsung?](/knowledge/most-private-way-to-buy-monero/)

  * [Mengapa Monero Menggunakan Pengaturan Tanpa Kepercayaan Tidak Seperti Zcash](/knowledge/monero-trustless-setup/)

  * [Mengapa Monero Adalah Penyimpan Nilai Yang Lebih Baik Dibandingkan Dengan Bitcoin](/knowledge/monero-better-store-of-value/)

  * [Bagaimana Monero Dapat Mengatasi Efek Jaringan Bitcoin](/knowledge/network-effect/)

  * [Mengapa Monero Memiliki Komunitas Dengan Pemikiran Paling Kritis](/knowledge/critical-thinking/)

  * [Penipuan yang Harus Diwaspadai Saat Menggunakan Monero](/knowledge/monero-scams/)

  * [Bagaimana Atomic Swap Akan Bekerja di Monero](/knowledge/monero-atomic-swaps/)

  * [Apa yang Perlu Diketahui Setiap Pengguna Monero Saat Berbicara tentang Jaringan](/knowledge/monero-networking/)

  * [Bagaimana RingCT Menyembunyikan Jumlah Transaksi Monero](/knowledge/monero-ringct/)

  * [Bagaimana Stealth Address Monero Melindungi Identitas Anda](/knowledge/monero-stealth-addresses/)

  * [Output Monero Dijelaskan](/knowledge/monero-outputs/)

  * [Praktik Terbaik Monero untuk Pemula](/knowledge/monero-best-practices/)

  * [Bagaimana Ring Signature Mengaburkan Output Monero](/knowledge/ring-signatures/)

  * [Bagaimana Monero Memecahkan Masalah Ukuran Blok Yang Mengganggu Bitcoin](/knowledge/dynamic-block-size/)

  * [Bagaimana CLSAG Akan Meningkatkan Efisiensi Monero](/knowledge/what-is-clsag/)

  * [Mengapa Monero Memiliki Tail Emission](/knowledge/monero-tail-emission/)

  * [Sejarah Singkat Monero](/knowledge/monero-history/)

  * [Majalah Wired Salah Tentang Monero, Ini Alasannya](/knowledge/wired-article-debunked/)

  * [Top 15 Mitos dan Kekhawatiran Monero Terbantahkan](/knowledge/monero-myths-debunked/)

  * [Bagaimana Dandelion++ Menjaga Kerahasiaan Asal Transaksi Monero](/knowledge/monero-dandelion/)

  * [Mengapa Monero Open Source Dan Terdesentralisasi](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa](/knowledge/monero-mining-randomx/)

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better/)