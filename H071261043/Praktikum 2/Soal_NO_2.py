print ("SOAL 2")
print ("Menghitung Tarif Pengiriman Barang")

jarak_pengiriman = int(input("Masukkan jarak pengiriman (km) : "))

if jarak_pengiriman < 0:
    print("Jarak pengiriman tidak valid (tidak boleh negatif). Program dihentikan.")
else:
    layanan_express = input("Apakah menggunakan layanan express? (ya/tidak) : ").lower()

    if layanan_express != "ya" and layanan_express != "tidak":
        print("Input layanan express tidak valid (harus 'ya' atau 'tidak'). Program dihentikan.")
    else:
        if jarak_pengiriman < 5:
            tarif = 10000
        elif jarak_pengiriman <= 20:
            tarif = 20000
        else:
            tarif = 35000
        express = 15000 if layanan_express == "ya" else 0
        hasil = tarif + express
        print(hasil)        
print()