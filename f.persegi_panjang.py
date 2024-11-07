# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Persegi panjang
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM PERSEGI PANJANG'.center(30))
print(30*'\33[92m=')

panjang = float(input('Masukan Panjang : '))
lebar = float(input('Masukan Lebar : '))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f'Luas = {luas:.2f}')
print(f'Keliling = {keliling:.2f}')