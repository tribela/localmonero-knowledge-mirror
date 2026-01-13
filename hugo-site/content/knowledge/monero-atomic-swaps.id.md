---
title: "Bagaimana Atomic Swap Akan Bekerja di Monero"
slug: "monero-atomic-swaps"
date: "2020-11-18"
image: "/images/atomic.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Dalam mengejar desentralisasi dan sistem yang benar-benar tanpa izin, beberapa hal didambakan dalam ruang kripto seperti pertukaran terdesentralisasi dan atomic swap. Sejak awal, Monero telah berjuang untuk mengimplementasikan atomic swap, karena fitur privasi menciptakan masalah unik saat mencoba merancang sebuah protokol.

Tapi pertama-tama, mari kembali ke belakang. Apa itu atomic swap? Atomic swap adalah sebuah protokol di mana dua mata uang kripto yang berbeda, pada blockchain yang berbeda, dapat ditukar dengan cara yang mengabaikan kepercayaan tanpa perantara. Ini berarti jika seseorang ingin menukarkan mata uang kripto A dengan mata uang kripto B, mereka dapat melakukannya tanpa sebuah exchange, baik tersentralisasi atau pun terdesentralisasi. Seperti yang bisa dibayangkan, ini membutuhkan banyak penelitian, dan detail teknis lengkap yang membuatnya mungkin, jadi sangat rumit. Sekali lagi, LocalMonero hadir untuk membantu dan memberikan penjelasan sederhana bagi orang awam.

Untuk memulai, mari pertimbangkan bentuk atomic swap yang paling sederhana, seperti yang telah diterapkan oleh Bitcoin. Jika seseorang ingin menukar Bitcoin dengan koin lain yang menggunakan teknologi hash time lock contract yang sama, mereka dapat melakukannya dengan cara berikut. Alice memiliki Bitcoin (BTC), tetapi menginginkan Litecoin (LTC), dan Bob memiliki LTC, tetapi menginginkan BTC. Mereka memutuskan untuk melakukan atomic swap sehingga masing-masing mendapatkan koin yang mereka inginkan. Alice mengirimkan BTC-nya ke alamat khusus, menggunakan skrip yang mengunci dana sehingga bahkan dia sendiri pun tidak dapat mengaksesnya. Anda dapat menganggapnya seperti Alice memasukkan BTC-nya ke dalam sebuah kotak kunci. Saat kotak kunci dibuat, dia mendapatkan kunci, dan mengirimkan hash dari kunci ini ke Bob. Sekarang Bob tidak memiliki kunci itu sendiri, hanya hash, jadi dia belum bisa mengakses dananya.

Bob menggunakan hash ini sebagai seed yang mana dari sana dia membuat kotak kuncinya sendiri, dan mengirimkan LTC-nya ke sana, di mana itu juga dikunci. Karena hash kunci Alice digunakan sebagai seed pembuatan kotak kunci Bob, dia dapat menggunakan kuncinya untuk mengklaim LTC di kotak kunci Bob. Kunci nya pas! Namun, dengan menggunakan sihir voodoo matematika, saat dia menggunakan kuncinya untuk membuka kunci LTC, dia memperlihatkan kunci tersebut kepada Bob, yang kemudian dapat menggunakannya untuk mengklaim BTC yang dia masukkan ke dalam kotak kuncinya. Dengan cara ini, tanpa perantara, Alice dan Bob berhasil menukar aset mereka.

Tapi ada sedikit masalah. Bagaimana jika Alice mengirim ke kotak kuncinya, dan Bob memutuskan bahwa dia tidak ingin melakukan perdagangan lagi. Sekarang, karena Alice tidak dapat mengakses BTC-nya yang dia kunci, dan Bob tidak akan menyelesaikan bagian transaksinya, Alice baru saja kehilangan uangnya selamanya. Nah, untungnya, Bitcoin memiliki teknologi kecil yang disebut dengan transaksi pengembalian dana, dan jadi setelah jangka waktu tertentu, jika BTC tersebut tidak diklaim oleh Bob, skripnya memiliki fail-safe bawaan, di mana BTC akan secara otomatis kembali ke Alice. Ini adalah speedbump utama untuk pengimplementasian atomic swap Monero. Karena [teknologi ring signature privacy ](/knowledge/ring-signatures) milik Monero, pengirim transaksi selalu tidak jelas. Bagaimana protokol dapat melakukan transaksi pengembalian dana jika bahkan tidak tahu dari mana transaksi berasal?

