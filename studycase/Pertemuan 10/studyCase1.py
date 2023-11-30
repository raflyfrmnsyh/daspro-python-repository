# Ketentuan Soal 
# 1. Array 1 Dimensi, menyimpan 10 data suhu dalam 10 hari terakhir.
# 2. Ilmuan tersebut ingin melakukan konfersi suhu Celcius to Farenhit
# 3. Note : Buat data dummy untuk suhu 10 hari tersebut

import numpy as np # Import Library

def fahrenhit(celcius) :
    result = (celcius * 9/5) + 32 # Rumus konfersi celcius to fahrenhit
    print(f"Dalam satuan Fahrenhit : {result}")
suhu = np.array([28,34,27,16,30,33,26,24,22,35])

print(f"Dalam satuan Celcius : {suhu}")
fahrenhit(suhu)