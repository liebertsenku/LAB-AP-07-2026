print("Selamat datang di Kasir Minimarket!")

def hitung_subtotal(harga, jumlah, adalah_member=False):
    #menghitung subtotal barang jika diskon 10% karena member
    sub_total = harga * jumlah
    if adalah_member:
        sub_total = sub_total * 90 // 100
    return sub_total

while True:
    pilihan = input("Apakah Anda member? (y/n): ").strip().lower()
    if pilihan in ("y", "n"):
        adalah_member = pilihan == "y"
        break
    print("Input tidak valid. Masukkan y atau n.")

total_belanja = 0

while True:
    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
        if nama_barang == "":
            break
        try:
            int(nama_barang)
        except ValueError:
            break
        print("Nama barang tidak boleh berupa angka.")


    while True:
        try:
            harga = int(input("Harga barang: "))
        except ValueError:
            print("Harga harus berupa angka.")
            continue
        if harga < 0:
            print("Harga tidak boleh negatif.")
            continue
        break

    while True:
        try:
            jumlah = int(input("Jumlah barang: "))
        except ValueError:
            print("Jumlah harus berupa angka.")
            continue
        if jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            continue
        break

    sub_total = hitung_subtotal(harga, jumlah, adalah_member)
    total_belanja += sub_total

    print(f"Subtotal {nama_barang}: Rp{sub_total}")
    print(f"Total belanja: {total_belanja}")