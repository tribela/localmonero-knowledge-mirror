---
title: "Lihat tag: Bagaimana satu byte akan mengurangi waktu sinkronisasi dompet Monero hingga 40%+"
slug: "view-tags-reduce-monero-sync-time"
date: "2022-02-03"
image: "/images/viewTags.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Salah satu keluhan paling umum seputar penggunaan Monero sehari-hari adalah waktu yang diperlukan untuk menyinkronkan dompet sebelum dapat mengirimkan Monero. Untungnya, pengembang dan peneliti di komunitas Monero telah menemukan cara brilian untuk mengurangi waktu yang Anda perlukan untuk menyinkronkan dompet hingga 40%+ tanpa tambahan penggelembungan blockchain, biaya, dll.

Masukkan "lihat tag", tambahan satu byte untuk data setiap transaksi – hadir di Monero dalam pemutakhiran jaringan berikutnya!

## Mengapa sinkronisasi dompet Monero lebih lambat daripada milik Bitcoin?

## Mengapa sinkronisasi dompet Monero lebih lambat daripada milik Bitcoin?

Salah satu pertanyaan pertama yang harus kami jawab untuk lebih memahami perlunya solusi seperti lihat tag adalah mengapa sinkronisasi dompet Monero lebih lambat daripada mata uang kripto seperti Bitcoin.

Dalam Bitcoin, karena semua transaksi tidak bersifat pribadi dan mengungkapkan koin yang dibelanjakan, jumlah, dan alamat yang terlibat dalam chain, dompet Bitcoin dapat dengan mudah mencari hasil transaksi yang tidak terpakai (UTXO) atau alamat yang digunakan untuk dompet tertentu , dengan cepat memindai blockchain hanya untuk UTXO yang dimiliki oleh alamat tersebut untuk mengetahui koin mana yang menjadi milik dompet Anda dan dapat dibelanjakan.

Namun, di Monero, semua transaksi menjaga privasi pengguna dengan menyembunyikan pengirim, penerima, dan jumlah yang terlibat dalam setiap transaksi. Privasi ini, meskipun penting untuk melindungi pengguna jaringan, juga memperkenalkan sinkronisasi dompet yang lebih lambat. Di Monero, dompet Anda harus membandingkan setiap output transaksi (TXO) yang ada di jaringan dengan kunci pribadi dompet Anda.

Perbandingan ini melibatkan banyak matematika dan kriptografi yang kompleks untuk memvalidasi bahwa suatu output benar-benar milik Anda, karena semua jumlah, alamat, dan output (atau koin) yang diketahui dihabiskan disembunyikan secara on-chain di Monero.

## Apa itu lihat tag?

## Apa itu lihat tag?

