import random

def cetak_garis(garis, posisi):
    display = [' '] * 20  # Representasi jalur balapan
    display[posisi] = '*'
    print(garis + ''.join(display))

def balap_kuda():
    print("Selamat datang di Balap Kuda!")
    print("Kontrol dengan menekan Enter untuk setiap langkah.")

    kuda_1 = 0
    kuda_2 = 0
    kuda_3 = 0

    while True:
        input("Tekan Enter untuk melanjutkan...")
        
        # Mengupdate posisi kuda
        kuda_1 += random.randint(1, 5)
        kuda_2 += random.randint(1, 5)
        kuda_3 += random.randint(1, 5)

        # Menampilkan jalur balapan
        cetak_garis("Kuda 1: ", kuda_1)
        cetak_garis("Kuda 2: ", kuda_2)
        cetak_garis("Kuda 3: ", kuda_3)
        
        # Cek pemenang
        if kuda_1 >= 20 or kuda_2 >= 20 or kuda_3 >= 20:
            if kuda_1 >= 20:
                print("Kuda 1 menang!")
            elif kuda_2 >= 20:
                print("Kuda 2 menang!")
            elif kuda_3 >= 20:
                print("Kuda 3 menang!")
            break

# Program utama
balap_kuda()
