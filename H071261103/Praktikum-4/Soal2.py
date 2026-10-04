def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah

nilai_siswa = []

while True:
    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")

    if nilai == "":
        break

    try:
        nilai = float(nilai)

        if nilai < 0 or nilai > 100:
            print("Nilai harus 0 - 100")
            continue

        nilai_siswa.append(nilai)

    except ValueError:
        print("Nilai harus berupa angka!")
        continue


if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)

    print(f"Rata-rata kelas: {rata_rata:g}")
    print(f"Nilai tertinggi: {tertinggi:g}")
    print(f"Nilai terendah: {terendah:g}")