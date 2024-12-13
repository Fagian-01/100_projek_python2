#ini adalah program MENGHITUNG HARGA DISKON
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG HARGA DISKON".center(30))
print(30 * "\033[38;5;13m=")

harga_asli = float(input("Masukkan harga asli barang: "))
diskon = float(input("Masukkan persen diskon: "))
harga_diskon = harga_asli - (harga_asli * (diskon / 100))
print(f"Harga setelah diskon: {harga_diskon}")
