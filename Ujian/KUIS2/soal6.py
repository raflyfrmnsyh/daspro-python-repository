# NAMA  : Rafly Firmansyah
# NIM   : 2310601
# KELAS : RPL 1C

jmlSiswa = int(input("Masukan jumlah siswa : "))
dataSiswa = []
nilaiSiswa = []

for i in range(jmlSiswa):
    nama = input("Masukan Nama Siswa : ")
    nilai = int(input("Masukan Nilai Akhir : "))
    dataSiswa.append({"nama":nama,"nilai":nilai,"peringkat":0})

for siswa in dataSiswa:
    pass

def sortingNilai(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


print(sortingNilai(nilaiSiswa))

def checkNilai(arr):
    n = len(arr)

    for nilai in arr :
        pass