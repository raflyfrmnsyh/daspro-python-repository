# PERTEMUAN 14
# RAFLY FIRMANSYAH | 2310601

import csv

def editStok(path, barang, tambah, kurang):
    with open(path, "r", newline='') as csvfile :
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    for row in rows :
        if row["Barang"] == barang:
            row["Jumlah"] == str(int(row["Jumlah"]) + tambah - kurang)
    with open(path, "w", newline='') as csvfile :
        nameField = ["Barang", "Jumlah"]
        writer = csv.DictWriter(csvfile, fieldnames=nameField)

        writer.writeheader()
        writer.writerows(rows)

def hitungStok(path):
    with open(path, "r", newline='') as csvfile :
        read = csv.DictReader(csvfile)
        stokAkhir = sum(int(row['Jumlah']) for row in read)
        
        return stokAkhir

path = "data/inventaris_barang.csv"
editStok(path, "Laptop", 10, 5)

stok = hitungStok(path)
print("----------------------------------------------------")
print("                    LIST BARANG                     ")
print("----------------------------------------------------")
with open(path, "r") as file :
    print(file.read())
print("----------------------------------------------------")
print(f"Stok Akhir : {stok}")
print("----------------------------------------------------")
