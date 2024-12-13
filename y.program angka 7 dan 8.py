#ini adalah program angka 7 dan 8
# dibuat pada 19/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM ANGKA 7 DAN 8".center(30))
print(30 * "\033[38;5;13m=")

i = int(input('masukan angka = '))

if i == 7:
    angka = i + 20
    print(angka)
elif i == 8:
    angka = i + 20
    print(angka)
else:
    print(i)
