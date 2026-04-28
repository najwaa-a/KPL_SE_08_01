## Pegawai.py
```python
class Pegawai:
```
Ini deklarasi class, gak ada kurung berarti dia gak punya parent — dia **induk utama**.

```python
def __init__(self, idPegawai: str, nama: str):
```
Constructor — dijalankan otomatis waktu bikin objek baru. `self` itu referensi ke objek itu sendiri.

```python
self.__idPegawai = idPegawai
self.__nama = nama
self.__alamat = ""
self.__noTelepon = ""
self.__statusAktif = False
```
Ini ngisi atribut-atributnya. `idPegawai` dan `nama` diisi dari parameter, sisanya dikasih nilai default dulu karena di diagram memang gak ada di constructor.

```python
def tampilkanData(self):
    pass
def hitungGaji(self) -> float:
    pass
def ubahStatus(self, status: bool):
    pass
```
Method-method yang dimiliki semua pegawai. `pass` artinya kosong dulu, nanti diisi. `-> float` artinya method ini nantinya harus return angka desimal.

---

## TenagaKependidikan.py
```python
class TenagaKependidikan(Pegawai):
```
Kurung `(Pegawai)` artinya dia **inherit dari Pegawai** — dia adalah child dari Pegawai.

```python
def __init__(self, idPegawai: str, nama: str, unitKerja: str):
    super().__init__(idPegawai, nama)
```
`super().__init__()` manggil constructor Pegawai dulu, ngoper `idPegawai` dan `nama` ke sana biar ke-isi.

```python
self.__unitKerja = unitKerja
self.__shiftKerja = ""
```
Baru setelah parent beres, dia nambahin atribut spesifik miliknya sendiri.

---

## Dosen.py
```python
class Dosen(Pegawai):
```
Dosen langsung inherit dari Pegawai, **bukan** dari TenagaKependidikan.

```python
def __init__(self, idPegawai: str, nama: str, nidn: str):
    super().__init__(idPegawai, nama)
    self.__nidn = nidn
    self.__bidangKeahlian = ""
    self.__jumlahSKS = 0
```
Sama polanya — panggil parent dulu, terus tambahin atribut khusus dosen.

```python
def mengajar(self, mataKuliah: str):
    pass
def membimbingMahasiswa(self, namaMahasiswa: str):
    pass
```
Method khusus dosen yang gak dimiliki pegawai lain.

---

## StaffAdministrasi.py
```python
class StaffAdministrasi(Pegawai):
```
Sama kayak Dosen, langsung inherit dari Pegawai.

```python
self.__bagian = bagian
self.__jamKerja = 0
```
Atribut spesifik admin — bagian mana dia kerja dan berapa jam kerjanya.

```python
def kelolaSurat(self):
    pass
def inputDataAkademik(self):
    pass
```
Method yang cuma dimiliki staff admin.

---

## Laboran.py
```python
class Laboran(TenagaKependidikan):
```
Laboran inherit dari **TenagaKependidikan**, bukan langsung dari Pegawai. Jadi dia dapat warisan dari dua tingkat sekaligus.

```python
def __init__(self, idPegawai: str, nama: str, unitKerja: str):
    super().__init__(idPegawai, nama, unitKerja)
```
`super().__init__()` di sini manggil TenagaKependidikan, yang mana TenagaKependidikan juga manggil Pegawai — jadi berantai ke atas otomatis.

```python
self.__namaLaboratorium = ""
self.__jumlahPeralatan = 0
```
Atribut spesifik laboran.

---

## Pustakawan.py
```python
class Pustakawan(TenagaKependidikan):
```
Sama kayak Laboran, inherit dari TenagaKependidikan.

```python
self.__kodePerpustakaan = ""
self.__jumlahBukuDikelola = 0
```
Bedanya cuma di atribut spesifiknya — urusan perpustakaan.

```python
def mengelolaPeminjamanBuku(self):
    pass
def mengaturKatalogBuku(self):
    pass
```
Method khusus pustakawan yang gak dimiliki class lain.

---

Intinya polanya sama semua — **panggil super() dulu, baru tambahin milik sendiri**. Makin ke bawah hierarkinya, makin banyak atribut yang dia punya karena numpuk dari parent-parentnya. 😄