# Program membuat kalkulator sederhana
print("=========================================\n")
print("      PROGRAM KALKULATOR SEDERHANA\n")
print("=========================================\n")

nilai1, nilai2, nilai3 = int(input("Nilai a : ")), int(input("Nilai b : ")), int(input("Nilai c : "))  # Menampung hasil inputan kedalam varibale nilai
print("=========================================\n")

perjumlahan = nilai1 + nilai2 + nilai3 # Melakukan perhitungan perjumlahan
pengurangan = nilai1 - nilai2 - nilai3 # Melakukan perhitungan Penguranga
perkalian = nilai1 * nilai2 * nilai3 # Melakukan perhitungan Perkalian
pembagian = nilai1 / nilai2 / nilai3 # Melakukan perhitungan Pembagian

print(f"{nilai1} + {nilai2} + {nilai3} = {perjumlahan}") # Menampilkan hasil perjumlahan
print("\n=========================================\n")
print(f"{nilai1} - {nilai2} - {nilai3} = {pengurangan}") # Menampilkan hasil pengurangan
print("\n=========================================\n")
print(f"{nilai1} x {nilai2} x {nilai3} = {perkalian}") # Menampilkan hasil perkalian
print("\n=========================================\n")
print(f"{nilai1} / {nilai2} / {nilai3} = {pembagian}") # Menampilkan hasil pembagian
print("\n=========================================\n")