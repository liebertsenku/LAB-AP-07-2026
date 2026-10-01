def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 90 // 100

    return subtotal


print("Selamat datang di Kasir Minimarket!")

while True:
    status_member = input("Apakah Anda member? (y/n): ").lower()
    if status_member in ("y", "n"):
        break
    print("Input harus y atau n")

adalah_member = status_member == "y"

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)

    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total += subtotal

print(f"Total belanja: Rp{total}")