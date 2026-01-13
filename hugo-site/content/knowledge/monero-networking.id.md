---
title: "Apa yang Perlu Diketahui Setiap Pengguna Monero Saat Berbicara tentang Jaringan"
slug: "monero-networking"
date: "2020-11-11"
image: "/images/networking.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Seharusnya sudah tidak mengejutkan siapa pun bahwa Monero, dan memang semua mata uang kripto, berjalan di internet. Namun, meskipun pernyataan ini tampak mendasar dan jelas, banyak yang tidak mempertimbangkan implikasi dari apa artinya ini sehubungan dengan privasi mereka. Dengan kata lain, ada beberapa hal yang Monero bisa dan tidak bisa lindungi, hanya karena berjalan di internet. Beberapa dari pertimbangan ini hanyalah ketidaknyamanan, sementara yang lain jauh lebih serius dalam skenario di mana privasi mutlak diperlukan. Mari luangkan waktu untuk membiasakan diri dengan bagaimana pengguna Monero berinteraksi satu sama lain di jaringan, dan apa artinya ini bagi privasi mereka.

Mulai dari hal-hal sepele, jika pengguna tidak memiliki akses ke internet, mereka tidak dapat mengunduh blok baru, menyebarkan transaksi atas nama orang lain, atau mengirim transaksi mereka sendiri. Hal yang menarik untuk dicatat adalah, pengguna dengan node penuh, tanpa akses internet dapat melakukan transaksi offline yang dapat dikirim nanti. Ini karena ring signature hanya membutuhkan output dari blockchain untuk disembunyikan. Pengingat singkat tentang [ cara kerja ring signature ](/knowledge/ring-signatures), ia menyembunyikan output nyata yang dikirim pengguna di antara kumpulan output tidak terafiliasi yang dipilih dari masa lalu. Jika pengguna memiliki akses ke output ini dalam bentuk blockchain yang diunduh sepenuhnya (node penuh) maka mereka dapat membuat ring signature dari output sebelumnya, dan setelah konektivitas internet dilanjutkan, sebarkan transaksi ke jaringan.

Pengguna yang menggunakan node jarak jauh tidak dapat melakukan ini, karena ketika mereka membuat ring signature mereka, mereka menghubungi node penuh jarak jauh agar output disertakan dalam ring signature. Tidak ada internet berarti mereka tidak dapat mencapai node ini, sehingga mereka tidak memiliki kemampuan konstruksi transaksi offline.

Sebelum kita melanjutkan ke beberapa pertimbangan privasi, mari kita lihat primer singkat tentang cara kerja internet secara keseluruhan. Seluruh internet tidak lebih dari komputer yang terhubung ke komputer lain. Itu dia. Blog yang suka kamu baca? Hanya beberapa file yang dihosting di komputer orang lain. Situs web tempat Anda sedang membaca artikel ini (LocalMonero)? File dan kode dihosting di komputer di suatu tempat. Bahkan situs gila besar bekerja dengan cara ini. Ambil YouTube misalnya. Hanya file video yang dihosting di sistem komputer raksasa Google, dan Anda menyambungkannya untuk mengunduh video ke komputer Anda sendiri sehingga Anda dapat menontonnya.

Komputer-komputer ini dapat membedakan satu sama lain karena setiap komputer yang terhubung ke internet diberi nomor identifikasi unik yang disebut alamat IP. Ini biasanya adalah empat rangkaian angka yang dipisahkan oleh titik, misalnya: 172.66.35.7. Penting untuk mengingat hal ini saat kami mempertimbangkan bagaimana informasi Monero dipindahkan di internet. Monero adalah jaringan peer-to-peer (P2P), artinya komputer terhubung langsung satu sama lain daripada menggunakan perantara. Jadi ketika node penuh pengguna mengunduh blok yang baru ditemukan, mereka tidak mengunduhnya dari server pusat, tetapi dari rekan-rekan mereka. Sisi negatifnya adalah, karena pengguna terhubung satu sama lain secara langsung, mereka mengetahui alamat IP masing-masing.

