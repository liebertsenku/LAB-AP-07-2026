inventaris = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)

def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    return hasil

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal, stok tidak mencukupi.")
            else:
                buku["stok"] = stok_baru

                if jumlah > 0:
                    print(
                        f"Stok '{buku['judul']}' bertambah "
                        f"{jumlah}. Stok sekarang: {buku['stok']}"
                    )
                elif jumlah < 0:
                    print(
                        f"Stok '{buku['judul']}' berkurang "
                        f"{abs(jumlah)}. Stok sekarang: {buku['stok']}"
                    )
                else:
                    print(
                        f"Stok '{buku['judul']}' tidak berubah. "
                        f"Stok sekarang: {buku['stok']}"
                    )

            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)

    jumlah_jenis = len(inventaris)

    total_stok = sum(
        buku["stok"] for buku in inventaris
    )

    total_aset = sum(
        buku["harga"] * buku["stok"]
        for buku in inventaris
    )

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")

    if inventaris:
        termahal = max(
            inventaris,
            key=lambda buku: buku["harga"]
        )

        print(
            f"Buku termahal     : {termahal['judul']} "
            f"(Rp{termahal['harga']})"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("=" * 40)


while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        judul = input("Judul buku: ").strip()
        penulis = input("Penulis: ").strip()

        if judul == "" or penulis == "":
            print("Judul dan penulis tidak boleh kosong.")
            continue
        if not penulis.replace(" ", "").replace("-", "").isalpha():
            print("Nama penulis harus berupa huruf.")
            continue

        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(
                    inventaris,
                    judul,
                    penulis,
                    harga,
                    stok
                )

                print(f"Buku '{judul}' berhasil ditambahkan!")

        except ValueError:
            print("Harga/stok harus berupa angka")

    elif menu == "2":
        kata_kunci = input("Masukkan kata kunci judul: ").strip()

        hasil = cari_buku(inventaris, kata_kunci)

        if hasil:
            print(f"Ditemukan {len(hasil)} buku:")

            for nomor, buku in enumerate(hasil, start=1):
                print(
                    f"  {nomor}. {buku['judul']} - "
                    f"{buku['penulis']} | Rp{buku['harga']} "
                    f"| Stok: {buku['stok']}"
                )
        else:
            print("Buku tidak ditemukan.")

    elif menu == "3":
        judul = input(
            "Judul buku yang ingin diupdate: "
        ).strip()

        try:
            jumlah = int(input(
                "Jumlah perubahan (positif=tambah, negatif=kurang): "
            ))

            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Jumlah perubahan stok harus berupa angka.")

    elif menu == "4":
        ringkasan_inventaris(inventaris)

    elif menu == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan menu tidak valid.")
