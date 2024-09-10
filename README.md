# heritage-craft
Nama: Namira Aulia
Tautan PWS: [heritagecraft](http://namira-aulia31-heritagecraft.pbp.cs.ui.ac.id/)


## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step
# MEMBUAT PROYEK DJANGO BARU
- Langkah pertama yang saya lakukan untuk mengimplementasikan checklist tugas 1 ini adalah mulai dari membuat direktori baru di lokal dengan nama "heritage-craft" kemudian direktori "heritage-craft" tersebut dibuka melalui command prompt untuk membuat virtual environment dan mengaktifkannya. 

- Selanjutnya saya mengkonfigurasi git agar direktori lokal dapat terhubung dengan git project dengan perintah git init.

- Kemudian, saya menambahkan berkas bernama requirements.txt pada direktori "heritage-craft" dan menambahkan dependencies pada berkas requirements.txt. Kemudian saya memasang dependencies tersebut dan membuat proyek Django baru dengan nama "heritage_craft" dengan perintah django-admin startproject heritage_craft . . 

- Setelah itu saya membuat repositori baru di github agar dapat dihubungkan dengan direktori lokal. Repositori baru ini saya namakan heritage-craft

- Setelah itu saya menambahkan ALLOWED_HOSTS di settings.py menjadi ["localhost", "127.0.0.1"] yang berfungsi sebagai daftar host yang diizinkan untuk mengakses aplikasi web.

- Sebelum dapat menghubungkan ke github saya membuat branch utama baru dengan menjalankan perintah git branch -M main dan kemudian menghubungkan direktori lokal dengan repositori dengan perintah git remote add origin https://github.com/naamiraa/heritage-craft.git

- Saya mengecek apakah project yang telah saya rencanakan berjalan maka saya mengaktifkan environment dan python manage.py runserver di direktori proyek untuk menjalankan server. Saya mengakses http://localhost:8000 yang terdapat animasi rocket yang berarti proyek Django telah berhasil dibuat. Ctrl+C untuk menghentikan server.

- Setelah memastikan project saya terhubung maka saya melakukan ``git add .``, ``git commit -m <komentar>`` , dan ``git push -u origin main`` untuk menyimpan isi direktori lokal ke github

# MEMBUAT APLIKASI DENGAN NAMA MAIN PADA PROYEK HERITAGE_CRAFT
- Pertama - tama saya menjalankan perintah ``"python manage.py startapp main"`` pada proyek heritage_craft untuk membuat aplikasi baru. 

- Kemudian saya mendaftarkan aplikasi main tersebut ke proyek dengan cara menambahkan `main` ke dalam daftar INSTALLED_APPS pada berkas ``settings.py`` dalam direktori heritage_craft

# MELAKUKAN ROUTING PADA PROYEK AGAR DAPAT MENJALANKAN APLIKASI MAIN
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main yaitu mengedit berkas `urls.py` pada direktori heritage_craft dan mengimpor fungsi include dari django.urls

- Kemudian menambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns

```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
]
```

# MEMBUAT MODEL PADA APLIKASI MAIN DENGAN NAMA PRODUCT 
- untuk membuat model pada aplikasi main dengan nama ``product`` dan memiliki atribut wajib yaitu ``name``, ``price``, dan ``description`` serta menambahkan beberapa atribut yang saya inginkan, langkah pertama adalah membuka berkas ``models.py`` pada direktori aplikasi ``main`` dan isi berkas tersebut dengan kode berikut

```python
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    # Kain batik, ulos, tenun, & berbagai kerajinan tangan
    category = models.CharField(max_length=100)
    # daerah asal
    place_of_origin = models.CharField(max_length=100)
    # tanggal penambahan produk
    date = models.DateField(auto_now_add=True)
```

- Karena saya memodifikasi berkas ``models.py`` maka selanjutnya saya melakukan migrasi skema model ke database Django dengan menggunakan perintah ``python manage.py makemigrations`` untuk persiapan migrasi dan ``python manage.py migrate`` untuk menerapkan skema model.

# MEMBUAT SEBUAH FUNGSI PADA VIEWS.PY UNTUK DIRETURN KE DALAM SEBUAH TEMPLATE HTML YANG MENAMPILKAN NAMA APLIKASI SERTA NAMA DAN KELAS
- Langkah yang saya lakukan adalah dengan membuka berkas ``views.py`` yang ada di dalam aplikasi main dan menambahkan kode berikut:
```python
from django.shortcuts import render
kemudian menambahkan fungsi show_main:
def show_main(request):
    context = {
        'name': 'Namira Aulia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```

- Kemudian pada berkas ``main.html`` yang ada di dalam direktori templates saya menambahkan nama app, npm, nama, dan class menjadi struktur Django yang sesuai untuk menampilkan data

# MEMBUAT ROUTING PADA URLS.PY PADA APLIKASI MAIN UNTUK MEMETAKAN FUNGSI YANG TELAH DICREATE PADA VIEWS.PY
- Membuat sebuah routing pada ``urls.py`` di aplikasi main untuk memetakan ungsi yang telah dibuat pada ``views.py``. Saya membuat file ``urls.py`` di dalam direktori ``main`` dan mengisinya dengan kode berikut:
```python
from django.urls import path
from main.views import show_author

app_name = 'main'

urlpatterns = [
    path('', show_author, name='show_author'),
]
```

# MELAKUKAN DEPLOYMENT KE PWS
Sebelum melakukan deployment ke PWS terlebih dulu syaa melakukan perintah python manage.py runserver yang kemudian dibuka pada http://localhost:8000/main untuk memastikan web dapat diakses. Kemudian saya memulai proses deployment pada PWS dengan langkah berikut:
1. Karena saya telah memiliki akun pada PWS langkah pertama yang saya lakukan hanyalah memulai dengan 'create new project'
2. Memberi project name kemudian klik create new project
3. Menyimpan informasi project credentials dan project command
4. Pada ``settings.py`` di proyek Django, saya menambahkan URL deployment pada ``ALLOWED_HOSTS`` yaitu namira-aulia31-heritagecraft.pbp.cs.ui.ac.id
5. Menjalankan perintah yang terdapat pada project command halaman PWS
6. Menjalankan perintah ``git branch -M main`` untuk kembali mengubah nama branch ke main
7. Menunggu status deployment hingga success


2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

- Pertama client akan mengirimkan permintaan (HTTP Request) melalui melalui browser untuk mengakses halaman web, lalu permintaan ini akan diteruskan ke sistem routing yang dikelola Django untuk mencari pola URL yang sesuai dengan request tersebut. 
- Setelah menemukan pola URL yang cocok, Django akan memanggil fungsi yang terkait dalam berkas views.py.
- Setelah itu, views.py akan mengatur berbagai macam bentuk interaksi agar di dalam models.py dapat mengelola dan menyajikan data yang telah diolah oleh models.py dapat ditampilkan pada templates dalam berkas html. 
- Setelah semua operasi selesai, fungsi yang sesuai dalam berkas views.py akan menghasilkan halaman web yang diminta oleh client dalam formt HTML yang dapat disebut dengan template
- Berkas HTML akan disimpan dalam direktori ``templates``  untuk penggunaan selanjutnya
- Browser client akan merender berkas HTML ini sebagai respons (HTTP Response) dari server Django sehingga menghasilkan tampilan yang sesuai yang dapat dilihat oleh user.


3. Fungsi git dalam pengembangan perangkat lunak
Fungsi git dalam pengembangan perangkat lunak adalah:
- Versioning: Git menyimpan versi dari setiap perubahan yang dilakukan pada kode sehingga memudahkan developer untuk melacak perubahan
- Kolaborasi: Git memungkinkan kolaborasi antar developer dengan sistem branch dan merge untuk dapat mengintegrasikan pekerjaan masing - masing
- Backup: Jika terjadi kesalahan, git memungkinkan developer untuk dapat kembali ke versi kode sebelumnya (versi kode yang sesuai)


4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django menyediakan banyak fitur bawaan (seperti ORM, admin interface, dan form handling), yang mempermudah pemula memulai proyek tanpa memerlukan banyak konfigurasi eksternal.
- Django memiliki struktur yang jelas dan tergorganisir sehingga sesuai untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak



5. Mengapa model pada Django disebut sebagai ORM?
Alasan model pada Django disebut sebagai ORM adalah karena Django memungkinkan untuk berinteraksi dengan database. Pada Django, ORM ini mampu menghubungkan  objek Python secara langsung ke tabel - tabel dalam database dan secara otomatis menangani query SQL di balik layar sehingga developer tidak perlu menulis query SQL secara manual
