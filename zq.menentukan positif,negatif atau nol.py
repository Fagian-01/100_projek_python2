#ini adalah program MENENTUKAN POSITIF,NEGATIF ATAU NOL
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENENTUKAN POSITIF,NEGATIF ATAU NOL".center(30))
print(30 * "\033[38;5;13m=")

n = float(input("Masukkan angka: "))
if n > 0:
    print(f"{n} adalah angka positif")
elif n < 0:
    print(f"{n} adalah angka negatif")
else:
    print(f"{n} adalah nol")
