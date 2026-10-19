
def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print("Error! Kandidat tidak ditemukan.")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print("HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for kandidat, suara in sorted(perolehan.items()):
        print(f"{kandidat}: {suara} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if perolehan:
        suara_tertinggi = max(perolehan.values())
        pemenang = [nama for nama, suara in perolehan.items()
                    if suara == suara_tertinggi]

        if len(pemenang) > 1:
            print("Hasil SERI antara: " + ", ".join(sorted(pemenang)))
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} "
                  f"dengan {suara_tertinggi} suara!")

    print("=" * 40)


kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print("SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        if len(kandidat_set) >= 2:
            break
        print("Minimal harus ada 2 kandidat!")
        continue

    daftar_kandidat(kandidat_set, nama)

print("Kandidat terdaftar:", kandidat_set)

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)