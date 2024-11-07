# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Lambda
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM TABUNG LAMBDA'.center(30))
print(30*'\33[92m=')

def input_user():
    '''Mengambil input user'''
    PHI = 3.14
    r = float(input('Masukan Jari Jari = '))
    t = float(input('Masukan Tinggi'))
    return PHI,r,t

'''Menghitung Luas Tabung'''
luas = lambda PHI,r: 2 * PHI * r * (r + 1)

'''Menghitung Keliling Tabung'''
keliling = lambda PHI,r: 2 * PHI * r

'''Menghitung volume tabung'''
volume = lambda PHI,r,t: PHI * r**2 * t 

PHI,r,t = input_user()
print(f'Luas = {luas(PHI,r):.2f}')
print(f'Keliling = {keliling(PHI,r):.2f}')
print(f'Volume = {volume(PHI,r,t):.2f}')