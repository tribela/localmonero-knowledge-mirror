---
title: "Bagaimana node jarak jauh memengaruhi privasi Monero"
slug: "remote-nodes-privacy"
date: "2022-02-16"
image: "/images/nodes.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Salah satu keuntungan terbesar yang dimiliki Monero dibandingkan mata uang kripto lainnya adalah privasi on-chain-nya, tetapi pernahkah Anda bertanya-tanya bagaimana privasi Monero bertahan saat Anda menggunakan node jarak jauh? Bagaimana jika Anda menggunakan server “dompet ringan” seperti MyMonero?

Dalam postingan ini kami akan menyelami beberapa detail di balik bagaimana Monero memberikan privasi on-chain yang luar biasa bahkan saat menggunakan node jarak jauh, serta apa yang harus diperhatikan saat menggunakan node jarak jauh.

## Apa fungsi node di Monero?

Bagi mereka yang kurang mengetahui cara kerja Monero, node (atau server) di jaringan Monero dapat dijalankan oleh siapa saja dan mengizinkan pemilik node – atau orang lain yang mereka pilih untuk membagikannya! – untuk menyinkronkan salinan blockchain dan memberikan salinan itu kepada orang lain di jaringan. Node-node ini juga memverifikasi semua transaksi yang terjadi di jaringan, serta semua blok yang dipublikasikan dan memastikan bahwa semuanya mengikuti aturan yang ditetapkan melalui konsensus.

Fungsi lain yang diberikan node di Monero adalah sebagai cara untuk menyediakan semua data yang dibutuhkan dompet Monero favorit Anda untuk memeriksa transaksi milik Anda dengan benar dan melakukan transaksi baru. Data ini disediakan oleh node dalam dua cara:

  * Data dari setiap blok di blockchain diminta oleh dompet, dipindai untuk transaksi milik Anda, lalu dibuang setelah diperiksa oleh dompet. 
    * Langkah ini akan segera ditingkatkan secara drastis, berkat [lihat tag](/knowledge/view-tags-reduce-monero-sync-time).
  * Saat mengirim transaksi, node yang Anda gunakan menyediakan daftar kemungkinan umpan (atau input palsu) untuk digunakan saat membuat transaksi, memastikan bahwa Anda memiliki kerumunan yang baik untuk bersembunyi setiap kali Anda membelanjakan Monero. 
    * Umpan ini adalah bagian dari [ring signatures](/knowledge/ring-signatures), bagian penting dari pendekatan Monero terhadap privasi on-chain.

## Apa cara paling pribadi dan aman untuk menggunakan Monero?

Hal terbaik untuk dilakukan, bahkan dengan privasi on-chain kuat yang disediakan oleh Monero saat menggunakan node jarak jauh, adalah menjalankan node Monero Anda sendiri untuk memastikan bahwa Anda memiliki salinan murni dari blockchain Monero yang berguna dan alamat IP Anda terlindungi dengan baik. Manfaat lain saat menjalankan node Anda sendiri adalah Anda dapat berkontribusi kembali ke jaringan, membiarkan node lain melakukan sinkronisasi dari node Anda atau bahkan membiarkan pengguna lain terhubung ke node Anda dengan dompet mereka.

