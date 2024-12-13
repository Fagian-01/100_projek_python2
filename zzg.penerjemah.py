def penerjemah():
    kamus = {
        'hello': 'halo',
        'goodbye': 'selamat tinggal',
        'thank you': 'terima kasih',
        'please': 'tolong'
    }
    
    kata = input("Masukkan kata dalam bahasa Inggris: ").lower()
    
    if kata in kamus:
        print(f"Terjemahan: {kamus[kata]}")
    else:
        print("Kata tidak ditemukan dalam kamus.")

penerjemah()
