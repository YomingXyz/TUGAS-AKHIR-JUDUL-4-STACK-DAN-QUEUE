A. PROGRAM MANAJEMEN RIWAYAT STOK (SITOSERBA) MENGGUNAKAN STACK ARRAY

B. Deskripsi Singkat
Program ini berfungsi sebagai fitur pencatatan dan pengelolaan riwayat masuknya barang, yang sangat cocok diimplementasikan pada sistem manajemen minimarket seperti SiToserba. Program ini memanfaatkan struktur data Stack (Tumpukan) dengan menggunakan list 1 dimensi (Array) statis. Prinsip utama yang berjalan di sini adalah LIFO (*Last In, First Out*), di mana catatan stok yang baru saja dimasukkan akan berada di urutan paling atas.

Program dilengkapi dengan fitur utama stack yaitu `push` (untuk menambah catatan), `pop` (untuk membatalkan/undo input terakhir), `peek` (melihat catatan paling baru), dan `display` (melihat keseluruhan riwayat). Untuk mencegah terjadinya *crash* saat program berjalan, menu input juga sudah dibungkus dengan validasi `try-except` sehingga jika pengguna memasukkan selain angka pada menu pilihan, program akan tetap berjalan dan memberikan peringatan.

C. Source Code


Penjelasan kode per baris:

* membuat `class StackArray:` sebagai cetak biru struktur data tumpukan
* membuat fungsi inisialisasi `def __init__(self, max_size=100):` dengan ukuran maksimal array *default* 100
* menyimpan batas maksimal tersebut ke dalam variabel `self.MAX`
* menyiapkan list `self.st = [None] * self.MAX` dengan ukuran `MAX` yang isinya masih kosong (`None`)
* menginisialisasi pointer `self.top_idx = -1` sebagai penanda bahwa tumpukan riwayat masih kosong
* membuat fungsi `is_empty(self):` untuk mengecek apakah stack sedang kosong
* mengembalikan nilai `True` jika `top_idx` bernilai -1
* membuat fungsi `is_full(self):` untuk mengecek apakah stack sudah mencapai batas penuh
* mengembalikan nilai `True` jika `top_idx` mencapai batas akhir indeks array (`MAX - 1`)
* membuat fungsi `push(self, x):` untuk menambahkan data `x` ke riwayat stok
* pengondisian `if self.is_full():` untuk mencegah penambahan jika riwayat penuh
* mencetak teks peringatan "Riwayat penuh!" lalu menggunakan `return` untuk menghentikan fungsi
* menaikkan nilai pointer dengan `self.top_idx += 1`
* menyimpan inputan teks `x` ke dalam array `st` tepat pada indeks `top_idx`
* mencetak konfirmasi "Catatan [...] berhasil ditambahkan." ke layar
* membuat fungsi `pop(self):` untuk membatalkan (undo) catatan stok terakhir
* pengondisian `if self.is_empty():` untuk mengecek jika riwayat masih kosong
* mencetak pesan error dan `return` agar proses pembatalan terhenti
* mencetak informasi data apa yang berhasil dibatalkan/dihapus dari indeks teratas
* menurunkan nilai indeks `self.top_idx -= 1` agar data teratas saat ini diabaikan dari tumpukan
* membuat fungsi `peek(self):` untuk melihat catatan stok teratas tanpa menghapusnya
* mengecek kekosongan riwayat menggunakan `is_empty()`
* menampilkan nilai dari `self.st[self.top_idx]` jika riwayat ada isinya
* membuat fungsi `display(self):` untuk menampilkan seluruh daftar riwayat stok
* melakukan perulangan `for` mundur dari nilai `top_idx` hingga ke angka 0 (batas -1)
* mencetak setiap elemen array `self.st[i]` dari urutan yang paling baru ke yang paling lama
* membuat fungsi `main():` sebagai pengatur antarmuka menu terminal
* membuat objek `riwayat_stok` dari class `StackArray`
* menyiapkan variabel `pilih = 0` untuk menampung input menu
* membuat perulangan `while pilih != 5:` agar menu terus muncul selama user tidak memilih keluar
* mencetak teks pilihan menu 1 sampai 5
* menggunakan blok `try` untuk meminta input `int(input(...))` dari user
* menangkap error dengan `except ValueError:` jika input bukan berupa angka, lalu mencetak peringatan dan menggunakan `continue` untuk mengulang menu
* pengondisian berantai `if`, `elif`, dan `else` untuk menjalankan aksi sesuai angka menu yang diinput
* jika user memilih menu 1, program meminta input string `val = input(...)` berisi data stok
* program memasukkan `val` ke dalam stack dengan memanggil `riwayat_stok.push(val)`
* menu 2 akan memanggil `riwayat_stok.pop()`
* menu 3 akan memanggil `riwayat_stok.peek()`
* menu 4 akan memanggil `riwayat_stok.display()`
* memastikan program utama berjalan dengan `if __name__ == "__main__":` lalu memanggil fungsi `main()`

D. Output Program

Penjelasan Output:
Saat program dijalankan, akan muncul antarmuka menu Manajemen Riwayat Stok. Pertama, user menginputkan angka "1" untuk mencatat stok masuk. Program lalu meminta deskripsi data stok, dan user mengetikkan "Tambah 12 Teh Pucuk". Program merespons dengan menampilkan pesan "Catatan [Tambah 12 Teh Pucuk] berhasil ditambahkan.". Kemudian user memilih menu "1" lagi dan memasukkan data kedua: "Masuk 50 pcs Indomie Goreng". Setelah itu, user memilih menu "4" untuk mengecek keseluruhan data. Program secara berurutan mencetak riwayat dari yang terbaru ke yang paling lama, yaitu Indomie Goreng di urutan teratas disusul Teh Pucuk di bawahnya.

Karena user menyadari ada salah input pada data terakhir, user memilih menu "2" (Batal Catat/Undo). Program langsung merespons dengan membatalkan catatan Indomie Goreng tanpa menghapus Teh Pucuk. Hal ini dibuktikan ketika user memilih menu "3" (Cek Riwayat Terakhir), program menampilkan bahwa riwayat terakhir yang berada di puncak tumpukan saat ini adalah "Tambah 12 Teh Pucuk". Terakhir, user menginputkan angka "5" dan program pun selesai dijalankan.

E. Link youtube
[https://youtu.be/7jyQuzIOrmw?si=o1Ja_B7Iy2sUm54g](https://youtu.be/7jyQuzIOrmw?si=o1Ja_B7Iy2sUm54g)
