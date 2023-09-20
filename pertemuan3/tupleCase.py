# Case study list

buah = ("Apel", "Jeruk", "Ceri", "Durian","Apel", "Mangga")

print(buah[2:5], "Nomor 1") # Mencetak data pada tupple 2-5
listType = list(buah) # Melakukan convert type data

listType.pop(3) # Menghapus data durian yang ada di index 3
listType.insert(2, "Manggis") # Menambahkan data manggis diantara Jeruk dan ceri

tuppleType = tuple(listType) # Konversi tipe data list ke tupple
print(tuppleType, "Nomor 2 & 3") # Melakukan Print
