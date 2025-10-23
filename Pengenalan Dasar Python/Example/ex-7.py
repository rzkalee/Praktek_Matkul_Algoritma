#Latihan 1.1 
print("LATIHAN 1.1 - Cek Batas Umur (SIM)")

usia_user = int(input("Masukan usia kamu: "))
memenuhi_syarat = usia_user >= 17

print(f"Apakah kamu memenuhi syarat membuat SIM? {memenuhi_syarat}")

#Operator >= (lebih besar dari atau sama dengan) sangat penting di sini. Jika pengguna memasukkan 17, hasilnya akan True. Jika kita hanya menggunakan >, maka 17 > 17 akan menjadi False.

#Latihan 1.2 
print("LATIHAN 1.2 - Perbandingan Password")

password_benar = "SuperAman123"
password_user = input("Masukan password kamu: ")
cocok_gak_yah = password_benar == password_user

print(f"Password yang kamu masukin bener gak yh: {cocok_gak_yah}")

#Latihan 2.2 
print("LATIHAN 2.2 - Syarat Kelulusan")

nilai_teori = float(input("Masukan nilai teori: "))
nilai_praktik = float(input("Masukan nilai praktek: "))

lulus = (nilai_teori > 75) and (nilai_praktik > 75)

print(f"Status Kelulusan : {lulus}")

#Latihan 2.3
print("LATIHAN 2.3 - Pengecekan Hari Libur")
is_weekend = False 
is_tanggal_merah = True

pergi_gacoan = is_weekend or is_tanggal_merah

print(f"Pergi ke Gacoan sahabat? {pergi_gacoan}")

#Latihan 2.4
print("LATIHAN 2.4 - Menggunakan not")

sedang_sibuk = True
apakah_aku_bebas = not sedang_sibuk

print(f"Apakah aku lagi sibuk? {sedang_sibuk}")
print(f"Apakah aku nyantai? {apakah_aku_bebas}")

#Tantangan 
print("Tantangan - Pengecekan Tiket Wahana")

tinggi_badan= int(input("Masukan tinggi badan kamu (cm): "))
usia = int(input("Masukan usia kamu (tahun): "))
jawaban_penyakit = input("Apakah kamu punya riwayat penyakit jantung (ya/tidak): ")

punya_penyakit_jantung = (jawaban_penyakit == "ya")

syarat_tinggi = (tinggi_badan >= 170)
syarat_usia = (usia >= 17)
syarat_kesehatan = not punya_penyakit_jantung

boleh_naik = syarat_tinggi and syarat_kesehatan and syarat_usia

print(f"Tinggi >= 160 cm: {syarat_tinggi}")
print(f"Usia >= 14 tahun: {syarat_usia}")
print(f"Tidak punya penyakit jantung: {syarat_kesehatan}")
print(f"--- Boleh Naik Wahana: {boleh_naik} ---")