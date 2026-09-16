menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4,3,5]

# Pertantnyaan 1
sub_kopi = jumlah [0] * harga [0]
sub_matcha = jumlah [1] * harga [1]
sub_americano = jumlah [2] * harga [2]

print("Kopi Susu = ", sub_kopi )
print("Matcha Latte = ", sub_matcha )
print("Americano = ", sub_americano )

# Pertanyaan 2
subtotal_pendapatan = [sub_kopi + sub_matcha + sub_americano]
print("Subtotal Pendapatan = ", subtotal_pendapatan[0])

# Pertanyaan 3
BIAYA_OPERASIONAL = 15000
total_seluruh = subtotal_pendapatan [0] - BIAYA_OPERASIONAL
pendapatan_bersih = total_seluruh
print("Pendapatan Bersih = ", pendapatan_bersih)

# pertanyaan 4
target_tercapai = 200000
jumlah_barang = sum(jumlah)
if sum(subtotal_pendapatan) >= target_tercapai and jumlah_barang > 10:
    print("Hasil Target = Tercapai")
else:
    print("Hasil Target = Tidak Tercapai")