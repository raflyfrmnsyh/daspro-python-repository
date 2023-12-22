import sys
sys.path.append('./database')

from data import question_list
from data import bakatList
from data import pekerjaanList

def testResult(skor):
    mbti_type = (
        "E" if skor["extrovert"] >= 0 else "I"
    ) + (
        "S" if skor["sensing"] >= 0 else "N"
    ) + (
        "F" if skor["feeling"] >= 0 else "T"
    ) + (
        "J" if skor["judging"] >= 0 else "P"
    )

    bakatUmum = bakatList.get(mbti_type, "Tidak Diketahui")
    careerRec = pekerjaanList.get(mbti_type, "Tidak Ddiketahui")

    return mbti_type, bakatUmum, careerRec

def test(question):
    skor = {
        "extrovert": 0,
        "sensing": 0,
        "feeling": 0,
        "judging": 0
    }

    for i, pertanyaan in enumerate(question, start=1):
        answer = input(f"Pertanyaan {i} : {pertanyaan['soal']}\nJawab s=setuju dan t=tidak setuju : ")

        if answer.lower() == 's': 
            skor[pertanyaan['tipe']] += 1
        elif answer.lower() == 't' :
            skor[pertanyaan['tipe']] -= 1
            
    # Panggil fungsi test_result untuk mendapatkan hasil tes
    tipe_mbti, bakat_umum, pekerjaan_rekomendasi = testResult(skor)

    # Tampilkan hasil
    print("\nHasil Tes Minat Bakat Anda:")
    print(f"Tipe MBTI: {tipe_mbti}")
    print(f"Bakat Umum: {bakat_umum}")
    print(f"Rekomendasi Pekerjaan: {pekerjaan_rekomendasi}")

# Contoh cara menggunakan
test(question_list)
