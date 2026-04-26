# di file ini kita bakalan bikin modul buat kalkulasi harga
# tanggung jawab: semua perhitungan angka -> maksudnya adalah semua fungsi yang berhubungan dengan perhitungan angka, misal diskon, pajak, total harga, dll

def hitung_diskon(harga, diskon): # ini dia fungsi untuk menghitung diskon, dia butuh harga asli dan persen diskon
    """Menghitung harga setelah diskon.""" 
    # ini dia bakalan ngitung total diskon, misal harga yang kita masukan 100.000 dan diskon 20, maka total diskonnya adalah 100.000 * (20/100) = 20.000
    totalDiskon = harga * (diskon / 100) 
    # nah terus dsini kita bakal nge return harga setelah diskon, yaitu harga asli dikurang total diskon, misal 100.000 - 20.000 = 80.000
    return harga - totalDiskon

def hitung_pajak(harga, pajak=11): # nah kalo ini dia fungsi untuk menghitung pajak, dia butuh harga setelah diskon dan persen pajak, defaultnya 11%
    """Menghitung harga setelah pajak.""" 
    # ini dia bakalan ngitung total pajak, misal harga setelah diskon 80.000 dan pajak 11, maka total pajaknya adalah 80.000 * (11/100) = 8.800
    return harga * (pajak / 100)


# terus yang ini dia fungsi untuk menghitung total harga setelah diskon dan pajak,
# dia butuh harga asli, persen diskon, dan persen pajak, default diskonnya 0% dan pajaknya 11%
def hitung_total(harga, diskon=0, pajak=11): 
    """Menghitung total harga setelah diskon dan pajak."""
    # pertama kita itung dulu harga setelah diskon, dengan memanggil fungsi hitung_diskon, 
    hargaSetelahDiskon = hitung_diskon(harga, diskon)
    # terus kita itung pajaknya dengan memanggil fungsi hitung_pajak, dengan harga setelah diskon dan persen pajak
    pajakHarga = hitung_pajak(hargaSetelahDiskon, pajak)
    # terakhir kita return harga setelah diskon ditambah pajak, misal 80.000 + 8.800 = 88.800
    return hargaSetelahDiskon + pajakHarga