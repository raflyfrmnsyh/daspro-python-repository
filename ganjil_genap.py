# Program Aplikasi untuk menentukan nilai ganjil genap
print("\nPROGRAM MENENTUKAN NILAI GANJIL GENAP\n")

angka = int(input("Masukan angka :"))

if angka % 2 == 0 :
    print("Angka yang anda masukan merupakan bilangan genap")
elif angka % 2 == 1 :
    print("Angka yang anda masukan merupakan bilangan ganjil")
else :
    print("Angka tidak terdifinisi")