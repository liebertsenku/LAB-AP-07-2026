
def tambah_buku(inventaris, judul, penulis, harga, stok):
    inventaris.append({"judul": judul,
                    "penulis": penulis,
                    "harga": harga,
                    "stok": stok})

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    print(f"Ditemukan {len(hasil)} buku:")
    
    for i, buku in enumerate(hasil, 1):
        print(f"{i}. {buku['judul']} - {buku['penulis']} | "
              f"Rp{buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru
                if jumlah < 0:
                    print(f"Stok '{buku['judul']}' berkurang "
                          f"{abs(jumlah)}. Stok sekarang: {stok_baru}")
                else:
                    print(f"Stok '{buku['judul']}' bertambah "
                          f"{jumlah}. Stok sekarang: {stok_baru}")
            return

    print("Error! Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)

    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)

    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")

    if inventaris:
        termahal = max(inventaris, key=lambda buku: buku["harga"])
        print(f"Buku termahal     : {termahal['judul']} " f"(Rp{termahal['harga']})")
    else:
        print("Buku termahal: Belum ada buku")

    print("=" * 40)

inventaris = []

print("=" * 40)
print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
                print(f"Buku '{judul}' berhasil ditambahkan!")
        except ValueError:
            print("Error! Harga harus angka dan stok harus bilangan bulat.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Error! Jumlah perubahan harus berupa bilangan bulat.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid!")
 