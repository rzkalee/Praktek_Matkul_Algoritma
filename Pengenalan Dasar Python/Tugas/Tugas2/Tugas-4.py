level_akses = str(input("Masukan role anda: "))
jam_masuk = int(input("Masukan jam masuk anda (0-23): "))

boleh_masuk = level_akses == "admin" or level_akses == "teknisi" and jam_masuk >= 8 and jam_masuk <= 17

print(f"Apakah anda boleh masuk? ", boleh_masuk)