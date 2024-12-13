def cek_palindrom(s):
    return s == s[::-1]

s = input("Masukkan kata atau angka: ")
if cek_palindrom(s):
    print(f"{s} adalah palindrom")
else:
    print(f"{s} bukan palindrom")
