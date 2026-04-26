# di file ini kita bakalan bikin modul buat tampilan & teks
# tanggung jawab: semua format output

# disini kita punya fungsi format_rupiah yang fungsinya untuk mengubah angka biasa menjadi format rupiah, misal 1000000 jadi Rp 1.000.000
def format_rupiah(angka):
    """Mengubah angka menjadi format rupiah."""
    # kita pake format string untuk mengubah angka menjadi format dengan titik sebagai pemisah ribuan, dan tanpa desimal, misal 1000000 jadi 1.000.000
    # terus kita tambahin "Rp " di depan angka, jadi hasil akhirnya adalah Rp 1.000.000
    # kita juga pake replace untuk mengganti koma dengan titik, karena format string defaultnya pake koma sebagai pemisah ribuan,
    #  jadi kita ganti jadi titik sesuai format rupiah
    return f"Rp {angka:,.0f}".replace(",", ".")

def format_struk(nama_item, harga_asli, diskon, total): # ini fungsi buat nyetak smuanya dalam bentuk struk
    """Mencetak Strukm belanja.""" # ini semacam header buat struk nya gtu
    print("=" * 30)
    print("STRUK PEMBELIAN")
    print("=" * 30)
        # terus kita print nama item, harga asli dalam format rupiah, persen diskon,
    print(f"Item: {nama_item}")
        # ini kita print harga asli dengan memanggil fungsi format_rupiah, jadi dia bakal tampil dalam format rupiah
    print(f"Harga Asli: {format_rupiah(harga_asli)}")
        # ini kita print persen diskon, misal 20%
    print(f"Diskon: {diskon}%")
        # ini kita print total harga setelah diskon dan pajak, dengan memanggil fungsi format_rupiah, jadi dia bakal tampil dalam format rupiah
    print(f"Total: {format_rupiah(total)}")
    print("=" * 30) # ini kita print garis pemisah di bawah struk, jadi tampilannya lebih rapi