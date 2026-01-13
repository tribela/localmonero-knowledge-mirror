---
title: "Bagaimana RingCT Menyembunyikan Jumlah Transaksi Monero"
slug: "monero-ringct"
date: "2020-10-28"
image: "/images/ringct.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Privasi Monero tidak bergantung pada satu mekanisme tunggal yang, jika rusak, akan mengungkapkan keseluruhan transaksi, melainkan tiga teknologi berbeda yang bekerja bersama-sama untuk memberikan privasi holistik sambil mengkompensasi kelemahan bagian lainnya. Pendekatan tiga cabang ini terdiri dari [ring signatures](/knowledge/ring-signatures), RingCT, dan [alamat rahasia](/knowledge/monero-stealth-addresses). Ketiga teknologi ini masing-masing menyembunyikan output asli (pengirim), jumlah, dan penerima. Hari ini kita akan membahas tentang RingCT.

RingCT bisa dibilang merupakan yang paling teknis di antara ketiganya, dan mungkin sulit untuk dipahami, jadi kami tidak akan membahas cara kerja tepatnya, melainkan menunjukkan bagaimana mungkin untuk tidak mengetahui jumlah dan masih mengonfirmasi hal-hal tentang itu . Dan jangan khawatir, kami akan menggunakan banyak contoh seperti biasa.

Pertama, mari kita jelajahi mengapa penting untuk memverifikasi apa pun tentang jumlah. Mengapa kita tidak bisa merahasiakannya saja? Jawabannya adalah, ada cara cerdas agar orang dapat menghasilkan uang dari tangan kosong jika diberi kesempatan. Bagaimana hal seperti ini bisa berhasil? Mari kita lihat sebuah contoh.

Jika Anda ingin membeli barang dari teman Anda, dan dia menginginkan sepuluh dolar untuk itu, maka Anda mulai dengan sepuluh dolar dan dia mulai dengan nol. Setelah Anda memberinya sepuluh dolar, dia memiliki sepuluh dolar dan Anda memiliki nol. Anda mulai dengan sepuluh, dan sekarang dia punya sepuluh. Tidak ada uang yang diciptakan atau dimusnahkan dalam transaksi ini.

Dengan mata uang kripto, individu yang cerdas dapat memberikan sepuluh dolar untuk item tersebut dan alih-alih menerima kembalian nol dolar, mereka dapat menerima kembali dua dolar. Alih-alih 0 dan 10 mengarah ke 10 dan 0 (atau 10=10), sekarang 0 dan 10 mengarah ke 10 dan 2 (atau 10=12). Dua Monero baru saja dibuat dari tangan kosong. Anda dapat membayangkan bahwa jika orang tersebut melakukan ini pada diri mereka sendiri beberapa kali, mereka akan dapat mengumpulkan kekayaan yang sangat besar dalam waktu singkat.

Dengan Bitcoin dan lainnya, ini akan mudah dilihat. Anda melihat input yang masuk ke dalam transaksi dan output yang keluar dan memastikan bahwa apa yang dikirim sama dengan apa yang diterima. Jika jumlah ini dienkripsi dan tidak terlihat maka pengguna tidak memiliki cara untuk memverifikasi bahwa apa yang dikirim dan apa yang diterima adalah sama.

Dalam upaya untuk meningkatkan privasi Bitcoin, Gregory Maxwell menciptakan Confidential Transactions (CT), sebuah teknologi baru yang memungkinkan jumlah terenkripsi, sambil membuktikan bahwa tidak ada yang dibuat atau dihancurkan dalam proses tersebut. Seperti kebanyakan teknologi privasi, itu tidak membuatnya menjadi Bitcoin, tetapi Monero tertarik untuk mengadopsinya. Hanya ada satu masalah. Teknologi ring signature yang sudah diterapkan tidak sesuai dengan ide yang diusulkan. Jadi, salah satu peneliti MRL saat itu, Shen Noether, memodifikasi CT menjadi RingCT, versi CT yang kompatibel dengan ring signature.

