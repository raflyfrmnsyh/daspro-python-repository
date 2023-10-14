# Program Aplikasi untuk check kelulusan nilai daspro
print("\nPROGRAM CHECK KELULUSAN NILAI DASPRO\n")

nilai = int(input("Masukan Nilai UTS anda : "))

if (nilai >= 90):
    print("Selamat Nilai anda A")
elif(nilai >= 80 and nilai <= 90):
    print("Selamat Nilai anda B")
elif(nilai >= 70 and nilai <= 80):
    print("Selamat Nilai anda C")
else:
    print("Maaf Nilai anda D")