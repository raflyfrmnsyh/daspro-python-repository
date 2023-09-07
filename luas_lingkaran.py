# Program Aplikasi untuk menghitung Luas Lingkaran
print("\nPROGRAM MENGHITUNG LUAS LINGKARAN\n")

phi = 3.14  # 1. Menginisialisasikan terlebih dahulu nilai phi
r = int(input("Nilai Jari Jari :")) # 2. Membuat input user untuk nilai jari jari
r2 = r ** 2 # 3. Menghitung r kuadrat

luas = phi * r2 # 4. Menghitung dengan rumus lingkaran phi x r kuadrat
print("Luas Lingkaran :", luas)

