#ini adalah program mencari bilangan ganjil atau genap
# dibuat pada 25/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENCARI BILANGAN GANJIL ATAU GENAP".center(30))
print(30 * "\033[38;5;13m=")

i = int(input("Masukkan angka: "))
if i % 2 == 0:
    print(f"{i} adalah angka genap")
else:
    print(f"{i} adalah angka ganjil")
