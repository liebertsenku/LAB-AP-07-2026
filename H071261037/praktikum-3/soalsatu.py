while True:
    try:
        item = int(input('Masukan jumlah item: '))
        if item == 0:
            print('toko tutup, sesi rekap selesai')
            break
        elif item > 100:
            print('maksimal 100 item per transaksi')
        elif item < 0:
            print('jumlah item tidak boleh negatif')
        else:
           print('Jumlah item yang berhasil diinput:', item)
    except:
        print('Input harus berupa angka')
        