Sekali lagi, cara kerjanya cukup teknis, dan akan sulit dijelaskan dalam artikel pengantar. Untuk penggemar kriptografi yang harus tahu, ada banyak artikel mendalam yang ditulis di internet tentang cara kerja CT. Bagi kita semua, artikel ini akan menunjukkan bagaimana mungkin untuk menyembunyikan jumlahnya, tetapi tetap membuktikan bahwa tidak ada yang diciptakan atau dimusnahkan.

Misalkan Alice ingin mengirim uang kepada Bob. Alice akan mengirimkan 10 XMR ke Bob, yang akan menerima 10 XMR. 10=10 jadi tidak ada yang salah disini. Tapi Alice tidak ingin ada yang tahu berapa banyak yang dia kirimkan. Jadi dia dan Bob membuat rahasia bersama. Pada dasarnya angka yang hanya diketahui oleh mereka berdua. Katakanlah angka itu adalah 22. Sekarang, Alice mengalikan 10 (apa yang sebenarnya dia kirim) dengan 22 untuk mendapatkan 220. Ini adalah angka yang dia bagikan dengan jaringan.

Para penambang sendiri tidak mengetahui nomor rahasianya. Jika ya, mereka dapat membagi nomor yang ditunjukkan dengan nomor rahasia dan mendapatkan jumlah sebenarnya yang dikirim. Tetapi karena tidak, mereka tidak bisa. Mereka memang melihat bahwa Bob akan menerima 220. 220 dikirim. 220 diterima. 220 = 220. Dengan cara ini, jaringan dapat memverifikasi bahwa tidak ada Monero yang dibuat atau dihancurkan, semuanya tanpa mengetahui jumlah sebenarnya yang dikirimkan Alice kepada Bob.

Karena Bob mengetahui nomor rahasia bersama, ketika dia menerima uang, dia hanya harus membaginya dengan 22 untuk mendapatkan jumlah sebenarnya yang dikirim Alice, 10. Alice dan Bob sama-sama tahu berapa banyak yang dikirim dan berapa banyak yang diterima, sementara itu semua orang diberi nomor palsu.

Sekali lagi, ini bukan cara kerja CT yang sebenarnya, tetapi ini memberi gambaran tentang bagaimana hal seperti ini mungkin terjadi. Cara sebenarnya melibatkan hal-hal seperti komitmen Pedersen, dua jumlah terkirim (satu jumlah terenkripsi ke penerima dan satu jumlah komitmen ke jaringan), dan… ya, sudah mudah untuk melihat bagaimana seseorang bisa tersesat dalam semua itu.

Namun satu hal yang perlu diperhatikan, adalah bahwa sementara RingCT menyembunyikan jumlah yang ditransaksikan antara dua pihak dalam sebuah transaksi, itu tidak menyembunyikan dua rangkaian angka lainnya.

Yang pertama adalah transaksi coinbase. Jika istilah ini asing bagi Anda, pada dasarnya itu berarti hadiah yang didapat penambang untuk menemukan blok berikutnya. Nomor ini tidak disembunyikan. Siapa pun dapat melihat berapa banyak yang diberikan protokol kepada penambang untuk layanan mereka. Dengan cara ini, jumlah Monero yang ada saat ini dapat diketahui dengan menjumlahkan semua transaksi coinbase. Jumlah mereka akan sama dengan Monero yang beredar saat ini.

Nomor kedua yang tidak disembunyikan adalah biaya yang dibayarkan kepada penambang saat pengguna mengirimkan transaksi. Biaya harus jelas sehingga penambang dapat mengetahui siapa yang harus diprioritaskan. Ini adalah cara pengguna dapat merusak privasi mereka, seolah-olah seseorang menggunakan biaya penambang unik setiap kali mereka mengirim transaksi (seperti 0,12345), maka transaksi mereka dapat ditautkan.

Selain kasus-kasus ini, RingCT telah menyembunyikan jumlah Monero sejak 2017, dan privasi kolektif kami menjadi lebih kuat karenanya.

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