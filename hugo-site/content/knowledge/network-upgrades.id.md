---
title: "Bagaimana Monero menggunakan hard-fork untuk memutakhirkan jaringan"
slug: "network-upgrades"
date: "2022-02-10"
image: "/images/upgrades.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Salah satu bagian yang paling sering disalahpahami dari pendekatan Monero untuk membangun mata uang kripto yang terdesentralisasi, menjaga privasi, dan aman adalah peran yang dimainkan hard-fork (atau peningkatan jaringan).

Dalam postingan ini kita akan membahas apa itu hard-fork, mengapa hard-fork penting bagi Monero, dan peran apa yang dapat Anda mainkan di dalamnya di masa mendatang.

## Mengapa Monero perlu untuk terus meningkatkan jaringan?

Komunitas Monero telah berkomitmen untuk mengulangi dan meningkatkan proyek dari waktu ke waktu, dan tampaknya komitmen tersebut bermuara pada dua aspek utama dari etos komunitas:

  1. Proyek Monero pada akhirnya adalah perangkat lunak – kode – yang ditulis oleh manusia. Hal ini dapat menyebabkan kebutuhan untuk memperbaiki bug, menambahkan perbaikan yang ditemukan atau ditemukan dari waktu ke waktu, menerapkan modernisasi pada protokol, atau sekadar memelihara proyek. Ini serupa dalam banyak hal dengan perangkat lunak lain yang Anda gunakan (seperti peramban tempat Anda membaca ini!), yang perlu terus diperbarui untuk menambahkan fitur baru dan memperbaiki bug.

  2. Proyek Monero adalah alat privasi, dan privasi adalah perlombaan senjata yang terus berkembang. Orang-orang dan kelompok yang tidak menginginkan apa pun selain menghapus dunia privasi (baik finansial maupun pribadi) terus meningkatkan, mengembangkan, dan menemukan cara baru untuk menyerang pendekatan modern untuk menjaga privasi, seperti yang digunakan di Monero. Saat musuh privasi menemukan pendekatan baru ini, jaringan Monero harus dapat beradaptasi dan berkembang untuk melawan dan mempertahankan hak kami atas privasi finansial.

Proyek Monero pada akhirnya adalah perangkat lunak – kode – yang ditulis oleh manusia. Hal ini dapat menyebabkan kebutuhan untuk memperbaiki bug, menambahkan perbaikan yang ditemukan atau ditemukan dari waktu ke waktu, menerapkan modernisasi pada protokol, atau sekadar memelihara proyek. Ini serupa dalam banyak hal dengan perangkat lunak lain yang Anda gunakan (seperti peramban tempat Anda membaca ini!), yang perlu terus diperbarui untuk menambahkan fitur baru dan memperbaiki bug.

Proyek Monero adalah alat privasi, dan privasi adalah perlombaan senjata yang terus berkembang. Orang-orang dan kelompok yang tidak menginginkan apa pun selain menghapus dunia privasi (baik finansial maupun pribadi) terus meningkatkan, mengembangkan, dan menemukan cara baru untuk menyerang pendekatan modern untuk menjaga privasi, seperti yang digunakan di Monero. Saat musuh privasi menemukan pendekatan baru ini, jaringan Monero harus dapat beradaptasi dan berkembang untuk melawan dan mempertahankan hak kami atas privasi finansial.

## Apa itu hard-fork?

Kompleksitas pemutakhiran Monero mulai berlaku setelah Anda memahami betapa berbedanya memutakhirkan mata uang kripto versus hanya mendorong pembaruan perangkat lunak ke sesuatu seperti peramban.

Dalam mata uang kripto, aturan jaringan (hal-hal seperti tampilan transaksi, cara kerja penambangan, dan cara memverifikasi setiap blok) harus disetujui oleh jaringan, sesuatu yang disebut "konsensus". Ketika salah satu aturan ini perlu diubah atau ditingkatkan, jaringan harus menyetujui aturan baru, menyebabkan "hard fork" - situasi di mana jaringan benar-benar terbagi menjadi dua rangkaian blok - satu pada aturan lama, dan satu di aturan baru.

