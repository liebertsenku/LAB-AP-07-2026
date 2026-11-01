
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    if durasi <= 0:
        print("Durasi harus berupa angka positif!")
        return
    
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print("Lagu '", judul, "' oleh", artis, "berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist kosong.")
        return
    
    print("==================================")
    print("No | Judul | Artis | Genre | Durasi")
    print("==================================")
    total_detik = 0
    i = 0
    while i < len(playlist):
        lagu = playlist[i]
        judul = lagu[0]
        artis = lagu[1]
        genre = lagu[2]
        durasi = lagu[3]
        
        total_detik += durasi
        
        menit = durasi // 60
        detik = durasi % 60
        if detik < 10:
            print(i + 1, ".", judul, "|", artis, "|", genre, "|", menit, ":0", detik)
        else:
            print(i + 1, ".", judul, "|", artis, "|", genre, "|", menit, ":", detik)
        i = i + 1
        
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print("==================================")
    print("Total durasi playlist:", total_menit, "menit", sisa_detik, "detik")

def filter_genre(playlist, genre_target):
    hasil_filter = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil_filter

def hapus_lagu(playlist, nomor):
    indeks_angka = nomor - 1
    if indeks_angka >= 0 and indeks_angka < len(playlist):
        lagu_dihapus = playlist.pop(indeks_angka)
        print("Lagu '", lagu_dihapus[0], "' berhasil dihapus.")
    else:
        print("Nomor lagu tidak valid!")

def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
    
    print("=== STATISTIK PLAYLIST PLAYTUNE ===")
    print("Total lagu:", len(playlist))
    print("Jumlah genre:", len(genre_set))
    print("Daftar genre:", genre_set)
    
    distribusi = {}
    for lagu in playlist:
        g = lagu[2]
        if g in distribusi:
            distribusi[g] = distribusi[g] + 1
        else:
            distribusi[g] = 1
            
    print("Distribusi genre:")
    for g in distribusi:
        hitung = distribusi[g]
        baris_tanda = "#" * hitung
        print(g, ":", baris_tanda, "(", hitung, ")")
        
    lagu_panjang = playlist[0]
    lagu_pendek = playlist[0]
    
    k = 1
    while k < len(playlist):
        if playlist[k][3] > lagu_panjang[3]:
            lagu_panjang = playlist[k]
        if playlist[k][3] < lagu_pendek[3]:
            lagu_pendek = playlist[k]
        k = k + 1
        
    m_panjang = lagu_panjang[3] // 60
    d_panjang = lagu_panjang[3] % 60
    
    m_pendek = lagu_pendek[3] // 60
    d_pendek = lagu_pendek[3] % 60
    
    print("Lagu terpanjang:", lagu_panjang[0], "(", m_panjang, ":", d_panjang, ")")
    print("Lagu terpendek:", lagu_pendek[0], "(", m_pendek, ":", d_pendek, ")")

playlist = []
genre_set = set()
    

print("Menu:")
print("1. Tambah Lagu")
print("2. Tampilkan Playlist")
print("3. Filter berdasarkan Genre")
print("4. Hapus Lagu")
print("5. Statistik Playlist")
print("6. Keluar")
while True:    
    pilihan = int(input("Pilih menu (1-6): "))
        
    if pilihan == 1:
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Error: Durasi harus berupa angka!")

    elif pilihan == 2:
        tampilkan_playlist(playlist)

    elif pilihan == 3:
        print("Genre tersedia:", genre_set)
        target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, target)
        print("Lagu bergenre '", target, "':")
        idx = 0
        while idx < len(hasil):
            m = hasil[idx][3] // 60
            d = hasil[idx][3] % 60
            print(idx + 1, ".", hasil[idx][0], "-", hasil[idx][1], "(", m, ":", d, ")")
            idx = idx + 1

    elif pilihan == 4:
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)
        except ValueError:
            print("Error: Masukkan nomor yang valid!")

    elif pilihan == 5:
        statistik_playlist(playlist, genre_set)

    elif pilihan == 6:
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 6.")

