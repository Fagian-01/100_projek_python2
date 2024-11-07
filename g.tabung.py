# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Tabung
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM TABUNG'.center(30))
print(30*'\33[92m=')

PHI = 3.14
r = float(input('Masukan Jari Jari = '))
t = float(input('Masukan Tinggi = '))

luas = 2 * PHI * r * (r + 1)
keliling = 2 * PHI * r
volume = PHI * r**2 * t

print(f'Luas = {luas:.2f}')
print(f'Keliling= {keliling:.2f}')
print(f'Volume = {volume:.2f}')
