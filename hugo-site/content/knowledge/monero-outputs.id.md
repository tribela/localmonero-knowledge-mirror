---
title: "Output Monero Dijelaskan"
slug: "monero-outputs"
date: "2020-09-30"
image: "/images/outputs.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero, seperti mata uang kripto lainnya, menggunakan output sebagai alat untuk menghitung dana. Banyak pengguna kripto yang mengerti mungkin pernah mendengar istilah ini sebelumnya, tetapi tidak semua orang mengerti apa artinya dan bagaimana cara kerjanya. Seperti yang dieksplorasi dalam artikel ring signature [ kami ](/knowledge/ring-signatures), output adalah unit aktual yang dipertukarkan di blockchain antara pihak yang bertransaksi. Mirip dengan uang dolar, tetapi jumlahnya tidak dalam denominasi tetap.

Jika Anda dibayar $16 untuk suatu pekerjaan, Anda mungkin menerima uang satu dolar, uang lima dolar, dan uang sepuluh dolar. Anda memiliki $16, tetapi Anda juga memiliki tiga tagihan berbeda di dompet Anda. Jika Anda ingin membayar seseorang 6 dolar, Anda dapat menggunakan tagihan 5 dan 1, tetapi jika Anda ingin membayar seseorang $8, Anda hanya dapat menggunakan $10 dan menerima kembali $2 sebagai kembaliannya. Terakhir, jika Anda ingin membayar seseorang $14, Anda harus menggunakan ketiga lembar uang tersebut, dan akan menerima kembali $2 sebagai kembalian, tetapi untuk sesaat, saat Anda menyerahkan ketiga lembar uang tersebut, Anda tidak memiliki uang di dompet Anda sampai Anda mendapatkan uang kembaliannya.

Monero bekerja dengan cara yang sama. Misalkan Anda menjalankan toko dan menghasilkan tiga penjualan untuk tiga item berbeda. Anda mungkin menerima 1,5 XMR, 2,25 XMR, dan 5,25 XMR dengan total 9 XMR, tetapi Anda juga memiliki tiga output berbeda di dompet Anda dari denominasi yang disebutkan sebelumnya. Sama seperti dengan dolar, Anda mungkin ingin membayar seseorang 3 XMR. Anda dapat menggunakan hanya keluaran 5,25 XMR, dan menerima uang kembalian 2,25 XMR, atau Anda dapat menggabungkan output XMR 1,5 dan 2,25 dan mendapatkan kembali 0,75 XMR dalam perubahan.

Namun, segera setelah Anda mengirim transaksi, output yang Anda gunakan dimasukkan ke dalam status "terkunci", artinya tidak dapat diakses sampai Anda menerima kembaliannya. Protokol membuka kunci dana (yaitu memberi Anda kembalian) setelah 10 konfirmasi, atau sekitar 20 menit. Sama seperti ketika Anda menyerahkan uang dolar dari dompet Anda, Anda tidak dapat menggunakan uang itu lagi sampai Anda menerima kembalian dari kasir, Monero Anda tidak dapat diakses sampai Anda menerima kembalian tersebut.

Mari kita kembali ke contoh mengirim 3 XMR ke seseorang, dan Anda menggunakan output 5,25 XMR. Sekarang, sementara Anda menunggu 1,75 XMR Anda kembali, Anda tidak dapat menggunakannya. 1,75 XMR ini tidak dapat Anda akses. Tetapi Anda masih dapat menggunakan output 1,5 XMR dan 2,25 XMR, karena ini tidak digunakan. Kembali ke contoh dolar, jika Anda membayar seseorang $8, seperti pada contoh sebelumnya, Anda tidak akan dapat menggunakan kembalian $2 yang Anda harapkan sampai diberikan kepada Anda, tetapi dalam contoh ini, Anda masih memiliki uang $10 yang tidak terpakai di dompet Anda. Ini masih dapat digunakan untuk membeli apa pun yang Anda inginkan sambil menunggu kembalian. Sama dengan Monero.

Ini sering menjadi titik kebingungan bagi pengguna baru Monero. Seringkali, pengguna mungkin hanya memiliki satu output di dompetnya, yang diterima dari exchange atau teman. Katakanlah output ini adalah 20 XMR. Mereka tidak memiliki output lain di dompet mereka. Mereka sekarang ingin memberikan sumbangan ke dua badan amal favorit mereka. Mereka mengirimkan 5 XMR ke badan amal pertama dan kemudian bingung karena, meskipun seharusnya sisa 15 XMR, mereka tidak dapat langsung mengirimkan sumbangan berikutnya ke badan amal kedua. Seperti yang mungkin sudah Anda duga, ini karena 15 XMR terkunci. Itu tidak dapat dihabiskan sampai dikembalikan sebagai kembalian (10 konfirmasi atau sekitar 20 menit). Setelah dana mereka dibuka, mereka dapat mengirimkan donasi kedua.

Hanya untuk menegaskan kembali intinya, mereka tidak akan mengalami masalah ini jika mereka memiliki beberapa output, seperti dua output 10 XMR atau serupa. Mereka dapat mengirimkan kedua donasi satu per satu, karena donasi pertama akan menggunakan salah satu dari 10 output XMR (dan menunggu 10 konfirmasi untuk menerima kembali 5 XMR sebagai kembaliannya), dan donasi kedua akan menggunakan output 10 XMR lainnya.

Beberapa dompet mata uang kripto memiliki fitur yang disebut 'manajemen keluaran', yang hanya menunjukkan kepada pengguna output mana yang mereka miliki saat ini (selain jumlah totalnya), serta memungkinkan mereka untuk memilih mana yang ingin mereka gunakan saat berbelanja mata uang kripto mereka.

Sampai sekarang, GUI Monero melakukan pemilihan output untuk pengguna secara otomatis, karena pengguna memilih output mereka sendiri sering menyebabkan kebingungan atau, dalam beberapa kasus, membahayakan privasi. Namun ada dompet yang sedang dibangun, seperti proyek Feather Wallet baru, yang akan berisi fitur manajemen output ini.

Kami telah berbicara banyak tentang bagian pengiriman, tetapi sesuatu yang menarik terjadi di pihak penerima. Kembali ke contoh kami mengirim 3 XMR ke seseorang, dan menggunakan output 1,5 XMR dan 2,25 XMR Anda dalam transaksi (sambil mengharapkan 0,75 XMR sebagai kembalian), penerima TIDAK menerima dua output 1,5 XMR dan 2,25 XMR. Mereka malah menerima output SATU 3 XMR.

Di latar belakang, protokol menggabungkan semua output yang digunakan untuk pengeluaran, dan memberikan penerima satu output dari jumlah yang dibayarkan, dan mengirimkan satu keluaran perubahan kembali ke pengirim. Jadi pengirim juga akan menerima satu keluaran kembali sebagai perubahan, terlepas dari apakah mereka menggunakan dua, tiga, atau sepuluh output untuk mengirim transaksi.

Kami harap ini telah menjernihkan beberapa kebingungan tentang output dan cara kerja akuntansi internal protokol, serta pengguna umum yang menghadapi masalah kebingungan saat menghadapi dana terkunci. Di artikel lain, kami akan mengeksplorasi pengelolaan output Anda untuk meminimalkan kemungkinan harus menunggu dana tidak terkunci sebelum mengirim transaksi di masa mendatang.

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