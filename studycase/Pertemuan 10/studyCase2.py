import numpy as np

# Data dummy nilai ujian untuk 30 siswa
nilaiUjian = np.array([85, 92, 78, 95, 88, 72, 90, 86, 89, 93,
                        80, 96, 87, 91, 82, 75, 94, 79, 83, 88,
                        77, 98, 84, 89, 76, 97, 81, 92, 74, 90])


urutanNilai = np.sort(nilaiUjian)[::-1] # Mengurutkan nilai ujian dari yang terbesar hingga terkecil

# Menampilkan seluruh nilai ujian
print("Seluruh nilai ujian:", urutanNilai)

# Menampilkan 5 nilai terbesar
print("5 nilai terbesar:", urutanNilai[:5])