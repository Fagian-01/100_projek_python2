#ini adalah program mencari nilai minimum dan maksimum
# dibuat pada 25/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENCARI NILAI MINIMUM DAN MAKSIMUM".center(30))
print(30 * "\033[38;5;13m=")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))
print("Nilai maksimum:", max(a, b, c))
print("Nilai minimum:", min(a, b, c))
