# Deret Fibonnaci menggunakan fungsi
# Contoh Fibonnaci
# Bilangan selanjutnya merupakan hasil penjumlahan dua bilangan sebelumnya

n = int(input("Masukan deret angka terakhir : "))

def fibonacci(n):
    fibo = [0, 1]

    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2]) # Menjumlahkan dua bilangan terakhir pada list fibo di variable fib_squence

    return fibo

# Contoh pemanggilan fungsi untuk mencetak deret Fibonacci dengan 10 angka
result = fibonacci(n)
print(f"Deret Fibonacci dengan {n} angka: {result}")