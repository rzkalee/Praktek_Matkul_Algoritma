ipk = float(input("Masukan IPK anda: "))
pendapatan_ortu = int(input("Masukan pendapatan Orang Tua anda: "))

lolos_seleksi = ipk == 4.0 or pendapatan_ortu > 1500000

print(f"Apakah anda mendapat Beasiswa?", lolos_seleksi)