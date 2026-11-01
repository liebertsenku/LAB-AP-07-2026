
import re

print("=== Validasi Data Mahasiswa ===")

def validasi_data(nim, email, nomor):
    match_nim = re.search(r'^H071\d{6}$', nim)
    match_email = re.search(r'^\w+@\w+\.\w+$', email)
    match_nomor = re.search(r'^\d{10,13}$', nomor)

    if match_nim:
        print("NIM valid.")
    else:
        print("Format NIM tidak valid!")

    if match_email:
        print("Email valid.")
    else:
        print("Format email tidak valid!")

    if match_nomor:
        print("Nomor telepon valid.")
    else:
        print("Nomor telepon tidak valid!")

    if match_nim and match_email and match_nomor:
        print("Data mahasiswa berhasil diverifikasi!")


nim = input("Masukkan NIM       : ").strip().capitalize()
email = input("Masukkan Email     : ").strip()
nomor = input("Masukkan No. Telp  : ").strip()

print("\n--- Hasil Validasi ---")
validasi_data(nim, email, nomor)
