# Nomor 3

while True:
    try:
        kuota_kursi = int(input("Masukkan maksimal kursi bus: "))
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

sisa_kursi = kuota_kursi
total_pendapatan = 0

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!\n")
        continue

    if umur <= 0:
        print("Umur tidak valid!\n")
        continue

    elif umur <= 5:
        kategori = "Balita - Tiket Gratis (Rp 0)"
        harga = 0
    elif umur <= 12:
        kategori = "Anak - Harga: Rp 50.000"
        harga = 50000
    else:
        kategori = "Dewasa - Harga: Rp 100.000"
        harga = 100000

    print(f"Kategori: {kategori}\n")
    
    sisa_kursi -= 1
    total_pendapatan += harga

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")