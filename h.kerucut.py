# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Kerucut
import math
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM KERUCUT'.center(30))
print(30*'\33[92m=')

PHI = 3.14
r = float(input('Masukan Jari Jari Alas Kerucut = '))
t = float(input('Masukan Tinggi Kerucut = '))

sisi_miring = math.sqrt(r**2 + t**2)
volume = 1/3 * PHI * r**2 * t
luas = PHI * r * (r + sisi_miring)

print(f'Volume kerucut adalah = {volume:.2f}')
print(f'Luas kerucut adalah = {luas:.2f}')