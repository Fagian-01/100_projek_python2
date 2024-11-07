#ini adalah program Ujian
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM UJIAN".center(30))
print(30 * "\033[38;5;13m=")

print('Siapakah peracik program PYTHON ? ')
# print('''A. Rafa Khadafi
# B. Adolf Hitler
# C. Guido Van Rossum
# D. Michael Jackson''')

list = {'A':'Rafa Khadafi','B':'Adolf Hitler','C':'Guido Van Rossum','D':'Michael Jackson'}
for i,nilai in list.items():
    print(f'{i}.{nilai}')
jawaban = str(input('Masukan jawaban anda = '))
if jawaban =='C':
    print('Pintarr')
else:
    print('Banyakin cari informasi !') 