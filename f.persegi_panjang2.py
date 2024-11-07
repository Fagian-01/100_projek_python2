# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 05 11 2024
# Ini Adalah Program Persegi panjang lambda
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM PERSEGI PANJANG LAMBDA'.center(30))
print(30*'\33[92m=')

def input_user():
    '''Memasukan Input User'''
    panjang = float(input('Masukan Panjang = '))
    lebar = float(input('Masukan Lebar = '))
    return panjang,lebar

'''Menghitung Luas Persegi Panjang'''
luas = lambda panjang,lebar: panjang*lebar

'''Menghitung Keliling Persegi Panjang'''
keliling = lambda panjang,lebar : 2 * (panjang + lebar)

panjang,lebar = input_user()
print(f'Luas = {luas(panjang,lebar):.2f}')
print(f'Keliling = {keliling(panjang,lebar):.2}')