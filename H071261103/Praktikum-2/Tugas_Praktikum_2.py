# Soal 1 
# level = int (input ("Masukkan Persentase Cabai : "))

# if level <0  :
#     print ("Angka Tidak Valid")
# elif level >=0 and level<=10:
#     print ("Level Aman")
# elif level >=11 and level <=40:
#     print ("Level Sedang")
# elif 41 <= level <= 70 :
#     print ("Level Pedas")
# else :
#     print ("Level Ektrem")


# Soal 2 
# jarak = int(input ("Masukkan Jarak Pengiriman (Km): "))
# express = input ("Layanan Express (Ya/Tidak): ").capitalize()
    
# if jarak <0 :
#     print ("Jarak Tidak Valid")
# elif jarak <5 :
#     tarif_awal = 10000
# elif jarak <=20 :
#     tarif_awal=20000
# else :
#     tarif_awal=35000
    
# if jarak >=0 :
#     tambahan = 15000 if express =="Ya" else 0
#     total = tarif_awal + tambahan 
#     print (f"Total Tarif Pengiriman: Rp {total}" )

# Soal 3
nilai = int(input("Masukkan Nilai Tes: "))
# pengalaman_bekerja= int(input("Masukkan Pengalaman Kerja (Tahun): "))

# if nilai >=80 :
#     print("Lolos ke Tahap Wawancara")
# elif nilai >=65 and pengalaman_bekerja>=2 :
#     print ("Lolos Bersyarat")
# else :
#     print("Tidak Lolos")
if nilai >=80:
    print ("Lolos")
elif  65<= nilai  <=80:
    pengalaman= int(input ("Masukkan Pengalaman Kerja (Tahun): "))
    if pengalaman >= 2:
        print ("Lolos Bersyarat")
    else:
        print ("tidak lolos")
else: 
    print ("tidak lolos")
    


# Soal 4
# Tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota): ").capitalize()
# Waktu = input("Masukkan Waktu (Pagi/Malam): ").capitalize()
# Tipe_Pengunjung = input("Masukkan Tipe Pengunjung (Anak/Dewasa): ").capitalize()

# match Tujuan:
#     case "Pantai":
#         if Waktu == "Pagi" :
#             print("Paket Rekomendasi: Paket A")
#         elif Waktu =="Malam" and Tipe_Pengunjung == "Dewasa" :
#             print("Paket Rekomendasi: Paket C")
#         else :
#             print("Tidak Ada Paket Yang Cocok")
            
#     case "Pegunungan":
#         if Waktu == "Pagi" and Tipe_Pengunjung == "Dewasa":
#             print("Paket Rekomendasi: Paket B")
#         elif Waktu =="Malam" and Tipe_Pengunjung == "Dewasa" :
#             print("Paket Rekomendasi: Paket C")
#         else:
#             print("Tidak Ada Paket Yang Cocok")
#     case "Kota":
#         if Waktu=="Malam":
#             print("Paket Rekomendasi: Paket C")
#         else :
#             print("Tidak Ada Paket Yang Cocok")
#     case _:
#         print("Tidak ada paket yang cocok")