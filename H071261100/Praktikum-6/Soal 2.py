def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
        

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih.strip()
    pemilih = nama_asli.lower()
    pilihan = pilihan.strip().capitalize()

    if pemilih in rekap_suara:
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak tersedia!")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {nama: 0 for nama in kandidat_set}

    for pilihan in rekap_suara.values(): #values = mengambil seluruh nilai dari pasangan kunci-nilai(key-value)
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n" + "=" * 40)
    print("     HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for nama, jumlah in sorted(perolehan.items()): 
        print(f"{nama}: {jumlah} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    if not perolehan:
        print("Belum ada kandidat.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [
        nama for nama, jumlah in perolehan.items()
        if jumlah == suara_tertinggi
    ]

    if len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(sorted(pemenang)))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {suara_tertinggi} suara!"
        )

    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    # Fase pendaftaran kandidat
    print("\n--- FASE PENDAFTARAN KANDIDAT ---")

    while True:
        nama = input(
            "Masukkan nama kandidat (kosongkan untuk selesai): "
        ).strip()

        if nama == "":
            break

        daftar_kandidat(kandidat_set, nama)

    while len(kandidat_set) < 2:
        print("Minimal harus ada 2 kandidat untuk melanjutkan.")
        nama = input(
            "Masukkan nama kandidat (kosongkan untuk selesai): "
        ).strip()

        if nama == "":
            print("Pendaftaran belum memenuhi syarat.")
            print("Program dihentikan.")
            return

        daftar_kandidat(kandidat_set, nama)

    print("\nKandidat terdaftar:", kandidat_set)

    # Fase pemungutan suara
    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input(
            "\nNama pemilih (kosongkan untuk selesai): "
        ).strip()

        if nama_pemilih == "":
            break

        print("Kandidat yang tersedia:", kandidat_set)
        pilihan = input("Pilih kandidat: ").strip()

        berikan_suara(
            rekap_suara,
            kandidat_set,
            nama_pemilih,
            pilihan
        )

    # Menghitung dan menampilkan hasil
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


if __name__ == "__main__":
    main()