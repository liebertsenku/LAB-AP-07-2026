tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket A")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            print("Paket B")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")          
    case _:
        print("Tidak ada paket yang cocok")