Pada tahun 2017, sekelompok kecil peneliti menguraikan sebuah metode berbeda yang mana atomic swap dapat bekerja di Monero. Setelah beberapa tahun penyempurnaan, para peneliti menyelesaikan proses di mana Monero dapat melakukan atomic swap dengan Bitcoin, bahkan tanpa transaksi pengembalian dana.

Karena adanya banyak hal dengan tingkat kerumitan teknis seperti ini, kami akan menjelaskan dengan lebih sederhana tentang beberapa hal agar ide tersebut dapat di pahami, tetapi masih akan tetap memberikan ide yang solid mengenai mekanismenya di mana proses ini akan bekerja.

Baik Alice (yang memiliki XMR dan menginginkan BTC) maupun Bob (yang memiliki BTC dan menginginkan XMR) harus mengunduh dan menjalankan program yang mendukung atomic swap. Hal ini bisa saja diimplementasikan ke dalam dompet, pertukaran terdesentralisasi, atau program khusus tertentu, tetapi perangkat lunak harus menjalankan protokol atomic swap. Pada langkah pertama, client Alice dan Bob terhubung satu sama lain dan membuat beberapa rahasia dan kunci yang dibagi bersama. Pada langkah ini, alamat Monero baru sudah dibuat, dengan Alice memiliki setengah kuncinya, dan Bob memiliki setengah kunci lainnya. Belum ada Monero di sana, jadi tidak ada yang perlu dibelanjakan. Satu hal terakhir yang perlu diperhatikan tentang alamat ini, keduanya memiliki kunci tampilan untuk dompet ini, sehingga keduanya dapat mengintip ke dalam untuk melihat apakah atau kapan Monero tiba.

Pada langkah kedua, Bob mengirimkan BTC-nya ke sebuah alamat khusus, mirip dengan protokol atomic swap Bitcoin yang telah kita bahas. Setelah Alice melihat BTC tiba di alamat ini pada blockchain, dia mengirimkan Monero-nya ke alamat Monero yang dia dan Bob sama-sama memiliki setengah kuncinya. Bob dapat memverifikasi bahwa Monero sudah tiba karena dia juga memiliki kunci tampilan, dan begitu dia melihat Monero dengan aman di dompet, dia mengirimkan sebagian dari kunci kepada Alice yang memungkinkannya untuk menarik Bitcoin. Mirip dengan protokol lainnya, proses mengklaim Bitcoin membuka setengah dari kunci Monero miliknya kepada Bob. Sekarang Bob memiliki kedua bagiannya, jadi dia dapat mengklaim Monero, sedangkan Alice hanya memiliki setengahnya, jadi dia tidak dapat mencoba mengambilnya sebelum Bob melakukannya.

Jadi jika Anda melihat semua ini dan masih agak bingung tentang bagaimana Monero dapat mengatasi masalah transaksi pengembalian dana, jawabannya cukup sederhana. Karena Monero sendiri tidak memiliki transaksi pengembalian uang, pembaca harus memperhatikan bahwa Bitcoin (yang memang memiliki transaksi pengembalian uang) dikirim terlebih dahulu, dan hanya setelah diverifikasi telah berada di blockchain barulah Monero dikirim. Hal ini memungkinkan Monero memanfaatkan kemampuan Bitcoin untuk membuat skrip dalam transaksi pengembalian dana dan memanfaatkannya, tanpa perlu memiliki kemampuan ini sendiri.

Atomic swap sekarang telah selesai, tetapi dari sini, Bob memiliki beberapa opsi untuk XMR yang baru diklaimnya. Dia bisa menggunakan dompet Monero ini sebagaimana adanya, atau memindahkan XMR ke dompet lain yang sudah dia miliki. Bob kemungkinan besar akan memindahkan Monero ke dompet lain, karena Alice masih memiliki kunci tampilan dan dapat melihat ke dalamnya.

Keindahan dari protokol ini adalah bahwa ini masih cukup baru, dan masih ada banyak ruang untuk pengoptimalan. Protokol ini juga cukup fleksibel dalam arsitekturnya, jadi implementasi di dompet lain atau exchange terdesentralisasi harus sederhana dan cocok dengan arsitektur yang ada. 

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