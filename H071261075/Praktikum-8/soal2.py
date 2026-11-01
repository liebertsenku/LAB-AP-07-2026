import re

def validasi_username(username):
    hasil = re.search(r'^[\w][\w]{4,12}$', username)
    return hasil

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

daftar_username = []

while True:
    username = input("Masukkan username: ").strip()
    if username.strip().upper() == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print("\n=== Rekapitulasi ===")
print("Username valid:", daftar_username)
print("Jumlah username valid:", len(daftar_username))

