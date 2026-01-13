---
title: "Seraphis: Apa yang Akan Dilakukannya untuk Monero"
slug: "seraphis-for-monero"
date: "2022-01-13"
image: "/images/seraphis.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
## Seraphis: peningkatan desain modular untuk transaksi Monero

Posting ini menjelaskan tentang [Seraphis](https://github.com/UkoeHB/Seraphis), sekumpulan struktur dan abstraksi protokol transaksi yang dikembangkan oleh kontributor penelitian dengan nama samaran [`koe`](https://github.com/UkoeHB) untuk ekosistem Monero, dan dengan analisis keamanan berkelanjutan oleh kontributor dengan nama samaran [`coinstudent2048`](https://github.com/coinstudent2048).  
Kami membuat beberapa penyederhanaan dan menghilangkan detail teknis tertentu demi kejelasan; untuk alasan ini, dan karena desain Seraphis masih dalam proses, pembaca yang tertarik harus merujuk ke dokumentasi Seraphis untuk mendapatkan informasi terbaru.

## Transaksi di Monero

Protokol seperti Bitcoin dan Monero dan lainnya bergantung pada operasi yang disebut "output model", di mana output __adalah representasi nilai yang dapat ditransfer.  
Transaksi menggunakan satu atau lebih output yang dikendalikan oleh pengirim, dan menghasilkan output baru yang diarahkan ke penerima (atau kembali ke pengirim sebagai kembalian); transaksi harus seimbang karena output yang dikonsumsi harus berisi nilai total yang persis sama dengan nilai dalam output baru (ditambah biaya yang dikenakan oleh jaringan).  
Di banyak protokol seperti Bitcoin, nilai yang terkandung dalam output ditulis dengan jelas, seperti penerimanya.  
Selain itu, dengan melihat blockchain, sangat mudah untuk melihat jika dan kapan suatu output telah digunakan (yaitu, apakah telah dikonsumsi dalam transaksi selanjutnya, dan transaksi mana yang membelanjakannya).

Sebaliknya, protokol seperti Monero memperkenalkan desain yang berbeda:

  * Nilai output disembunyikan dan tidak terlihat di blockchain
  * Alamat penerima disembunyikan dengan menggunakan protokol pengalamatan satu kali pakai
  * Apakah output telah digunakankan atau tidak dikaburkan oleh penggunaan signature yang ambigu

Hasilnya adalah, tanpa adanya informasi eksternal, sulit untuk menentukan apakah output yang diberikan telah digunakan, berapa nilainya, dan siapa penerimanya.

Protokol transaksi Monero saat ini disebut _RingCT_ , dan menggunakan beberapa blok penyusun kriptografi untuk mencapai tujuan desain ini.

  * _Komitmen_ menyembunyikan jumlah dengan cara yang berguna secara matematis
  * _Range proofs_ mencegah luapan yang dapat menggelembungkan persediaan
  * _Ring signature yang dapat ditautkan_ memberikan penanda ambiguitas dan mencegah upaya pembelanjaan ganda
  * _Pengimbangan komitmen_ menyatakan bahwa transaksi berimbang

Blok penyusun ini terjalin dengan hati-hati untuk membuat protokol RingCT.

Properti yang berguna dari protokol RingCT adalah bahwa beberapa blok penyusun dapat diubah atau ditingkatkan dengan cara yang menjaga keseluruhan desain dan properti tetap utuh, namun dapat memberikan peningkatan efisiensi atau keamanan. Faktanya, peningkatan semacam ini telah terjadi (atau direncanakan akan terjadi) beberapa kali dalam sejarah Monero. Bukti jangkauan dalam protokol RingCT asli berukuran besar dan lambat; mereka kemudian diperbarui ke konstruksi yang disebut [Bulletproof](https://eprint.iacr.org/2017/1066) yang membuat transaksi lebih kecil dan lebih cepat dengan analisis keamanan yang lebih baik, dan direncanakan untuk diperbarui ke konstruksi yang lebih baru disebut [Bulletproof+](https://eprint.iacr.org/2020/735) untuk manfaat efisiensi yang lebih besar. 

Proses serupa dilakukan dengan blok penyusun ring signature yang dapat ditautkan. Dalam protokol asli, konstruksi yang disebut [MLSAG](https://ledger.pitt.edu/ojs/ledger/article/view/34) digunakan. Ini kemudian diperbarui ke konstruksi yang lebih baru bernama [CLSAG](https://eprint.iacr.org/2019/654) yang lebih cepat, menghasilkan transaksi yang lebih kecil, dan memiliki analisis keamanan yang lebih baik. Konstruksi ring signature yang dapat ditautkan yang lebih baru berdasarkan [Triptych](https://eprint.iacr.org/2020/018) diusulkan, tetapi ini tidak dipilih untuk penerapan karena dampaknya pada operasi multi signature.

## Seraphis

Seraphis mengambil ide ini selangkah lebih jauh.  
Daripada memperbarui masing-masing blok penyusun dari protokol transaksi RingCT yang ada, ia memperkenalkan protokol berbeda yang dapat memanfaatkan blok penyusun yang berbeda dan menawarkan fungsionalitas yang lebih baik.

## Blok bangunan

Seraphis menggunakan kumpulan blok penyusun kriptografi yang berbeda untuk mencapai tujuan desainnya.

  * _Komitmen_ masih menyembunyikan jumlah
  * _Range proof_ masih mencegah limpahan dan inflasi pasokan
  * _Membership proof_ memberikan ambiguitas penandatangan
  * _Commitment Offset_ masih menegaskan keseimbangan
  * _Authorizing proof_ mencegah upaya pembelanjaan ganda

Perhatikan perubahannya di sini: ring signature yang dapat ditautkan diganti dengan kombinasi bukti keanggotaan dan bukti otorisasi. Bahasa kasarnya, bukti keanggotaan menunjukkan bahwa output yang dikonsumsi adalah bagian dari set yang lebih besar, mirip dengan yang terjadi di RingCT. Namun tidak seperti RingCT, bukti keanggotaan sama sekali tidak melibatkan tag penautan! Bukti otorisasi menunjukkan bahwa tag penautan valid dan digunakan untuk menandatangani transaksi akhir.

Karena RingCT memasukkan tag penautan ke dalam signature yang ambigu, operasi penandatanganan (dan multitanda tangan) lebih intensif secara komputasi, dan menjadi lebih menantang untuk membangun fungsionalitas terkait tag lainnya. Namun di Seraphis, pembuatan bukti keanggotaan dapat didelegasikan dengan aman dari perangkat yang sangat tepercaya (yang mungkin memiliki daya komputasi terbatas, seperti dompet perangkat keras) ke perangkat yang kurang tepercaya, dan operasi penandatanganan (dan multitanda tangan) jauh lebih mudah menggunakan bukti otorisasi yang jauh lebih sederhana. .

Untungnya, beberapa blok bangunan yang dibutuhkan oleh Seraphis sudah ada di tempat lain, dan tidak perlu didesain dari awal. Konstruksi Bulletproofs dan Bulletproofs+ dapat digunakan sebagai range proof. Modifikasi pada sistem pembuktian tipe Schnorr dapat digunakan untuk mengotorisasi pembuktian. Dan [sistem pembuktian](https://eprint.iacr.org/2015/643) yang efisien sudah digunakan sebagai dasar untuk Triptych, [Lelantus](https://eprint.iacr.org/2019/373), dan [Spark](https://eprint.iacr.org/2021/1173)* dapat dimodifikasi untuk bukti keanggotaan.

* Cypher Stack menerima dana untuk pengembangan Spark.

## Pengalamatan

Sayangnya, alamat Monero yang digunakan saat ini tidak kompatibel dengan Seraphis. Pengguna perlu membuat alamat baru dari kunci dompet mereka untuk menerima Monero jika Seraphis diimplementasikan. Namun, biaya ekosistem ini disertai dengan sejumlah manfaat.

Selain dari manfaat struktural yang dibahas di atas, desain Seraphis menerima banyak kemungkinan konstruksi alamat yang berbeda, yang masing-masing dilengkapi dengan pengorbanan. Meskipun konstruksi alamat akhir yang akan digunakan di Seraphis [masih diputuskan](https://github.com/monero-project/research-lab/issues/92) (satu skema yang menerima banyak perhatian disebut [JAMTIS](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)), kami dapat menjelaskan beberapa fitur yang umum dan berguna.

Anda mungkin tahu bahwa alamat Monero menawarkan fungsionalitas _view key_ , di mana Anda dapat memberikan kunci tampilan ke perangkat atau pihak ketiga dan mengizinkannya untuk mengawasi output yang masuk atas nama Anda, tetapi tanpa harus menyerahkan otoritas penggunaan. Ini berguna untuk dompet, yang dapat terus mengetahui aktifitas terbaru sambil menjaga agar kunci pembelanjaan Anda terkunci dengan aman. Ini juga berguna untuk kasus di mana Anda menginginkan akses tampilan eksternal, seperti badan amal publik yang menawarkan transparansi atau perusahaan dengan departemen akuntansi.

Kelemahan dari kunci tampilan Monero adalah mereka tidak memberikan akses tampilan yang lengkap atau terperinci. Tidak mungkin untuk mendeteksi dengan andal saat dompet membelanjakan dana, sehingga sulit untuk menghitung saldo dompet dengan benar saat kunci pembelanjaan tidak tersedia. Saat ini juga tidak mungkin untuk mendeteksi output yang masuk tanpa juga mempelajari nilai yang terkandung dalam output tersebut (yang berarti pihak ketiga mana pun yang bertanggung jawab untuk menemukan output yang masuk akan mempelajari dengan tepat berapa banyak Monero yang Anda peroleh).

Konstruksi pengalamatan Seraphis dapat menyelesaikan ini. Dengan Seraphis, alamat Anda dilengkapi dengan kunci berbeda yang dapat melakukan hal berbeda: 

  * Melihat output yang masuk, tetapi sembunyikan nilainya
  * Melihat output yang masuk, tetapi tunjukkan nilainya
  * Melihat output keluar
  * Membantu Anda menghasilkan transaksi, tetapi tidak menandatanganinya
  * Buat alamat baru (berguna untuk pengecer atau exchange dengan banyak pelanggan)

Sebagai pemegang alamat, Anda dapat memutuskan berapa banyak otoritas yang Anda delegasikan ke perangkat lain atau pihak ketiga.

## Gambaran besar

Seraphis merupakan perubahan besar pada ekosistem Monero. Meskipun melibatkan modifikasi pada alamat dan blok bangunan transaksi, desainnya menawarkan fleksibilitas dan fungsionalitas berguna yang tidak mungkin dilakukan dengan protokol RingCT saat ini. Sementara sebagian besar desain sedang diselesaikan dan dikembangkan ke dalam [implementasi ](https://github.com/UkoeHB/monero/tree/seraphis_lib), desain alamat dan analisis keamanan sedang berlangsung. Seraphis menawarkan peluang bagus untuk mendorong ekosistem Monero ke depan!

Bacaan lebih lanjut