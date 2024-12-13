#ini adalah program TAHUN KABISAT
# dibuat pada 25/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM TAHUN KABISAT".center(30))
print(30 * "\033[38;5;13m=")

tahun = int(input("Masukkan tahun: "))
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")
