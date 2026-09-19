tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").upper()
waktu = input("Masukkan waktu (Pagi/Malam): ").upper()
tipe = input("Anak/Dewasa: ").upper()

match tujuan:
    case "PANTAI":
        if waktu == "PAGI" : print("Paket  Rekomendasi: Paket A")
        else:
            if tipe == "DEWASA": print("Paket Rekomendasi: Paket C")
            else: 
                print("Tidak ada paket yang cocok")
    case "PEGUNUNGAN":
        if waktu == "PAGI": 
            if tipe == "DEWASA": print("Paket rekomendasi: Paket B")
        else:
            print("Tidak ada paket yang cocok")
    case "KOTA":
        if waktu == "MaALAM" :
            print("Paket rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tidak ada paket yang cocok")