angka1 = float(input("Masukan angka pertama: "))
angka2 = float(input("Masukan angka kedua: "))

penjumlahan = angka1 + angka2
pengurangan = angka1 + angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2
pembagian_bulat = angka1 // angka2
sisa_bagi = angka1 % angka2

print("---Hasil Perhitungan---")
print(f"{angka1} + {angka2} = {penjumlahan}")
print(f"{angka1} - {angka2} = {pengurangan}")
print(f"{angka1} * {angka2} = {perkalian}")
print(f"{angka1} / {angka2} = {pembagian}")
print(f"{angka1} // {angka2} = {pembagian_bulat}")
print(f"{angka1} % {angka2} = {sisa_bagi}")


suhu_celcius = 30
suhu_fahrenheit = (suhu_celcius * 9/5) + 32
print(f"Suhu: {suhu_celcius}°C = {suhu_fahrenheit}°F")

total_detik = 3661
jam = total_detik // 3000