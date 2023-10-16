# KETENTUAN SOAL
# 1. Diskon berdasarkan total belanjaan
# 2. Jika melebihi 500.000 maka pelanggan akan mendapatkan diskon sebesar 10%
# 3. Jika belanjaan kurang dari 500.000 maka tidak akan mendapatkan diskon
# 4. Input total belanjaan pelanggan dan menentukan apakah mereka berhak mendapatkan diskon atau    tidak
# 5. Hitung total yang harus dibayar setelah diskon (Jika berhak mendapatkan diskon)

print("====================================")
print("|      SISTEM PEMBAYARAN KASIR      |")
print("====================================")

nama = input("Masukan Nama Pelanggan : ")
bayar = int(input("Masukan Total harga belanja : "))
diskon = (bayar/100)*10
if bayar > 500000:
    total = bayar - diskon
    print(f"Bapak/Ibu {nama} selamat anda mendapatkan Diskon 10%\n")
    print("====================================")
    print("         KWITANSI PEMBELIAN         ")
    print("====================================")
    print(f"Pelanggan : {nama}\nDiskon : Dapat potongan 10%\nTotal : {bayar}\nPotongan : - Rp.{int(diskon)}\n====================================\nTotal Harga : Rp.{int(total)}")
    print("====================================")
else:
    print(f"Maaf Bapak/Ibu {nama} belum mendapatkan Diskon 10%\n")
    print("====================================")
    print("         KWITANSI PEMBELIAN         ")
    print("====================================")
    print(f"Pelanggan : {nama}\nDiskon : Tidak dapat\nTotal : {bayar}\nPotongan : - Rp.0\n====================================\nTotal Harga : Rp.{int(bayar)}")
    print("====================================")
