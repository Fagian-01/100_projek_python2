#ini adalah program segitiga bintang sempurna
# dibuat pada 07/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM SEGITIGA BINTANG SEMPURNA".center(30))
print(30 * "\033[38;5;13m=")

user = int(input('Masukan nilai segitiga = '))
print()
print("ini adalah bintang sempurna")

for i in range(1,user + 1):
    print((user - i) * " " + (2 * i - 1) * "*")
for i in range(user, 0, -1):
    print((user - i) * " " + (2 * i - 1) * "*")