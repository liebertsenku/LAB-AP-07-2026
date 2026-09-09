menu = ['kopi susu', 'matcha latte', 'americano']
jumlah = [4, 3, 5]
harga = [18000, 22000, 15000]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano ]

BIAYA_OPERASIONAL = 15000
total_keseluruhan = sub_kopi + sub_matcha + sub_americano
pendapatan_bersih = total_keseluruhan - BIAYA_OPERASIONAL
jumlah_barang = sum(jumlah)
hasil_target = pendapatan_bersih > 200000  and jumlah_barang > 10

print('subtotal:', total_keseluruhan)
print('pendapatan bersih:', pendapatan_bersih)
print('hasil target:', hasil_target )

 