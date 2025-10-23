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

print("=== HASIL KALKULASI KEUANGAN ===")
print(f"Saldo Awal: Rp {saldo_awal:,.0f}")
print(f"Pemasukan Bulanan: Rp {pemasukan_bulanan:,.0f}")
print(f"Pengeluaran Tetap: Rp {pengeluaran_tetap:,.0f}")
print(f"Investasi Bulanan: Rp {investasi_bulanan:,.0f}")
print("========================================")
print(f"1. Saldo setelah transaksi: Rp {saldo_setelah_transaksi:,.0f}")
print(f"2. Investasi 6 bulan (5% bunga): Rp {investasi_6_bulan:,.2f}")
print(f"3. Persentase tabungan: {persentase_tabungan:.2f}%")
print(f"4. Prediksi saldo 1 tahun: Rp {saldo_1_tahun:,.0f}")