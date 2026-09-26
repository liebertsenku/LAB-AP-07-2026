while True:
    try:
        kursi = int(input('masukan maksimal kursi bus: '))
        if kursi <= 0:
            print('kursi tidak boleh kurang dari 1')
            continue
        break
    except ValueError:
        print('input jumlah kursi harus angka')

print('---sistem reservasi PO BUS dimulai')

sisa_kursi = kursi
total_pendapatan = 0
while sisa_kursi > 0 :
    try:
        print('sisa kursi :', sisa_kursi)
        umur = int(input('masukan umur penumpang:'))
        if umur >=0 and umur <= 5 :
            harga = 0
            print('kategori: balita - tiket', harga)
        elif umur >= 6 and umur <=12 :
            harga = 50000
            print('kategori: anak - tiket', harga)
        elif umur >12 :
            harga = 100000
            print('kategori: dewasa - tiket', harga)
        else:
            print('umur tidak valid')
            continue
        total_pendapatan += harga
        sisa_kursi -= 1
    except ValueError:
        print('input jumlah kursi harus angka')
    
print('---semua kursi terisi---')
print('total pendapatan perjalanan PO BUS kali ini:', total_pendapatan)