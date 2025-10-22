saldo_awal = 5000000
pemasukan_bulanan = 7500000
pengeluaran_tetap = 4500000
investasi_bulanan = 1000000

saldo_setelah_transaksi = saldo_awal + pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan

investasi_6_bulan = investasi_bulanan * 6 
investasi_6_bulan += investasi_bulanan * 0.05

tabungan =  pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan
persentase_tabungan = (tabungan / pemasukan_bulanan) * 100

saldo_1_tahun = saldo_awal
saldo_1_tahun += (pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan) * 12

print("==== HASIL KALKULASI KEUANGAN ====")
print("Saldo Awal: Rp.", saldo_awal)
print("Pemasukan Bulanan : Rp.", pemasukan_bulanan)
print("Pengeluaran Tetap: Rp.", pengeluaran_tetap)
print("Investasi Bulanan: Rp.", investasi_bulanan)