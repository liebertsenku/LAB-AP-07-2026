inventaris = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        'judul' : judul,
        'penulis' : penulis,
        'harga' : harga,
        'stok' : stok,
    }
    inventaris.append(buku)
    print('buku', judul , 'berhasil ditambahkan')

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku['judul'].lower():
            hasil.append(buku)
    if hasil:
        print('ditemukan', len(hasil), 'buku:')
        for i in range(len(hasil)):
            print(i + 1, ". ", hasil[i]['judul'])
            print(hasil[i]['penulis'], " | Rp", hasil[i]['harga'], " | Stok: ", hasil[i]['stok'])
    else:
        print('buku tidak ditemukan')

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku['judul'].lower() == judul.lower():
            stok_baru = buku['stok'] + jumlah
            if stok_baru < 0:
                print('eror: jumlah tidak boleh minus')
            else:
                buku['stok'] = stok_baru
                print('buku', buku['judul'], 'berhasil diupdate. stok sekarang:', buku['stok']  )

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print('inventaris belum terisi')
    jumlah_jenis = len(inventaris)

    for buku in inventaris:
        total_stok = 0
        total_stok += buku['stok']

    for buku in inventaris:
        total_aset = 0
        total_aset += (buku['harga'] * buku['stok'])

    for buku in inventaris:
        buku_termahal = inventaris[0]
        if buku['harga'] > buku_termahal['harga']:
            buku_termahal = buku

    print('==================================')
    print('RINGKASAN INVESTARIS BOOKNEST')
    print('==================================')
    print('jumlah jenis buku:', jumlah_jenis)
    print('total seluruh buku:', total_stok)
    print('total nilai aset:', total_aset)
    print('buku termahal:', buku_termahal, 'Rp', buku_termahal['harga'])

print('======================================')
print('SISTEM INVESTARIS TOKO BUKU BOOKNEST')
print('======================================')

while True:
    print('menu')
    print('1. tambah buku')
    print('2. cari buku')
    print('3. update stok')
    print('4. ringkasan inventaris')
    print('5. keluar')
    pilihan = int(input('pilih menu (1-5):'))
    if pilihan == 1:
        judul = input('judul buku:')
        penulis = input('penulis:')
        try:
            harga = int(input('harga:'))
            stok = int(input('stok awal:'))
            if harga < 0 or stok < 0:
                print('harga/stok tidak boleh minus')
            tambah_buku(inventaris, judul, penulis, harga, stok)
        except:
            print('harga/stok harus berupa angka')
        
    elif pilihan == 2:
        kata_kunci = input('masukan kata kunci judul:')
        cari_buku(inventaris, kata_kunci)

    elif pilihan == 3:
        judul = input('judul buku yang ingin diupdate:')
        try:
            jumlah = int(input('jumlah perubahan (positif = tambah, negatif = kurang):'))
            update_stok(inventaris, judul, jumlah)
        except:
            print('jumlah harus berupah angka')
            continue

    elif pilihan == 4:
        ringkasan_inventaris(inventaris)

    elif pilihan == 5:
        print('terimah kasih telah menggunakan booknest')
        break

    else:
        print('pilihan hanya 1-5')