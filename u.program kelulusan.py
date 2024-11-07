#ini adalah program kelulusan
# dibuat pada 07/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KELULUSAN".center(30))
print(30 * "\033[38;5;13m=")

nilai = int(input('Masukan nilai anda = '))

if 90 <= nilai <= 100 :
    print('Anda LULUS dengan nilai A')
elif 80 <= nilai < 90 :
    print('Anda LULUS dengan nilai B')
elif 70 <= nilai < 80 :
    print('Anda LULUS dengan nilai c')
elif nilai >= 101:
    print('Berotak SENKU!!')
else :
    print('Maaf anda TIDAK LULUS ')
    