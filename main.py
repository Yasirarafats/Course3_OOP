"""
MENGGUNAKAN OOP
"""
from geometri.bangun_ruang import BangunRuang
from geometri.peresgipanjang import PersegiPanjang
from geometri.segitiga import Segitiga


p1 = PersegiPanjang(10, 9)

print(f'\n {p1.info()}')
print(f'\n hasilnya adalah = {p1.hitung_luas()} meter persegi')

s1 = Segitiga(4, 7)

print(f'\n {s1.info()}')
print(f'\n hasilnya adalah {s1.hitung_luas()} cm')

print('\nMencoba membuat objek dari class bangun ruang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

"""
Polymorphism adalah kemampuan sebuah object untuk merespon terhadap pemanggilan method yang sama
"""

print('\nMencoba Polymorphism')
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.hitung_luas())
    print(bangun_ruang.info())