Ketika semua orang di komunitas menyetujui perubahan aturan, itu disebut "hard-fork tanpa perdebatan", dan chain yang masih memiliki aturan lama mati dan tidak ditambang setelah hard-fork. Hal ini telah terjadi di hampir setiap hard-fork Monero, dan satu-satunya kelanjutan dari aturan lama adalah dengan proyek yang mencoba mengambil untung dari hard-fork.

Sementara hard-fork non-perdebatan adalah satu-satunya cara untuk meningkatkan aspek-aspek penting dari jaringan Monero dengan benar, mereka juga memiliki efek samping yang membuat frustrasi – perangkat lunak lama, dirilis sebelum hard-fork direncanakan, tidak dapat memahami aturan jaringan yang baru dan tidak berfungsi setelah hard-fork! Hal ini dapat menyebabkan pengguna berpikir dana hilang, berpikir blockchain Monero telah berhenti, dan tidak dapat memindahkan dana sampai mereka meningkatkan dompet mereka.

## Siapa yang memutuskan kapan jaringan Monero ditingkatkan dan apa saja yang disertakan?

Karena tidak ada otoritas sentral, CEO, atau presiden Monero, pekerjaan seputar memutuskan kapan harus memutakhirkan jaringan, apa yang harus disertakan, dan bagaimana melakukannya jatuh ke tangan _kami_ , orang-orang di komunitas Monero yang memilih untuk terlibat dan berinteraksi! Ini adalah bagian yang sangat penting dari proyek terdesentralisasi, karena perencanaan dan pengambilan keputusan untuk proyek tersebut pada akhirnya terdesentralisasi dan bersumber dari komunitas.

Perencanaan waktu dan fitur yang disertakan dalam setiap peningkatan jaringan di Monero terjadi di dua tempat utama:

  1. Di IRC dan Matrix, platform obrolan yang paling banyak digunakan di komunitas Monero (yang dijembatani bersama). Platform ini memungkinkan untuk obrolan grup besar dan tempat semua pertemuan komunitas Monero yang dijadwalkan, pertemuan pengembang, dan pertemuan riset lab diadakan. Pertemuan ini adalah cara terbaik bagi Anda untuk mendengarkan (atau berkontribusi!) pada perencanaan dan diskusi seputar pemutakhiran jaringan di Monero.

  2. Di Github, platform komunikasi utama untuk diskusi, perencanaan, dan organisasi Monero yang berjalan lebih lama. Komunitas Monero menggunakan Github untuk mengatur pertemuan, mendiskusikan fitur dan ide baru, dan mengoordinasikan perencanaan peningkatan jaringan selain menyimpan kode untuk proyek Monero.

Di IRC dan Matrix, platform obrolan yang paling banyak digunakan di komunitas Monero (yang dijembatani bersama). Platform ini memungkinkan untuk obrolan grup besar dan tempat semua pertemuan komunitas Monero yang dijadwalkan, pertemuan pengembang, dan pertemuan riset lab diadakan. Pertemuan ini adalah cara terbaik bagi Anda untuk mendengarkan (atau berkontribusi!) pada perencanaan dan diskusi seputar pemutakhiran jaringan di Monero.

Di Github, platform komunikasi utama untuk diskusi, perencanaan, dan organisasi Monero yang berjalan lebih lama. Komunitas Monero menggunakan Github untuk mengatur pertemuan, mendiskusikan fitur dan ide baru, dan mengoordinasikan perencanaan peningkatan jaringan selain menyimpan kode untuk proyek Monero.

Jika Anda memiliki ide penting untuk pemutakhiran jaringan, tidak menyukai pendekatan yang diambil, atau memiliki kekhawatiran seputar waktu pemutakhiran, penting bagi Anda untuk angkat bicara dan mempresentasikan kasus Anda dengan jelas kepada komunitas!

## Bagaimana saya bisa membantu dengan pemutakhiran jaringan?

