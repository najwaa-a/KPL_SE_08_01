from pegawai import Pegawai
from pertemuan9.sistem_manajemen_pegawai_kampus import pegawai

class Dosen(Pegawai):
    def __init__(self, idPegawai: str, nama: str, nidn: str):
        super().__init__(idPegawai, nama)
        self.__nidn = nidn
        self.__bidangKeahlian = ""
        self.__jumlahSKS = 0

    def mengajar(self, mataKuliah: str):
        pass

    def membimbing_Mahasiswa(self, namaMahasiswa: str):
        pass

    def hitung_Gaji(self) -> float:
        pass