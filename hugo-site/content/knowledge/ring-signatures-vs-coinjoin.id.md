---
title: "Ring signature Monero vs CoinJoin seperti di Wasabi"
slug: "ring-signatures-vs-coinjoin"
date: "2022-03-22"
image: "/images/coinjoin.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Karena alat privasi Bitcoin telah mendapatkan lebih banyak perhatian dan penggunaan, mereka berada di bawah pengawasan peraturan yang lebih ketat. Pengawasan ini telah menyebabkan [pengumuman baru-baru ini](https://twitter.com/wasabiwallet/status/1503091503207432193) oleh alat privasi Bitcoin, Dompet Wasabi, bahwa mereka akan mulai menyensor dan menolak input yang masuk ke dalam campuran yang mereka anggap terlarang atau bertentangan dengan ToS mereka, dan akan membayar perusaahn analisis blockchain untuk "memeriksa" peserta campuran yang masuk.

Penggunaan transaksi CoinJoin untuk mengaburkan sumber dana dalam Bitcoin telah menjadi inti dari privasi Bitcoin selama bertahun-tahun sekarang, dan masalah serta risiko yang melekat dalam penggunaannya adalah beberapa masalah inti yang diperbaiki dan dicegah oleh ring signature Monero .

Dalam posting blog ini kami akan secara singkat membahas perbandingan CoinJoin dan ring signature, serta mengapa pendekatan yang diambil di Monero mengarah pada ketahanan sensor yang lebih besar, privasi yang lebih besar, dan lebih sedikit kerumitan bagi pengguna. 

## Apa itu transaksi CoinJoin?

## Apa itu transaksi CoinJoin?

Karena semua transaksi benar-benar transparan dalam Bitcoin - mengungkapkan pengirim, penerima, dan jumlah - pengguna harus mengambil langkah ekstra untuk menjaga privasi mereka dari pengirim sebelumnya dan penerima dana mereka di masa mendatang atau merisikokan penyensoran, pengawasan, atau pencurian dana melalui kekerasan fisik.

