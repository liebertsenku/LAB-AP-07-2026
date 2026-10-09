DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    error = []
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error
    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh ada spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")

    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
    
    if email.lower() in [e.lower() for e in email_valid]:
        error.append("Email sudah terdaftar (Duplikat).")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    lebar_isi = max(len(e) for e in daftar_email_valid)
    lebar_total = lebar_isi + 4 
    garis = karakter_border * lebar_total

    baris = [garis]
    for e in daftar_email_valid:
        baris.append(karakter_border + ' ' + e + ' ' + karakter_border)
    baris.append(garis)

    return "\n".join(baris)

print("--- Sistem Pencatatan email valid ---")
masukan_border = input("Masukkan border dengan karakter bebas: ")
karakter_border = masukan_border[0] if masukan_border else "*"
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

email_valid = []
email_ditolak = []

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    if error:
        print("Email DITOLAK karena:")
        for pesan in error:
            print("   -" ,pesan)
        email_ditolak.append((email, error))
    else:
        print("Email VALID!")
        email_valid.append(email)

print("=== DAFTAR EMAIL VALID ===")
if email_valid:
    print(cetak_daftar(email_valid, karakter_border))
else:
    print("(Tidak ada email valid)")




