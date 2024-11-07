#ini adalah program mengubah hari menjadi tahun
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGUBAH HARI MENJADI TAHUN".center(30))
print(30 * "\033[38;5;13m=")

TAHUN = 365
BULAN = 30
hari = int(input('Hari :'))
tahun = int(hari/TAHUN)
hari = hari % TAHUN
bulan = int(hari/BULAN)
hari = hari % BULAN

print('Adalah',tahun,'Tahun',bulan,'Bulan','dan',hari,'Hari')
