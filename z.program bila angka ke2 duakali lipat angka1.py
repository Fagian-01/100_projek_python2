#ini adalah program angka2 duakali lipat angka1
# dibuat pada 19/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM ANGKA2 DUAKALI LIPAT ANGKA1".center(30))
print(30 * "\033[38;5;13m=")

angka1 = int(input('Masukan Angka : '))
angka2 = int(input('Masukan Angka : '))

if angka1 * 2 == angka2:
    hasil = angka2 * 3
    print(hasil)
else:
    hasil = angka1 + angka2
    print(hasil)    
