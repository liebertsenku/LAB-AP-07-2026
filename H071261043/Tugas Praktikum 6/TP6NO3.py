GENRE_VALID = {"pop": "Pop", "rock": "Rock", "jazz": "Jazz",
               "rnb": "RnB", "dangdut": "Dangdut"}


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"      


def teks_set(kumpulan):
    return "{" + ", ".join(f"'{x}'" for x in sorted(kumpulan)) + "}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)          
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    
    lj = max(len("Judul"), max(len(l[0]) for l in playlist))
    la = max(len("Artis"), max(len(l[1]) for l in playlist))
    lg = max(len("Genre"), max(len(l[2]) for l in playlist))

    header = f"{'No':<3} {'Judul':<{lj}} {'Artis':<{la}} {'Genre':<{lg}} Durasi"
    garis = "=" * len(header)
    print(garis)
    print(header)
    print(garis)
    for nomor, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{nomor:<3} {judul:<{lj}} {artis:<{la}} {genre:<{lg}} {format_durasi(durasi)}")
    print(garis)

    total = sum(l[3] for l in playlist)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):

    return [lagu for lagu in playlist if lagu[2] == genre_target]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print(f"Nomor {nomor} tidak valid! Pilih nomor 1 sampai {len(playlist)}.")
        return False
    lagu = playlist.pop(nomor - 1)                
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    return True


def statistik_playlist(playlist, genre_set):
    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        print("========================================")
        return

    
    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    print(f" Total lagu      : {len(playlist)}")
    print(f" Jumlah genre    : {len(genre_set)}")
    print(f" Daftar genre    : {teks_set(genre_set)}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"  {genre:<8}: {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek  : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("========================================")


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")



playlist = []
genre_set = set()

print("========================================")
print(" PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()
        genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().lower()
        if judul == "" or artis == "":
            print("Judul dan artis tidak boleh kosong!")
        elif genre_input not in GENRE_VALID:
            print("Genre tidak valid! Pilih salah satu: Pop/Rock/Jazz/RnB/Dangdut.")
        else:
            try:
                durasi = int(input("Durasi (dalam detik): "))
            except :
                print("Durasi harus berupa angka bulat!")
            else:
                if durasi <= 0:
                    print("Durasi harus lebih dari 0!")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis,
                                GENRE_VALID[genre_input], durasi)

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Playlist masih kosong.")
        else:
            print(f"Genre tersedia: {teks_set(genre_set)}")
            genre_input = input("Masukkan genre yang ingin difilter: ").strip().lower()
            if genre_input not in GENRE_VALID or GENRE_VALID[genre_input] not in genre_set:
                print("Genre tidak ada di playlist!")
            else:
                target = GENRE_VALID[genre_input]
                hasil = filter_genre(playlist, target)
                print(f"Lagu bergenre '{target}':")
                for nomor, (judul, artis, genre, durasi) in enumerate(hasil, start=1):
                    print(f" {nomor}. {judul} - {artis} ({format_durasi(durasi)})")

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong, tidak ada lagu yang bisa dihapus.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            except :
                print("Nomor harus berupa angka bulat!")
            else:
                if hapus_lagu(playlist, nomor): 
                    genre_set.clear()
                    genre_set.update(lagu[2] for lagu in playlist)

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid! Masukkan angka 1-6.")
    print()
