# Nama  : Rafly Firmansyah
# NIM   : 2310601   
# Kelas : RPL 1C


thisArr = []
n = int(input("Masukan jumlah array yang akan anda buat : "))

for i in range(n):
    arr = int(input("Masukan nilai Array : "))
    thisArr.append(arr)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


print(f"Ini adalah array sebelum di sorting : {thisArr}")
print(f"Ini adalah array sesudah di sorting : {bubbleSort(thisArr)}")