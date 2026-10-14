
def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Email harus memiliki tepat satu karakter @.")
        return error

    # Memisahkan local dan domain
    posisi_at = email.find("@")
    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    # Aturan
    if local != "":
        if local[0] == ".":
            error.append("Bagian local tidak boleh diawali titik.")

        elif local[-1] == ".":
            error.append("Bagian local tidak boleh diakhiri titik.")

        elif ".." in local:
            error.append("Bagian local tidak boleh mengandung titik berurutan.")

    if domain == "" or "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")

    elif ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    elif not (domain.endswith(".com")
        or domain.endswith(".id")
        or domain.endswith(".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "Tidak ada email valid."

    panjang_maks = 0

    for email in daftar_email_valid:
        if len(email) > panjang_maks:
            panjang_maks = len(email)

    lebar = panjang_maks + 4
    hasil = karakter_border * (lebar + 2) + "\n"

    for email in daftar_email_valid:
        hasil += "| " + email
        sisa = panjang_maks - len(email)
        hasil += " " * sisa + " |\n"

    hasil += karakter_border * (lebar + 2)

    return hasil


daftar_email_valid = []
daftar_email = []

print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    # Memeriksa duplikat
    if email in daftar_email:
        error = ["Email sudah terdaftar (Duplikat)."]

    if len(error) == 0:
        daftar_email_valid.append(email)
        daftar_email.append(email)
        print(">> Email VALID!")

    else:
        print(">> Email DITOLAK karena:")

        for masalah in error:
            print("-", masalah)

        if email not in daftar_email:
            daftar_email.append(email)

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_email_valid, karakter_border))
