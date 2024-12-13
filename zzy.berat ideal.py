def berat_ideal(tinggi, jenis_kelamin):
    if jenis_kelamin.lower() == 'laki-laki':
        berat_ideal = 0.9 * (tinggi - 100)
    else:
        berat_ideal = 0.85 * (tinggi - 100)
    return berat_ideal

def tampilkan_berat_ideal():
    tinggi = float(input("Masukkan tinggi badan (dalam cm): "))
    jenis_kelamin = input("Masukkan jenis kelamin (laki-laki/perempuan): ")
    print(f"Berat ideal: {berat_ideal(tinggi, jenis_kelamin):.2f} kg")

