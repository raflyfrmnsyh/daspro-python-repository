def checkSearch(result, n, t) :
    if result != -1 :
        print(f"Data {n} ditemukan pada index ke-{result} dengan metode {t}")
    else:
        print(f"Data {n} tidak ditemukan pada List Mahasiswa")

def linearSearch(arr, n) :
    x = len(arr)

    for i in range(x) :
        if arr[i] == n:
            return i
    return -1

def binarySearch(arr, n) :
    inLow = 0
    inHigh = len(arr)

    while inLow <= inHigh :
        mid = (inLow + inHigh) // 2
        midValue = arr[mid]

        if midValue == n :
            return mid
        elif midValue < n :
            inLow = mid + 1
        else :
            inHigh = mid - 1
    return -1


rplC = [
    "hilman", "daniel", "dhexy", "didra", "dyna", "fadli", "fahri", "gilang", "kinta", "kiroman", "laras", "mirza", "fatir", "daffa", "dzaky", "fauzan", "mufthi", "ilham", "nabil", "afkar", "nia", "purba", "rafly", "restu", "roy", "septiawan", "steven", "syahrul", "vina"
]
linear = "Linear Search"
binary = "Binary Search"
search = input("Cari mahasiswa : ").lower()

linearResult = linearSearch(rplC, search)
binaryResult = binarySearch(rplC, search)

checkSearch(linearResult, search, linear)
checkSearch(binaryResult, search, binary)