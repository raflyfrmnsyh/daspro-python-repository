# KETENTUAN 
# Bilangan ganjil > 50
# Jika tidak memenuhi user akan dimintai lagi menginputkan angka

# Menginputkan data user
# Melakukan pengecheckan nilai yang di inputkan
# Jika angka yang di inputkan kurang dari 50 maka beri pesan error/wrong action
# Jika angka yang diinputkan lebih dari 50
    # Lakukan pengecheckan apakah yang di inputkan tersebut merupakan bilangan ganjil atau genap
        # Jika genap, beri pesan salah inputkan lagi -> dan kembali menginput
        # Jika benar maka beri pesan benar


while True:
    
    bilangan = int(input("Masukan bilangan ganjil lebih dari 50 : "))

    if bilangan > 50 :
        if bilangan % 2 == 0 :
            print(f"Salah, inputkan lagi : {bilangan}")
        elif bilangan % 2 == 1:
            print(f"Benar")
            break
    else:
        print("Nilai yang anda inputkan kurang dari 50, inputkan lagi!!")

