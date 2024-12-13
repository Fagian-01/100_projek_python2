#ini adalah program QUIZZ
# dibuat pada 6/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM QUIZZ".center(30))
print(30 * "\033[38;5;13m=")

def tampilkan_menu():
    print("\n=== Kuis Sederhana ===")
    print("1. Mulai Kuis")
    print("2. Keluar")

def kuis():
    pertanyaan = [
        {
            "soal": "Siapa presiden pertama Indonesia?",
            "pilihan": ["a. Soekarno", "b. Soeharto", "c. BJ Habibie", "d. Megawati"],
            "jawaban": "a"
        },
        {
            "soal": "Berapa hasil dari 5 x 6?",
            "pilihan": ["a. 11", "b. 30", "c. 20", "d. 25"],
            "jawaban": "b"
        },
        {
            "soal": "Apa ibu kota Jepang?",
            "pilihan": ["a. Beijing", "b. Tokyo", "c. Seoul", "d. Bangkok"],
            "jawaban": "b"
        },
        {
            "soal": "Siapa penemu bola lampu?",
            "pilihan": ["a. Nikola Tesla", "b. Thomas Edison", "c. Alexander Graham Bell", "d. Isaac Newton"],
            "jawaban": "b"
        },
        {
            "soal": "Planet terbesar di tata surya?",
            "pilihan": ["a. Bumi", "b. Mars", "c. Jupiter", "d. Saturnus"],
            "jawaban": "c"
        },
        {
            "soal": "Berapa jumlah provinsi di Indonesia saat ini?",
            "pilihan": ["a. 33", "b. 34", "c. 35", "d. 36"],
            "jawaban": "b"
        },
        {
            "soal": "Apa simbol kimia untuk air?",
            "pilihan": ["a. H2O", "b. CO2", "c. O2", "d. NaCl"],
            "jawaban": "a"
        },
        {
            "soal": "Siapa tokoh utama dalam novel 'Laskar Pelangi'?",
            "pilihan": ["a. Ikal", "b. Mahar", "c. Lintang", "d. Arai"],
            "jawaban": "a"
        },
        {
            "soal": "Dalam olahraga sepak bola, berapa jumlah pemain di satu tim?",
            "pilihan": ["a. 10", "b. 11", "c. 12", "d. 13"],
            "jawaban": "b"
        },
        {
            "soal": "Apa nama alat musik tradisional dari Jawa Barat?",
            "pilihan": ["a. Angklung", "b. Gamelan", "c. Sasando", "d. Kolintang"],
            "jawaban": "a"
        },
        {
            "soal": "Apa ibu kota Australia?",
            "pilihan": ["a. Sydney", "b. Melbourne", "c. Canberra", "d. Brisbane"],
            "jawaban": "c"
        },
        {
            "soal": "Siapa ilmuwan yang mengemukakan teori relativitas?",
            "pilihan": ["a. Isaac Newton", "b. Albert Einstein", "c. Galileo Galilei", "d. Stephen Hawking"],
            "jawaban": "b"
        },
        {
            "soal": "Apa bahasa pemrograman yang sering digunakan untuk pengembangan web?",
            "pilihan": ["a. Python", "b. JavaScript", "c. C++", "d. Ruby"],
            "jawaban": "b"
        },
        {
            "soal": "Apa nama proses tumbuhan membuat makanan sendiri?",
            "pilihan": ["a. Respirasi", "b. Fotosintesis", "c. Fermentasi", "d. Transpirasi"],
            "jawaban": "b"
        },
        {
            "soal": "Hewan apa yang dikenal sebagai raja hutan?",
            "pilihan": ["a. Harimau", "b. Singa", "c. Macan", "d. Cheetah"],
            "jawaban": "b"
        }
    ]

    skor = 0

    for i, q in enumerate(pertanyaan):
        print(f"\nPertanyaan {i+1}: {q['soal']}")
        for pilihan in q['pilihan']:
            print(pilihan)

        jawaban = input("Masukkan huruf jawaban Anda: ").lower()
        if jawaban == q['jawaban']:
            print("Benar!")
            skor += 1
        else:
            print("Salah!")

    print(f"\nKuis selesai! Skor Anda: {skor} dari {len(pertanyaan)}")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            kuis()
        elif pilihan == "2":
            print("Terima kasih telah bermain! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
