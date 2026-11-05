import re


def validasi_username(username):
    if not isinstance(username, str) or not username:
        return False
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None


def tampilkan_rekap(username_valid):
    print("\n=== Rekapitulasi ===")
    if username_valid:
        print("Username valid:")
        for i, nama in enumerate(username_valid, start=1):
            print(f"{i}. {nama}")
    else:
        print("Tidak ada username yang valid.")

    print(f"\nJumlah username valid: {len(username_valid)}")


def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.\n")

    username_valid = []

    while True:
        try:
            username = input("Masukkan username: ").strip()
        except (KeyboardInterrupt):
            print("\n\nInput dihentikan.")
            break

        if username == "SELESAI":
            break

        if not username:
            print("Username tidak boleh kosong. Username tidak valid!\n")
            continue

        if validasi_username(username):
            print("Username tersedia.\n")
            username_valid.append(username)
        else:
            print("Username tidak valid!\n")

    tampilkan_rekap(username_valid)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nTerjadi kesalahan tak terduga: {e}")
