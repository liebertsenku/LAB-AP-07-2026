while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        if N <= 0:
            print("Input jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka! ")

print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = N
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        continue
    if umur <= 0:
        print("Umur tidak valid")
        continue
    elif umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: (Rp 50000)")
    else:
        harga = 100000
        print("Kategori: Dewasa - Harga (Rp 100000)")

    sisa_kursi -= 1
    total_pendapatan += harga

print("--- Sisa Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")

