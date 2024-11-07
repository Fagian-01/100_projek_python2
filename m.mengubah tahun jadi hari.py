#ini adalah program mengubah tahun menjadi hari
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGUBAH TAHUN MENJADI HARI".center(30))
print(30 * "\033[38;5;13m=")

HARI = 365
tahun = int(input('Masukan Tahun :'))
hari = int(tahun*HARI)

print(tahun,'Tahun','Adalah',hari,'Hari')