# Redis---Counter--INCR

Menggunakan Docker : Docker memungkinkan Anda untuk menjalankan Redis dalam wadah (container) yang terisolasi.

# Tutorial Redit menggunakan Docker
<p>Instal Docker:

Pastikan Anda sudah menginstal Docker di komputer Anda. Jika belum, Anda dapat mengunduh dan menginstalnya dari situs resmi Docker.
Jalankan Container Redis:

Buka terminal atau command prompt di komputer Anda.
Jalankan Redis Container:

Untuk menjalankan Redis dalam container Docker, gunakan perintah berikut:
bash
Copy code
docker run --name my-redis-container -p 6379:6379 -d redis
--name my-redis-container memberikan nama untuk container Redis yang Anda jalankan. Anda dapat mengganti my-redis-container dengan nama yang Anda inginkan.
-p 6379:6379 menghubungkan port 6379 di host Anda dengan port 6379 di container Redis. Ini memungkinkan Anda untuk terhubung ke Redis dari host Anda.
-d menjalankan container dalam mode detached (background).
redis adalah nama image Redis yang akan digunakan. Jika image belum ada di komputer Anda, Docker akan mengunduhnya secara otomatis.
Verifikasi Instalasi Redis:

Untuk memastikan Redis berjalan dengan baik, Anda dapat menggunakan client Redis untuk terhubung ke container Redis yang baru saja Anda buat. Anda dapat menginstal client Redis di komputer Anda atau menggunakan Docker untuk itu juga:
bash
Copy code
docker run -it --link my-redis-container:redis --rm redis redis-cli -h redis -p 6379
-it menjalankan container dalam mode interaktif.
--link my-redis-container:redis menghubungkan container Redis ke client Redis.
--rm menghapus container Redis setelah selesai.
redis-cli -h redis -p 6379 menjalankan client Redis untuk terhubung ke container Redis.
Menghentikan dan Menghapus Container Redis:

Jika Anda ingin menghentikan dan menghapus container Redis, Anda dapat menggunakan perintah berikut:
bash
Copy code
docker stop my-redis-container
docker rm my-redis-container
Sekarang Anda telah berhasil menginstal Redis menggunakan Docker dan dapat mengaksesnya dari komputer Anda melalui port 6379. Anda dapat menggunakan Redis seperti biasa dalam konteks Docker ini. Pastikan untuk menjaga container berjalan jika Anda ingin terus mengakses Redis.</p>