Sebagai cara untuk membantu mengurangi waktu sinkronisasi untuk dompet Monero, [ seorang peneliti bernama UkoeHB datang dengan pendekatan baru ](https://github.com/monero-project/research-lab/issues/73) – menambahkan "tag" 1-byte ke setiap transaksi menggunakan rahasia bersama yang hanya diketahui kepada pengirim dan penerima transaksi tersebut.

Rahasia bersama ini dihasilkan oleh pengirim menggunakan alamat yang diberikan oleh penerima kepada mereka, dan tidak memerlukan kolaborasi aktif apa pun dari pengirim dan penerima. Byte (atau karakter) pertama dari rahasia bersama ini kemudian ditambahkan ke data transaksi saat memublikasikannya ke jaringan Monero.

Ketika salah satu peserta dalam transaksi itu ingin menyinkronkan dompet mereka dengan blockchain Monero sesudahnya, alih-alih harus melakukan semua matematika dan kriptografi yang rumit untuk setiap TXO di jaringan, dompet sekarang dapat memeriksa bidang 1-byte itu di setiap transaksi dan baru kemudian melakukan verifikasi yang memakan waktu pada transaksi yang memiliki tag tersebut – tepatnya 1/256 TXO di jaringan!

Tag ini tidak mengungkapkan informasi apa pun tentang transaksi kepada observer luar, hanya menambahkan 1 byte (jumlah yang dapat diabaikan) ke ukuran transaksi, namun memungkinkan kami mengurangi waktu sinkronisasi hingga 40%+ dengan mengurangi verifikasi rumit yang diperlukan!

## Lihat tag: contoh sederhana

## Lihat tag: contoh sederhana

Bayangkan Anda memiliki 4.096 kotak di sebuah ruangan, dan hanya 5 kotak yang menjadi milik Anda. Semua kotak sama sekali tidak dapat dibedakan dari luar, dan satu-satunya cara untuk mengetahui apakah sebuah kotak untuk Anda adalah dengan membukanya dan menyelesaikan soal matematika pemakan waktu yang tertulis di dalamnya untuk memastikan bahwa itu adalah milik Anda.

Sekarang, bayangkan Anda memutuskan untuk meminta orang yang mengirimi Anda 5 kotak itu membuat kode khusus menggunakan alamat Anda, lalu letakkan hanya karakter pertama dari kode yang dihasilkan di bagian luar setiap kotak yang dikirimkan kepada Anda. Semua orang melakukan hal yang sama untuk kotak mereka (untuk memastikan semua kotak masih tidak dapat dibedakan), tetapi sekarang Anda cukup melihat satu kode karakter di bagian luar kotak, dan hanya membuka kotak yang memiliki karakter tersebut.

Meskipun kotak lain akan cocok dengan kode Anda, bahkan beberapa kotak yang tidak Anda miliki, jumlah kotak yang Anda perlukan untuk membuka dan menyelesaikan soal matematika sekarang hanya 16 (1/256 kotak!), bukan semuanya 4.096. 

Sekarang Anda buka 16 kotak itu, selesaikan soal matematika, dan simpan 5 kotak yang benar-benar milik Anda dari grup itu!

## Kapan lihat tag tersedia di Monero?

## Kapan lihat tag tersedia di Monero?

Lihat tag adalah salah satu fitur yang saat ini direncanakan untuk disertakan dalam [Pemutakhiran jaringan mendatang](https://github.com/monero-project/meta/issues/630), dan akan dirilis pada musim semi ini. Komunitas [ mengumpulkan 23.3XMR](https://bounties.monero.social/posts/28/implement-view-tags-to-decrease-wallet-sync-times-in-monero) (pada saat penulisan) untuk mendorong pengembangan dan penerapan lihat tag, dan sebagai hasilnya, sebagian besar pekerjaan untuk menyertakan lihat tag dalam basis kode Monero telah dilakukan. diselesaikan oleh j-berman bekerja sama dengan pengulas dan peneliti.

Setelah lihat tag diberlakukan oleh jaringan, semua transaksi yang dikirim setelah pemutakhiran jaringan akan mendapat manfaat dari waktu sinkronisasi dompet yang ditingkatkan secara drastis. Anda tidak perlu melakukan sesuatu yang khusus untuk mulai menggunakan lihat tag, dompet favorit Anda untuk Monero akan mulai menggunakannya setelah peningkatan jaringan secara otomatis!

## Bagaimana saya bisa belajar lebih banyak?

## Bagaimana saya bisa belajar lebih banyak?

Jika hal ini menarik rasa ingin tahu Anda seputar lihat tag, lihat beberapa tautan tambahan di bawah ini yang membahas topik secara mendalam:

  * [Mengurangi waktu pemindaian dengan 'lihat tag' 1-byte-per-output](https://github.com/monero-project/research-lab/issues/73)
  * [Tambahkan lihat tag ke output untuk mengurangi waktu pemindaian dompet](https://github.com/monero-project/monero/pull/8061)

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies)/

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin)/

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys)/

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero)/

  * [Bagaimana node jarak jauh memengaruhi privasi Monero](/knowledge/remote-nodes-privacy)/

  * [Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan](/knowledge/network-upgrades)/

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