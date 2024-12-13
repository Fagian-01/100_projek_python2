#ini adalah program KONVERSI CELSIUS KE FARENHEITH
# dibuat pada 27/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KONVERSI CELSIUS KE FARENHEITH".center(30))
print(30 * "\033[38;5;13m=")

celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
