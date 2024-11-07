# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 22 10 2024
# Ini Adalah Program Segitiga
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM Segitiga'.center(30))
print(30*'\33[92m=')

sisi_a = float(input('Masukan sisi a ='))
sisi_b = float(input('Masukan sisi b ='))
sisi_c = float(input('Masukan sisi c ='))
alas = float(input("Masukan alas = "))
tinggi = float(input('masukan tinggi ='))

luas = alas * tinggi / 2
keliling = sisi_a + sisi_b + sisi_c

print('Luas Segitiga Adalah = ',luas,'cm')
print('keliling Segitiga Adalah =',keliling,'cm2')