# Selisih Waktu

fTimeInput = input("Masukan waktu dengan format, Jam-Menit-Detik [3 jam 8 menit 10 detik] : ")
lTimeInput = input("Masukan waktu dengan format, Jam-Menit-Detik [3 jam 8 menit 10 detik] : ")

def selisih(awal, akhir):
    awal = [int(item) for item in awal]
    akhir = [int(item) for item in akhir]
    
    jam = akhir[0] - awal[0]
    menit = akhir[1] - awal[1]
    detik = akhir[2] - awal[2]

    print(f"Selisih waktunya adalah : {jam} Jam - {menit} menit - {detik} detik")

def validate(inputAwal, inputAkhir):
    inputAwal = inputAwal.lower()
    inputAwal = inputAwal.replace(' jam', ' ').replace(' menit', ' ').replace(' detik', ' ')
    a = inputAwal.split()

    inputAkhir = inputAkhir.lower()
    inputAkhir = inputAkhir.replace(' jam', ' ').replace(' menit', ' ').replace(' detik', ' ')
    b = inputAkhir.split()

    valuesA = len(a)
    valuesB = len(b)
    if valuesA == 3 and valuesB > 3 :
        print("format inputan waktu akhir anda salah!")
    elif valuesA > 3 and valuesB == 3 :
        print("format inputan waktu awal anda salah!")
    elif valuesA and valuesB > 3 : 
        print("Anda memasukan format yang salah")
    elif valuesA and valuesB == 3 :
        print(f"=== Jam Mulai ===\nJam : {a[0]}\nMenit : {a[1]}\nDetik : {a[2]}")
        print(f"=== Jam Akhir ===\nJam : {b[0]}\nMenit : {b[1]}\nDetik : {b[2]}")
        selisih(a, b)

validate(fTimeInput, lTimeInput)
    

