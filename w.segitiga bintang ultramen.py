#ini adalah program segitiga bintang ultramen
# dibuat pada 07/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM SEGITIGA BINTANG ULTRAMEN".center(30))
print(30 * "\033[38;5;13m=")

user = int(input('Masukan nilai segitiga = '))

print()
print("ini adalah bintang ultramen")
for i in range(user):
    print("*"*i)
    i += 1
no = 1
for no in range(user):
    print("*"*user)
    user-=1