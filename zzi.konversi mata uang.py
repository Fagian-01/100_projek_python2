def konversi_uang():
    jumlah = float(input("Masukkan jumlah uang yang ingin dikonversi: "))
    kurs = float(input("Masukkan nilai tukar (misalnya 1 USD = 15.000 IDR): "))
    
    hasil = jumlah * kurs
    print(f"Hasil konversi: {hasil:.2f} dalam mata uang tujuan.")

konversi_uang()
