import re

MAKS_DATA = 100


def bersihkan_nomor(nomor):
   
    if not isinstance(nomor, str):
        return ""
    return re.sub(r"[\s-]", "", nomor)


def validasi_nomor(nomor_bersih):
    if not isinstance(nomor_bersih, str) or not nomor_bersih:
        return False
    return re.fullmatch(r"\d{10,13}", nomor_bersih) is not None


def minta_jumlah():
    
    while True:
        try:
            teks = input("Masukkan jumlah data: ").strip()
        except (KeyboardInterrupt):
            return None

        try:
            jumlah = int(teks)
        except ValueError:
            print("Input harus berupa angka bulat! Coba lagi.\n")
            continue

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0! Coba lagi.\n")
        elif jumlah > MAKS_DATA:
            print(f"Jumlah maksimal {MAKS_DATA} data! Coba lagi.\n")
        else:
            return jumlah


def main():
    print("=== Pembersihan Data Nomor Telepon ===\n")

    jumlah = minta_jumlah()
    if jumlah is None:
        print("\n\nInput dibatalkan. Program dihentikan.")
        return

    data_sebelum = []
    data_sesudah = []
    nomor_valid = []

    print()
    for i in range(1, jumlah + 1):
        try:
            nomor = input(f"Nomor ke-{i}: ")
        except (KeyboardInterrupt):
            print("\n\nInput dihentikan. Memproses data yang sudah dimasukkan...")
            break
        print()
        data_sebelum.append(nomor)
        data_sesudah.append(bersihkan_nomor(nomor))

    if not data_sebelum:
        print("Tidak ada data yang diproses.")
        return

    print("\n--- Hasil Pembersihan ---\n")
    for i, (sebelum, sesudah) in enumerate(zip(data_sebelum, data_sesudah), start=1):
        valid = validasi_nomor(sesudah)
        if valid:
            nomor_valid.append(sesudah)

        print(f"Data {i}:")
        print(f"Sebelum : {sebelum}")
        print(f"Sesudah : {sesudah}")
        print(f"Status  : {'Valid' if valid else 'Tidak valid'}\n")

    print(f"Jumlah nomor valid: {len(nomor_valid)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nTerjadi kesalahan tak terduga: {e}")
