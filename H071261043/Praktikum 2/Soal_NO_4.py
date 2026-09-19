print ("SOAL 4")
print ("Sistem Rekomendasi Paket Wisata")
tempat_tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota) : ").capitalize()
waktu = input("Masukkan Waktu (Pagi/Malam) : ").capitalize()
tipe_pengunjung = (input("Masukkan tipe pengunjung (Anak/Dewasa) : " )).capitalize()
match tempat_tujuan:
    case "Pantai" :
        if waktu == "Pagi":
            paket = "Paket A"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            paket = "Paket B"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
                    paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case _:
        paket = "Tidak ada paket yang cocok"
print("Paket Rekomendasi : ", paket)



        