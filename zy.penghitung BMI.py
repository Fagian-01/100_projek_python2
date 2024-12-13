#ini adalah program MENGHITUNG MENGHITUNG BMI
# dibuat pada 1/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM MENGHITUNG MENGHITUNG BMI".center(30))
print(30 * "\033[38;5;13m=")

def hitung_bmi():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))
    bmi = berat / (tinggi ** 2)
    
    print(f"Nilai BMI Anda adalah: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Kategori: Kurus")
    elif 18.5 <= bmi < 24.9:
        print("Kategori: Normal")
    elif 25 <= bmi < 29.9:
        print("Kategori: Gemuk")
    else:
        print("Kategori: Obesitas")

hitung_bmi()
