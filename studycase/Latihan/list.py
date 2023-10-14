# STUDI KASUS LIST & TUPLE
# Buatlah sebuah list yaitu buah = ["apel", "jeruk", "ceri", "durian", "apel“, “mangga“]
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(buah[2:5]) # 1. Buatlah program untuk mengambil list ke 2-5
print("--------------------------------")
buah.pop(4) # 2. Hapus item “apel“ yang kedua
buah[2] = "cherry" # 3. Ganti item dengan nama “ceri” menjadi “cherry”
buah.insert(2, 'strawberry') # 4. Tambahkan item dengan nama “strawberry” ke dalam index ke-3
buah.sort() # 5. Urutkan item pada list sesuai dengan abjadnya
print(buah)
print("--------------------------------")

