import random
import time

def spin_wheel():
    options = ["Hadiah 1", "Hadiah 2", "Hadiah 3", "Hadiah 4", "Hadiah 5", "Hadiah 6"]
    spins = random.randint(1, 10)  # Jumlah putaran acak (1 hingga 10)

    print("Memutar roda...")
    time.sleep(2)  # Tunggu 2 detik untuk efek spin

    result = options[random.randint(0, len(options) - 1)]  # Pilih hadiah secara acak
    print(f"Hasil spin: {result}")

# Program utama
print("Selamat datang di Spin Roda Keberuntungan!")
spin_wheel()
