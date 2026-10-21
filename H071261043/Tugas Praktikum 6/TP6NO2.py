def daftar_kandidat(kandidat_set, nama):
    if nama == "":
        return False
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.strip()
    kunci = nama_pemilih.lower()         
    pilihan = pilihan.strip().capitalize()

    if kunci in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False
    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak terdaftar! Suara tidak dicatat.")
        return False

    rekap_suara[kunci] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    
    perolehan = {kandidat: 0 for kandidat in sorted(kandidat_set)}
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    total_suara = sum(perolehan.values())
    for kandidat, jumlah in perolehan.items():
        print(f" {kandidat}: {jumlah} suara")
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara masuk, pemenang belum bisa ditentukan.")
        return

    tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == tertinggi]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")


def teks_set(kumpulan):
    return "{" + ", ".join(f"'{x}'" for x in sorted(kumpulan)) + "}"



kandidat_set = set()
rekap_suara = {}

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")
print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip().capitalize()
    if nama == "":
        if len(kandidat_set) < 2:
            print(f"Minimal harus ada 2 kandidat! Saat ini baru {len(kandidat_set)}.")
            continue
        break
    daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {teks_set(kandidat_set)}")
print()
print("--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {teks_set(kandidat_set)}")
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

print("========================================")
print(" HASIL PEMILIHAN KETUA KELAS")
print("========================================")
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
print("========================================")
