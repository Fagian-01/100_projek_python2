#ini adalah program PERBEDAAN 2 TANGGAL
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM PERBEDAAN 2 TANGGAL".center(30))
print(30 * "\033[38;5;13m=")

from datetime import datetime
tanggal1 = datetime.strptime(input("Masukkan tanggal pertama (yyyy-mm-dd): "), "%Y-%m-%d")
tanggal2 = datetime.strptime(input("Masukkan tanggal kedua (yyyy-mm-dd): "), "%Y-%m-%d")
selisih = abs(tanggal2 - tanggal1)
print(f"Selisih antara kedua tanggal adalah {selisih.days} hari.")
