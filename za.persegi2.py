# Dibuat Oleh Muhammad Fagian Darmawan
# Dibuat Pada 08 10 2024
# Ini Adalah Program Persegi Lambda
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM PERSEGI LAMBDA'.center(30))
print(30*'\33[92m=')

'''mengambil input user'''
def input_user():
    sisi = float(input('Masukan sisi persegi\t\t\t: '))
    return sisi

'''menghitung luas persegi'''
luas_persegi = lambda sisi : sisi ** 2

'''menghitung keliling persegi'''
keliling_persegi = lambda sisi : sisi * 4

sisi = input_user()
print('Hasil Perhitungan Luas Persegi\t\t:',luas_persegi(sisi),'cm2')
print('Hasil Perhitungan keliling Persegi\t:',keliling_persegi(sisi),'cm')