import os
import random
import datetime

FOLDER_INVOICE = "invoices"
FILE_HISTORY = "trx_history.txt"
LEBAR = 60


def siapkan_folder():
    if not os.path.exists(FOLDER_INVOICE):
        os.mkdir(FOLDER_INVOICE)


def format_rupiah(nominal):
    return "Rp" + format(nominal, ",").replace(",", ".")


def buat_id_transaksi(nama_kasir, waktu):
    inisial = ""

    for kata in nama_kasir.split():
        inisial += kata[0].upper()

    tanggal_waktu = waktu.strftime("%y%m%d%H%M")

    while True:
        angka_acak = random.randint(100, 999)
        id_transaksi = inisial + tanggal_waktu + str(angka_acak)
        nama_file = os.path.join(
            FOLDER_INVOICE, id_transaksi + ".txt"
        )

        if not os.path.exists(nama_file):
            return id_transaksi, nama_file


def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))

            if angka < 0:
                print("Angka tidak boleh negatif!")
                continue

            return angka

        except ValueError:
            print("Masukkan angka yang benar!")


def buat_invoice(nama_kasir, waktu, id_transaksi, produk, total):
    nama_file = os.path.join(FOLDER_INVOICE, id_transaksi + ".txt")

    try:
        with open(nama_file, "w") as file:
            file.write("TOKO".center(LEBAR) + "\n")
            file.write("=" * LEBAR + "\n")
            file.write("Nama kasir       : " + nama_kasir + "\n")
            file.write("Waktu transaksi  : " + waktu.strftime("%d/%m/%y %H:%M") + "\n")
            file.write("=" * LEBAR + "\n\n")
            file.write("Daftar Produk".center(LEBAR) + "\n\n")

            file.write("-" * LEBAR + "\n")
            file.write(
                "| {:<16} | {:>9} | {:>6} | {:>12} |\n".format(
                    "Nama", "Harga", "Jumlah", "Total"
                )
            )
            file.write("-" * LEBAR + "\n")

            for item in produk:
                file.write(
                    "| {:<16} | {:>9} | {:>6} | {:>12} |\n".format(
                        item[0][:16],
                        format_rupiah(item[1]),
                        item[2],
                        format_rupiah(item[3])
                    )
                )

            file.write("-" * LEBAR + "\n")
            file.write(
                "| {:<38} | {:>12} |\n".format("TOTAL", format_rupiah(total)))
            file.write("=" * LEBAR + "\n\n")
            file.write("TERIMA KASIH TELAH BERBELANJA".center(LEBAR) + "\n")
            file.write("=" * LEBAR + "\n")

        return True

    except OSError as error:
        print("Gagal menyimpan invoice:", error)
        return False


def siapkan_riwayat():
    if not os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, "w") as file:
            file.write("=" * LEBAR + "\n")
            file.write("RIWAYAT TRANSAKSI".center(LEBAR) + "\n")
            file.write("=" * LEBAR + "\n")
            file.write(
                "| {:<14} | {:<20} | {:>16} |\n".format(
                    "Waktu", "ID Transaksi", "Nominal Transaksi"
                )
            )
            file.write("=" * LEBAR + "\n")


def catat_riwayat(waktu, id_transaksi, total):
    try:
        with open(FILE_HISTORY, "a") as file:
            file.write(
                "| {:<14} | {:<20} | {:>16} |\n".format(
                    waktu.strftime("%d/%m/%y %H:%M"),
                    id_transaksi,
                    format_rupiah(total)
                )
            )
            file.write("=" * LEBAR + "\n")

        return True

    except OSError as error:
        print("Gagal menyimpan riwayat:", error)
        return False


def transaksi_baru(nama_kasir):
    print("\n" + "=" * LEBAR)
    print("TRANSAKSI BARU".center(LEBAR))
    print("=" * LEBAR)

    produk = []
    total = 0

    while True:
        print("=" * LEBAR)

        nama_produk = input("Masukkan nama produk   : ").strip()

        if nama_produk == "":
            print("Nama produk tidak boleh kosong!")
            continue

        harga = input_angka("Masukkan harga produk  : ")

        if harga == 0:
            print("Harga harus lebih dari 0!")
            continue

        jumlah = input_angka("Masukkan jumlah produk : ")

        if jumlah == 0:
            print("Jumlah harus lebih dari 0!")
            continue

        subtotal = harga * jumlah
        total += subtotal

        produk.append([nama_produk, harga, jumlah, subtotal])

        print("=" * LEBAR)

        tambah = input("Tambah produk? (y/t)   : ").strip().lower()

        while tambah not in ("y", "t"):
            tambah = input("Masukkan y atau t      : ").strip().lower()

        if tambah == "t":
            break

    waktu = datetime.datetime.now()
    id_transaksi, nama_file = buat_id_transaksi(nama_kasir, waktu)

    berhasil = buat_invoice(
        nama_kasir, waktu, id_transaksi, produk, total
    )

    if not berhasil:
        print("Transaksi gagal disimpan!")
        return

    berhasil_riwayat = catat_riwayat(
        waktu, id_transaksi, total
    )

    print("=" * LEBAR)
    print("TRANSAKSI BERHASIL".center(LEBAR))
    print("=" * LEBAR)


def cari_invoice():
    print("\n" + "=" * LEBAR)
    print("CARI TRANSAKSI".center(LEBAR))
    print("=" * LEBAR)

    id_dicari = input("Masukkan ID transaksi  : ").strip()

    if id_dicari == "" or id_dicari.endswith(".txt"):
        print("Masukkan ID saja tanpa .txt.")
        return

    nama_file = os.path.join(
        FOLDER_INVOICE, id_dicari + ".txt"
    )

    if os.path.isfile(nama_file):
        with open(nama_file, "r") as file:
            print("=" * LEBAR)
            print(file.read())
    else:
        print("Invoice tidak ditemukan.")


def main():
    siapkan_folder()
    siapkan_riwayat()

    print("\n" + "=" * LEBAR)
    print("SELAMAT DATANG".center(LEBAR))
    print("=" * LEBAR)

    nama_kasir = input("Masukkan nama kasir    : ").strip()

    while nama_kasir == "":
        print("Nama kasir tidak boleh kosong.")
        nama_kasir = input("Masukkan nama kasir    : ").strip()

    print("=" * LEBAR)

    while True:
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * LEBAR)

        pilihan = input("Masukkan opsi pilihan  : ").strip()

        if pilihan == "1":
            transaksi_baru(nama_kasir)

        elif pilihan == "2":
            cari_invoice()

        elif pilihan == "3":
            print("=" * LEBAR)
            print("SAMPAI JUMPA".center(LEBAR))
            print("=" * LEBAR)
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()