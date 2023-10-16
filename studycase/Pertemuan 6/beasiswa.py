print("==========================")
print("PROGRAM KELULUSAN BEASISWA")
print("==========================")

nama = input("Masukan Nama anda : ")
nilai = int(input("Masukan nilai ujian anda :"))
penghasilan = int(input("Masukan penghasilan orang tua : "))

full = nilai > 90 and penghasilan < 2000000
parsial = (nilai > 80 and nilai <= 90) and (penghasilan < 4000000)

if (full):
    print(f"Siswa bernama {nama} berhak mendapatkan Beasiswa Full")
elif (parsial):
    print(f"Siswa bernama {nama} berhak mendapatkan Beasiswa Parsial")
else:
    print(f"Maaf kepada saudara/i {nama} belum berhak mendapatkan Beasiswa")
