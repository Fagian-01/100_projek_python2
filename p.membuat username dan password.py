#ini adalah program membuat username dan password
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KODE KEAMANAN".center(30))
print(30 * "\033[38;5;13m=")

USERNAME = 'fagian030709@gmail.com'
PASSWORD = 'Agi030709'

username = input('Masukan Username\t :')
password  = input('Masukan Pasword\t\t :')

if username != USERNAME:
    print("Salah akun ya?")
elif username == USERNAME and password != PASSWORD:
    print('Salah Pasword')
else:
    print('Wilujeng Sumping',username)