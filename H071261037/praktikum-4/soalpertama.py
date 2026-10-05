print('selamat datang di kasir minimarket')

def hitung_subtotal(harga, jumlah, member=False):
    total = harga * jumlah
    if member:
        total *= 0.9
    return total

while True:
    member_input = input('apakah anda member?(y/n):').lower()
    if member_input in ('y', 'n'):
        break
    else:
        print('masukkan "y" untuk ya atau "n" untuk tidak.')
        continue
member = True if member_input == 'y' else False

ttl_kslrhn = 0
while True:
    nama_barang = input('masukan nama barang(kosongkan jika selesai):')
    if nama_barang == '':
        break
    try:
        harga = int(input('harga barang:'))
        if harga < 0:
            print('harga tidak boleh negatif.')
            continue
        jumlah = int(input('masukan jumlah barang:'))
        if jumlah < 0:
            print('jumlah tidak boleh negatif.')
            continue
    except ValueError:
        print('input tidak valid. masukkan angka.')
        continue

    subtotal = hitung_subtotal(harga, jumlah, member)
    ttl_kslrhn += subtotal

    print('subtotal', nama_barang, ':', int(subtotal))
print('total belanja:',int(ttl_kslrhn))

