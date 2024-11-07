#ini adalah program menghitung menggunakan eval
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM PERULANGAN KALIMAT".center(30))
print(30 * "\033[38;5;13m=")
print()
print('''contoh penggunaan
      - 1 + 3
      - 5 - 4
      - 6 * 5
      - 9 / 3
      - 6 ** 2
      - 10 % 7
                ''')
inputan_user = input('Masukan yang mau di hitung = ')
hasil = eval(inputan_user)
print(f'Hasil nya adalah = {hasil}')