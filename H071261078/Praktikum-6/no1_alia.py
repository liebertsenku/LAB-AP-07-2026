def cari_buku_sama(inventaris, judul, penulis, harga):
    for buku in inventaris:
        if (buku['judul'].lower() == judul.lower() and 
            buku['penulis'].lower() == penulis.lower() and 
            buku['harga'] == harga):
            return buku
    return None

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku_lama = cari_buku_sama(inventaris, judul, penulis, harga)
    
    if buku_lama:
        buku_lama['stok'] += stok
        print(f"Buku '{buku_lama['judul']}' oleh {buku_lama['penulis']} sudah ada. Stok bertambah {stok}. Stok sekarang: {buku_lama['stok']}")
    else:
        inventaris.append({
            "judul": judul,
            "penulis": penulis,
            "harga": harga,
            "stok": stok
        })
        print(f"Buku '{judul}' berhasil ditambahkan ke inventaris.")

def cari_buku(inventaris, kata_kunci):
    hasil = [buku for buku in inventaris if kata_kunci.lower() in buku['judul'].lower()]
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        for i, buku in enumerate(hasil, 1):
            print(f"{i}. {buku['judul']} | {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
    else:
        print("Buku tidak ditemukan.")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku['judul'].lower() == judul.lower():
            stok_baru = buku['stok'] + jumlah
            if stok_baru < 0:
                print("Gagal: Stok tidak boleh menjadi negatif.")
                return
            buku['stok'] = stok_baru
            print(f"Stok '{buku['judul']}' {'bertambah' if jumlah > 0 else 'berkurang'} {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            return
    print("Error: Buku tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris kosong.")
        return

    jumlah_jenis_buku = len(inventaris)
    total_stok_buku = sum(buku['stok'] for buku in inventaris)
    total_aset = sum(buku['harga'] * buku['stok'] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x['harga'])

    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku : {jumlah_jenis_buku}")
    print(f"Total seluruh stok: {total_stok_buku}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("========================================")

def main_soal():
    inventaris = []
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif.")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga dan stok harus berupa angka.")
        elif pilihan == '2':
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
        elif pilihan == '3':
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif = tambah, negatif = kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error: Jumlah perubahan harus berupa angka.")
        elif pilihan == '4':
            ringkasan_inventaris(inventaris)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid.")

main_soal()