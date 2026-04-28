from tenagaKependidikan import TenagaKependidikan

class Laboran(TenagaKependidikan):
    def __init__(self, idPegawai: str, nama: str, unitKerja: str):
        super().__init__(idPegawai, nama, unitKerja)
        self.__namaLaboratorium = ""
        self.__jumlahPeralatan = 0

    def menyiapkan_Praktikum(self):
        pass

    def mengecek_Alat_Lab(self):
        pass

    def hitung_Gaji(self) -> float:
        pass