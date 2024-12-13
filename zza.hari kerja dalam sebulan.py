#ini adalah program HARI KERJA DALAM SEBULAN
# dibuat pada 2/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM HARI KERJA DALAM SEBULAN".center(30))
print(30 * "\033[38;5;13m=")

import calendar

def hari_kerja():
    tahun = int(input("Masukkan tahun: "))
    bulan = int(input("Masukkan bulan (1-12): "))
    
    jumlah_hari = calendar.monthrange(tahun, bulan)[1]
    hari_kerja = 0
    for i in range(1, jumlah_hari + 1):
        if calendar.weekday(tahun, bulan, i) < 5:  # Senin sampai Jumat
            hari_kerja += 1
    
    print(f"Jumlah hari kerja di bulan {calendar.month_name[bulan]}: {hari_kerja} hari")

hari_kerja()
