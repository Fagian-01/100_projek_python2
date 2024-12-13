#ini adalah program MENGHITUNG PANJANG STRING
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG PANJANG STRING".center(30))
print(30 * "\033[38;5;13m=")

text = input("Masukkan string: ")
print(f"Panjang string: {len(text)}")
