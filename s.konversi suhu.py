#ini adalah program konversi suhu
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM KONVERSI SUHU".center(30))
print(30 * "\033[38;5;13m=")

sc = float(input('Masukan Suhu Dalam Celcius :'))
print('suhu celcius',sc,'C')

rm = (4/5) * sc
print('suhu dalam reamur :',rm,"R")

fh = ((9/5) * sc) + 32
print('suhu dalam fahrenheit :',fh,'F')

k = sc + 273
print('suhu dalam kelvin :',k,'K')
