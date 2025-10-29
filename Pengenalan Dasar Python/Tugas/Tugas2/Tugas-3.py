angka = int(input("Masukan Angka: "))

genap = angka % 2 == 0
ganjil = not genap

print(f"Ganjil? ", ganjil)