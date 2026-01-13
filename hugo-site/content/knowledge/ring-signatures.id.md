---
title: "Bagaimana Ring Signature Mengaburkan Output Monero"
slug: "ring-signatures"
date: "2020-09-08"
image: "/images/rings.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Monero dikenal jauh dan luas di ruang kripto sebagai raja koin privasi. Meskipun semua orang tahu Monero menawarkan privasi yang baik, tidak banyak yang memahami cara kerja privasi.

Banyak koin privasi lainnya menerbitkan infografis bagan perbandingan, yang mencantumkan nama teknologi privasi masing-masing koin, dan di sebagian besar mereka memberi label teknologi Monero sebagai RingCT, tetapi ini hanya sebagian yang benar. Monero sebenarnya memiliki tiga pendekatan privasi. Satu teknologi untuk menyembunyikan penerima transaksi, satu untuk menyembunyikan jumlah yang dikirim, dan satu lagi untuk menyembunyikan output yang digunakan, masing-masing adalah stealth address, RingCT, dan ring signature.

Pendekatan tiga cabang ini berarti bahwa jika salah satu teknologi rusak, yang lain tidak serta merta mengalami nasib yang sama. ring signature adalah link terlemah dalam skema privasi; kata lemah di sini berarti paling rentan terhadap serangan heuristik. Mari luangkan waktu untuk menjelajahinya, oke?

Seperti disebutkan di atas, tujuan ring signature adalah untuk mengaburkan output yang digunakan dalam transaksi. Jika terminologi 'input/output' mata uang kripto membingungkan Anda, jangan khawatir. Sebenarnya tidak terlalu rumit. Ketika Anda mendengar 'output', pikirkan saja cek. Salah satu dari hal-hal itu, tidak begitu umum lagi, yang digunakan orang untuk membayar. Seperti cek, itu dapat dilambangkan dalam jumlah berapa pun - $10, $32,50, dll - dan dipertukarkan antara pihak yang bertransaksi. Bagi mata uang kripto, output menjalankan fungsi ini.

Ketika seseorang membayar Anda 10 Monero, Anda menerima output 10 XMR. Output ini memiliki nilai (10), dan merupakan apa yang diambil dari dompet pengirim, dengan cara yang sama ketika Anda membayar layanan, tagihan muncul dari dompet fisik Anda dan diberikan kepada pedagang tempat Anda membeli.

Cara output disembunyikan adalah dengan membuat ring (maka dari itu namanya) output umpan. Tapi umpan ini bukanlah output 'palsu'. Mereka adalah output masa lalu yang nyata dari blockchain yang tidak ada hubungannya dengan transaksi saat ini, tetapi bagi pengamat luar, masing-masing output ini mungkin terlihat sama kemungkinannya dengan yang asli. Ukuran set output umpan, ditambah yang asli disebut ringsize, dan saat ini ukuran Monero adalah sebelas. Jadi ada sepuluh output umpan dan satu output nyata.

Mengapa kita tidak meningkatkan jumlah ini menjadi 100 atau bahkan 1000? Semakin banyak semakin baik, bukan? Ya, dari sudut pandang privasi, ya, tapi ada hal lain yang perlu dipertimbangkan. Mari kembali ke contoh fisik untuk melihat apa yang saya maksud. Jika Anda ingin menyembunyikan salah satu uang dolar Anda di antara sepuluh umpan, Anda perlu membawa sekitar sebelas dolar di dompet Anda untuk setiap dolar yang ingin Anda belanjakan. Satu dolar asli, dan sepuluh dolar palsu. Ini sudah menjadi sangat rumit jika Anda ingin menghabiskan bahkan beberapa dolar. Sekarang bayangkan kita meningkatkan jumlah umpan menjadi 1.000. Untuk setiap satu dolar yang ingin Anda belanjakan, Anda perlu membawa sekitar 1.001 dolar. Anda harus membawa tas kerja hanya untuk membeli satu batang permen! Penting untuk dicatat bahwa ring signature tidak berfungsi seperti ini, misalnya, umpan itu sendiri bukan bagian dari signature, hanya merujuk ke mereka, tetapi kami berharap analogi ini dapat membantu dalam menggambarkan konsep dasar.< /p>

Umpan pada blockchain bekerja dengan cara yang sama. Setiap umpan tambahan meningkatkan waktu dan biaya verifikasi transaksi. Setiap node harus mengunduh seluruh ring signature untuk setiap transaksi, dan setiap ring signature berisi output nyata, serta umpan. Tidak hanya itu, tetapi juga harus memverifikasi matematikanya bahwa setidaknya satu dari output ini nyata, dan waktu verifikasi matematika juga meningkat dengan setiap umpan. Ini berarti kita harus menemukan jalan tengah yang menyenangkan, di mana ringsize cukup besar untuk mengaburkan hasil nyata secara memadai, bahkan terhadap banyak serangan heuristik, tetapi cukup kecil agar tidak menyebabkan blockchain meningkat secara masif. Tidaklah cukup hanya memilih nomor acak, atau hanya menambah ringsize saat kita membuat tanda tangan lebih kecil (seperti dengan CLSAG). Komunitas Monero menginginkan bukti matematis yang konkret di mana ringsize menawarkan pertukaran terbaik. Angka yang terlalu kecil, dan privasi tidak akan cukup kuat terhadap serangan heuristik. Terlalu besar, dan kami mungkin hanya mendapatkan keuntungan kecil di sisi privasi, dan penderitaan yang tidak perlu dalam hal penskalaan.

