#ini adalah program ZODIAK
# dibuat pada 1/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM ZODIAK".center(30))
print(30 * "\033[38;5;13m=")

def zodiak():
    bulan = int(input("Masukkan bulan lahir (1-12): "))
    tanggal = int(input("Masukkan tanggal lahir: "))
    
    if (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        print("Zodiak Anda adalah Aries")
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        print("Zodiak Anda adalah Taurus")
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        print("Zodiak Anda adalah Gemini")
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        print("Zodiak Anda adalah Cancer")
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        print("Zodiak Anda adalah Leo")
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        print("Zodiak Anda adalah Virgo")
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        print("Zodiak Anda adalah Libra")
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        print("Zodiak Anda adalah Scorpio")
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        print("Zodiak Anda adalah Sagitarius")
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        print("Zodiak Anda adalah Capricorn")
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        print("Zodiak Anda adalah Aquarius")
    else:
        print("Zodiak Anda adalah Pisces")

zodiak()
