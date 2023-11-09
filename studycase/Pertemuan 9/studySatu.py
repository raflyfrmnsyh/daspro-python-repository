# Deret Fibonnaci menggunakan fungsi
# Contoh Fibonnaci
# [1,1,2,3,5,8]
# Bilangan selanjutnya merupakan hasil penjumlahan dua bilangan sebelumnya

n = int(input("Masukan deret angka terakhir : "))

def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # Menjumlahkan dua bilangan terakhir pada list fibo di variable fib_squence

    return fib_sequence

# Contoh pemanggilan fungsi untuk mencetak deret Fibonacci dengan 10 angka
result = fibonacci(n)
print(f"Deret Fibonacci dengan 10 angka: {result}")