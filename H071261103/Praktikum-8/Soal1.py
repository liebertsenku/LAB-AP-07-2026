import re

print("=== Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM     : ")
email = input("Masukkan Email   : ")
telepon = input("Masukkan No. Telp : ")

def validasi_mahasiswa(nim, email, telepon):
    pola_nim = r'^H071\d{6}$'
    pola_email = r'^[a-zA-Z0-9]+@(gmail|yahoo|outlook)\.(com|id)$'
    pola_telepon = r'^\d{10,13}$'

    cek_nim = re.match(pola_nim, nim)
    cek_email = re.match(pola_email, email)
    cek_telepon = re.match(pola_telepon, telepon)

    print("\n--- Hasil Validasi ---")
    if cek_nim:
        status_nim = "Valid"
    else:
        status_nim = "Tidak Valid"
    print(f"{'NIM':<13} : {status_nim}")

    if cek_email:
        status_email = "Valid"
    else:
        status_email = "Tidak Valid"
    print(f"{'Email':<13} : {status_email}")

    if cek_telepon:
        status_telepon = "Valid"
    else:
        status_telepon = "Tidak Valid"
    print(f"{'No. Telepon':<13} : {status_telepon}")

    if cek_nim and cek_email and cek_telepon:
        print("\nData mahasiswa berhasil diverifikasi!")
    else :
        print("\nData mahasiswa tidak berhasil diverifikasi!")
        
validasi_mahasiswa(nim, email, telepon)