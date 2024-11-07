# Dibuat Pada 22 10 2024
# Ini Adalah Program Segitiga Lambda
import os
os.system('cls')
print(30*'\33[92m=')
print('PROGRAM Segitiga'.center(30))
print(30*'\33[92m=')

def input_user():
    '''mengambil inputan user'''
    sisi_a = float(input('Masukan Sisi a ='))
    sisi_b = float(input('Masukan Sisi b ='))
    sisi_c = float(input('Masukan Sisi c ='))
    alas   = float(input('Masukan Alas ='))
    tinggi = float(input('Masukan Tinggi ='))
    return sisi_a,sisi_b,sisi_c,alas,tinggi

'''menghitung luas segitiga'''
luas_segitiga = lambda alas,tinggi: alas * tinggi /2

'''menghitung keliling segitiga'''
keliling_segitiga = lambda sisi_a,sisi_b,sisi_c : sisi_a + sisi_b + sisi_c

sisi_a,sisi_b,sisi_c,alas,tinggi = input_user()
print(f'Hasil Perhitungan Luas = {luas_segitiga(alas,tinggi)} cm2')
print(f'Hasil Perhitungan Keliling = {keliling_segitiga(sisi_a,sisi_b,sisi_c)} cm')

