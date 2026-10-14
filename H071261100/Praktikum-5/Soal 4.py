def deteksi_anomali_email(email):
    error = []

    # aturan 1
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @")
        return error
    local, domain = email.split("@")

    # aturan 2
    if local == "" or domain == "":
        error.append("Bagian local atau domain tidak boleh kosong")

    # aturan 3
    if " " in email:
        error.append("Email tidak boleh mengandung spasi")

    # aturan 4
    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak valid")

    # aturan 5
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik")

    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak valid")

    # aturan 7
    domain_resmi = [".com", ".id", ".ac.id"]
    valid_domain = False

    for d in domain_resmi:
        if domain.endswith(d):
            valid_domain = True

    if not valid_domain:
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "Tidak ada email valid"

    panjang = 0

    for email in daftar_email_valid:
        if len(email) > panjang:
            panjang = len(email)

    lebar = panjang + 4

    hasil = karakter_border * lebar + "\n"

    for email in daftar_email_valid:
        hasil += "| " + email + " " * (panjang - len(email)) + " |\n"

    hasil += karakter_border * lebar

    return hasil


# Program utama

daftar_email_valid = []

while True:
    email = input("Masukkan email: ")

    if email == "tutup":
        break

    error = deteksi_anomali_email(email)

    if len(error) == 0:

        if email in daftar_email_valid:
            print("Email DITOLAK karena:")
            print("Email sudah terdaftar (Duplikat).")

        else:
            daftar_email_valid.append(email)
            print("Email VALID!")

    else:
        print("Email DITOLAK karena:")
        for e in error:
            print("-", e)


border = input("Masukkan border dengan karakter bebas: ")

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_email_valid, border))