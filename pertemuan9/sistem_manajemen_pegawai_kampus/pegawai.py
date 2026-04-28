class Pegawai:
    def __init__(self, idPegawai: str, nama: str):
        self.__idPegawai = idPegawai
        self.__nama = nama
        self.__alamat = ""
        self.__noTelepon = ""
        self.__statusAktif = False

    def tampilkan_Data(self):
        pass

    def hitung_Gaji(self) -> float:
        pass

    def ubah_Status(self, status: bool):
        pass