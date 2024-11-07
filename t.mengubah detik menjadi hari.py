#ini adalah program mengubah detik menjadi hari
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGUBAH DETIK MENJADI HARI".center(30))
print(30 * "\033[38;5;13m=")

HARI_DETIK = 60 * 60 * 24 
JAM_DETIK = 60 * 60
detik = int(input('Detik :'))
hari = int(detik/HARI_DETIK)
sisa_detik = detik % HARI_DETIK
jam = int(detik/JAM_DETIK)
detik = detik % JAM_DETIK
menit = int(detik / 60)
detik = detik % 60
print('adalah',hari,'Hari',jam,'Jam',menit,'Menit','Dan',detik,'Detik')
