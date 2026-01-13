---
title: "P2Pool dan Perannya dalam Desentralisasi Penambangan Monero"
slug: "p2pool-decentralizing-monero-mining"
date: "2022-01-27"
image: "/images/p2pool.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Salah satu tujuan inti dalam proyek Monero adalah untuk mengaktifkan jaringan yang adil, terdesentralisasi, dan aman melalui pendekatan baru dan inovatif untuk penambangan proof-of-work (PoW), cara utama mengamankan jaringan cryptocurrency saat ini.

Meskipun algoritme penambangan unik [ seperti RandomX ](/knowledge/monero-mining-randomx) sangat penting untuk tujuan ini karena membantu memastikan bahwa siapa pun yang memiliki komputer dapat berkontribusi cukup banyak untuk keamanan jaringan, RandomX tidak menyelesaikan masalah yang dapat terjadi akibat pool mining. Pool Mining sejauh ini merupakan cara paling umum untuk menambang mata uang kripto saat ini, termasuk Monero, tetapi untungnya munculnya penambangan p2pool dengan cepat mengubah hal itu.

## Apa itu pool mining?

## Apa itu pool mining?

Pool mining adalah cara bagi penambang untuk berbagi tugas mencoba memecahkan blok di jaringan dan kemudian membagikan hadiah secara merata untuk semua blok yang ditemukan oleh pool. Meskipun hal ini sangat membantu untuk meratakan frekuensi dengan yang mana penambang dibayar versus menambang Monero saja, ini bukannya tanpa masalah sentralisasi yang serius.

Karena setiap penambang menyumbangkan pekerjaan ke pool, mereka menyerahkan kendali atas pekerjaan apa pun yang mereka lakukan dan blok-blok yang mereka temukan ke pool itu sendiri, mempercayai bahwa kumpulan akan membagikan hadiah secara jujur dan adil di antara semua penambang berdasarkan jumlah pekerjaan yang telah dilakukan masing-masing. Jika semuanya berjalan lancar, operator pool mengumpulkan pekerjaan dari semua penambang, mengirimkannya ke jaringan, dan membagikan hadiahnya secara merata.

## Ada masalah apa dengan pool mining?

## Ada masalah apa dengan pool mining?

Sayangnya, ini bergantung sepenuhnya pada kepercayaan dan memungkinkan operator pool untuk melakukan hal-hal jahat dengan pekerjaan yang dilakukan oleh penambang. Operator pool dapat menggunakan pekerjaan yang dilakukan untuk menyerang jaringan, mencoba membelanjakan dana dua kali lipat (jika kumpulan cukup besar), atau hanya menggunakan pekerjaan yang dilakukan oleh penambang untuk membayar diri mereka sendiri dan tidak pernah menghadiahi penambang dengan layak untuk pekerjaan mereka. .

Risiko terbesar untuk jaringan adalah jika pool (atau beberapa pool yang bekerja bersama) memiliki lebih dari 51% hashrate jaringan di bawah kendali mereka, karena mereka dapat menggunakan ini untuk menipu dan membelanjakan dana dua kali (serangan pengeluaran ganda) atau mencoba mengubah aturan jaringan.

## Apa itu p2pool?

## Apa itu p2pool?

p2pool adalah konsep yang awalnya dibuat untuk menambang Bitcoin pada tahun 2011, tetapi tidak pernah mendapatkan adopsi yang luas dan praktis tidak digunakan pada Bitcoin. Syukurlah, salah satu pengembang utama di balik RandomX, SChernykh, menghabiskan liburannya dengan mencari solusi untuk beberapa masalah implementasi Bitcoin dari p2pool dan menulis ulang semua perangkat lunak dari awal.

p2pool di Monero memungkinkan cara yang benar-benar tanpa kepercayaan bagi penambang untuk bekerja sama memecahkan blok dan mengamankan jaringan Monero dengan menggunakan perangkat lunak node khusus untuk p2pool agar dapat berbagi pekerjaan.

Ini dilakukan dengan menggunakan blockchain baru (sebuah "side chain") yang mencatat pekerjaan yang dilakukan setiap penambang, alamat dompet mereka, dan berapa banyak Monero yang telah mereka hasilkan, dan kemudian membayar hadiahnya dengan cara yang tanpa kepercayaan dan terdesentralisasi. Karena side chain ini memiliki penambang yang jauh lebih sedikit, jauh lebih mudah untuk menemukan dan mengirimkan blok di dalamnya daripada di jaringan utama Monero, sehingga lebih mudah bagi penambang untuk mendapatkan pembayaran yang konsisten dibandingkan menambang Monero saja.

## Bagaimana p2pool memecahkan masalah pool mining?

## Bagaimana p2pool memecahkan masalah pool mining?

Di p2pool, tidak ada pool tersentralisasi, operator pool tersentralisasi, atau satu orang yang memegang dana dan mendistribusikan pembayaran. Semua pekerjaan yang dilakukan secara kolektif oleh penambangan tersebut melalui p2pool diperiksa oleh blockchain p2pool dan operator node lainnya untuk memastikan bahwa itu legal, dan semua penambang dibayar sesuai dengan pekerjaan yang telah mereka lakukan segera ketika sebuah blok ditemukan langsung dari hadiah di blok yang ditemukan itu.

