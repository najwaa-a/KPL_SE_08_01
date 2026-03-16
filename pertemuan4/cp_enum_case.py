from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2


patients = []

def addpatient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis kelamin harus LAKI_LAKI atau PEREMPUAN")
    
    addpatient("John Doe", JenisKelamin.LAKI_LAKI)


    patients.append({
        "name": name,
        "gender": gender.name
    })

    print(f"Pasien {name} dengan jenis kelamin {gender.name} berhasil ditambahkan.")

    addpatient("Jane Doe", JenisKelamin.PEREMPUAN)
    addpatient("Alex Smith", JenisKelamin.LAKI_LAKI)  

    for patient in patients:
        print(f"Nama: {patient['name']}, Jenis Kelamin: {patient['gender']}")