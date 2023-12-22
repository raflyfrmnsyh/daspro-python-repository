import re
import time

# Inisialisasi data penyimpanan
data_pengguna = []

# Fungsi untuk mengecek kekuatan password
def cek_kekuatan_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()-_=+{};:,<.>]", password):
        return False
    return True

# Fungsi untuk mendaftar
def mendaftar():
    print("=== Mendaftar ===")
    print("Note: Jangan berikan informasi pribadi atau menggunakan kata sandi yang mudah ditebak.")
    print("Perhatian: Kata sandi harus memiliki panjang minimal 8 karakter, mengandung setidaknya satu huruf kapital, satu angka, dan satu simbol khusus.")

    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = input("Masukkan kata sandi: ")

    # Validasi kata sandi
    while not cek_kekuatan_password(kata_sandi):
        print("Kata sandi tidak memenuhi persyaratan.")
        kata_sandi = input("Masukkan kata sandi yang valid: ")

    # Menambahkan data pengguna ke dalam array
    data_pengguna.append({"nama_pengguna": nama_pengguna, "kata_sandi": kata_sandi})
    print("Pendaftaran berhasil. Selamat datang,", nama_pengguna)

# Fungsi untuk masuk
def masuk():
    print("=== Masuk ===")
    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = input("Masukkan kata sandi: ")

    # Mencari pengguna di dalam array
    pengguna_ditemukan = False
    for pengguna in data_pengguna:
        if pengguna["nama_pengguna"] == nama_pengguna and pengguna["kata_sandi"] == kata_sandi:
            pengguna_ditemukan = True
            break

    if pengguna_ditemukan:
        print("Login berhasil. Selamat datang kembali,", nama_pengguna)
        # Masuk ke sistem selanjutnya (coming soon)
    else:
        print("Nama pengguna atau kata sandi tidak valid. Silakan coba lagi.")
        percobaan_masuk = 0

        # Memberikan kesempatan maksimal 5 kali
        while percobaan_masuk < 5:
            nama_pengguna_percobaan = input("Masukkan nama pengguna lagi (atau ketik 'cls' untuk menyerah): ")

            # Jika pengguna menyerah
            if nama_pengguna_percobaan.lower() == 'cls':
                print("Anda menyerah. Terima kasih telah menggunakan layanan kami.")
                break

            kata_sandi_percobaan = input("Masukkan kata sandi lagi: ")

            # Mencari pengguna di dalam array
            pengguna_ditemukan = False
            for pengguna in data_pengguna:
                if pengguna["nama_pengguna"] == nama_pengguna_percobaan and pengguna["kata_sandi"] == kata_sandi_percobaan:
                    pengguna_ditemukan = True
                    break

            if pengguna_ditemukan:
                print("Login berhasil. Selamat datang kembali,", nama_pengguna)
                # Masuk ke sistem selanjutnya (coming soon)
                break
            else:
                print("Nama pengguna atau kata sandi tidak valid. Silakan coba lagi.")
                percobaan_masuk += 1

                # Mengalami jeda dengan waktu yang ditentukan
                waktu_tunggu = 5 * percobaan_masuk
                print(f"Anda harus menunggu {waktu_tunggu} detik sebelum mencoba lagi.")
                time.sleep(waktu_tunggu)

# Fungsi untuk mengganti kata sandi
def ganti_kata_sandi():
    print("=== Ganti Kata Sandi ===")
    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = input("Masukkan kata sandi saat ini: ")

    # Mencari pengguna di dalam array
    pengguna_ditemukan = False
    for pengguna in data_pengguna:
        if pengguna["nama_pengguna"] == nama_pengguna and pengguna["kata_sandi"] == kata_sandi:
            pengguna_ditemukan = True
            break

    if pengguna_ditemukan:
        kata_sandi_baru = input("Masukkan kata sandi baru: ")

        # Validasi kata sandi baru
        while not cek_kekuatan_password(kata_sandi_baru):
            print("Kata sandi harus memenuhi persyaratan.")
            kata_sandi_baru = input("Masukkan kata sandi baru yang valid: ")

        # Mengganti kata sandi
        pengguna["kata_sandi"] = kata_sandi_baru
        print("Kata sandi berhasil diubah.")
    else:
        print("Nama pengguna atau kata sandi tidak valid. Tidak dapat mengubah kata sandi.")

# Fungsi untuk menghapus akun
def hapus_akun():
    print("=== Hapus Akun ===")
    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = input("Masukkan kata sandi: ")

    # Mencari pengguna di dalam array
    pengguna_ditemukan = False
    for pengguna in data_pengguna:
        if pengguna["nama_pengguna"] == nama_pengguna and pengguna["kata_sandi"] == kata_sandi:
            pengguna_ditemukan = True
            break

    if pengguna_ditemukan:
        konfirmasi = input("Apakah Anda yakin ingin menghapus akun Anda? (ya/tidak): ")
        if konfirmasi.lower() == "ya":
            data_pengguna.remove(pengguna)
            print("Akun berhasil dihapus.")
        else:
            print("Penghapusan akun dibatalkan.")
    else:
        print("Nama pengguna atau kata sandi tidak valid. Tidak dapat menghapus akun.")

# Fungsi untuk menampilkan menu
def tampil_menu():
    print("\n=== Menu ===")
    print("1. Mendaftar")
    print("2. Masuk")
    print("3. Ganti Kata Sandi")
    print("4. Keluar")

# Menampilkan menu saat pertama kali pengguna mengakses sistem
tampil_menu()

# Menu utama
while True:
    pilihan = input("Masukkan pilihan Anda (1-5): ")

    if pilihan == "1":
        mendaftar()
    elif pilihan == "2":
        masuk()
    elif pilihan == "3":
        ganti_kata_sandi()
    elif pilihan == "5":
        print("Selamat tinggal!")
        break
    else:
        print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 5.")