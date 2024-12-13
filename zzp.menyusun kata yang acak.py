import itertools

def acak_kata():
    kata = input("Masukkan kata: ")
    hasil = [''.join(p) for p in itertools.permutations(kata)]
    print(f"Permutasi dari '{kata}': {hasil}")

if __name__ == "__main__":
    acak_kata()
