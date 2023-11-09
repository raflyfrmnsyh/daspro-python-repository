# Program Kalkulator Sederhana
print("=========================================\n")
print("      PROGRAM KALKULATOR SEDERHANA\n")
print("=========================================\n")
print("Pilih Oprator Aritmatika\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulus")
print("\n=========================================\n")
oprator = input("Pilih Oprator : ")
print("\n=========================================\n")

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



