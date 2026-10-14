def deteksi_anomali_email(email):
    error = []

    
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")

    
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    
    for ch in email:
        if ch.isspace():           
            error.append("Tidak boleh mengandung spasi.")
            break

    
    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    
    if domain.startswith("."):
        error.append("Bagian domain tidak boleh diawali titik.")

    
    if not email.lower().endswith((".com", ".id", ".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
   
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    lebar = terpanjang + 2                       
    garis = "+" + karakter_border * lebar + "+"

    hasil = garis + "\n"
    for email in daftar_email_valid:
        hasil += "| " + email.ljust(terpanjang) + " |\n"
    hasil += garis
    return hasil


def main():
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    if border == "":
        border = "="
    border = border[0]

    print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")
    valid = []
    terdaftar = []   

    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        error = deteksi_anomali_email(email)
        if not error and email.lower() in terdaftar:
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for e in error:
                print("   -", e)
        else:
            print(">> Email VALID!")
            valid.append(email)
            terdaftar.append(email.lower())

    print("\n--- HASIL EMAIL VALID ---")
    print(cetak_daftar(valid, border))


if __name__ == "__main__":
    main()
