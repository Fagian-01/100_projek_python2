#ini adalah program MENCARI MODULUS
# dibuat pada 27/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENCARI MODULUS".center(30))
print(30 * "\033[38;5;13m=")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
print(f"{a} modulus {b} = {a % b}")
