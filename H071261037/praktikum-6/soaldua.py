def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    kandidat_set.add(nama)
    print('kandidat', nama, 'berhasil didaftarkan')

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    if nama_pemilih in rekap_suara:
        print('pemilih', nama_pemilih, 'sudah memberikan suara')
        return

    pilihan = pilihan.capitalize()
    if pilihan not in kandidat_set:
        print('kandidat', pilihan, 'tidak ada di daftar kandidat')
        return

    rekap_suara[nama_pemilih] = pilihan
    print('suara', nama_pemilih, 'untuk', pilihan, 'berhasil dicatat')

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat : 0 for kandidat in kandidat_set}
    for pemilih, pilihan in rekap_suara.items():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print('===== HASIL PEMILIHAN KETUA KELAS =====')
    total_suara = 0
    suara_tertinggi = -1
    pemenang = []

    for kandidat, jumlah in perolehan.items():
        print(kandidat, ':', jumlah, 'suara')
        total_suara += jumlah
        if jumlah > suara_tertinggi:
            suara_tertinggi = jumlah
            pemenang = [kandidat]
        elif jumlah == suara_tertinggi:
            pemenang.append(kandidat)

    print('total suara masuk:', total_suara)
    if len(pemenang) > 1 and suara_tertinggi > 0:
        print('hasil seri antara:', ','.join(pemenang))
        print('perlu pemilihan ulang')
    elif total_suara == 0:
        print('tidak ada suara yang masuk')
    else:
        print('pemenang', pemenang[0], 'dengan', suara_tertinggi, 'suara')

kandidat_set = set()
rekap_suara = {}
print('===== FASE PENDAFTARAN KANDIDAT =====')
while True:
    nama = input('masukkan nama kandidat(ksosongkan jika selesai):')
    if nama == '':
        if len(kandidat_set) < 2:
            print('minimal 2 kandidat')
            continue
        else:
            break
    daftar_kandidat(kandidat_set, nama)
print('kandidat terdaftar:', kandidat_set)

print('=====FASE PEMUNGUTAN SUARA=====')
while True:
    nama_pemilih = input('nama pemilih(kososngkan untuk selesai):')
    if nama_pemilih == '':
        break
    print('kandidat yang tersedia:', kandidat_set)
    pilihan = input('pilih kandidat: ')
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

hasil_perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(hasil_perolehan)