# Method untuk mengambil data tahun sekarang
import datetime
today = datetime.date.today() 
nowYear = today.strftime("%Y")

nama = input(str("Nama Anda :")) # Mengambil nilai nama
tahun = int(input("Masukan tahun lahir anda : ")) # Mengambil nilai umur
umur = int(nowYear) - tahun # melakukan oprasi perhitungan

print(f"Nama anda adalah {nama} dan kamu berumur {umur} tahun ") 