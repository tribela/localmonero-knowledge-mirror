---
title: "Majalah Wired Salah Tentang Monero, Ini Alasannya"
slug: "wired-article-debunked"
date: "2020-06-24"
image: "/images/wired.png"
image_credit: "Illustration by CypherStack"
image_credit_url: "https://cypherstack.com"
---
Baik dalam ranah privasi maupun mata uang kripto, misinformasi sering kali merajalela. Kami memiliki [ artikel yang menguraikan lima belas asumsi umum yang salah atau usang tentang Monero ](/knowledge/monero-myths-debunked), tetapi kami ingin meluangkan waktu untuk membahas satu artikel tertentu yang sering dikutip dan diedarkan oleh para skeptis Monero.

Wired Publication mengeluarkan [sebuah artikel](https://www.wired.com/story/monero-privacy/) pada tanggal 27 Maret 2018, yang ditulis sendiri sebagai tanggapan atas makalah baru dari pers yang diterbitkan oleh berbagai akademisi berjudul: “Analisis Empiris ketertelusuran dalam Monero Blockchain”.

Meskipun makalah ini ditulis bersama oleh individu dengan konflik kepentingan yang jelas (baca: mereka adalah penasihat, dan memiliki saham di Zcash), makalah tersebut diterima dengan cukup baik oleh komunitas Monero sebagai konfirmasi hal-hal yang sudah diketahui oleh komunitas dan ditulis dalam makalah Monero Research Lab mereka sendiri ([MRL-0001](https://web.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) dan [MRL-0004](https://web.getmonero.org/resources/research-lab/pubs/MRL-0004.pdf)) yang paling awal diterbitkan empat tahun sebelumnya. Ada juga beberapa rasa frustrasi akan hal tersebut, terutama konflik kepentingan, fakta bahwa masalah sudah diketahui, dibahas dan – dalam beberapa kasus – diperbaiki, dan kesalahan karakterisasi jaminan privasi Monero pada saat itu. Komunitas mengomentari pracetak karya tersebut, dan banyak dari rekomendasi mereka berhasil sampai ke makalah akhir.

Tapi sebenarnya apa yang salah dikarakterisasi? Fakta bahwa Monero tidak memiliki kekurangan dibahas di koran selama lebih dari setahun. Transaksi sebelum tahun 2017 memang rentan terhadap suatu bentuk kebocoran privasi, tetapi pada saat penerbitan, Monero telah mengatasi sebagian besar masalah tersebut. Agar adil bagi penulis, mereka membahas solusi Monero dalam skala kecil, tetapi tidak cukup untuk mempengaruhi efeknya pada siklus media kripto pada saat itu. Oleh karena itu artikel Wired muncul.

Meskipun kami dapat memeriksa artikel Wired yang dipermasalahkan sebagai bagian periode, dan seberapa benar atau tidak benarnya pada saat itu, fakta bahwa itu masih dibagikan hari ini sebagai alasan mengapa jaminan privasi Monero lemah sebenarnya mengundang analisis tentang bagaimana karya itu bertahan di masa sekarang. Kami dengan senang hati menerima undangan ini.

Pembacaan cepat artikel tersebut menunjukkan beberapa kalimat sensasional, seperti "[Temuan] seharusnya tidak hanya membuat khawatir siapa pun yang mencoba menghabiskan Monero secara diam-diam hari ini" dan seluruh nada artikel yang mendalilkan penelitian sebagai 'baru', sebagian besar didasarkan pada publikasi. Makalah akademis itu sendiri memiliki rekomendasi seperti memperingatkan pengguna Monero tentang potensi kompromi anonimitas mereka, terlepas dari fakta bahwa diskusi ini tidak hanya terjadi sejak 2014, tetapi seruan komunitas adalah agar orang tidak membeli Monero dan itu sangat eksperimental.

Tapi bagaimana dengan kritik itu sendiri? Kenyataannya adalah bahwa banyak masalah dengan Monero sebagai koin privasi tidak lagi berlaku untuk Monero, atau berbagi masalah dengan koin privasi sebagai kategori mata uang kripto berbasis blockchain. Mari mulai membahas ini.

Salah satu kritik yang paling sering dikutip dari Monero adalah bahwa, karena keabadian dan kekekalan blockchain, jika teknologi masa depan melanggar privasi, semua transaksi masa lalu Monero akan dibongkar. Dengan kata lain, privasi Anda memiliki jam yang terus berdetak.

Kami tidak bisa cukup menekankan hal ini. Secara harfiah setiap koin privasi yang menggunakan metode on-chain untuk pengaburan dan privasi memiliki kelemahan ini, namun sering digunakan untuk melawan Monero (ironisnya, berkali-kali oleh koin privasi pesaing dengan masalah yang sama), dan juga digunakan dalam artikel ini. Tanggapan terhadap kritik ini mungkin mengejutkan bagi sebagian orang, tetapi Monero sebenarnya mungkin kurang rentan dibandingkan koin privasi lainnya karena fakta bahwa ia memiliki pendekatan privasi multi-cabang.

Monero menyembunyikan output (pengirim), jumlah, dan penerima melalui tiga teknologi berbeda, ring signature, RingCT, dan stealth address. Dari jumlah tersebut, ring signature adalah yang paling lemah, dan paling rentan terhadap heuristik modern dan teknologi teoritis masa depan yang bersifat pemecah privasi. Hal ini telah diketahui oleh komunitas Monero selama bertahun-tahun, dan penelitian aktif sedang dilakukan untuk memperbaiki atau mengganti skema ring signature seluruhnya. 

Namun, bahkan jika ring signature rusak seluruhnya, hanya output sebenarnya yang akan terungkap. BUKAN pengirim (seperti pada individu), tetapi hasilnya. Untuk memasangkan output dengan identitas bukanlah hal yang tidak mungkin, tetapi akan membutuhkan lebih banyak metadata dan sumber daya. Ditambah dengan fakta bahwa RingCT dan stealth address TIDAK akan terungkap mengurangi dampak lebih jauh. 

Perlu dicatat bahwa artikel Wired dengan ringan membahas informasi di atas di bagian di mana mereka menghubungi Riccardo 'fluffypony' Spagni untuk memberikan komentar, tetapi waktu yang diberikan singkat, dan hampir terlihat seperti melompati informasi krusial ini. Kurangnya pemahaman terutama terlihat ketika mencoba mendiskusikan hal-hal ini dengan orang-orang yang iseng berbagi artikel di zaman modern ini.

Kritik lain yang jauh lebih sulit untuk ditanggapi adalah bagaimana dunia luar memandang Monero, dan bagaimana hal itu berhubungan dengan bagaimana komunitas di sekitar Monero memandang koin tersebut. Sebagai contoh, pembaca tidak perlu melihat lebih jauh dari judul artikel itu sendiri: “Mata Uang Favorit The Dark Web Kurang Untraceable Dari Kelihatannya”.

Setiap orang yang menghabiskan banyak waktu di komunitas Monero dapat membuktikan fakta bahwa komunitas Monero berusaha keras untuk menunjukkan betapa sulitnya privasi sebenarnya untuk dicapai, bahkan sampai gangguan pemasaran atau upaya adopsi. Jika komunitas menyediakan banyak sumber daya untuk membahas koin dan kekurangannya secara akurat, pada titik tertentu, ketidaktahuan menjadi kesalahan pengguna yang percaya bahwa hanya koin yang mereka butuhkan untuk menjadi 100% pribadi.

Pada titik ini, seharusnya sudah terbukti bahwa komunitas Monero menganggap serius privasinya, dan kejujurannya tentang kelemahan di dalamnya dan perbaikan selanjutnya. Artikel, seperti yang dipermasalahkan, benar-benar merindukan semangat inovasi di Monero ini. Ini menyamakan Monero dengan mata uang kripto lain yang membuat klaim muluk-muluk, dengan hanya memikirkan keuntungan dan memangsa calon investor yang tidak berpendidikan.

Kenyataannya sangat berbeda. Monero sangat menyadari kelemahannya, berusaha untuk terus membangun untuk memperbaikinya, memperketat sambungan yang kendor, dan mencapai tujuan yang sangat nyata, tetapi sangat sulit untuk memberikan kepada dunia sebuah privasi, mata uang kripto fungible yang dapat digunakan oleh semua orang, dan lakukan semuanya dengan cara yang adil, terdesentralisasi, dan digerakkan oleh komunitas. Mungkin sudah waktunya untuk mengesampingkan sensasi dan berbagi artikel sebagai sarana untuk memamerkan tas dan mempromosikan pesaing. Mungkin sudah waktunya untuk menceritakan kisah lain.

Bacaan lebih lanjut