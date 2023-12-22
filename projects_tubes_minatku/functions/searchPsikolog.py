import sys
sys.path.append('./database')

from data import dataPsikolog

dataPsikolog.sort(key=lambda x: x["nama"].lower())  # Urutkan nama dalam huruf kecil

targetName = input("Masukkan nama psikolog atau sebagian dari nama yang ingin dicari: ").lower()


def is_partial_match(name, partial):
    return partial in name.lower()

def binary_search_partial(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = arr[mid]["nama"].lower()

        if is_partial_match(mid_name, target):
            return arr[mid]
        elif mid_name < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

def display_result(result):
    if result:
        print("Psikolog ditemukan:")
        print("Nama:", result["nama"])
        print("Kategori:", result["category"])
        print("Instagram:", result["instagram"])
    else:
        print("Psikolog tidak ditemukan.")

# Lakukan pencarian binary
result = binary_search_partial(dataPsikolog, targetName)
# Tampilkan hasil
display_result(result)
