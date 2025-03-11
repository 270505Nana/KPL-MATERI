from enum import enum

class JenisKelamin(enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin,LAKI_LAKI) #value of enum
print(JenisKelamin,LAKI_LAKI.value) #value of LAKI LAKI = 1
print(JenisKelamin,LAKI_LAKI.name) #value namanya => laki
