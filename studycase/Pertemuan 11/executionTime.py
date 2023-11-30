# Rafly Firmansyah
# 2310601 - 1C
import time # import modul time

# Bubble Sort
def bubbleSort(arr) :
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertionSort(arr) :
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# QuickSort
def quickSort(arr) :
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

# MergeSort
def mergeSort(arr) :

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


unoRay = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76,
10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

# Mengukur waktu untuk Bubble Sort
start_time = time.time()
bubbleSort(unoRay.copy())  # Salin array untuk menghindari perubahan array asli
end_time = time.time()
print("Waktu eksekusi Bubble Sort:", end_time - start_time, "detik")

# Mengukur waktu untuk Insertion Sort
start_time = time.time()
insertionSort(unoRay.copy())
end_time = time.time()
print("Waktu eksekusi Insertion Sort:", end_time - start_time, "detik")

# Mengukur waktu untuk QuickSort
start_time = time.time()
quickSort(unoRay.copy())
end_time = time.time()
print("Waktu eksekusi QuickSort:", end_time - start_time, "detik")

# Mengukur waktu untuk MergeSort
start_time = time.time()
mergeSort(unoRay.copy())
end_time = time.time()
print("Waktu eksekusi MergeSort:", end_time - start_time, "detik")