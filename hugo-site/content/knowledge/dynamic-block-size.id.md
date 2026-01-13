---
title: "Bagaimana Monero Memecahkan Masalah Ukuran Blok Yang Mengganggu Bitcoin"
slug: "dynamic-block-size"
date: "2020-08-28"
image: "/images/blocks.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
_**Catatan:** Sangat disarankan agar pembaca sudah membaca artikel kami ["Mengapa Monero Memiliki Emisi Ekor"](/knowledge/monero-tail-emission) dan [“Penambangan Monero: Apa yang Membuat RandomX sangat Istimewa”](/knowledge/monero-mining-randomx). Artikel ini dibangun dari konsep yang disajikan di sana._

Setiap kali seseorang mendiskusikan tentang masalah dengan blockchain, salah satu kata pertama yang muncul adalah 'scaling'. Bukan rahasia bahwa blockchain tidak dapat diskalakan dengan baik, tetapi kebanyakan orang tidak tahu alasannya.

kebenarannya adalah bahwa scaling sebenarnya merupakan istilah umum yang mencakup dua kategori berbeda: Dukungan protokol dan dukungan teknologi pada titik waktu tertentu. Pada artikel ini, kita akan memfokuskan perhatian kita pada satu hal, dukungan Protokol pada dasarnya adalah sebuah ukuran mengenai berapa banyak transaksi yang dapat ditangani oleh protokol pada waktu tertentu.

Bitcoin memiliki batas ukuran blok, yang berarti setelah cukup transaksi disertakan dalam satu blok, setiap transaksi tambahan harus mengantri untuk blok berikutnya. Sebuah analogi yang sangat membantu mungkin adalah jika kita berpikir tentang kereta api. Sebuah kereta berhenti di stasiun, dan mereka yang mengantre masuk. Setelah kereta penuh, siapa pun yang tertinggal di luar harus menunggu kereta berikutnya.

Bitcoin menggunakan biaya untuk menentukan siapa yang masuk ke blok atau tidak. Melompat kembali ke analogi kereta api, dapat dibayangkan seorang calon penumpang, yang akan ditinggalkan, menawarkan masinis kereta lima dolar untuk memberinya tempat duduk. Penumpang lain mengikuti, dan akhirnya terjadi perang penawaran untuk melihat siapa yang mendapatkan kursi yang mana. Terserah pada pengemudi untuk memutuskan apakah dia ingin menghormati kebijakan siapa cepat dia dapat, tetapi adalah demi kepentingan terbaik bagi keuangannya untuk memaksimalkan pendapatannya dengan mengambil penawar tertinggi yang masuk.

Dalam analogi ini, penambang adalah masinis kereta. Mereka dapat menyertakan transaksi mana pun yang mereka inginkan ke dalam blok, tetapi umumnya mereka akan memilih transaksi yang memiliki biaya pembayaran tertinggi.

Alternatifnya, jika blok tidak terlalu penuh, orang tidak memiliki insentif untuk membayar biaya tinggi karena ada banyak kursi kosong yang tersisa.

Pada puncak ledakan mata uang kripto di 2017, Bitcoin dibanjiri dengan transaksi, dan biaya meroket bagi mereka yang ingin dimasukkan ke dalam blok berikutnya, atau blok mana pun dalam waktu dekat. Mereka yang tidak mau membayar biaya tinggi melihat transaksi mereka mundur selama berjam-jam, berhari-hari, atau bahkan keluar dari antrian sama sekali.

Ini adalah wawasan yang mengerikan tentang bagaimana nasib Bitcoin jika 'adopsi massal' yang sering dibicarakan itu terjadi. Jika Bitcoin akan digunakan oleh massa, keadaan akan menjadi lebih buruk daripada tahun 2017, dan Bitcoin tidak akan dapat diakses oleh siapa pun kecuali orang kaya, hanya karena throughputnya kecil diakibatkan oleh ukuran blok yang tetap, menyebabkan biaya pasar mengambil alih.

Monero meramalkan ini dan ingin melakukan sesuatu yang berbeda. Jadi pengembang Monero menerapkan ukuran blok dinamis.

Pada dasarnya, Monero juga memiliki ukuran blok cap, tetapi itu adalah soft cap. Ketika antrean menunggu transaksi terlalu panjang, para penambang dapat menambah ukuran blok. Dengan analogi kereta kita, Anda dapat membayangkan menambahkan lebih banyak gerbong kereta agar menyesuaikan dengan penumpang ekstra. Setelah antrian kosong, blok menyusut kembali ke ukuran aslinya seterusnya. 

