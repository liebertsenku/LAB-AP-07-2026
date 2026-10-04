def analisis_nilai(*nilai):
    if len(nilai) == 0:
        return None, None, None

    rata_rata = sum(nilai) / len(nilai)
    return rata_rata, max(nilai), min(nilai)


nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()

    if input_nilai == "":
        break

    try:
        nilai_siswa.append(float(input_nilai))
    except ValueError:
        print("Input tidak valid, harus berupa angka.")


rata_rata, nilai_tertinggi, nilai_terendah = analisis_nilai(*nilai_siswa)

if rata_rata is None:
    print("Data nilai tidak tersedia.")
else:
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {int(nilai_tertinggi)}")
    print(f"Nilai terendah: {int(nilai_terendah)}")