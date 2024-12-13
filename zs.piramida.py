#ini adalah program PIRAMIDA
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM PIRAMIDA".center(30))
print(30 * "\033[38;5;13m=")

n = int(input("Masukkan jumlah baris: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
