
def deteksi_anomali_email(email, daftar_email=None):
    if daftar_email is None:
        daftar_email = []

    error = []

    if email.count("@") != 1:
        error.append("Email harus memiliki tepat satu karakter @.")

    if email.count("@") == 1:
        local, domain = email.split("@")
    else:
        local, domain = "", ""

    if local == "" or domain == "":
        error.append("Bagian local dan domain tidak boleh kosong.")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    if (
        local.startswith(".")
        or local.endswith(".")
        or ".." in local
    ):
        error.append(
            "Bagian local tidak boleh diawali atau diakhiri titik, "
            "atau memiliki titik berurutan."
        )

    if (
        "." not in domain
        or ".." in domain
        or domain.endswith(".")
    ):
        error.append(
            "Domain harus memiliki titik, tidak boleh memiliki "
            "titik berurutan, dan tidak boleh diakhiri titik."
        )

    if email.lower() in [e.lower() for e in daftar_email]:
        error.append("Email tidak boleh duplikat.")

    if not email.lower().endswith((".com", ".id", ".ac.id")):
        error.append("Email harus berakhiran .com, .id, atau .ac.id.")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(karakter_border) != 1:
        raise ValueError("Karakter border harus satu karakter.")

    if not daftar_email_valid:
        return "Belum ada email valid."

    lebar = max(len(email) for email in daftar_email_valid) + 4
    border = karakter_border * lebar

    hasil = border + "\n"

    for email in daftar_email_valid:
        hasil += "| " + email.ljust(lebar - 4) + " |\n"

    hasil += border

    return hasil


daftar_email_valid = []

while True:
    try:
        email = input(
            "Masukkan email (ketik 'tutup' untuk selesai): "
        )

        if email.lower() == "tutup":
            break

        if email == "":
            raise ValueError("Email tidak boleh kosong.")

        error = deteksi_anomali_email(email, daftar_email_valid)

        if error:
            print("\nEmail tidak valid:")
            for pesan in error:
                print("-", pesan)
        else:
            daftar_email_valid.append(email)
            print("\nEmail valid!")
            print(cetak_daftar([email], "="))

    except ValueError as e:
        print("Error:", e)

print("\nDaftar seluruh email valid:")
print(cetak_daftar(daftar_email_valid, "="))