from pegawai import Pegawai
from dosen import Dosen
from staffAdministrasi import StaffAdministrasi
from tenagaKependidikan import TenagaKependidikan
from laboran import Laboran
from pustakawan import Pustakawan
def main():

if __name__ == "__main__":
    Dosen1 = Dosen("D001", "Dr. Andi", "NIDN001")
    Dosen.hitung_Gaji(Dosen1)
    Dosen.membimbing_Mahasiswa(Dosen1, "Mahasiswa A")



    Staff1 = StaffAdministrasi("S001", "Budi", "Keuangan")
    Tenaga1 = TenagaKependidikan("T001", "Siti", "Perpustakaan")
    Laboran1 = Laboran("L001", "Rina", "Laboratorium Kimia")
    Pustakawan1 = Pustakawan("P001", "Agus", "Perpustakaan")          

