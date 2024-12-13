#ini adalah program DADU
# dibuat pada 13/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM DADU".center(30))
print(30 * "\033[38;5;13m=")

import random

def lempar_dadu():
    return random.randint(1, 6)

def main_game():
    print("Selamat datang di Game Dadu!")
    while True:
        input("Tekan Enter untuk melempar dadu...")
        hasil = lempar_dadu()
        print(f"Hasil lemparan dadu: {hasil}")
        
        lagi = input("Apakah Anda ingin melempar dadu lagi? (y/n): ").lower()
        if lagi != 'y':
            break

if __name__ == "__main__":
    main_game()
