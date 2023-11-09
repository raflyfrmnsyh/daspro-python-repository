panjang = int(input("Panjang : "))
lebar = int(input("lebar : "))
tinggi = int(input("Tinggi : "))

def totalHarga(panjang, lebar, tinggi):
    a = 2 * (panjang*tinggi) + 2 * (lebar*tinggi)
    harga = 450000
    print(f"Rp.{a * harga}")

totalHarga(panjang, lebar, tinggi)
