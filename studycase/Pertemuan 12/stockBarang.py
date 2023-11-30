# Sebuah toko memiliki stok barang yang tersedia, buatlah program untuk mencari apakah suatu barang tersedia dalam stok toko

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
        print(f"Stok barang {n} ditemukan pada index ke-{result}")
    else:
        print(f"Stock barang {n} tidak ditemukan pada array stok barang")


arrStk = [1,2,5,7,8,10,16,18,19,23,24,26,28,29,32]
searchBox = int(input("Search stok : "))
resultSearch = binarySearch(arrStk, searchBox)
checkSearch(resultSearch, searchBox)
