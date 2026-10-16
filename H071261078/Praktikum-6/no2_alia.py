def daftar_kandidat(kandidat_set, nama):
    if nama:
        kandidat_set.add(nama.capitalize())
        print(f"'{nama.capitalize()}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih , pilihan):
    nama_pemilih_lower = nama_pemilih.lower()
    pilihan_cap = pilihan.capitalize()

    if nama_pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
        return

    if pilihan_cap not in kandidat_set:
        print("Error: Kandidat tidak terdaftar.")
        return

    rekap_suara[nama_pemilih_lower] = pilihan_cap
    print(f"Suara '{nama_pemilih.capitalize()}' untuk '{pilihan_cap}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for suara in rekap_suara.values():
        perolehan[suara] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("\n========================================")

    total_suara = sum(perolehan.values())

    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")

    print(f"Total suara masuk: {total_suara}")
    if total_suara > 0:
        suara_tertinggi = max(perolehan.values())
        pemenang = [k for k, s in perolehan.items() if s == suara_tertinggi]

        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang} dengan {suara_tertinggi} suara!")
    print(f"========================================")

def main_soal():
    kandidat_set = set()
    rekap_suara = {}

    print("========================================")
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("========================================")
    print("FASE PENDAFTARAN KANDIDAT")

    while True:
        nama = input("Masukkan nama nama kandidat (kosongkan untuk selesai): ")
        if not nama:
            if len(kandidat_set) >= 2:
                print(f"Kandidat terdaftar: {kandidat_set}")
                break
            else:
                print("Minimal harus ada 2 kandidat untuk melanjutkan")
        else:
            daftar_kandidat(kandidat_set, nama)

    print("\nFASE PEMUNGUTAN SUARA")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if not nama_pemilih:
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih Kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

main_soal()