# si __init__.py ini tu gunanya buat pintu masuuk library kita
# jadi kalo kita import toko_utils, dia bakal masuk ke __init__.py dulu, baru dia tau mau ngambil apa
# import semua fungsi agar bisa dipakai langsung

from .hitung import hitung_diskon, hitung_total, hitung_pajak
from .format import format_rupiah, format_struk

# Apakah Namanya Harus __init__.py?
#Ya, harus persis __init__.py. Ini bukan nama bebas, ini sudah aturan baku Python.
#Alasannya: Python secara otomatis mencari file bernama __init__.py 
# di dalam sebuah folder untuk mengenalinya sebagai package (library). 
# Kalau namanya diganti jadi init.py, library.py, atau apapun — Python tidak akan mengenalinya sebagai package dan import toko_utils akan error.
