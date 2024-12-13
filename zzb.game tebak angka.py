#ini adalah program GAME TEBAK ANGKA
# dibuat pada 2/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM GAME TEBAK ANGKA".center(30))
print(30 * "\033[38;5;13m=")

import random

def game_tebak_angka():
    print("=== Selamat Datang di Game Tebak Angka ===")
    print("Saya telah memilih sebuah angka antara 1 hingga 100.")
    print("Coba tebak angkanya!")

    # Komputer memilih angka secara acak
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1

            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba angka yang lebih besar.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba angka yang lebih kecil.")
            else:
                print(f"Selamat! Anda menebak dengan benar dalam {jumlah_tebakan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    game_tebak_angka()
