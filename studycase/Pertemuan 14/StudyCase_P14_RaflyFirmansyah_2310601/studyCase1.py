# PERTEMUAN 14
# RAFLY FIRMANSYAH | 2310601

def hitung_rata_rata(file):
    total_nilai = 0
    jumlah_siswa = 0

    with open(file, "r") as file:
        for i in file:
            parts = i.strip().split(":")
            if len(parts) == 2 :
                nama = parts[0].strip()
                nilai = int(parts[1].strip())

                total_nilai += nilai
                jumlah_siswa += 1
    if jumlah_siswa > 0 :
        rata_rata = total_nilai / jumlah_siswa
        return rata_rata
    else :
        return 0

path = "data/dataSiswa.txt"
rata_rata_nilai = hitung_rata_rata(path)

with open(path, "r") as siswa :
    print(siswa.read())

print("----------------------------------------------------")
print(f"Nilai rata-rata ujian : {rata_rata_nilai:.2f}")
print("----------------------------------------------------")