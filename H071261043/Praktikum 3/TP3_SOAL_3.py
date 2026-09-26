while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
    except: 
        print("Input jumlah kursi berupa angka\n")
        continue

    break

print ("---Sistem Reservasi PO BUS Dimulai---")

sisa_kursi = N 
total_pendapatan = 0

while sisa_kursi > 0:
    print (f"Sisa kursi: {sisa_kursi}")
    
    try:
        umur = int(input("Masukkan umur penumpang :" ))
    except : 
        print("Input umur harus berupa angka!\n")
        continue

    if umur <0:
        print ("Umur Tidak Valid!")
        continue
    
    elif umur >= 0 and umur <= 5:
        kategori = "Balita - Tiket Gratis (Rp 0)"
        harga = 0
    elif umur <= 12:
        kategori = "Anak - Harga: Rp 50.000"
        harga = 50000
    else:
        kategori = "Dewasa - Harga: Rp 100.000"
        harga = 100000
    
    print (f"Kategori 0: {kategori}\n")
    
    sisa_kursi -= 1
    total_pendapatan += harga 
    
print ("--- Semua Kursi Terisi ---")
print (f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")

    