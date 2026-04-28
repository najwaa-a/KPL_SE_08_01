from pegawai import Pegawai

class StaffAdministrasi(Pegawai):
    def __init__(self, idPegawai: str, nama: str, bagian: str):
        super().__init__(idPegawai, nama)
        self.__bagian = bagian
        self.__jamKerja = 0

    def kelola_Surat(self):
        pass

    def input_Data_Akademik(self):
        pass

    def hitung_Gaji(self) -> float:
        pass