# Program Kalkulator Sederhana
print("=========================================\n")
print("      PROGRAM KALKULATOR SEDERHANA\n")
print("=========================================\n")
print("Pilih Oprator Aritmatika\n 1. Penjumlahan\n 2. Pengurangan\n 3. Perkalian\n 4.Pembagian\n5.Modulus")
print("=========================================\n")
oprator = input("Pilih Oprator : ")
print("=========================================\n")

if oprator == "1" :
    nilai1 = int(input("Masukan nilai pertama : "))
    nilai2 = int(input("Masukan nilai kedua : "))

    hasil = nilai1 + nilai2
    print(f"{nilai1} + {nilai2} = {hasil}")
elif oprator == "2" :
    nilai1 = int(input("Masukan nilai pertama : "))
    nilai2 = int(input("Masukan nilai kedua : "))

    hasil = nilai1 - nilai2
    print(f"{nilai1} - {nilai2} = {hasil}")
elif oprator == "3" :
    nilai1 = int(input("Masukan nilai pertama : "))
    nilai2 = int(input("Masukan nilai kedua : "))

    hasil = nilai1 * nilai2
    print(f"{nilai1} x {nilai2} = {hasil}")
elif oprator == "4" :
    nilai1 = int(input("Masukan nilai pertama : "))
    nilai2 = int(input("Masukan nilai kedua : "))

    hasil = nilai1 / nilai2
    print(f"{nilai1} / {nilai2} = {hasil}")
elif oprator == "5" :
    nilai1 = int(input("Masukan nilai pertama : "))
    nilai2 = int(input("Masukan nilai kedua : "))

    hasil = nilai1 % nilai2
    print(f" {nilai1} % {nilai2} = {hasil}")
else :
    print("Tidak terdifinisi")



