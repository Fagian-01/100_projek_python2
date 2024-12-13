#ini adalah program PENENTU HARI
# dibuat pada 6/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM PENENTU HARI".center(30))
print(30 * "\033[38;5;13m=")

import calendar

def tanggal():
    tanggal = int(input("Masukkan tanggal (1-31): "))
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun : "))
    
    hari = calendar.weekday(tahun, bulan, tanggal)
    hari_list = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    
    print(f"Tanggal {tanggal}/{bulan}/{tahun} jatuh pada hari {hari_list[hari]}")

tanggal()
