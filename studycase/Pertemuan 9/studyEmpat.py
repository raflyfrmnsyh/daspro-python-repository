# Fitur Login Sederhana
# Ketentuan, Kesempatan login hanya 3 kali apabila login gagal berturut-turut

dataBase = {
    "username" : "Daspro2023",
    "password" : "Latihan"
}

chance = 3
username = input("Masukan Username : ")

def login(username):
    global chance
    
    while chance > 0:
        password = input("Masukan Password : ")
        if username != dataBase["username"] and password != dataBase["password"]:
            chance -= 1
            if chance > 0 :
                print(f"Maaf username dan password salah!, kesempatan anda tersisa {chance} kali lagi")
            elif chance == 0 :
                print(f"Akses login diblokir!")
        elif username == dataBase["username"] and password == dataBase["password"]:
            print("Login Berhasil!")
            break

login(username)