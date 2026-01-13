---
title: "Penambangan Monero: Apa yang Membuat RandomX begitu Istimewa"
slug: "monero-mining-randomx"
date: "2020-02-20"
image: "/images/mining.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Pada tanggal 30 November 2019, Monero mengadakan hard fork semi tahunan, dengan perubahan yang paling diantisipasi adalah peralihan dari algoritma PoW lama, cryptonight, ke yang benar-benar baru, yang dikembangkan secara internal, RandomX. Komunitas Monero percaya bahwa RandomX adalah langkah besar menuju penambangan egaliter, tetapi mari kita gali lebih dalam untuk melihat apakah memang demikian.

## Maksud

Untuk menilai apakah RandomX merupakan sebuah peningkatan, pertama-tama kita harus memahami apa tujuan penambangan itu. Penambangan mengamankan blockchain dari pengeluaran ganda melalui Konsensus Nakamoto. Kerumitan yang tepat tentang cara ia melakukannya berada di luar cakupan artikel ini, tetapi hal tersebut dapat dipelajari dari berbagai sumber di internet. Yang terpenting adalah keamanan berasal dari hash-hash yang dihasilkan oleh komputer (penambang), bersaing satu sama lain untuk menemukan solusi matematis yang diperlukan untuk membuat blok lain. Saat mereka melakukan ini, mereka menambahkan transaksi baru ke blockchain. Sebagai imbalan atas pekerjaan mereka (hash), mereka diberi kompensasi dengan koin yang baru dicetak.   
  
Ada sejumlah masalah yang dapat terjadi dengan setup ini, dan hal mereka memerlukan insentif yang tepat agar bekerja dengan benar, tetapi kami akan berfokus pada satu masalah tertentu yang mungkin muncul. Jika penambangan seharusnya menjadi kompetisi, apa yang terjadi jika satu penambang mendapat keunggulan?

## Latar belakang

Untuk konteksnya, mari kita bicara sedikit tentang perangkat keras penambangan. Penambang menggunakan komputer untuk melakukan pekerjaan, tetapi kita semua tahu bahwa tidak semua komputer dibuat sama. Beberapa komputer cukup kuat untuk menjalankan jaringan AI atau game yang intens, sementara yang lain kesulitan bahkan dengan tugas-tugas sederhana. Perbedaan daya komputasi ini juga memengaruhi tingkat hash, atau tingkat pencarian solusi blok.   
  
Tetapi bahkan perbedaan antara komputer ini tidak ada apa-apanya jika dibandingkan dengan tingkat hash dari perangkat keras khusus, atau dikenal sebagai Application Specific Integrated Circuits (ASICs), yang mengungguli komputer biasa sebanyak beberapa tingkatan.  
  
Mari luangkan sedikit waktu untuk mengeksplorasi apa yang membuat ASIC begitu kuat. Bayangkan semua komputer berada di suatu tempat dalam spektrum, yang berkisar dari mampu melakukan banyak hal, tetapi tidak melakukan apa pun dengan baik, hingga hanya melakukan satu hal, tetapi melakukannya dengan sangat baik. CPU dan ASIC berada di ujung yang berlawanan dari spektrum ini.   
  
CPU yang ada di semua komputer standar ada di ujung pertama. Mereka dapat melakukan banyak hal, seperti menelusuri web, bermain game, atau merender video, tetapi tidak melakukannya dengan baik. Namun fleksibilitas ini mengorbankan efisiensi.  
  
ASIC ada di ujung lain, di mana mereka hanya bisa melakukan satu hal, tetapi melakukannya dengan kecepatan yang luar biasa. Mereka hanya dapat melakukan satu fungsi matematika, tetapi karena mereka dapat mengabaikan yang lainnya, perolehan kinerjanya sangat besar. Namun, efisiensi ini mengorbankan fleksibilitas, jadi jika fungsinya berubah sedikit saja – contohnya adalah x + y = z berubah menjadi 2x + y = z – maka ASIC akan berhenti berfungsi sama sekali.   
  
Tidak semua orang memiliki ASIC, tetapi semua orang memiliki komputer. Ini dapat menyebabkan keunggulan yang tidak adil.

## Sebuah analogi yang menyenangkan

Jika masih bingung, mungkin analogi berikut bisa membantu. Bayangkan sebuah lotere di mana seribu dolar dihadiahkan setiap jam, dan lotre ini memungkinkan Anda untuk mencetak tiket Anda sendiri! Anda mulai mencetak tiket sebanyak mungkin di printer rumah Anda, yang dapat mencetak satu tiket per detik. Setelah dikurangi biaya listrik dan tinta, Anda melihat bahwa Anda masih bisa mendapat untung, meskipun Anda hanya memenangkan lotere setiap beberapa minggu sekali.  
  
