#ini adalah program KONVERSI FARENHEITH KE CELSIUS
# dibuat pada 27/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KONVERSI FARENHEITH KE CELSIUS".center(30))
print(30 * "\033[38;5;13m=")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")
