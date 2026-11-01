import re 
print ("=== Registrasi Username ===")
print ("Ketik 'SELESAI' untuk mengakhiri.")
username_valid = []
def cek_username (nama) :
    validasi_username = r'^[a-zA-Z]\w{4,11}$'
    cek_username = re.match(validasi_username,nama)
    if cek_username :
        print ("Username tersedia.")
        return True
    else :
        print ("Username tidak valid!")
        return False

while True :
    nama = input ("\nMasukkan username: ")
    if nama.upper() == "SELESAI" :
        break
    if cek_username(nama):
        username_valid.append(nama)

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, user in enumerate(username_valid, 1):
    print(f"{i}. {user}")
print(f"Jumlah username valid: {len(username_valid)}")