from tenagaKependidikan import TenagaKependidikan

class Pustakawan(TenagaKependidikan):
    def __init__(self, idPegawai: str, nama: str, unitKerja: str):
        super().__init__(idPegawai, nama, unitKerja)
        self.__kodePerpustakaan = ""
        self.__jumlahBukuDikelola = 0

    def mengelola_Peminjaman_Buku(self):
        pass

    def mengatur_Katalog_Buku(self):
        pass

    def hitung_Gaji(self) -> float:
        pass