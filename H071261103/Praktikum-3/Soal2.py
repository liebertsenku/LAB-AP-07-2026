while True :
    while True :
        try :
            jumlahBaris = int(input("Masukkan jumlah baris: "))  
            if jumlahBaris <=0 :
                print("Jumlah baris harus lebih dari 0!")
                continue 
            break
        except :
            print ("Input baris harus berupa angka")
                
    while True :
        try :
            jumlahKursi = int(input("Masukkan jumlah kursi per baris: "))
            if jumlahBaris <=0 :
                print("Jumlah baris harus lebih dari 0!")
                continue
            break 
        except:
            print ("Input baris harus berupa angka")
            
    print("\nDaftar Kursi Tersedia")      
    for baris in range (1, jumlahBaris +1):
        for kursi in range (1, jumlahKursi +1):
            if kursi == 13 :
                continue
            if baris == 1 :
                if kursi % 2 != 0 : 
                    print ("Baris",baris,"- Kursi",kursi)
            else :
                print ("Baris",baris,"- Kursi",kursi)
    ulang = input ("Apakah ingin lanjut (Ya/Tidak)").capitalize()
    if ulang== "Ya":
        continue
    else :
        break