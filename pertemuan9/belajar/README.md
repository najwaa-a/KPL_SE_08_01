# Belajar Library Construction

### Apa itu Code Reuse?
Code Reuse adalah praktik menggunakan kembali kode yang sudah ada untuk membangun perangkat lunak baru, tanpa menulis ulang dari nol.  
Manfaatnya:
1. Menghemat waktu dan tenaga pengembangan
2. Mengurangi kemungkinan bug (kode yang sudah teruji)
3. Meningkatkan konsistensi antar proyek
4. Mempermudah pemeliharaan (maintenance)

### Apa itu Library?
Library (pustaka) adalah kumpulan kode yang sudah ditulis dan dikemas, yang bisa digunakan ulang oleh program lain.   
Library berisi fungsi, kelas, atau modul yang siap pakai tanpa perlu tahu cara kerja dalamnya (abstraksi).

### Library Construction (Membangun Library)
Bagaimana cara membuat library sendiri.  
Langkah-langkah umum:
1. Identifikasi kode yang bisa di-reuse — fungsi/kelas yang sering dipakai berulang
2. Modularisasi — pisahkan kode menjadi unit-unit mandiri
3. Buat antarmuka (API/interface) yang jelas — pengguna library tidak perlu tahu implementasi dalamnya
4. Dokumentasi — tulis cara penggunaan (docstring, README)
5. Packaging & distribusi — kemas agar bisa diinstall/diimpor orang lain

### Alat untuk mengunduh dan mengelola library secara otomatis:
1. Python -> pip
2. JavaScript -> npm/yarn
3. Java -> Maven/Gradle
4. PHP -> Composer
5. Rust -> Cargo

### Rangkuman Singkat untuk Hafalan
```
-> Library = kumpulan kode siap pakai. 
-> Code Reuse = pakai ulang kode biar efisien. 
-> Library Construction = proses merancang, memodularisasi, mendokumentasi, dan mengemas kode agar bisa digunakan orang lain. 
-> Prinsip utama: high cohesion, low coupling, dokumentasi jelas, versioning.
```


### Contoh Proyek: 
# toko_utils — Library Python Sederhana
 
> Library Python untuk kalkulasi harga dan format tampilan toko/kasir.  
> lalu kita import Library yang sudah kita buat ke file utama kita yaitu `main.py`
 
---
 
## Struktur Proyek
 
```
toko_utils/
│
├── toko_utils/
│   ├── __init__.py       ← pintu masuk library (wajib ada)
│   ├── hitung.py         ← modul kalkulasi harga
│   └── format.py         ← modul format tampilan
│
└── main.py               ← file utama yang memakai library
```
 
---
 
## Cara Menjalankan
 
### 1. Pastikan Python sudah terinstall
 
Buka terminal / CMD, lalu ketik:
 
```bash
python --version
```
 
Jika muncul versi Python (misal `Python 3.11.0`), berarti sudah siap.
 
### 2. Clone atau buat folder proyek
 
Buat struktur folder seperti di atas, lalu isi setiap file dengan kode yang tersedia.
 
### 3. Jalankan file utama
 
Masuk ke folder proyek terlebih dahulu:
 
```bash
cd path/ke/folder/proyek
```
 
Kemudian jalankan:
 
```bash
python main.py
```
 
### 4. Output yang diharapkan
 
```
==============================
  STRUK PEMBELIAN
==============================
Barang  : Laptop Asus
Harga   : Rp 8.000.000
Diskon  : 20%
------------------------------
TOTAL   : Rp 7.128.000
==============================
```
 
---
 
## Penjelasan Setiap File
 
### `__init__.py`
 
File wajib yang menjadikan folder `toko_utils` sebagai **Python Package**.  
Berisi import dari semua modul agar pengguna cukup menulis `import toko_utils`.
 
```python
from .hitung import hitung_diskon, hitung_total, hitung_pajak
from .format import format_rupiah, format_struk
```
-> Apakah Namanya Harus __init__.py?
Ya, harus persis __init__.py. Ini bukan nama bebas, ini sudah aturan baku Python.  
Alasannya: Python secara otomatis mencari file bernama __init__.py di dalam sebuah folder untuk mengenalinya sebagai package (library).  
Kalau namanya diganti jadi init.py, library.py, atau apapun — Python tidak akan mengenalinya sebagai package dan import toko_utils akan error.

 
### `hitung.py`
 
Modul yang bertanggung jawab atas semua **kalkulasi angka**.  
Menerapkan prinsip *high cohesion* — satu file, satu tanggung jawab.
 
| Fungsi | Parameter | Keterangan |
|---|---|---|
| `hitung_diskon(harga, persen)` | harga asli, % diskon | Menghitung harga setelah diskon |
| `hitung_pajak(harga, persen)` | harga, % pajak (default 11%) | Menghitung nilai pajak |
| `hitung_total(harga, diskon, pajak)` | harga, % diskon, % pajak | Menghitung total akhir |
 
### `format.py`
 
Modul yang bertanggung jawab atas **tampilan output**.  
Dipisah dari `hitung.py` karena beda tanggung jawab (*separation of concerns*).
 
| Fungsi | Parameter | Keterangan |
|---|---|---|
| `format_rupiah(angka)` | angka | Mengubah angka ke format `Rp 8.000.000` |
| `format_struk(nama, harga, diskon, total)` | data barang | Mencetak struk belanja |
 
### `main.py`
 
File utama yang **memakai** library. File ini tidak perlu tahu cara kerja dalam library — cukup import dan gunakan. Inilah manfaat utama library: **abstraksi**.
 
---
 
## Konsep yang Diterapkan
 
| Konsep | Penerapan dalam Proyek |
|---|---|
| **Code Reuse** | Fungsi `hitung_diskon` dan `format_rupiah` bisa dipakai di mana saja |
| **Modularisasi** | Kode dibagi ke beberapa file berdasarkan fungsinya |
| **High Cohesion** | `hitung.py` hanya berisi fungsi kalkulasi, `format.py` hanya berisi fungsi tampilan |
| **Low Coupling** | `format.py` dan `hitung.py` tidak saling bergantung satu sama lain |
| **Abstraksi** | `main.py` tidak perlu tahu cara kerja dalam fungsi, cukup memanggilnya |
 
---
 
## Cara Menggunakan Library di File Lain
 
```python
# Import seluruh library
import toko_utils
 
total = toko_utils.hitung_total(10_000_000, diskon=15)
print(toko_utils.format_rupiah(total))
```
 
```python
# Import fungsi spesifik saja
from toko_utils import hitung_diskon, format_rupiah
 
harga_diskon = hitung_diskon(50_000, 10)
print(format_rupiah(harga_diskon))
```
