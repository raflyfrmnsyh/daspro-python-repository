# Fitur Login Sederhana
# Ketentuan, Kesempatan login hanya 3 kali apabila login gagal berturut-turut

dataBase = {
    "username" : "Daspro2023",
    "password" : "Latihan"
}
chance = 3
def loginProcess(username, password) :
    global chance
    if username != dataBase["username"] and password != dataBase["password"] :
        chance -= 1

        if chance > 0 :
            print(f"Login gagal! kesempatan tersisa {chance} kali lagi")
        elif chance == 0 :
            print(f"Akses Login diblokir!")

        return False
    elif username == dataBase["username"] and password == dataBase["password"]:
        print(f"Login success! Selamat datang {username}")
        return True



while chance > 0 :
    print("=====================================")
    print("             HALAMAN LOGIN           ")
    print("=====================================")
    username = input("Masukan Username :")
    password = input("Masukan Password :")
    print("=====================================")

    if loginProcess(username, password):
        break