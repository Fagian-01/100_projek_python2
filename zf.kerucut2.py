# Dibuatoleh M Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Kerucut
import math
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM KERUCUT'.center(30))
print(30*'\33[92m=')

def input_user():
    '''Membuat input user'''
    PHI = 3.14
    r = float(input('Masukan Jari Jari Alas Kerucut = '))
    t = float(input('Masukan Tinggi Kerucut = '))
    sisi_miring = math.sqrt( r**2 + t**2)
    return PHI,r,t,sisi_miring

'''menghitung volume kerucut'''
volume = lambda PHI,r,t: 1/3 * PHI * r**2 * t

'''menghitung luas kerucut'''
luas = lambda PHI,r,sisi_miring : PHI * r * (r + sisi_miring)

PHI,r,t,sisi_miring = input_user()
print(f'Volume adalah = {volume(PHI,r,t):.2f}')
print(f'Luas adalah = {luas(PHI,r,sisi_miring):.2f}')