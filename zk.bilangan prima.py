#ini adalah program BILANGAN PRIMA
# dibuat pada 25/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM BILANGAN PRIMA".center(30))
print(30 * "\033[38;5;13m=")

n = int(input("Masukkan angka: "))
prima = True
for i in range(2, n):
    if n % i == 0:
        prima = False
        break
if prima and n > 1:
    print(f"{n} adalah bilangan prima")
else:
    print(f"{n} bukan bilangan prima")
