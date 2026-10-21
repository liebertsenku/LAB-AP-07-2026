
def cari_buku_by_judul(inventaris, judul):
    
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            return buku
    return None


def tambah_buku(inventaris, judul, penulis, harga, stok):
    
    if judul == "" or penulis == "":
        print("Judul dan penulis tidak boleh kosong!")
        return False
    if harga < 0 or stok < 0:
        print("Harga dan stok tidak boleh negatif!")
        return False
    if cari_buku_by_judul(inventaris, judul) is not None:
        print(f"Buku '{judul}' sudah ada di inventaris!")
        return False

    inventaris.append({"judul": judul, "penulis": penulis,
                       "harga": harga, "stok": stok})
    print(f"Buku '{judul}' berhasil ditambahkan!")
    return True


def cari_buku(inventaris, kata_kunci):
    if kata_kunci == "":
        print("Kata kunci tidak boleh kosong!")
        return
    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
        return

    
    hasil = [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]

    if len(hasil) == 0:
        print("Tidak ada buku yang ditemukan.")
        return
    print(f"Ditemukan {len(hasil)} buku:")
    for nomor, b in enumerate(hasil, start=1):
        print(f" {nomor}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")


def update_stok(inventaris, judul, jumlah):
    buku = cari_buku_by_judul(inventaris, judul)
    if buku is None:
        print(f"Error: buku '{judul}' tidak ditemukan!")
        return False
    if jumlah == 0:
        print("Jumlah perubahan tidak boleh 0.")
        return False

    stok_baru = buku["stok"] + jumlah
    if stok_baru < 0:
        print(f"Gagal! Stok '{buku['judul']}' tidak cukup (stok sekarang: {buku['stok']}).")
        return False

    buku["stok"] = stok_baru
    if jumlah > 0:
        print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
    else:
        print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}")
    return True


def ringkasan_inventaris(inventaris):
    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
    else:
        total_stok = sum(b["stok"] for b in inventaris)
        total_aset = sum(b["harga"] * b["stok"] for b in inventaris) 
        termahal = max(inventaris, key=lambda b: b["harga"])
        print(f"Jumlah jenis buku : {len(inventaris)}")
        print(f"Total seluruh stok: {total_stok}")
        print(f"Total nilai aset  : Rp{total_aset}")
        print(f"Buku termahal     : {termahal['judul']} (Rp{termahal['harga']})")
    print("========================================")


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")



inventaris = []

print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        judul = input("Judul buku: ").strip()
        penulis = input("Penulis: ").strip()
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
        except :
            print("Harga dan stok harus berupa angka!")
        else:
            tambah_buku(inventaris, judul, penulis, harga, stok)

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ").strip()
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ").strip()
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
        except :
            print("Jumlah perubahan harus berupa angka bulat!")
        else:
            update_stok(inventaris, judul, jumlah)

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid! Masukkan angka 1-5.")
    print()