Jika ini terlihat seperti ide yang bagus, tampaknya masuk akal untuk bertanya mengapa Monero adalah satu-satunya mata uang kripto yang menerapkan ini. Mengapa tidak menambahkannya ke Bitcoin untuk menghentikan masalah throughput?

Sayangnya, ini tidak mungkin. Ada beberapa alasan mengapa, dan kami akan berusaha menjelaskannya.

Selalu menjadi kepentingan terbaik bagi penambang untuk memiliki blok yang besar. Dengan blok besar, mereka dapat melakukan lebih banyak transaksi, dan menghasilkan lebih banyak uang dari biaya, serta hadiah blok. Hal ini berpotensi menyebabkan serangan spam, di mana seseorang mengirimkan banyak transaksi-transaksi kecil, dengan biaya kecil, untuk membengkakkan chain. Penambang hanya akan menaikkan ukuran blok memasukkan semuanya karena uang tetaplah uang, tidak peduli seberapa kecilnya. Hal ini akan mengarahkan pada blok yang besar secara konsisten dengan sedikit manfaat ekonomi. Bitcoin menyelesaikan ini dengan membatasi ukuran blok secara artifisial, sehingga menghasilkan pasar biaya. Penyerang spam harus mengalahkan pengguna lain dalam hal biaya, dan itu tidak akan murah lagi. Tapi ini berarti blok menjadi penuh, membiarkan beberapa transaksi menunggu seperti yang disebutkan di atas.

Jadi bagaimana Monero bisa memiliki ukuran blok dinamis tetapi mampu menghindari serangan spam? Jawabannya sederhana, namun cerdas. Penalti pada hadiah blok diperkenalkan ketika blok menjadi lebih besar dari biasanya. Jika seorang penambang ingin meningkatkan ukuran blok, hadiah yang mereka dapatkan dari menemukan blok itu akan lebih sedikit daripada yang seharusnya mereka terima. Jadi mereka hanya akan meningkatkan ukuran blok ketika biaya transaksi yang dibayarkan pengguna lebih besar daripada bagian yang hilang dari hadiah blok. Misalnya, jika penambang kehilangan 0,5 XMR dengan menaikkan ukuran blok, dan jumlah biaya transaksi yang dibayarkan menjadi 0,4 XMR, maka akan ada kerugian bersih sebesar 0,1 XMR jika mereka menaikkan ukuran, jadi mereka tidak akan melakukan hal itu. Sebaliknya, jika total biaya transaksi dijumlahkan menjadi 0,7 XMR, maka akan ada keuntungan bersih sebesar 0,2 XMR, meskipun mereka kehilangan 0,5 XMR dari pinalti hadiah blok, sehingga penambang akan meningkatkan ukurannya.

Blok dinamis ini, memungkinkan jaringan untuk tumbuh secara organik, tanpa membatasi ukuran blok secara artifisial untuk membuat pasar biaya yang dipaksakan, sambil tetap menghindari serangan spam. Ada beberapa sudut lagi yang dapat kami lihat dari ide ini, dan lebih banyak alasan mengapa hal itu tidak mungkin ditambahkan ke Bitcoin, tetapi untuk saat ini, kami berharap bahwa pembaca memiliki pemahaman tentang bagaimana Monero menghindari beberapa masalah dalam Bitcoin dan turunannya, dan bagaimana rencananya untuk menskalakan throughputnya ke masa depan.

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

  * [Bagaimana Sub Alamat Monero Mencegah Penautan Identitas](/knowledge/monero-subaddresses/)

  * [Output Monero Dijelaskan](/knowledge/monero-outputs/)

  * [Praktik Terbaik Monero untuk Pemula](/knowledge/monero-best-practices/)

  * [Bagaimana Ring Signature Mengaburkan Output Monero](/knowledge/ring-signatures/)

  * [Bagaimana CLSAG Akan Meningkatkan Efisiensi Monero](/knowledge/what-is-clsag/)

  * [Mengapa Monero Memiliki Tail Emission](/knowledge/monero-tail-emission/)

  * [Sejarah Singkat Monero](/knowledge/monero-history/)

  * [Majalah Wired Salah Tentang Monero, Ini Alasannya](/knowledge/wired-article-debunked/)

  * [Top 15 Mitos dan Kekhawatiran Monero Terbantahkan](/knowledge/monero-myths-debunked/)

  * [Bagaimana Dandelion++ Menjaga Kerahasiaan Asal Transaksi Monero](/knowledge/monero-dandelion/)

  * [Mengapa Monero Open Source Dan Terdesentralisasi](/knowledge/why-monero-is-open-source-and-decentralized/)

  * [Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa](/knowledge/monero-mining-randomx/)

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better/)