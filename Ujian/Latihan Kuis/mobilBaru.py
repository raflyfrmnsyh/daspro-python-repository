mobil = {
    "merk" : "Honda",
    "tipe" : "HRV",
    "tahun" : 2018,
    "warna" : "hitam",
    "noPolice" : "D 1234 ABC",
    "bensin" : "pertalite",
    "transmisi" : "manual"
}

print("=================================")
print(f"Mobil lama pak oki adalah : \nMerk : {mobil['merk']}\nTipe Mobil : {mobil['tipe']}\nWarna : {mobil['warna']}\nTahun : {mobil['tahun']}\n=================================")

merk = input("Merk mobil baru : ")
tipe = input("Tipe mobil baru : ")
tahun = input("Tahun mobil baru : ")
warna = input("Warna mobil baru : ")
noPOlice = input("Nomor polisi mobil baru : ")
bensin = input("Jenis bensin pada mobil baru : ")
transmisi = input("Transmisi mobil baru : ")
print("=================================")
mobil.update({"merk":merk, "tipe":tipe, "tahun":tahun, "noPolice":noPOlice,"bensin":bensin, "transmisi":transmisi})

print(f"Mobil Baru pak oki adalah : \nMerk : {mobil['merk']}\nTipe Mobil : {mobil['tipe']}\nWarna : {mobil['warna']}\nTahun : {mobil['tahun']}\n=================================")