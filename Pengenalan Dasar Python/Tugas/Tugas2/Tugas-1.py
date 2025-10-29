status_member = str(input("Apakah anda memiliki member? (Ya/Tidak) " ))
total_belanja = int(input("Total Belanja: "))

dapat_diskon = status_member = "Ya" and total_belanja > 500000

print(f"Apakah anda mendapat diskon? ", dapat_diskon)