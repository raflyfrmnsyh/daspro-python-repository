import time
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

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

start_time = time.perf_counter()
linearSearch(array, 60)
end = time.perf_counter()

print(f"Waktu yang dibutuhkan untuk melakukan linear search adalah {(end - start_time):.17f} ms")