menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Sub total masing-masing menu
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah [2]

# 2. Masukkan sub total ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. Hitung total dan pendapatan bersih
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. Jumlah semua barang yang terjual dan target
total_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000 and total_barang > 10)

print("Subtotal pendapatan : Rp", subtotal_pendapatan)
print("Total pendapatan bersih : Rp", pendapatan_bersih)
print("Hasil target : ", target_tercapai)
