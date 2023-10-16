# KETENTUAN SOAL
# 1. Karyawan (sangat baik) akan mendapatkan bonus 20% dari gajih mereka
# 2. Karyawan (cukup) akan mendapatkan bonus 10%
# 3. Karyawan lainnya hanya mendapatkan bonus 5%
# 4. User melakukan input performa dan gaji karyawan.
# 5. Menghitung jumlah bonus yang diterima

print("==============================")
print("SISTEM GAJIH PT.CREATIVEAGENCY")
print("==============================")
nama = input("Nama Karyawan : ")
print("PERFORMA KARYAWAN PT.CREATIVEAGENCY\n1. Sangat Baik\n2. Baik\n3.Kurang baik\n4. Buruk")
perform = int(input("PERFORMA KARYAWAN :"))

if (perform == 1):
    gaji = int(input("Masukan Gaji bulan ini : "))
    bonus = (gaji / 100) * 20
    total = gaji + bonus
    print(f"Total Gaji yang didapatkan oleh {nama} sebesar Rp.{total},00")
elif (perform == 2):
    gaji = int(input("Masukan Gaji bulan ini : "))
    bonus = (gaji / 100) * 10
    total = gaji + bonus
    print(type(total))
    print(f"Total Gaji yang didapatkan oleh {nama} sebesar Rp.{total},00")
elif (perform == 3 & perform == 3):
    gaji = int(input("Masukan Gaji bulan ini : "))
    print(
        f"Karyawan bernama {nama} belum memiliki intensif bonus gaji bulan ini")
else:
    print(f"Maaf yang anda inputkan tidak sesuai")
