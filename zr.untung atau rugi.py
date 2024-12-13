#ini adalah program MENENTUKAN UNTUNG ATAU RUGI
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENENTUKAN ".center(30))
print(30 * "\033[38;5;13m=")

harga_beli = float(input("Masukkan harga beli: "))
harga_jual = float(input("Masukkan harga jual: "))
if harga_jual > harga_beli:
    print(f"Keuntungan: {harga_jual - harga_beli}")
elif harga_jual < harga_beli:
    print(f"Kerugian: {harga_beli - harga_jual}")
else:
    print("Tidak ada keuntungan atau kerugian.")
