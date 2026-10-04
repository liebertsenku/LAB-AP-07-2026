def rekap_nilai(*args): 
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)

    return rata_rata, tertinggi, terendah

nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_nilai == "":
        break

    try:
        nilai = int(input_nilai)
    except:
        print("Input harus berupa angka. Silakan input ulang.")
        continue

    if nilai < 0:
            print("Nilai tidak boleh negatif. Silakan input ulang.")
            continue

    nilai_siswa.append(nilai)

if nilai_siswa:
    rata_rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data tidak tersedia")

#':g digunakan untuk format umum yang ringkas, seperti hilangkan nol desimal yang tidak diperlukan

