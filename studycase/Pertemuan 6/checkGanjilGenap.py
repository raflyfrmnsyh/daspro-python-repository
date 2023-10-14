# Program Aplikasi untuk menentukan nilai ganjil genap
print("\nPROGRAM MENENTUKAN NILAI GANJIL GENAP\n")

input = input("Masukan angka :") # User melakukan input
# Pengecheckan Tipe data yang di inputkan
if input.isdigit():
    print(f"{input} merupakan integer")
    angka = int(input)

    # Pengecheckan angka yang diinputkan
    if angka % 2 == 0 :
        print(f"Angka {angka} merupakan bilangan Genap ")
    elif angka % 2 == 1:
        print(f"Angka {angka} merupakan bilangan Ganjil")

# Kondisi apabila user menginputkan bukan angka
elif input.isalpha():
    print(f"Maaf silahkan masukan angka”")