Seiring waktu, Anda memperluas operasi hingga Anda memiliki seluruh ruangan yang didedikasikan untuk printer. 20 seluruhnya. Semuanya baik-baik saja...sampai suatu hari yang ditakdirkan.  
  
Ada berita besar. Seseorang telah menemukan printer jenis baru. printer itu hanya dapat mencetak tiket lotre. Ia tidak dapat mencetak gambar, atau dokumen kantor, atau melakukan pencetakan dua sisi. Hanya tiket lotre. Tapi ia bisa mencetaknya dengan kecepatan 1000 tiket per detik. Anda melihat di ruang printer kecil Anda. 20 printer. Anda memerlukan 980 printer lagi hanya untuk menyamai SATU dari printer raksasa ini, dan jika seseorang memiliki dua…?  
  
Anda dengan sedih keluar dari permainan lotre karena Anda tidak dapat lagi mengatasi biaya listrik dan tinta.  
  
Tapi tunggu! Beberapa minggu kemudian ada lebih banyak berita! Desain tiket telah berubah. Sekarang angka-angka yang dulunya di atas, kini berada di bawah. Printer monster baru sangat tidak fleksibel sehingga mereka tidak dapat melakukannya. Mereka hanya bisa membuat desain sebelumnya. Tidak lama kemudian Anda sekali lagi dengan senang hati mencetak. Setidaknya sampai seseorang membuat printer monster baru untuk desain baru.

## RandomX

Di mana RandomX cocok masuk dalam semua ini? Ia berusaha untuk meratakan keuntungan ASIC dengan membuat ASIC sangat sulit dibuat. Ini dilakukan dengan meminta penambang untuk membuat dan mengeksekusi kode acak sebagai pengganti hashing berdasarkan algoritme.  
  
Mungkin membingungkan bagaimana ini benar-benar membantu apa pun, jadi mari kita kembali ke analogi printer kita. Ingat apa yang terjadi ketika desain berubah? Printer monster lama menjadi usang setiap malam, dan yang baru harus dikembangkan dengan mempertimbangkan desain baru. Apa yang akan terjadi jika setiap tiket hadiah lotre baru, harus mematuhi standar desain baru untuk setiap jackpot baru?   
  
Membuat printer monster baru akan menjadi sangat sulit. Anda tidak bisa hanya merencanakan satu desain tiket lagi. Karena desainnya acak, pembuat printer monster harus menambahkan kapabilitas warna, cara untuk mencetak berbagai huruf dan batas serta bentuk, dan banyak lagi. Singkatnya, mesin yang akhirnya mereka temukan akan menjadi printer standar dan biasa. Sama seperti yang dimiliki orang lain.  
  
Dengan hanya menerapkan keacakan ini dalam desain tiket, kami secara substansial mengurangi keuntungan besar yang diperoleh dari perangkat keras khusus. RandomX melakukan hal yang sama, tetapi dengan menambang.  
  
Dengan cara ini, keuntungan yang diperoleh oleh beberapa orang kaya terpilih dapat diminimalkan, seolah-olah mereka berinvestasi dalam membuat "ASIC" untuk menambang RandomX, mereka sebenarnya hanya akan menciptakan CPU yang lebih kuat dan lebih baik, yang menguntungkan dunia secara luas.  
  
[ X1455X] Ini berarti si kecil dengan 20 pencetak tiketnya kembali bermain. Dia mungkin masih mengalami masa lebih sulit karena orang-orang kaya ini masih dapat membeli lebih banyak printer daripada dia, tetapi setidaknya sekarang dia tidak kalah dalam urutan besar hanya dari satu mesin. Dia kompetitif dalam caranya yang kecil.  
  
Mengetahui bahwa orang kecil sekalipun dapat bersaing dalam menambang Monero, kami mendorong semua orang untuk mencobanya, baik di dompet GUI Monero, yang memiliki dukungan untuk penambangan solo, atau dengan mengunduh perangkat lunak yang dikelola komunitas. Mudah, kompetitif, dan terbuka untuk semua.

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

  * [Mengapa Monero Lebih Baik dari Dash, Zcash, Zcoin (Bahkan dengan Lelantus), Grin dan Bitcoin Mixer Seperti Wasabi (Diperbarui Mei 2020)](/knowledge/why-monero-is-better)/