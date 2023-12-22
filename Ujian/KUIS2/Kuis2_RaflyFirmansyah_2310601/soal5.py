# Nama  : Rafly Firmansyah
# NIM   : 2310601
# KELAS : RPL 1C

daftarMenu = ["ayam gulai", "babat","cumi", "ikan kembung", "kikil", "limpa", "otak", "paru", "rendang", "telur", "usus"]
cariMenu = input("Cari Menu : ")
n = cariMenu.lower()

def binarySearch(arr, n) :
    indexLow = 0
    indexHigh = len(arr)

    while indexLow <= indexHigh :
        mid = (indexLow + indexHigh) // 2 
        midValue = arr[mid]

        if midValue == n :
            return mid
        elif midValue < n :
            indexLow = mid + 1
        else :
            indexHigh = mid - 1
    return -1

def checkSearch(result, n) :
    if result != -1 :
        print(f"Tersedia")
    else:
        print(f"Tidak Tersedia")

result = binarySearch(daftarMenu, n)
checkSearch(result, n)