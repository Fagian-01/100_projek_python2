from datetime import datetime

def hitung_usia():
    tanggal_lahir = input("Masukkan tanggal lahir (format: YYYY-MM-DD): ")
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    hari_ini = datetime.now()
    
    usia = hari_ini.year - tanggal_lahir.year
    if hari_ini.month < tanggal_lahir.month or (hari_ini.month == tanggal_lahir.month and hari_ini.day < tanggal_lahir.day):
        usia -= 1
    
    print(f"Usia Anda saat ini: {usia} tahun")

hitung_usia()
