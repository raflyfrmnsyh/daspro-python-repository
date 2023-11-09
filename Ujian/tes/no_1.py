# 1. ANALISIS SOAL
# 2. TEMUKAN KEYPOINT PADA SOAL/BRIEF
# KEYPOINT
# - Menghitung total biaya yang Pak Abi harus keluarkan
# - biaya = Rp. 450.000/m2
# - rumus 2 × (Panjang × Tinggi) + 2 × (Lebar × Tinggi)
# - panjang = 8 meter
# - lebar = 1000 centimeter
# - tinggi = 4 meter

# Dari sini kita bisa melihat jika terdapat perbedaan satuan panjang. kita bisa membuat program konversi satuan angka tapi karena di soal tidak ada perintah seperti itu jadi asumsikan kita tahu dalam satu meter itu berapa centimeter

biaya = 450000
panjang = 8
lebar = 4
tinggi = 10
rumus = 2 * (panjang * tinggi) + 2 * (lebar*tinggi)

total_biaya = rumus * biaya

print(f"Total biaya yang perlu dibayarkan adalah Rp.{total_biaya}")