Ketika penambang memilih untuk menggunakan p2pool daripada pool tersentralisasi, mereka menghapus semua kekuatan dan kepercayaan dari operator pool dan memastikan bahwa pekerjaan mereka berkontribusi pada kebaikan jaringan dan imbalan mereka sendiri, mengurangi risiko serangan jaringan, penyalahgunaan pekerjaan mereka, atau pencurian imbalan yang menjadi hak mereka.

Hal ini tidak hanya membantu mereka melindungi kepentingan mereka sendiri, tetapi juga mengurangi risiko yang dapat ditimbulkan oleh kumpulan terpusat ke jaringan Monero secara keseluruhan. penggunaan p2pool juga sangat membantu untuk mengurangi risiko yang dapat ditimbulkan oleh negara-bangsa atau regulator terhadap kesehatan jaringan, karena tidak ada tekanan dari operator pool tersentralisasi, tidak ada konsentrasi geografis dari pool untuk bersandar, atau titik tekanan mudah lainnya untuk mereka gunakan melawan Monero.

## Apa kekurangannya?

## Apa kekurangannya?

Untungnya p2pool di Monero telah dirancang dan dibangun dengan baik, dan berfungsi dengan sangat baik! Namun, kelemahan utama penambangan p2pool adalah bahwa setiap penambang yang ingin menggunakan p2pool harus menjalankan node Monero mereka sendiri, menyebabkan proses memulai menjadi sedikit lebih rumit. Namun, node ini kemudian digunakan untuk menghitung semua informasi yang diperlukan untuk membangun dan memeriksa blok, dan memastikan bahwa penambang memiliki kendali penuh atas pekerjaan mereka. Node juga dapat berfungsi sebagai node jarak jauh untuk dompet milik penambang, berkontribusi pada jaringan, dan banyak lagi. 

Perbedaan utama lainnya dari penambangan terpusat adalah bahwa penambang kecil yang menggunakan p2pool akan memiliki sedikit lebih banyak "varians", atau jeda waktu pembayaran, daripada pool terpusat yang besar -- tetapi ' adalah _sangat_ penting untuk dicatat bahwa ini tidak akan menyebabkan penghasilan Monero berkurang dari waktu ke waktu! p2pool akan sama menguntungkannya bahkan untuk penambang kecil dari waktu ke waktu seperti pool terpusat. Beberapa varian ini juga diimbangi oleh p2pool yang secara alami memiliki biaya 0%, karena tidak ada operator pool terpusat yang dibayar untuk layanan mereka!

## Bagaimana saya bisa memulai?

## Bagaimana saya bisa memulai?

Untungnya, karena desain implementasi p2pool Monero ' yang luar biasa dan banyak orang di komunitas yang telah meluangkan waktu untuk membantu menyederhanakan proses penambangan melalui p2pool, memulai menjadi semakin sederhana dari waktu ke waktu. Ada beberapa cara untuk memulai menambang dengan p2pool, tetapi karena detail teknisnya berada di luar cakupan artikel ini, silakan lompat ke tautan di bawah tergantung pada sistem operasi Anda:

  * [Windows](https://www.youtube.com/watch?v=yfbvTksF9ic)
  * [Linux](https://sethforprivacy.com/guides/run-a-p2pool-node/)

## Bagaimana saya bisa belajar lebih banyak?

## Bagaimana saya bisa belajar lebih banyak?

Jika hal ini memancing rasa ingin tahu Anda seputar penambangan p2pool, lihat beberapa tautan dan penjelasan tambahan di bawah tentang p2pool, cara kerjanya, dan apa artinya bagi Monero:

  * [Github resmi untuk p2pool](https://github.com/SChernykh/p2pool)
  * [Dokumen resmi tentang penggunaan p2pool](https://github.com/SChernykh/p2pool#how-to-mine-on-p2pool)
  * [Monero P2Pool sekarang aktif](https://www.getmonero.org/2021/10/05/p2pool-released.html)
  * [p2pool.observer, semacam "block explorer" untuk p2pool](https://p2pool.observer/)
  * [Monero p2pool docker-compose](https://github.com/WeebDataHoarder/p2pool-compose)
  * [Sergei Chernykh: Tentang pengembangan P2Poolnya, Kumpulan Penambangan XMR Terdesentralisasi](https://www.monerotalk.live/sergei-chernykh-on-his-development-of-p2pool-a-decentralized-xmr-mining-pool)

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies)/

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys)/

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero)/

  * [Bagaimana node jarak jauh memengaruhi privasi Monero](/knowledge/remote-nodes-privacy)/

  * [Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan](/knowledge/network-upgrades)/

  * [Lihat tag: Bagaimana satu byte akan mengurangi waktu sinkronisasi dompet Monero hingga 40%+](/knowledge/view-tags-reduce-monero-sync-time)/

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

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better)/

Bacaan lebih lanjut