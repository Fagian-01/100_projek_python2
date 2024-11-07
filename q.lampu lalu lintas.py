#ini adalah program lampu lalu lintas
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM LAMPU LALU LINTAS".center(30))
print(30 * "\033[38;5;13m=")

lampu_lalu_lintas = str(input('Masukan warna lampu lalu lintas pakai kapital = '))

if lampu_lalu_lintas == 'MERAH':
    print('STOP!!')
elif lampu_lalu_lintas == 'KUNING':
    print('Hati-Hati!!')
elif lampu_lalu_lintas == 'HIJAU':
    print('MAJU!!')
else:
    print('Tau lampu lalulintas gak?')