Meskipun demikian, Monero masih memberikan privasi yang sangat baik saat menggunakan node jarak jauh. Jika Anda tertarik untuk menjalankan node Monero Anda sendiri, berikut adalah panduan yang mudah diikuti untuk melakukannya: 

  * [Jalankan Monero Node](https://sethforprivacy.com/guides/run-a-monero-node/)

## Apa yang bisa dipelajari node jarak jauh tentang saya?

Saat menggunakan node jarak jauh, ada beberapa informasi penting yang terpapar ke node jarak jauh dan beberapa cara utama node dapat menyerang Anda, mencegah Anda bertransaksi, dan banyak lagi.

Hal pertama yang dapat dipelajari node jarak jauh tentang Anda adalah alamat IP publik Anda. Meskipun ini mudah-mudahan akan disembunyikan melalui VPN atau Tor, node jarak jauh dapat mengaitkan alamat IP publik Anda dengan transaksi, membantu mereka mempersempit dari mana Anda bertransaksi. Node jarak jauh juga dapat mempelajari blok terakhir yang disinkronkan dompet Anda dan menggunakan ini untuk mencoba dan membuat tebakan cerdas tentang Anda, seperti saat Anda biasanya menggunakan Monero dan saat terakhir Anda membelanjakan Monero. Ini terutama benar jika Anda selalu berasal dari alamat IP yang sama (seperti rumah Anda). Hal penting terakhir yang dapat dipelajari node jarak jauh tentang Anda adalah informasi dasar tentang transaksi yang Anda kirim melaluinya. Meskipun ini mungkin data paling jelas yang diperoleh operator node jarak jauh tentang Anda, penting untuk dipahami bahwa ini dapat digunakan untuk membantu melacak pengirim transaksi saat menggabungkan informasi tersebut dengan data off-chain lainnya. Ini bisa sangat berbahaya jika node jarak jauh dijalankan oleh entitas jahat, perusahaan analitik blockchain, atau negara-bangsa penindas.

Node jarak jauh juga dapat mencoba untuk menimbulkan masalah bagi Anda dengan menyembunyikan blok-blok dari Anda, membuat dompet Anda mengira itu telah disinkronkan padahal sebenarnya tidak. Hal ini dapat membuat Anda mengira dana hilang atau mencegah Anda membelanjakan dana hingga Anda terhubung ke node lain. Hal utama terakhir yang dapat dilakukan node jarak jauh adalah memberi dompet Anda daftar umpan yang dimanipulasi. Ini dapat menyebabkan dompet Anda gagal sepenuhnya untuk membangun transaksi (membuat Anda tidak dapat membelanjakan dana), atau dapat memungkinkan node jarak jauh untuk mencoba dan memberikan umpan yang diketahui telah dihabiskan untuk mengurangi anonimitas yang Anda terima dalam setiap transaksi.

## Jaminan privasi apa yang masih ada saat menggunakan node jarak jauh?

Meskipun artikel ini mungkin sedikit membuat Anda takut, penting untuk disadari bahwa privasi yang disediakan oleh Monero sangat baik bahkan saat menggunakan node jarak jauh, dan jauh melampaui mata uang kripto lainnya saat digunakan dengan cara ini. Anda masih mendapatkan privasi on-chain yang kuat yang disediakan oleh Monero, karena node jarak jauh tidak pernah mengetahui input sebenarnya (koin apa yang Anda belanjakan), jumlah yang dihabiskan Monero dalam transaksi, atau alamat penerima transaksi. Pengamat luar juga tidak dapat melihat input, jumlah, atau alamat sebenarnya yang terlibat (apa pun jenis node yang Anda pilih untuk digunakan!), memastikan bahwa di luar node jarak jauh bahkan alamat IP Anda, informasi sinkronisasi dompet, dan transaksi memiliki jaminan privasi yang kuat .

Node jarak jauh juga tidak pernah memiliki akses ke transaksi sebelumnya yang telah Anda kirim atau terima atau jumlah Monero yang saat ini ada di dompet Anda, dan kehilangan semua visibilitas transaksi Anda saat Anda mulai menggunakan node lain. Tidak ada kunci pribadi (baik kunci pembelanjaan atau tampilan) yang pernah diberikan ke node jarak jauh, sehingga dompet Anda tetap pribadi, aman, dan dapat digunakan. Terlepas dari node jarak jauh, Anda juga tidak akan pernah berisiko kehilangan Monero atau dicuri, karena node tidak dapat menyunting alamat penerima, tidak pernah memiliki akses ke kunci pribadi dompet Anda, dan tidak dapat menyita Monero Anda dengan cara apa pun.

## Bagaimana dengan “dompet ringan” seperti MyMonero?

Meskipun topiknya sedikit di luar cakupan artikel ini, saya memang ingin membahas jenis dompet unik di Monero – dompet ringan. Nama dompet ringan berasal dari fakta bahwa dompet Anda (di ponsel atau komputer Anda) tidak harus melakukan sinkronisasi blockchain apa pun, menjadikan pengalaman lebih cepat dan lebih lancar.

Namun, dompet seperti ini datang dengan trade-off privasi yang parah untuk saat ini – dompet Anda mengirimkan kunci tampilan pribadi ke server jarak jauh yang Anda gunakan (seperti default di MyMonero), memberikan visibilitas penuh kepada server jarak jauh ke dalam setiap dana yang diterima sejak pembuatan dompet Anda (dan sampai Anda berhenti menggunakan dompet atau seed itu). Ini mengurangi privasi yang Anda terima dari operator node secara drastis, dan harus didekati dengan hati-hati.

Untungnya, komunitas Monero sedang berupaya meningkatkan perangkat lunak yang dapat Anda gunakan untuk menghosting Light Wallet Server (LWS) Anda sendiri, yang akan memungkinkan Anda melakukan sinkronisasi cepat tanpa mempercayai pihak ketiga dengan kunci tampilan pribadi Anda – karena Anda akan menjalankan perangkat lunak di mana dompet Anda mengirimkan kunci tampilan pribadi!

Untuk informasi lebih lanjut tentang server dompet ringan khusus, lihat repositori Github di bawah ini:

  * [monero-lws](https://github.com/vtnerd/monero-lws)

## Bagaimana saya bisa belajar lebih banyak?

Jika Anda penasaran dan ingin lebih memahami node di Monero dan mencari cara untuk menggunakan node jarak jauh atau menjalankan node Anda sendiri, lihat tautan di bawah untuk mengetahui tempat yang bagus untuk memulai:

  * [Monero World, daftar node jarak jauh yang dikelola komunitas yang dapat digunakan](https://moneroworld.com/#nodes)
  * [Node Monero dijalankan oleh Seth For Privacy, penulis artikel ini](https://sethforprivacy.com/about/#high-performance-monero-nodes)
  * [monero.fail, daftar node jarak jauh dengan status yang sering diperiksa< /a>](https://monero.fail/)
  * [Cara menghubungkan ke node jarak jauh dalam dompet GUI](https://www.getmonero.org/resources/user-guides/remote_node_gui.html)
  * [Moneropedia - Node Jarak Jauh](https://www.getmonero.org/resources/moneropedia/remote-node.html)

Bacaan lebih lanjut

  * [Bagaimana Monero secara unik memungkinkan ekonomi sirkular](/knowledge/monero-circular-economies/)

  * [Ring signature Monero vs CoinJoin seperti di Wasabi](/knowledge/ring-signatures-vs-coinjoin/)

  * [Mengapa (dan bagaimana!) Anda harus memegang kunci Anda sendiri](/knowledge/hold-your-keys/)

  * [Berkontribusi kembali ke Monero](/knowledge/contributing-to-monero/)

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