import os
import random
from datetime import datetime

os.makedirs("invoices", exist_ok=True)

print("\n===========================")
print("     Selamat Datang    ")
print("===========================")

while True:
    kasir = input("Nama kasir: ").strip()
    if kasir and kasir.isalpha():
        break
    print("Nama kasir tidak boleh kosong dan Harus berupa huruf!")

def buat_invoice(kasir):
    waktu = datetime.now()
    inisial = kasir[:3].upper()
    # inisial = "".join(k[0] for k in kasir.split()).upper()

    id_transaksi = inisial + waktu.strftime("%y%m%d%H%M") + str(random.randint(100, 999))

    produk = []
    total = 0

    while True:
        nama = input("Nama produk: ").strip()
        if not nama:
            print("Nama produk tidak boleh kosong!")
            continue

        try:
            harga = float(input("Harga produk: "))
            jumlah = int(input("Jumlah produk: "))

            if harga <= 0 or jumlah <= 0:
                print("Harga dan jumlah harus lebih besar dari 0!")
                continue

        except ValueError:
            print("Harga harus berupa angka dan jumlah harus berupa bilangan bulat!")
            continue

        subtotal = harga * jumlah
        total += subtotal
        produk.append((nama, harga, jumlah, subtotal))

        while True:
            tambah_produk = input("Tambah Produk ? (y/t): ").strip().lower()
            if tambah_produk in ["y", "t"]:
                break
            print("Pilihan tidak valid! Harap masukkan 'y' atau 't'.")

        if tambah_produk == "t":
            break

    if not produk:
        print("Transaksi dibatalkan!")
        return

    with open(f"invoices/{id_transaksi}.txt", "w") as f:
        f.write("==============================\n")
        f.write("       INVOICE BELANJA        \n")
        f.write("==============================\n")
        f.write(f"ID Transaksi : {id_transaksi}\n")
        f.write(f"Kasir        : {kasir}\n")
        f.write(f"Waktu        : {waktu:%Y-%m-%d %H:%M:%S}\n")
        f.write("-" * 30 + "\n")

        for nama, harga, jumlah, subtotal in produk:
            f.write(f"{nama:<15} | Rp{harga:,.0f} x {jumlah} = Rp{subtotal:,.0f}\n")

        f.write("-" * 30 + "\n")
        f.write(f"TOTAL: Rp{total:,.0f}\n")
        f.write("==============================\n")

    history_file = "trx_history.txt"
    file_exists = os.path.isfile(history_file)

    with open(history_file, "a") as f:
        if not file_exists:
            f.write("==================================================================\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<17} |\n")
            f.write("==================================================================\n")
        
        f.write(f"| {waktu.strftime('%Y-%m-%d %H:%M:%S')} | {id_transaksi:<18} | Rp. {total:<13,.0f} |\n")
        f.write("==================================================================\n")

    print("Transaksi Berhasil")


def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ").strip()
    file = f"invoices/{id_transaksi}.txt"

    if os.path.isfile(file):
        print("\n--- ISI INVOICE ---")
        with open(file, "r") as f:
            print(f.read())
    else:
        print("Invoice tidak ditemukan!")


def lihat_riwayat():
    if os.path.isfile("trx_history.txt"):
        print("\n=== RIWAYAT TRANSAKSI ===")
        with open("trx_history.txt", "r") as f:
            print(f.read())
    else:
        print("Belum ada riwayat transaksi!")

while True:
    print("===========================")
    print("1. Buat invoice")
    print("2. Cari invoice")
    print("3. Riwayat transaksi")
    print("0. Keluar")

    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        buat_invoice(kasir)
    elif pilih == "2":
        cari_invoice()
    elif pilih == "3":
        lihat_riwayat()
    elif pilih == "0":
        print("Terima kasih telah menggunakan aplikasi kasir!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 0-3.")