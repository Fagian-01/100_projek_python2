# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 08 10 2024
# Ini Adalah Program Lingkaran Lambda
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM Lingkaran LAMBDA'.center(30))
print(30*'\33[92m=')

PHI = 3.14

def input_user():
    '''mengambil input dari user'''
    r = int(input('MASUKAN JARI JARI LINGKARAN:'))
    return r

'''rumus menghitung lingkaran'''
luas_lingkaran = lambda r : r ** 2 * PHI

'''rumus menghitung keliling lingkaran'''
keliling_lingkaran = lambda r : 2 * PHI * r

r = input_user()
print(f'hasil perhitungan luas lingkaran = {luas_lingkaran(r)}')
print(f'hasil perhitungan keliling lingkaran = {keliling_lingkaran(r)}')