Solusi terbaik saat ini untuk privasi pada Bitcoin adalah alat yang disebut [“CoinJoin”](https://bitcoiner.guide/qna/coinjoin/), di mana 2 atau lebih pengguna bekerja sama (biasanya melalui koordinator terpusat) untuk membuat transaksi khusus yang menyulitkan observer dari luar untuk menghubungkan input dengan output. Setiap partisipan berkomunikasi untuk bersama-sama membangun transaksi tanpa menyerahkan penahanan atas dana mereka, dan menerima luaran pada akhirnya yang sejarah sebelumnya sekarang jadi tidak jelas (atau dikaburkan) bagi pengamat dari luar.

Ini memecahkan sejarah UTXO tertentu, memungkinkan pengguna Bitcoin untuk mendapatkan sedikit dari forward-secrecy saat bertransaksi. Namun, CoinJoin (seperti yang diterapkan di Dompet Wasabi dan Dompet Samourai, dua alat CoinJoin yang paling banyak digunakan untuk Bitcoin) memiliki beberapa kelemahan besar:

  * Karena transaksi CoinJoin sepenuhnya ikut serta dan memerlukan partisipasi aktif, setiap peserta harus menunjukkan bahwa mereka mencari privasi yang lebih besar daripada pengguna Bitcoin "normal", yang berpotensi memilih mereka dan menyebabkan masalah pengeluaran dana di banyak exchange atau entitas yang diatur. Setiap pengguna tidak dapat menyangkal bahwa mereka berpartisipasi dalam transaksi CoinJoin.
  * Untuk menemukan orang lain yang dapat CoinJoin dengan kita, sebagian besar pendekatan ke CoinJoin (termasuk Dompet Wasabi) menggunakan koordinator tersentralisasi yang menghubungkan peserta dan membantu mereka berkomunikasi dan membangun transaksi CoinJoin yang baik. Koordinator tersentralisasi ini tidak pernah menahan dana pengguna, tetapi memang mendapatkan wawasan luas tentang transaksi yang mereka koordinasikan, dapat menyensor input yang masuk (seperti dalam kasus Dompet Wasabi), dan dapat ditekan untuk mengumpulkan atau berbagi informasi tentang partisipan CoinJoin. 
  * Pengguna dengan jumlah dana yang besar untuk CoinJoin dapat seringkali harus menunggu berjam-jam (atau bahkan berhari-hari!) untuk menemukan cukup banyak peserta untuk CoinJoin dengan mereka, yang menyebabkan penundaan besar sejak pengguna menerima dana hingga saat mereka dapat membelanjakannya secara pribadi. 
  * Privasi yang disediakan oleh transaksi CoinJoin menurun dari waktu ke waktu karena peserta lain membelanjakan dana atau menautkan output mereka ke identitas mereka melalui pertukaran KYC, pedagang yang membutuhkan ID, dll. Hal ini berarti pengguna idealnya menjaga dana mereka agar tetap berputar di transaksi CoinJoin untuk menjaga set anonimitas mereka (“kerumunan untuk bersembunyi”) sesegar mungkin.
  * Di sebagian besar pendekatan CoinJoin, peserta harus menggunakan UTXO dalam ukuran tetap (yaitu 0,1 BTC) untuk mempersulit koneksi input dan output transaksi CoinJoin. Hal ini menyebabkan biaya yang lebih tinggi (lebih banyak transaksi terpisah diperlukan untuk setiap input besar), lebih banyak “perubahan beracun” (dana yang tidak dapat digunakan tanpa risiko serius terhadap privasi), dan dapat menghalangi pengguna yang lebih kecil untuk dapat berbaur sama sekali jika mereka tidak memiliki saldo minimum yang diperlukan.

## Bagaimana ring signature memecahkan masalah ini?

## Bagaimana ring signature memecahkan masalah ini?

Karena [ kita telah melihat secara mendalam apa itu ring signature di masa lalu ](/knowledge/ring-signatures), saya tidak akan menjelaskan secara mendetail tentang aspek teknis tentang cara kerjanya di entri blog ini. Sebagai gantinya, kita akan melihat bagaimana pendekatan yang diambil di Monero menyelesaikan masalah tentang CoinJoin yang dibahas di atas.

> CoinJoin itu opt-in dan memerlukan partisipasi

CoinJoin itu opt-in dan memerlukan partisipasi

Ring signature Monero adalah fitur inti dari protokol privasi, dan _setiap_ transaksi di jaringan menggunakannya. Ini berarti bahwa tidak ada transaksi pengguna yang menonjol untuk mencari privasi yang lebih besar daripada pengguna Monero "normal", dan semua pengguna mendapatkan penyangkalan yang masuk akal bahwa mereka membelanjakan dana dalam setiap transaksi tertentu. Karena dana pembelanjaan pengguna tidak berkoordinasi atau berpartisipasi dengan input umpan dalam suatu transaksi, para pengguna tersebut yang memiliki input dan kebetulan terpilih sebagai umpan dapat dengan jujur mengatakan bahwa mereka tidak berpartisipasi dalam transaksi itu, memperkuat privasi mereka.

> Penggunaan koordinator tersentralisasi

Penggunaan koordinator tersentralisasi

Karena ring signature Monero sepenuhnya tidak terkoordinasi dan hanya membutuhkan pembelanja dana yang sebenarnya untuk membuat transaksi, tidak diperlukan koordinator terpusat di Monero. Hal ini memastikan bahwa _tidak seorang pun_ dapat menolak Anda mengakses privasi di Monero, dan tidak ada entitas terpusat yang dapat ditekan, tidak ada serangan Sybil yang mudah terhadap likuiditas, dll. Selama transaksi Anda membayar biaya yang sesuai, Anda mendapatkan akses tanpa sensor ke privasi, keamanan, dan anonimitas di Monero.

> CoinJoin membutuhkan likuiditas

CoinJoin membutuhkan likuiditas

"Likuiditas" yang tersedia bagi siapa saja yang membelanjakan Monero untuk digunakan sebagai umpan selalu merupakan rangkaian total output on-chain sehingga tidak akan pernah ada kekurangan umpan untuk bersembunyi dengan Monero. Seseorang yang ingin membelanjakan Monero dapat melakukannya ~20 menit setelah menerima dana, dan tidak perlu melakukan langkah tambahan apa pun untuk mendapatkan privasi yang kuat di Monero.

> Privasi CoinJoin menurun seiring waktu

Privasi CoinJoin menurun seiring waktu

Karena luaran Monero tidak pernah known-spent oleh jaringan, privasi yang diberikan oleh ring signature jauh lebih rentan terhadap degradasi dari waktu ke waktu. Seorang pengguna tidak perlu terus-menerus memutar output di Monero, dan di luar keadaan yang sangat jarang terjadi, tidak akan kehilangan privasi seiring berjalannya waktu.

Namun, jika pengguna memang ingin "menyegarkan" umpan yang digunakan dengan output, mereka cukup mengirim kembali dana tersebut ke diri mereka sendiri dan dapat membelanjakannya ~20 menit kemudian seperti biasa.

> CoinJoin biasanya membutuhkan input berukuran tetap

CoinJoin biasanya membutuhkan input berukuran tetap

Karena jumlah disembunyikan dalam setiap transaksi menggunakan [“Transaksi Rahasia”](/knowledge/monero-ringct) (bagian dari “RingCT”), umpan yang digunakan dalam transaksi apa pun dapat berukuran berapa pun. Tidak ada alasan untuk khawatir tentang heuristik berbasis jumlah di Monero, sehingga transaksi jauh lebih mudah dibuat dan dapat memanfaatkan umpan dari titik waktu mana pun dan dalam jumlah berapa pun di blockchain Monero.

## Bagaimana saya bisa belajar lebih banyak?

## Bagaimana saya bisa belajar lebih banyak?

Jika Anda penasaran dan ingin lebih memahami ring signature atau transaksi CoinJoin, lihat tautan di bawah untuk mendapatkan tempat yang bagus dalam memulai:

  * [Bagaimana Ring Signature Mengaburkan Luaran Monero](/knowledge/ring-signatures)
  * [Ring Signature - Moneropedia](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
  * [Coinjoin Q+A](https://bitcoiner.guide/qna/coinjoin/)
  * [Uraian Singkat CoinJoin](https://6102bitcoin.com/coinjoin-overview/)

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies)/

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

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better)/

Bacaan lebih lanjut