Karena pemutakhiran pada jaringan Monero memerlukan koordinasi dan persetujuan komunitas bersama dengan pembaruan perangkat lunak, sangat penting bagi sebanyak mungkin orang untuk terlibat dalam proses perencanaan, pengujian, dan komunikasi pemutakhiran jaringan.

Berikut adalah beberapa cara mudah yang dapat Anda lakukan untuk membantu memuluskan berbagai hal seputar pemutakhiran jaringan:

  1. Bergabunglah dengan rapat perencanaan [yang diposting di Github](https://github.com/monero-project/meta/issues), dengarkan, dan berikan kontribusi jika Anda memiliki sesuatu yang relevan untuk diangkat.
  2. Komunikasikan detail seputar waktu pemutakhiran jaringan (setelah diputuskan!) ke exchange, dompet, atau kumpulan penambangan favorit Anda. Mungkin sulit untuk memberi tahu semua pengguna Monero tentang pemutakhiran dengan benar, jadi penting bagi kita semua untuk membantu sebisa mungkin untuk menyebarkan berita.
  3. Uji perangkat lunak sebelum peningkatan jaringan. Akan ada panggilan untuk penguji sebelum pemutakhiran jaringan, baik di testnet maupun stagenet, untuk memastikan bahwa setiap aspek pemutakhiran telah direncanakan dan diterapkan dengan benar dalam perangkat lunak. Semakin banyak orang yang terlibat dan menguji versi baru secara menyeluruh, semakin besar kemungkinan pemutakhiran jaringan akan berjalan lancar!
  4. Setelah rilis yang kompatibel dengan pemutakhiran jaringan dipublikasikan, pastikan untuk segera memutakhirkan! Semakin banyak orang yang ditingkatkan dan siap untuk peningkatan jaringan, semakin lancar jaringan akan menanganinya dan semakin sedikit sakit kepala yang dialami pengguna.

## Apa yang dapat saya harapkan dalam peningkatan jaringan Monero berikutnya?

Meskipun belum ada tanggal pasti, akan segera ada pemutakhiran jaringan untuk mengimplementasikan beberapa pemutakhiran dan fitur utama di Monero: 

  1. Peningkatan ringsize dari 11 menjadi 16, meningkatkan set anonimitas dasar (baca: penyangkalan yang masuk akal, atau privasi dasar) dari setiap transaksi di jaringan
  2. [Lihat tag, cara brilian untuk mengurangi waktu sinkronisasi dompet sebesar 30-40%](https://localmonero.co/knowledge/view-tags-reduce-monero-sync-time)
  3. Perubahan biaya, meningkatkan keamanan dan ketahanan jaringan terhadap perubahan cepat di pasar biaya atau serangan oleh entitas jahat
  4. [Bulletproofs+, peningkatan lebih lanjut dalam efisiensi transaksi Monero](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html)

Perubahan ini akan sangat membantu dalam meningkatkan privasi, efisiensi, dan keamanan jaringan, sekaligus membuka jalan bagi [Seraphis](https://localmonero.co/knowledge/seraphis-for-monero), protokol transaksi generasi berikutnya untuk Monero.

## Bagaimana saya bisa belajar lebih banyak?

Topik hard-fork dan pemutakhiran jaringan sangat luas dan ada sejarah panjang dan bertingkat tentangnya di Monero, jadi pastikan untuk menggali beberapa tautan berikut jika Anda ingin mempelajari lebih lanjut tentang riwayat, proses, atau perencanaan yang sedang berlangsung untuk pemutakhiran jaringan yang akan datang!

  * [perencanaan hard-fork Monero v15](https://github.com/monero-project/meta/issues/630)
  * [Pemutakhiran perangkat lunak terjadwal (di Monero)](https://github.com/monero-project/monero#scheduled-software-upgrades)
  * [Catatan tentang pemutakhiran protokol terjadwal](https://web.getmonero.org/2020/09/01/note-scheduled-upgrades.html)

Bacaan lebih lanjut