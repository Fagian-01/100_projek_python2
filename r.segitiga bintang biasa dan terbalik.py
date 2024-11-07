#ini adalah program segitiga bintang biasa
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM SEGITIGA BINTANG BIASA".center(30))
print(30 * "\033[38;5;13m=")

user = int(input("masukan nilai segtiga = "))
print("ini adalah segitiga biasa")
for i in range(1,user + 1):
    # maksudnya adalah kita mulai dari 1 dan
    # user akan ditambah 1 karena index nya dari 0 
    # jadi kalo misal user input 7 maka kalo tidak ditambah maka akan 6
    # tapi jika ditambah maka akan tetap 7
    print(i*"*")
print()
print("ini adalah segitiga biasa terbalk")

for i in range(1,user + 1):
    print((user - i + 1) * "*")
