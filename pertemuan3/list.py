a = ["Apel", "Jeruk", "Ceri", "Durian", "Apel"]

print(len(a)) # Mengetahui jumlah data pada list
print(a[2]) # Mengambil data pada list
print(a[1:4]) # Mengambil beberapa data pada list

# Menambahkan data di akhir list
a.append("Semangka") 
print(a)

a.insert(3, "Manggis") # Menambahkan data pada tengah tengah atau index yang di tentukan
print(a) 

a[2] = "Kelengkeng"
print(a)

a.pop(3) # Menghapus data pada list
print(a)

test = ["Apple", ["Jam", "Dinding"], "Android"]
print(test[1][1])