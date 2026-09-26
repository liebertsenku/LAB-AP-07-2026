while True :
    try :
        barisKursi = int(input("Masukkan jumlah kursi bus: "))  
        if barisKursi <=0 :
            print ("Jumlah tidak valid !\n")
            continue
    except :
            print ("Input jumlah kursi harus berupa angka\n")
            continue
    total = 0
    print ("--- Sistem Reservasi PO BUS Dimulai ---\n")
    
    while barisKursi >0 :
        print ("Sisa Kursi: ",barisKursi)
        
        try :
            umur = int (input ("Masukkan umur penumpang: "))
            if umur <0 :
                print ("Umur tidak valid")
                continue
            if 0<= umur <=5 :
                print ("Kategori: Balita - Tiket Gratis (Rp 0)")
                harga = 0
            elif 6<= umur <=12 :
                print ("Kategori: Anak - Harga: Rp 50.000")
                harga = 50000
            else :
                print ("Kategori: Dewasa - Harga: Rp 100.000")
                harga = 100000
        except :
                print ("Input umur harus berupa angka\n")
                continue
        total += harga 
        barisKursi -= 1
        
        if barisKursi == 0:
            break
    print ("--- Semua kursi terisi ---")
    print ("Total pendapatan perjalanan PO BUS kali ini:","RP", total)
    break