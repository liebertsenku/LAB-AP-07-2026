playlist = []
genre_set = set()

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = genre.capitalize()
    lagu = (judul, artis, genre, durasi)

    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return

    print("\n" + "=" * 75)
    print(f"{'No':<4}{'Judul':<25}{'Artis':<20}{'Genre':<12}{'Durasi':<10}")
    print("=" * 75)

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu

        menit = durasi // 60
        sisa_detik = durasi % 60
        print(
            f"{nomor:<4}{judul:<25}{artis:<20}"
            f"{genre:<12}{menit}:{sisa_detik:02d}"
        )

        total_durasi += durasi

    print("=" * 75)
    print(
        f"Total durasi playlist: "
        f"{total_durasi // 60} menit {total_durasi % 60} detik"
    )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil

def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus.")


def statistik_playlist(playlist, genre_set):
    print("\n" + "=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)

    print("Total lagu   :", len(playlist))
    print("Jumlah genre :", len(genre_set))
    print("Daftar genre :", genre_set)
    # if not genre_set:
    #     print("Daftar genre : kosong.")
    # else:
    #     print("Daftar genre :", genre_set)

    if not playlist:
        print("Playlist masih kosong.")
        print("=" * 40)
        return

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    print("\nDistribusi genre:")

    for genre, jumlah in sorted(distribusi.items()):
        print(f"  {genre:<12}: {'#' * jumlah} ({jumlah})")

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    menit_panjang = terpanjang[3] // 60
    detik_panjang = terpanjang[3] % 60

    menit_pendek = terpendek[3] // 60
    detik_pendek = terpendek[3] % 60
    
    print(
        f"\nLagu terpanjang: {terpanjang[0]} "
        f"({menit_panjang}:{detik_panjang:02d})"
    )
    print(
        f"Lagu terpendek: {terpendek[0]} "
        f"({menit_pendek}:{detik_pendek:02d})"
    )

    print("=" * 40)


while True:
    print("\n" + "=" * 40)
    print("PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()

        if judul == "" or artis == "" or genre == "":
            print("Judul, artis, dan genre tidak boleh kosong.")
            continue
        # if genre.lower() not in ["pop", "rock", "jazz", "rnb", "dangdut"]:
        #     print("Genre tidak tersedia! Silakan pilih genre yang tertera.")
        #     continue

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
            else:
                tambah_lagu(
                    playlist, genre_set,
                    judul, artis, genre, durasi
                )

        except ValueError:
            print("Durasi harus berupa angka bulat.")

    elif menu == "2":
        tampilkan_playlist(playlist)

    elif menu == "3":
        if not genre_set:
            print("Belum ada genre yang tersedia.")
            continue

        print("Genre tersedia:", genre_set)
        genre_target = input(
            "Masukkan genre yang ingin difilter: "
        ).strip()

        hasil = filter_genre(playlist, genre_target)

        if hasil:
            print(f"\nLagu bergenre '{genre_target}':")

            for nomor, lagu in enumerate(hasil, start=1):
                menit = lagu[3] // 60
                sisa_detik = lagu[3] % 60
                print(
                    f"{nomor}. {lagu[0]} - {lagu[1]} "
                    f"({menit}:{sisa_detik:02d})"
                )
        else:
            print("Tidak ada lagu dengan genre tersebut.")

    elif menu == "4":
        tampilkan_playlist(playlist)

        if not playlist:
            continue

        try:
            nomor = int(input("Nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)

            # Perbarui set agar hanya berisi genre yang masih ada.
            genre_set.clear()

            for lagu in playlist:
                genre_set.add(lagu[2])

        except ValueError:
            print("Nomor lagu harus berupa angka bulat.")

    elif menu == "5":
        statistik_playlist(playlist, genre_set)

    elif menu == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid.")
