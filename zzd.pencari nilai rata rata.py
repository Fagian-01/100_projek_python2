
def rata_rata():
    angka = [int(x) for x in input("Masukkan angka (pisahkan dengan spasi): ").split()]
    print(f"Rata-rata: {sum(angka) / len(angka)}")

rata_rata()
