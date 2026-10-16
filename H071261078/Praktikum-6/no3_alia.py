def format_waktu(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist kosong.")
        return
    
    print("\n========================================")
    print(f"{'No':<3} | {'Judul':<20} | {'Artis':<15} | {'Genre':<10} | {'Durasi':<6}")
    print("-" * 65)

    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        print(f"{i:<3} | {judul:<20} | {artis:<15} | {genre:<10} | {format_waktu(durasi):<6}")

    print("\n========================================")
    menit_total = total_detik // 60
    detik_total = total_detik % 60
    print(f"Total durasi playlist: {menit_total} menit {detik_total} detik")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, genre_set, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        genre_dihapus = lagu_dihapus[2]
        masih_ada = any(lagu[2].lower() == genre_dihapus.lower() for lagu in playlist)
        if not masih_ada:
            genre_terhapus = [g for g in genre_set if g.lower() == genre_dihapus.lower()]
            for g in genre_terhapus:
                genre_set.remove(g)

        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid.")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong.")
        return

    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)

    distribusi_genre = {genre: 0 for genre in genre_set}
    for lagu in playlist:
        for key in distribusi_genre:
            if key.lower() == lagu[2].lower():
                distribusi_genre[key] += 1

    terpanjang = max(playlist, key=lambda x: x[3])
    terpendek = min(playlist, key=lambda x: x[3])

    print("\n========================================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"Total lagu        : {total_lagu}")
    print(f"Jumlah genre      : {jumlah_genre}")
    print(f"Daftar genre      : {genre_set}")
    print("Distribusi genre  :")
    for genre, jumlah in distribusi_genre.items():
        print(f"{genre:<10}        : {'#' * jumlah} ({jumlah})")
    print(f"Lagu terpanjang   : {terpanjang[0]} ({format_waktu(terpanjang[3])})")
    print(f"Lagu terpendek    : {terpendek[0]} ({format_waktu(terpendek[3])})")
    print("========================================")

def main_soal():
    playlist = []
    genre_set = set()

    print("========================================")
    print("PLAYLIST MUSIK PLAYTUNE")
    print("========================================")

    while True:
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut dll): ")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi > 0:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
                else:
                    print("Durasi harus positif.")
            except ValueError:
                print("Error: Durasi harus berupa angka.")
        elif pilihan == '2':
            tampilkan_playlist(playlist)
        elif pilihan == '3':
            if not genre_set:
                print("Belum ada genre yang tersedia.")
                continue
            print(f"Genre tersedia : {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ")
            hasil_filter = filter_genre(playlist, genre_target)
            if hasil_filter:
                print(f"\nLagu bergenre '{genre_target}':")
                for i, lagu in enumerate(hasil_filter, 1):
                    print(f"{i}. {lagu[0]} oleh {lagu[1]} ({format_waktu(lagu[3])})")
            else:
                print("Tidak ada lagu dengan genre tersebut.")
        elif pilihan == '4':
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, genre_set, nomor)
                except ValueError:
                    print("Error: Nomor harus berupa angka.")
        elif pilihan == '5':
            statistik_playlist(playlist, genre_set)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_soal()