Jadi? Apa masalahnya? Itu hanya angka, kan? Tidak tepat. Alamat IP itu sendiri berisi informasi tentang pengguna, seperti negara asal, dan penyedia jaringan, tetapi, lebih buruk lagi, penyedia layanan internet (ISP) mengetahui alamat IP setiap orang yang menggunakan layanan mereka. Ini berarti ISP ini dan orang-orang yang bekerja dengan mereka dapat melihat lalu lintas internet pengguna dan, dengan menggunakan beberapa taktik cerdik, mengetahui bahwa mereka menggunakan Monero. Sekarang sebelum Anda takut, perhatikan kata-kata di sana. Yang dapat dilakukan pengintai ini hanyalah melihat bahwa seseorang terhubung ke node lain di jaringan Monero. Karena teknologi privasi Monero, tidak ada lagi yang dibocorkan tentang individu tersebut. Bukan apakah mereka menjalankan node atau tidak, atau jika/ketika mereka mengirim transaksi, dan jika transaksi dikirim, tidak ada informasinya yang diketahui. Semua ISP ini dapat melihat bahwa salah satu pengguna mereka terhubung ke jaringan Monero. 

Sekarang, bagi sebagian orang, di beberapa lokasi, informasi ini saja mungkin cukup untuk merusak reputasi atau kebebasan. Atau mungkin gagasan tentang seseorang yang menyerang privasi Anda dan apa yang Anda lakukan di internet, dengan alasan apa pun, tidak dapat Anda terima. Orang-orang ini didorong untuk hanya terhubung ke jaringan Monero menggunakan VPN, Tor, atau I2P, yang semuanya merupakan layanan yang menyembunyikan alamat IP pengguna dari orang lain serta menyembunyikan apa yang dilakukan pengguna dari ISP mereka. Perbedaan antara layanan ini berada di luar cakupan artikel ini, tetapi ada banyak artikel berkualitas tinggi yang ditulis tentang topik tersebut, sehingga pengguna yang peduli disarankan untuk mempelajarinya!

Bagi kita semua, kita mungkin berpikir bahwa membuat orang lain tahu bahwa kita terhubung ke jaringan Monero bukanlah masalah besar. Lagipula, isi sebenarnya dari transaksi kita, atau jika kita mengirimkannya, disembunyikan untuk umum, jadi apa salahnya? Meskipun ini mungkin benar, pengguna didorong untuk mempertimbangkan fakta bahwa daya tarik utama mata uang kripto adalah menjadi bank mereka sendiri. Saat Anda memegang kunci pribadi Anda, dan jika sesuatu terjadi padanya, tidak ada yang dapat membantu Anda memulihkan dana Anda yang hilang.

Menjadi bank Anda sendiri berarti mempertimbangkan, bukan hanya keamanan digital Anda, tetapi juga keamanan fisik Anda. Sangat mungkin bahwa pengetahuan seseorang yang terhubung ke jaringan Monero dapat membawa perhatian yang tidak diinginkan, tidak harus dari aktor skala besar seperti negara bangsa, tetapi aktor kecil dengan kepentingan egois, seperti peretas yang mencari uang dengan mudah. Memang ada cerita yang tak terhitung jumlahnya di seluruh ruang kripto dari skenario seperti itu yang benar-benar terjadi. 

Artikel ini tidak dimaksudkan untuk menakut-nakuti, melainkan mendorong pengguna untuk melakukan penelitian tentang metode perlindungan penjelajahan web apa yang tepat untuk mereka. Kabar baiknya adalah, keterampilan ini juga akan ditransfer ke penggunaan internet umum, bukan hanya penggunaan Monero, dan dengan demikian, di dunia kita yang semakin terhubung dengan internet, pengguna yang cerdas tidak akan salah mengumpulkan pengetahuan dan keterampilan yang tepat agar tetap aman. dan benar-benar menjadi bank mereka sendiri.

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