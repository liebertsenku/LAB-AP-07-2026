menu = ("Kopi Susu", "Matcha Latte", "Americano")
menu.append("stroberry")
print(menu)
harga = [18000, 22000, 15000]
harga.append(50000)
jumlah = [4, 3, 5]
BIAYA_OPERASIONAL = 15000

sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]

subtotal_pendapatan = [sub_kopi,sub_matcha, sub_americano]
                       
total_pendapatan = sub_kopi + sub_matcha + sub_americano
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL
jumlah_barang_terjual = sum(jumlah)

target_tercapai = (total_pendapatan > 200000) and (jumlah_barang_terjual > 10)

print("Subtotal Pendapatan Kopi Susu : Rp ", subtotal_pendapatan[0] )
print("Subtotal Pendapatan Matcha Latte : Rp ", subtotal_pendapatan[1] )
print("Subtotal Pendapatan Americano : Rp ", subtotal_pendapatan[2] )

print("Sub Total Pendapatan Menu : RP", sum(subtotal_pendapatan))

print("Pendapatan Bersih : Rp", pendapatan_bersih)
print("Hasil Target : ", target_tercapai)





