#ini adalah program Penghitung Point
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG POINT".center(30))
print(30 * "\033[38;5;13m=")

uts = int(input('Masukan nilai uts = '))
uas = int(input('Masukan nilai uas = '))
tugas = int(input('Masukan nilai tugas = '))
jumlah = uts + uas + tugas
rata_rata = jumlah / 3
# a > 85
# b 70 - 84
# c 60 - 79 
# d < 60
print(f'Jumlah = {jumlah}')
print(f'Rata-rata = {rata_rata:.2f}')
if rata_rata >= 85:
    print(f'Nilai anda A')
elif 70 <= rata_rata < 85:
    print(f'Nilai anda B')
elif 60 <= rata_rata < 70:
    print(f'Nilai anda C')
elif rata_rata < 60:
    print(f'Nilai anda D')