# heritage-craft
Nama: Namira Aulia
Tautan PWS: [heritagecraft](http://namira-aulia31-heritagecraft.pbp.cs.ui.ac.id/)


## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step
## Membuat proyek django baru
- Langkah pertama yang saya lakukan untuk mengimplementasikan checklist tugas 1 ini adalah mulai dari ``membuat direktori baru`` di lokal dengan nama "heritage-craft" kemudian direktori "heritage-craft" tersebut dibuka melalui command prompt untuk membuat virtual environment dan mengaktifkannya. 

- Selanjutnya saya mengkonfigurasi git agar direktori lokal dapat terhubung dengan git project dengan perintah ``git init``.

- Kemudian, saya menambahkan berkas bernama ``requirements.txt`` pada direktori "heritage-craft" dan menambahkan dependencies pada berkas requirements.txt. Kemudian saya memasang dependencies tersebut dan membuat proyek Django baru dengan nama "heritage_craft" dengan perintah django-admin startproject heritage_craft . . 

- Setelah itu saya membuat ``repositori baru`` di github agar dapat dihubungkan dengan direktori lokal. Repositori baru ini saya namakan heritage-craft

- Setelah itu saya menambahkan ``ALLOWED_HOSTS`` di ``settings.py`` menjadi ["localhost", "127.0.0.1"] yang berfungsi sebagai daftar host yang diizinkan untuk mengakses aplikasi web.

- Sebelum dapat menghubungkan ke github saya membuat branch utama baru dengan menjalankan perintah ``git branch -M main`` dan kemudian menghubungkan direktori lokal dengan repositori dengan perintah ``git remote add origin https://github.com/naamiraa/heritage-craft.git``

- Saya mengecek apakah project yang telah saya rencanakan berjalan maka saya ``mengaktifkan environment`` dan ``python manage.py runserver`` di direktori proyek untuk menjalankan server. Saya mengakses http://localhost:8000 yang terdapat animasi rocket yang berarti proyek Django telah berhasil dibuat. Ctrl+C untuk menghentikan server.

- Setelah memastikan project saya terhubung maka saya melakukan ``git add .``, ``git commit -m <komentar>`` , dan ``git push -u origin main`` untuk menyimpan isi direktori lokal ke github

## Membuat Aplikasi dengan nama main pada proyek heritage_craft
- Pertama - tama saya menjalankan perintah ``"python manage.py startapp main"`` pada proyek heritage_craft untuk membuat aplikasi baru. 

- Kemudian saya mendaftarkan aplikasi main tersebut ke proyek dengan cara menambahkan `main` ke dalam daftar INSTALLED_APPS pada berkas ``settings.py`` dalam direktori heritage_craft

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main yaitu mengedit berkas `urls.py` pada direktori heritage_craft dan mengimpor fungsi include dari django.urls

- Kemudian menambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns

```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
]
```

## Membuat model pada aplikasi main dengan nama Product
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

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template html yang menampilkan nama aplikasi serta nama dan kelas
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

## Membuat routing pada urls.py pada apliasi main untuk memetakan fungsi yang telah dibuat pada views.py 
- Membuat sebuah routing pada ``urls.py`` di aplikasi main untuk memetakan ungsi yang telah dibuat pada ``views.py``. Saya membuat file ``urls.py`` di dalam direktori ``main`` dan mengisinya dengan kode berikut:
```python
from django.urls import path
from main.views import show_author

app_name = 'main'

urlpatterns = [
    path('', show_author, name='show_author'),
]
```

## Melakukan deployment ke PWS
Sebelum melakukan deployment ke PWS terlebih dulu syaa melakukan perintah python manage.py runserver yang kemudian dibuka pada http://localhost:8000/main untuk memastikan web dapat diakses. Kemudian saya memulai proses deployment pada PWS dengan langkah berikut:
- Karena saya telah memiliki akun pada PWS langkah pertama yang saya lakukan hanyalah memulai dengan 'create new project'
- Memberi project name kemudian klik create new project
- Menyimpan informasi project credentials dan project command
- Pada ``settings.py`` di proyek Django, saya menambahkan URL deployment pada ``ALLOWED_HOSTS`` yaitu namira-aulia31-heritagecraft.pbp.cs.ui.ac.id
- Menjalankan perintah yang terdapat pada project command halaman PWS
- Menjalankan perintah ``git branch -M main`` untuk kembali mengubah nama branch ke main
- Menunggu status deployment hingga success


## 2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](static/images/MVT.png)

- Pertama client akan mengirimkan permintaan (HTTP Request) melalui melalui browser untuk mengakses halaman web, lalu permintaan ini akan diteruskan ke sistem routing yang dikelola Django untuk mencari pola URL yang sesuai dengan request tersebut. 
- Setelah menemukan pola URL yang cocok, Django akan memanggil fungsi yang terkait dalam berkas views.py.
- Setelah itu, views.py akan mengatur berbagai macam bentuk interaksi agar di dalam models.py dapat mengelola dan menyajikan data yang telah diolah oleh models.py dapat ditampilkan pada templates dalam berkas html. 
- Setelah semua operasi selesai, fungsi yang sesuai dalam berkas views.py akan menghasilkan halaman web yang diminta oleh client dalam formt HTML yang dapat disebut dengan template
- Berkas HTML akan disimpan dalam direktori ``templates``  untuk penggunaan selanjutnya
- Browser client akan merender berkas HTML ini sebagai respons (HTTP Response) dari server Django sehingga menghasilkan tampilan yang sesuai yang dapat dilihat oleh user.


## 3. Fungsi git dalam pengembangan perangkat lunak
Fungsi git dalam pengembangan perangkat lunak adalah:
- Versioning: Git menyimpan versi dari setiap perubahan yang dilakukan pada kode sehingga memudahkan developer untuk melacak perubahan
- Kolaborasi: Git memungkinkan kolaborasi antar developer dengan sistem branch dan merge untuk dapat mengintegrasikan pekerjaan masing - masing
- Backup: Jika terjadi kesalahan, git memungkinkan developer untuk dapat kembali ke versi kode sebelumnya (versi kode yang sesuai)


## 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django menyediakan banyak fitur bawaan (seperti ORM, admin interface, dan form handling), yang mempermudah pemula memulai proyek tanpa memerlukan banyak konfigurasi eksternal.
- Django memiliki struktur yang jelas dan tergorganisir sehingga sesuai untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak



## 5. Mengapa model pada Django disebut sebagai ORM?
Alasan model pada Django disebut sebagai ORM adalah karena Django memungkinkan untuk berinteraksi dengan database. Pada Django, ORM ini mampu menghubungkan  objek Python secara langsung ke tabel - tabel dalam database dan secara otomatis menangani query SQL di balik layar sehingga developer tidak perlu menulis query SQL secara manual



# (TUGAS 3)
## 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengimplementasian platfrom, data delivery (pengiriman data) adalah aspek yang penting karena sebuah platform biasanya terhubung dengan berbagai client (seperti web atau mobile app) dan server. Platform sering melibatkan beberapa layanan atau komponen yang memerlukan pertukaran data, seperti antara frontend dan backend, atau dari aplikasi ke database. Proses data delivery memungkinkan komunikasi antara client dan server, sehingga data seperti produk apa saja yang tersedia di ecommerce ini dapat dikirim dan diterima secara efisien. Selain itu, di masa modern sekarang sangat dibutuhkan aplikasi yang berbasis real-time artinya kebutuhan akan data delivery yang cepat dan akurat menjadi sangat penting untuk menjaga performa platform.

## 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON (JavaScript Object Notation) dan XML (eXtensible Markup Language) adalah dua format pertukaran data yang banyak digunakan. Berdasarkan sumber yang saya baca, berikut adalah perbandingan antara XML dan JSON:
1. XML
    - XML lebih kompleks karena memiliki struktur dengan elemen - elmen yang lebih panjang
    - XML lebih fleksibel karena bisa mengakomodasi format data yang lebih kompleks (misalnya data dengan atribut)
    - XML bisa menggabungkan skema untuk validasi data
2. JSON
    - JSON lebih mudah dibaca dan sedergana karena struktur datanya lebih ringkas dan mirip dengan objek JavaSCript
    - JSON sering kali lebih efisien dalam hal ukuran data yang dikirim karena tidak menggunakan tag penutup seperti XML
    - JSON diintegrasikan secara native dengan JavaSCript yang menjadikannya lebih cepat dan praktis dalam aplikasi web modern
Berdasarkan perbandingan di atas, menurut saya JSON lebih baik salah satu alasannya karena JSON lebih mudah dibaca dan ditulis, baik oleh mesin maupun manusia, karena menggunakan format key-value yang langsung. XML menggunakan tag yang lebih kompleks. Namun, XML masih relevan untuk kasus di mana diperlukan fitur-fitur seperti validasi skema (XML Schema) atau ketika menangani data dengan struktur yang sangat kompleks.

JSON lebih populer karena sederhana dan lebih mudah diproses di sisi client (khususnya di aplikasi web yang banyak menggunakan JavaScript). JSON juga lebih hemat dalam ukuran file dan lebih mudah dibaca oleh manusia dibandingkan dengan XML. Dalam aplikasi web dan API modern, JSON lebih disukai karena lebih mudah di-parse oleh mesin dan lebih mudah diintegrasikan dalam berbagai bahasa pemrograman.

## 3. Fungsi dari method ``is_valid()`` pada form DJango dan mengapa membutuhkan method tersebut?
Method ``is_valid()`` pada form Django digunakan untuk memvalidasi data yang diinput oleh pengguna. Fungsi ini akan mengecek apakah semua data yang diisi di form memenuhi kriteria validasi yanng telah ditentukan seperti apakah tipe data sesuai, apakah ada field yang belum terisi. 

Kita memerlukan ``is_valid()`` untuk memastikan bahwa data yang dikirim ke aplikasi adalah benar dan sesuai sebelum diolah lebih lanjut. Hal ini perlu untuk mencegah kesalahan dalam aplikasi yang disebabkan data yang tidak valid. Jika data tidak valid, Django akan secara otomatis mengembalikan pesan kesalahan yang dapat digunakan untuk memberi tahu pengguna tentang apa yang salah.

## 4. Mengapa kita membutuhkan ``csrf_token`` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan ``csrf_token`` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Forgery) adalah serangan di mana penyerang bisa membuat pengguna yang sudah terautentikasi melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka, seperti mengirimkan permintaan berbahaya ke server. ``csrf_token`` diperlukan pada form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). ``csrf_token`` memastikan bahwa form yang di-submit berasal dari sumber yang sah (pengguna aplikasi itu sendiri) dan bukan dari situs atau sumber berbahaya. Dengan adanya token ini, server dapat memverifikasi bahwa permintaan POST atau perubahan data berasal dari pengguna yang sah dan bukan dari pihak luar yang berbahaya.

Jika form tidak dilindungi oleh ``csrf_token``, penyerang dapat memanfaatkan form tanpa token untuk memodifikasi data, menghapus informasi, atau melakukan tindakan yang menguntungkan penyerang, seperti mencuri uang atau informasi.

Penyerang dapat mengirim permintaan dari situs eksternal atau skrip yang menyebabkan pengguna secara tidak sengaja melakukan aksi di situs yang mereka kunjungi, seperti mentransfer uang atau menghapus data, tanpa menyadari tindakan tersebut. Dengan adanya ``csrf_token``, setiap permintaan POST dari form harus menyertakan token unik yang hanya diketahui oleh server dan client yang sah. Jika token ini tidak ada atau tidak cocok, permintaan akan dianggap tidak valid dan ditolak, sehingga melindungi aplikasi dari serangan CSRF.


## 5. Cara mengimplementasikan checklist tugas secara step - by step
1. Memastikan struktur direktori & repositori heritage-craft sudah sesuai 
2. Membuat skeleton terlebih dahulu sebagai kerangka views dengan cara membuat direktori ``template`` pada ``root folder`` dan menambahkan berkas baru bernama ``base.html`` serta mengisinya dengan kode yang telah dijelaskan pada tutorial 2
3. Membuka settings.py dan menambahkan kode berikut agar berkas ``base.html`` terdeteksi sebagai templates
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
```
3. Memperbarui isi file ``main.html`` yang ada pada direktori main agar menggunakan ``base.html`` sebagai template utama
4. Mengubah primary key dari integer menjadi UUID pada ``models.py`` agar mencegah adanya kerentanan terhadap keamanan aplikasi
5. Melakukan migrations karena terdapat perubahan pada ``models.py``
6. Membuat form input data dan menampilkan product pada HTML dengan cara berikut:
    - Pertama saya membuat berkas baru pada direktori ``main`` dengan nama ``forms.py`` untuk membuat struktur form yang dapat menerima data Product baru. 
    - Menambahkan import redirect pada file ``views.py`` 
    - Saya juga menambahkan function baru dengan nama ``create_product_entry`` yang menerima parameter ``request`` pada berkas ``views.py``. 
    - Mengubah fungsi ``show_main`` yang ada pada file ``views.py`` dengan menambahkan variabel ``product_entries``valuenya adalah ``Product.objects.all()`` yang digunakan untuk mengambil seluruh objek ``Product`` yang tersimpan pada database
    - Membuka ``urls.py`` pada direktori ``main`` dan import fungsi create_product_entry yang telah saya buat sebelumnya dan menambahkan path tersebut ke ``urlpatterns`` pada ``urls.py``
    - Membuat berkas HTML baru dengan nama ``create_product_entry`` pada direktori ``main/templates`` dan mengisi kode dengan block untuk form dengan metode POST, token, template tag yang digunakan untuk menampilkan fields form yang sudah dibuat tadi, dan juga tombol submit untuk kirim request ke view ``create_product_entry(request)``
    - Menambahkan kode dalam block contect main.html untuk menampilkan data product dalam bentuk tabel serta tombol "Add New Product Entry"
    - Setelah itu tentunya saya mencoba menjalankan perintah runserver untuk mengecek apakah aplikasi dapat berjalan sesuai rencana awal. Karena bentuk aplikasi sudah sesuai rencana maka saya menambahkan 3 data product baru dan data yang saya input berhasil ditampilkan pada halaman utama aplikasi
    - Melakukan git add, commit, push 
7. Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID dan membuat routing URl untuk masing - masing views dengan langkah berikut:
    - Menambahkan import ``HttpResponse`` dan ``Serializer`` pada bagian paling atas berkas ``views.py``
    - Membuat function baru yang menerima parameter request dengan nama ``show_XML`` dan membuat sebuah variabel yang menyimpan query dari seluruh data yang ada pada ``Product`` seperti berikut:
    ```python
            {
                def show_xml(request):
                    data = MoodEntry.objects.all()
                    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            }
    ```
    - Menambahkan import fungsi yang telah dibuat (show_XML) ke dalam ``urls.py`` dan menambahkan path url ke dalam ``urlpatterns`` seperti berikut:
        ```python
            {
            ...
            path('xml/', show_xml, name='show_xml'),
            ...
            }
        ```
    - Coba menjalankan proyek Django dengan perintah ``python manage.py runserver`` dan membuka local host yang ditambahkan path xml/ serta memastikan data yang ada sesuai dengan objek yang telah saya tambahkan sebelumnya
    - Saya melakukan hal yang sama (mulai bullet 2 - 4) untuk format JSON dengan menyesuaikan nama function, variabel, contect_type, serta path yang digunakan agar sesuai dengan ketentuan format JSON
    - Untuk format XML_by_ID dan JSON_by_ID saya menambahkan parameter pada functionnya yaitu menjadi ``def show_xml_by_id(request, id)``
    - Saya juga mengubah method yang digunakan pada variabel data menjadi  ``data = Product.objects.filter(pk=id)`` 
    - Import fungsi ``show_xml_by_id`` dan ``show_json_by_id`` pada ``urls.py`` dan juga menambahkan path URL ke ``urlpatterns``
    - Cek proyek Django dengan runserver
8. Menggunakan Postman sebagai Data Viewer
    - Setelah saya memastikan proyek sudah berjalan aman di localhost, selanjutnya saya mencoba cek url dengan mengirimkan request baru dengan method get ke postman untuk mengetes apakah data terkirimkan dengan baik
    - Memastikan data yang ditampilkan sesuai ketika jalan di localhost
    - Screenshot untuk masing - masing request URL dan menyimpan screenshot tersebut di folder ``static/images`` agar dapat dengan mudah ditambahkan pada README.md
9. Melakukan ``add-commit-push`` ke github

## Screenshot hasil akses URL dalam format XML pada Postman
![](static/images/XML.png)

## Screenshot hasil akses URL dalam format JSON pada Postman
![](static/images/JSON.png)

## Screenshot hasil akses URL dalam format XML_by_ID pada Postman
![](static/images/XML_by_ID.png)

## Screenshot hasil akses URL dalam format JSON_by_ID pada Postman
![](static/images/JSON_by_ID.png)