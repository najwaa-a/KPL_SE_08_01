# disini dia adalah file utama yang memakai library yang sudah kita buat di folder toko_utils

import toko_utils # ini kita panggil library toko_utils yang sudah kita buat, jadi kita bisa pakai semua fungsi yang ada di dalamnya, misal hitung_total, format_struk, dll

# disini kita tinggal isi data nya
nama = "sepatu nice"
harga = 8_000_000
diskon = 20 

# terus kita hitung total harga setelah diskon dan pajak, dengan memanggil fungsi hitung_total dari library toko_utils
total = toko_utils.hitung_total(harga, diskon=diskon)

# terakhir kita cetak struknya dengan memanggil fungsi format_struk dari library toko_utils
toko_utils.format_struk(nama, harga, diskon, total)



