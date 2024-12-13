#ini adalah program MENGHITUNG JUMLAH KATA DALAM KALIMAT
# dibuat pada 29/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG JUMLAH KATA DALAM KALIMAT".center(30))
print(30 * "\033[38;5;13m=")

kalimat = input("Masukkan kalimat: ")
jumlah_kata = len(kalimat.split())
print(f"Jumlah kata dalam kalimat: {jumlah_kata}")
