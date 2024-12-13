#ini adalah program nama lengkap
# dibuat pada 19/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM NAMA LENGKAP".center(30))
print(30 * "\033[38;5;13m=")

first = str(input('Hello Masukan First Name Anda = '))
middle = str(input('Hello Masukan Middle Name Anda = '))
last = str(input('Hello Masukan Last Name Anda = '))

print(f"Hello {first},apakah marga kamu {last},bolehkah saya manggil kamu {middle}?  ")