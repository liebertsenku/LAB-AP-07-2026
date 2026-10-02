def kasir(harga, jumlah, member=False):
    subtotal = harga * jumlah

    if member:
        subtotal = subtotal * 0.9

    return subtotal


print("Selamat Datang Di Kasir Minimarket!")

while True:
    status_member = input("Apakah Anda member? (y/n): ").strip().lower()

    if status_member == "y":
        member = True
        break
    elif status_member == "n":
        member = False
        break
    else:
        print("Input hanya boleh y atau n!\n")


total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break

    if nama_barang.lstrip("-").isdigit():
        print("Nama barang tidak boleh berupa angka!\n")
        continue
    
    try:
        harga = int(input("Harga barang: "))

        if harga < 0:
            print("Harga tidak boleh negatif!\n")
            continue

        jumlah = int(input("Jumlah barang: "))

        if jumlah <= 0:
            print("Jumlah barang harus lebih dari 0!\n")
            continue

        subtotal = kasir(harga, jumlah, member)

        total += subtotal

        print(f"Subtotal {nama_barang}: Rp {subtotal:.0f}")

    except ValueError:
        print("Harga dan jumlah harus berupa angka bulat!\n")

print(f"Total Belanja: Rp {total:.0f}\n")


