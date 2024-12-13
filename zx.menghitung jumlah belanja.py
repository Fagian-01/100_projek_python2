#ini adalah program MENGHITUNG JUMLAH BELANJA
# dibuat pada 1/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG JUMLAH BELANJA".center(30))
print(30 * "\033[38;5;13m=")

def penghitung_belanja():
    total = 0
    while True:
        barang = input("Masukkan nama barang (atau 'selesai' untuk menghentikan): ")
        if barang.lower() == 'selesai':
            break
        harga = float(input(f"Masukkan harga {barang}: "))
        jumlah = int(input(f"Masukkan jumlah {barang}: "))
        total += harga * jumlah

    diskon = float(input("Masukkan persentase diskon (0-100): "))
    total_setelah_diskon = total * (1 - diskon / 100)
    print(f"Total belanja setelah diskon: {total_setelah_diskon}")

penghitung_belanja()
