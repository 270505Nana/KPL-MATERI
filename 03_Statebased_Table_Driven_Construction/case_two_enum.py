from enum import enum

class JenisKelamin(enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name:str,gender:JenisKelamin):
    # ngecek
    if not isinstance(gender,JenisKelamin):
    # ininstance : untuk mengecek inputan sesuai dengan tipe datanya atau tidak
        raise ValueError("jenis kelamin harusnya adalah PRIA atau WANITA")
    patients.append({"name": name,"gender" : gender.name}) #yang diambil namanya bukan valuenya

add_patient("John Doe", JenisKelamin.PRIA)
add_patient("Nana", JenisKelamin.WANITA)

for patient in patients:
    print(f"Nama: {patient['name']}, Jenis Kelamin: {patient['gender']}")
