# Web-Server-Berbasis-TCP

Proyek ini terdiri dari dua bagian: server dan client yang berkomunikasi menggunakan protokol TCP. Server berfungsi sebagai web server sederhana yang dapat menerima permintaan HTTP dari client, mencari file yang diminta, dan mengirimkannya kembali dalam format HTTP. Client mengirimkan beberapa permintaan HTTP ke server dan menampilkan respon yang diterima.

**Server**
- Menangani permintaan HTTP dari client.
- Mengirimkan respon HTTP 200 OK jika file ditemukan, atau 404 Not Found jika file tidak ditemukan.
- Menggunakan multi-threading untuk menangani beberapa koneksi secara bersamaan.
- Dikonfigurasi dengan alamat IP dan port yang dapat disesuaikan.
**Client**
- Mengirimkan permintaan HTTP GET ke server.
- Menerima dan menampilkan respon dari server.
- Mendukung pengiriman beberapa permintaan secara paralel menggunakan thread.
