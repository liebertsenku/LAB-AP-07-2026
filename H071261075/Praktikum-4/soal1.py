def hitung_subtotal(harga, jumlah, member=False):
    subtotal = harga * jumlah

    if member:
        subtotal = subtotal * 0.9
    return subtotal

print("Selamat datang di Kasir Minimarket")

status = input("Apakah Anda member? (y/n): ").lower()
if status == "y":
    member = True
elif status == "n":
    member = False

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
          
    subtotal = hitung_subtotal(harga, jumlah, member)

    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total_belanja += subtotal
print(f"Total belanja: Rp{total_belanja}")

