#ini adalah program membalikan string
# dibuat pada 25/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MEMBALIKAN STRING".center(30))
print(30 * "\033[38;5;13m=")

string = input("Masukkan string: ")
print(string[::-1])
