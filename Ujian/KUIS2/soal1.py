# Nama  : Rafly Firmansyah
# NIM   : 2310601
# KELAS : RPL 1C


daftarBuku = [
    {
        "judul":"Petualangan Sang Pemberani",
        "penulis":"Dewi Kusuma",
        "kode":"BK001",
        "status":"tersedia"
    },
    {
        "judul":"Misteri Kota Terlarang",
        "penulis":"Budi Santoso",
        "kode":"BK002",
        "status":"tersedia"
    },
    {
        "judul":"Jalan Panjang Pulang",
        "penulis":"Linda Wijaya",
        "kode":"BK003",
        "status":"tersedia"
    }
]

judul = input("Masukan Judul buku :")
penulis = input("Masukan penulis buku : ")
kode = input("Masukan Kode Buku : ")

def tambahBuku(judul, penulis, kode):
    newBook = {
        "judul":judul,
        "penulis":penulis,
        "kode":kode,
        "status":"tersedia"
    }
    daftarBuku.append(newBook)
    print(daftarBuku)


def pinjamBuku(kode) :
    pass

def kembalikanBuku(kode):
    pass

def lihatBuku(arr):
    pass

def searchBuku(arr, search):
    pass