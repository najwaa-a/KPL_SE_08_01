from pegawai import Pegawai

class TenagaKependidikan(Pegawai):
    def __init__(self, idPegawai: str, nama: str, unitKerja: str):
        super().__init__(idPegawai, nama)
        self.__unitKerja = unitKerja
        self.__shiftKerja = ""

    def mendukung_Operasional(self):
        pass

    def membuat_Laporan_Kerja(self):
        pass

    def hitung_Gaji(self) -> float:
        pass