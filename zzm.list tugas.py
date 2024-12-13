#ini adalah program LIST TUGAS
# dibuat pada 6/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM LIST TUGAS".center(30))
print(30 * "\033[38;5;13m=")

def show_menu():
    print("\n=== List ===")
    print("1. Tambahkan Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ")
    daftar_tugas.append(tugas)
    print(f"Tugas '{tugas}' telah ditambahkan.")

def lihat_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("\nTugas Anda:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")

def hapus_tugas(daftar_tugas):
    lihat_tugas(daftar_tugas)
    if daftar_tugas:
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(daftar_tugas):
                tugas_dihapus = daftar_tugas.pop(nomor - 1)
                print(f"Tugas '{tugas_dihapus}' telah dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Harap masukkan nomor yang valid.")

def main():
    daftar_tugas = []

    while True:
        show_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_tugas(daftar_tugas)
        elif pilihan == "2":
            lihat_tugas(daftar_tugas)
        elif pilihan == "3":
            hapus_tugas(daftar_tugas)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program To-Do List. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
