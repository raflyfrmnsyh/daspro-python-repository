panjang = 100 # meter
lebar = 4800 # centimeter
putaran = 10 # 10 kali putaran

panjang = panjang / 1000
lebar = lebar / 10000

def kelilingPersegiPanjang():
    a = 2 * (panjang + lebar)
    print(a * putaran)

kelilingPersegiPanjang()