# NAMA  : RAFLY FIRMANSYAH
# NIM   : 2310601
# KELAS : RPL 1C

arr = []
n = int(input("Masukan jumlah array : "))

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
        print(f"Array {n} ditemukan pada index ke-{result}")
    else:
        print(f"Maaf nilai yang anda cari tidak ada")

for i in range(n):
    array = int(input("Masukan Nilai array : "))
    arr.append(array)

search = int(input("Cari nilai array : "))
result = binarySearch(arr, search)
checkSearch(result, search)

    