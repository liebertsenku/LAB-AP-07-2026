def rekap_nilai(*nilai):
    if len(nilai) >0:
        rataa = sum(nilai) / len(nilai)
        tinggi = max(nilai)
        rendah = min(nilai)
        return rataa, tinggi, rendah
    return None, None, None


daftar_nilai = []
while True:
    nilai = (input('masukkan nilai ujian siswa(kosongkan untuk selesai):'))
    try:
        nilai = int(nilai)
        if nilai < 0:
            print('nilai tidak boleh negatif.')
            continue
    except ValueError:
        nilai = nilai
        if nilai == '':
                break
    try:
        daftar_nilai.append(float(nilai))
    except ValueError:
        print('input harus berupa angka.')

rata, tinggi, rendah = rekap_nilai(*daftar_nilai)

if rata is None:
    print('data nilai tidak tersedia:')
else:
    print('rata rata kelas:', rata)
    print('nilai tertinggi:', tinggi)
    print('nilai terendah:', rendah)