Satu hal terakhir yang perlu disebutkan. Beberapa literatur Monero menyederhanakan dan mengatakan bahwa ring signature menyembunyikan pengirimnya, tetapi ini tidak sepenuhnya benar, dan perbedaannya bukan hanya bertele-tele. Perbedaan antara pengirim (manusia) dan output (tagihan) sangat besar dalam hal menjaga privasi. Sementara output mungkin memiliki ikatan dengan pengirim, output itu sendiri tidak sama dengan pengirim. Jadi, meskipun ring signature akan rusak, itu belum tentu terkait dengan identitas seseorang, dan baik jumlah maupun penerima masih disembunyikan, meminimalkan kerusakan yang terjadi pada privasi semua pihak.

Bukan berarti ring signature yang rusak itu tidak penting. Metadata apa pun yang bocor itu buruk, dan berpotensi mengungkapkan lebih banyak informasi daripada yang kami pikirkan, terutama jika digunakan bersama dengan metadata lain. Jadi, kami melakukan yang terbaik untuk memastikan bahwa ringsize yang dipilih memiliki ketelitian akademis di balik keputusan tersebut, kebocoran metadata lainnya diminimalkan, dan pengguna mengalami default untuk tindakan terbaik yang mungkin.

Namun jika kemungkinan rusaknya signature masih membuat Anda khawatir, ada beberapa berita luar biasa yang akan segera hadir. Protokol privasi generasi berikutnya yang sedang dikerjakan, seperti Triptych, Arcturus, dan Lelantus, memiliki kemampuan yang sangat rapi. Dalam protokol ini, skala ukuran secara logaritmis, bukan linier, seiring dengan peningkatan ringize. Artinya, kami dapat memuat 100 umpan, tetapi ruang yang digunakan mendekati ringsize 10 di teknologi lama. Itulah perbedaannya, dan akan meningkatkan privasi secara signifikan.

Dalam permainan kucing dan tikus yang mengutamakan privasi, Monero terus berinovasi untuk tetap menjadi yang terdepan dan memastikan privasi praktis terbaik untuk semua.

Umpan pada blockchain bekerja dengan cara yang sama. Setiap umpan tambahan meningkatkan waktu dan biaya verifikasi transaksi. Setiap node harus mengunduh seluruh ring signature untuk setiap transaksi, dan setiap ring signature berisi output nyata, serta umpan. Tidak hanya itu, tetapi juga harus memverifikasi matematikanya bahwa setidaknya satu dari output ini nyata, dan waktu verifikasi matematika juga meningkat dengan setiap umpan. Ini berarti kita harus menemukan jalan tengah yang menyenangkan, di mana ringsize cukup besar untuk mengaburkan hasil nyata secara memadai, bahkan terhadap banyak serangan heuristik, tetapi cukup kecil agar tidak menyebabkan blockchain meningkat secara masif. Tidaklah cukup hanya memilih nomor acak, atau hanya menambah ringsize saat kita membuat tanda tangan lebih kecil (seperti dengan CLSAG). Komunitas Monero menginginkan bukti matematis yang konkret di mana ringsize menawarkan pertukaran terbaik. Angka yang terlalu kecil, dan privasi tidak akan cukup kuat terhadap serangan heuristik. Terlalu besar, dan kami mungkin hanya mendapatkan keuntungan kecil di sisi privasi, dan penderitaan yang tidak perlu dalam hal penskalaan.

Satu hal terakhir yang perlu disebutkan. Beberapa literatur Monero menyederhanakan dan mengatakan bahwa ring signature menyembunyikan pengirimnya, tetapi ini tidak sepenuhnya benar, dan perbedaannya bukan hanya bertele-tele. Perbedaan antara pengirim (manusia) dan output (tagihan) sangat besar dalam hal menjaga privasi. Sementara output mungkin memiliki ikatan dengan pengirim, output itu sendiri tidak sama dengan pengirim. Jadi, meskipun ring signature akan rusak, itu belum tentu terkait dengan identitas seseorang, dan baik jumlah maupun penerima masih disembunyikan, meminimalkan kerusakan yang terjadi pada privasi semua pihak.

Bukan berarti ring signature yang rusak itu tidak penting. Metadata apa pun yang bocor itu buruk, dan berpotensi mengungkapkan lebih banyak informasi daripada yang kami pikirkan, terutama jika digunakan bersama dengan metadata lain. Jadi, kami melakukan yang terbaik untuk memastikan bahwa ringsize yang dipilih memiliki ketelitian akademis di balik keputusan tersebut, kebocoran metadata lainnya diminimalkan, dan pengguna mengalami default untuk tindakan terbaik yang mungkin.

Namun jika kemungkinan rusaknya signature masih membuat Anda khawatir, ada beberapa berita luar biasa yang akan segera hadir. Protokol privasi generasi berikutnya yang sedang dikerjakan, seperti Triptych, Arcturus, dan Lelantus, memiliki kemampuan yang sangat rapi. Dalam protokol ini, skala ukuran secara logaritmis, bukan linier, seiring dengan peningkatan ringize. Artinya, kami dapat memuat 100 umpan, tetapi ruang yang digunakan mendekati ringsize 10 di teknologi lama. Itulah perbedaannya, dan akan meningkatkan privasi secara signifikan.

Dalam permainan kucing dan tikus yang mengutamakan privasi, Monero terus berinovasi untuk tetap menjadi yang terdepan dan memastikan privasi praktis terbaik untuk semua.

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