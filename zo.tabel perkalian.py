#ini adalah program TABEL PERKALIAN
# dibuat pada 27/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM TABEL PERKALIAN".center(30))
print(30 * "\033[38;5;13m=")

n = int(input("Masukkan angka untuk tabel perkalian: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
