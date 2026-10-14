def hitung_subtotal(harga, jumlah, is_member=False):
    subtotal = harga * jumlah
    if is_member:
        subtotal = subtotal * 90 // 100
    return subtotal

print("Selamat datang di Kasir Minimarket!")
while True:
    status_member = input("Apakah Anda member? (y/n): ").strip().lower()
    if status_member == "y" or status_member == "n":
        break
    print("Input tidak valid, masukkan y atau n.")
is_member = status_member == "y"

total = 0
while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
    if nama == "":
        break
    if nama.isdigit():
        print("Nama barang tidak boleh berupa angka saja.")
        continue
    try:
        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))
    except:
        print("Harga dan jumlah harus berupa bilangan bulat.")
        continue
    if harga <= 0 or jumlah <= 0:
        print("Harga dan jumlah harus lebih dari 0.")
        continue
    subtotal = hitung_subtotal(harga, jumlah, is_member)
    print(f"Subtotal {nama}: Rp{subtotal}")
    total += subtotal

print(f"Total belanja: Rp{total}")