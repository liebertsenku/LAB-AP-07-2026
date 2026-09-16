
menu = ["Kopi Susu", "Matcha Latte", "Americano", ]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]        
sub_matcha = harga[1] * jumlah[1]      
sub_americano = harga[2] * jumlah[2] 

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano, ]

BIAYA_OPERASIONAL = 15000

total_seluruh = sub_kopi + sub_matcha + sub_americano 
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL


total_barang_terjual = jumlah[0] + jumlah[1] + jumlah[2]

target_tercapai = total_seluruh > 200000 and total_barang_terjual > 10
garis = "-" * 60

print("=== LAPORAN PENJUALAN KOPI SENJA ===")
print("Subtotal Kopi Susu    : Rp ", sub_kopi)
print("Subtotal Matcha Latte : Rp", sub_matcha)
print("Subtotal Americano    : Rp", sub_americano)
print("List Subtotal         :", subtotal_pendapatan)
print(garis) 

print("Total Pendapatan      :", total_seluruh)
print("Biaya Operasional     :", BIAYA_OPERASIONAL)
print("Pendapatan Bersih     :", pendapatan_bersih)
print(garis)

print("Total Barang Terjual  :", total_barang_terjual)

if target_tercapai:
    print("Status Target         : Target tercapai!✅")
else:
    print("Status Target         : Target belum tercapai.")
