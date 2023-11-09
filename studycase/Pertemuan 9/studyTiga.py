# Menjumlahkan total nilai dan rata-ratanya
numInput = input("Masukan nilai-nilai, pisahkan dengan koma : ")
number = numInput.split(',')

def averageTotal (semua):
    result = []
    for i in semua:
        new = int(i)
        result.append(new)

    values = len(result)
    total = sum(result)
    average = total/values
    print(f"Total Nilai : {total}\nRata-Rata Nilai : {average}")

averageTotal(number)