menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [15000, 22000, 18000]
jumlah = [4, 3, 5]

sub_kopi = harga [2] * jumlah [0]
sub_matcha = harga [1] * jumlah [1]
sub_americano = harga [0] * jumlah [2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_seluruh = sub_kopi + sub_matcha + sub_americano

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
total_barang = jumlah [0] + jumlah [1] + jumlah [2]
target_tercapai = total_seluruh > 200000 and total_barang > 10

print("Sub Total Kopi Susu:", sub_kopi)
print("Total Seluruh:", total_seluruh)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)