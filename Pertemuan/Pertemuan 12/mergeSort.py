def splitArray(arr):
    if len(arr) > 1 :
        middle = len(arr) // 2 # Membagi dua jumlah array
        left = arr[:middle] # Memisahkan array menjadi dua ke komplek kiri
        right = arr[middle:] # Memisahkan array menjadi dua ke komplek kanan

        return [left, right]

a = [12, 11, 7, 5, 10, 17, 1]

print(splitArray(a))
