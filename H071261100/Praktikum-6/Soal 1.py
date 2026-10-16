def tambah_buku(inventaris, judul, penulis, harga, stok):
    try:
        judul = judul.strip()
        penulis = penulis.strip()
        harga = int(harga)
        stok = int(stok)

        if judul == "" or penulis == "":
            print("Error: Judul dan penulis tidak boleh kosong!")
            return False

        if harga <= 0:
            print("Error: Harga harus positif!")
            return False

        if stok < 0:
            print("Error: Stok tidak boleh negatif!")
            return False

        buku = {
            "judul": judul,
            "penulis": penulis,
            "harga": harga,
            "stok": stok
        }

        inventaris.append(buku)

        print(f"Buku '{judul}' berhasil ditambahkan!")
        return True

    except ValueError:
        print("Error: Data buku tidak valid!")
        return False


def cari_buku(inventaris, kata_kunci):
    try:
        kata_kunci = kata_kunci.strip().lower()

        if kata_kunci == "":
            print("Error: Kata kunci tidak boleh kosong!")
            return False

        ditemukan = False
        jumlah_ditemukan = 0

        for buku in inventaris:
            if kata_kunci in buku["judul"].lower():
                jumlah_ditemukan += 1

        if jumlah_ditemukan > 0:
            print(f"Ditemukan {jumlah_ditemukan} buku:")

            nomor = 1

            for buku in inventaris:
                if kata_kunci in buku["judul"].lower():
                    print(
                        f"{nomor}. {buku['judul']} - {buku['penulis']} "
                        f"| Rp{buku['harga']} | Stok: {buku['stok']}"
                    )
                    nomor += 1

                    ditemukan = True

            return True

        print("Buku tidak ditemukan!")
        return False

    except ValueError:
        print("Error: Kata kunci tidak valid!")
        return False


def update_stok(inventaris, judul, jumlah):
    try:
        judul = judul.strip().lower()
        jumlah = int(jumlah)

        for buku in inventaris:
            if buku["judul"].lower() == judul:

                stok_baru = buku["stok"] + jumlah

                if stok_baru < 0:
                    print("Error: Stok tidak boleh negatif!")
                    return False

                buku["stok"] = stok_baru

                if jumlah > 0:
                    print(
                        f"Stok '{buku['judul']}' bertambah {jumlah}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
                elif jumlah < 0:
                    print(
                        f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
                else:
                    print(
                        f"Stok '{buku['judul']}' tetap. "
                        f"Stok sekarang: {buku['stok']}"
                    )

                return True

        print("Error: Buku tidak ditemukan!")
        return False

    except ValueError:
        print("Error: Perubahan stok buku tidak valid!")
        return False


def ringkasan_inventaris(inventaris):
    print("\n" + "=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)

    if len(inventaris) == 0:
        print("Inventaris masih kosong!")
        return False

    jumlah_buku = len(inventaris)
    total_stok = 0
    total_nilai = 0
    buku_termahal = inventaris[0]

    for buku in inventaris:
        total_stok += buku["stok"]
        total_nilai += buku["harga"] * buku["stok"]

        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print(f"Jumlah jenis buku : {jumlah_buku}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_nilai}")
    print(
        f"Buku termahal: {buku_termahal['judul']} "
        f"(Rp{buku_termahal['harga']})"
    )

    print("=" * 40)

    return True


def main():
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

        try:
            pilihan = int(input("Pilih menu (1-5): "))

            if pilihan == 1:
                judul = input("Judul buku: ")
                penulis = input("Penulis: ")

                try:
                    harga = int(input("Harga: "))
                    stok = int(input("Stok awal: "))
                except ValueError:
                    print("Error: Harga atau stok tidak valid!")
                    continue

                tambah_buku(
                    inventaris,
                    judul,
                    penulis,
                    harga,
                    stok
                )

            elif pilihan == 2:
                kata_kunci = input("Masukkan kata kunci judul: ")
                cari_buku(inventaris, kata_kunci)

            elif pilihan == 3:
                judul = input("Judul buku yang ingin diupdate: ")

                try:
                    jumlah = int(
                        input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
                    )
                except ValueError:
                    print("Error: Perubahan stok harus berupa bilangan bulat!")
                    continue

                update_stok(
                    inventaris,
                    judul,
                    jumlah
                )

            elif pilihan == 4:
                ringkasan_inventaris(inventaris)

            elif pilihan == 5:
                print("Terima kasih telah menggunakan BookNest!")
                break

            else:
                print("Error: Pilihan menu harus antara 1 sampai 5!")

        except ValueError:
            print("Error: Pilihan menu harus berupa angka!")


if __name__ == "__main__":
    main()