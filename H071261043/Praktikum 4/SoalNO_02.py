def hitung_statistik(*args):
    rata_rata = sum(args) / len(args)
    return rata_rata, max(args), min(args)

daftar_nilai = []

while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()

    if masukan == "":
        break

    try:
        nilai = int(masukan)
    except ValueError:
        try:
            nilai = float(masukan)
        except ValueError:
            print("Input tidak valid, masukkan angka.")
            continue

    if nilai < 0 or nilai > 100:
        print("Input tidak valid, masukkan nilai antara 0 dan 100.")
        continue

    print("Input diterima.")
    daftar_nilai.append(nilai)

if daftar_nilai:
    rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data nilai tidak tersedia.")