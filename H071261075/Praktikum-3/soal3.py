while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break
    
    except:
        print("Input jumlah kursi harus berupa angka!")

sisa_kursi = N
total_pendapatan = 0

print("--- Sistem Reservasi PO BUS Dimulai ---")

while sisa_kursi > 0:
    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0:
            print("Umur tidak valid!")
            continue

        elif umur <= 5:
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")

        elif umur <= 12:
            harga = 50000
            print("Kategori Anak - Harga: Rp 50.000")

        else: 
            harga = 100000
            print("Kategori: Dewasa - Harga: Rp 100.000")

        total_pendapatan += harga 
        sisa_kursi -= 1

        if sisa_kursi > 0:
            print(f"Sisa kursi: {sisa_kursi}")

    except:
        print("Input harus berupa angka!")

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan PO BUS kali ini: Rp {total_pendapatan}")

