import re


def validasi_nim(nim):
    
    if not isinstance(nim, str) or not nim:
        return False
    return re.match(r"H071\d{6}", nim) 


def validasi_email(email):
   
    if not isinstance(email, str) or not email:
        return False
    pola = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    return re.fullmatch(pola, email) is not None


def validasi_telepon(telepon):
    if not isinstance(telepon, str) or not telepon:
        return False
    return re.fullmatch(r"\d{10,13}", telepon) is not None


def main():
    print("=== Validasi Data Mahasiswa ===\n")

    try:
        nim = input("Masukkan NIM      : ").strip()
        email = input("Masukkan Email    : ").strip()
        telepon = input("Masukkan No. Telp : ").strip()
    except (KeyboardInterrupt):
        print("\n\nInput dibatalkan. Program dihentikan.")
        return

    nim_ok = validasi_nim(nim)
    email_ok = validasi_email(email)
    telepon_ok = validasi_telepon(telepon)

    print("\n--- Hasil Validasi ---")
    print("NIM         :", "Valid" if nim_ok else "Format NIM tidak valid!")
    print("Email       :", "Valid" if email_ok else "Format email tidak valid!")
    print("No. Telepon :", "Valid" if telepon_ok else "Nomor telepon tidak valid!")

    if nim_ok and email_ok and telepon_ok:
        print("\nData mahasiswa berhasil diverifikasi!")
    else:
        print ("Tidak Terverifikas")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nTerjadi kesalahan tak terduga: {e}")
