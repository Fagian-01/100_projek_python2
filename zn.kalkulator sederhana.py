#ini adalah program KALKULATOR SEDERHANA
# dibuat pada 27/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KALKULATOR SEDERHANA".center(30))
print(30 * "\033[38;5;13m=")

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilih = input("Masukkan pilihan (1/2/3/4): ")

n1 = float(input("Masukkan angka pertama: "))
n2 = float(input("Masukkan angka kedua: "))

if pilih == '1':
    print(f"{n1} + {n2} = {add(n1, n2)}")
elif pilih == '2':
    print(f"{n1} - {n2} = {subtract(n1, n2)}")
elif pilih == '3':
    print(f"{n1} * {n2} = {multiply(n1, n2)}")
elif pilih == '4':
    print(f"{n1} / {n2} = {divide(n1, n2)}")
else:
    print("Pilihan tidak valid")
