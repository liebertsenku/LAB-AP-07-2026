import os
import random
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_INVOICE = os.path.join(BASE_DIR, "invoices")
FILE_HISTORY = os.path.join(BASE_DIR, "trx_history.txt")

LEBAR = 58
GARIS = "=" * LEBAR
LABEL = 24 

def garis():
    print(GARIS)

def judul(teks):
    garis()
    print(teks.center(LEBAR))
    garis()

def tanya(label):
    return input(label.ljust(LABEL) + ": ").strip()

def tanya_angka(label, tipe=int):
    while True:
        nilai = tanya(label)
        try:
            angka = tipe(nilai)
            if angka <= 0:
                print("Nilai harus lebih dari 0!")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka!")

def tampilkan_menu():
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    garis()

#Soal 1: Invoice
def ambil_inisial(nama):
    inisial = "".join(kata[0] for kata in nama.split() if kata)
    return inisial.upper()

def buat_id_transaksi(nama_kasir, waktu):
    inisial = ambil_inisial(nama_kasir)
    tanggal_waktu = waktu.strftime("%y%m%d%H%M")  
    acak = random.randint(100, 999)
    return f"{inisial}{tanggal_waktu}{acak}"

def rupiah(angka):
    return f"Rp. {angka}"

def buat_invoice(id_trx, nama_kasir, waktu, daftar_produk, total):
    os.makedirs(FOLDER_INVOICE, exist_ok=True)

    baris = []
    baris.append(GARIS)
    baris.append("INVOICE".center(LEBAR).rstrip())
    baris.append(GARIS)
    baris.append(f"ID Transaksi : {id_trx}")
    baris.append(f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}")
    baris.append(f"Kasir        : {nama_kasir}")
    baris.append(GARIS)
    baris.append(f"{'Produk':<20}{'Harga':>10}{'Jml':>6}{'Subtotal':>14}")
    baris.append("-" * LEBAR)
    for nama, harga, jumlah in daftar_produk:
        subtotal = harga * jumlah
        baris.append(f"{nama[:19]:<20}{harga:>10}{jumlah:>6}{subtotal:>14}")
    baris.append(GARIS)
    baris.append(f"{'TOTAL':<36}{rupiah(total):>22}")
    baris.append(GARIS)
    baris.append("Terima kasih atas kunjungan Anda".center(LEBAR).rstrip())
    baris.append(GARIS)

    path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")
    with open(path, "w") as g:
        g.write("\n".join(baris) + "\n")

# Soal 3: Riwayat transaksi
W_WAKTU = 21
W_ID = 18
W_NOMINAL = 19

def format_baris_history(waktu, id_trx, nominal):
    return (
        f"| {waktu:<{W_WAKTU - 2}} "
        f"| {id_trx:<{W_ID - 2}} "
        f"| {nominal:<{W_NOMINAL - 2}} |"
    )

def catat_history(waktu, id_trx, total):
    garis_tabel = "=" * (W_WAKTU + W_ID + W_NOMINAL + 4)
    baris_baru = format_baris_history(
        waktu.strftime("%Y-%m-%d %H:%M:%S"), id_trx, rupiah(total)
    )

    if os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, "r") as f:
            isi = f.read().splitlines()
        if isi and isi[-1] == garis_tabel:
            isi.pop()
    else:
        isi = [
            garis_tabel,
            format_baris_history("Waktu", "ID Transaksi", "Nominal Transaksi"),
            garis_tabel,
        ]

    isi.append(baris_baru)
    isi.append(garis_tabel)

    with open(FILE_HISTORY, "w") as f:
        f.write("\n".join(isi) + "\n")


def transaksi_baru(nama_kasir):
    daftar_produk = []

    while True:
        garis()
        nama = tanya("Masukkan nama produk")
        while not nama:
            print("Nama produk tidak boleh kosong!")
            nama = tanya("Masukkan nama produk")
        harga = tanya_angka("Masukkan harga produk")
        jumlah = tanya_angka("Masukkan jumlah produk")
        daftar_produk.append((nama, harga, jumlah))

        garis()
        lagi = tanya("Tambah produk? (y/t)").lower()
        while lagi not in ("y", "t"):
            print("Masukkan 'y' atau 't' saja!")
            lagi = tanya("Tambah produk? (y/t)").lower()
        if lagi == "t":
            break

    waktu = datetime.now()
    total = sum(harga * jumlah for _, harga, jumlah in daftar_produk)
    id_trx = buat_id_transaksi(nama_kasir, waktu)

    buat_invoice(id_trx, nama_kasir, waktu, daftar_produk, total)
    catat_history(waktu, id_trx, total)

    judul("TRANSAKSI BERHASIL")
    print(f"ID Transaksi : {id_trx}")
    garis()

# Soal 2 / Menu 2: Cari transaksi
def cari_transaksi():
    garis()
    id_trx = tanya("Masukkan ID transaksi").upper()
    garis()

    path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")
    if id_trx and os.path.isfile(path):
        with open(path, "r",) as f:
            print(f.read())
    else:
        judul("TRANSAKSI TIDAK DITEMUKAN")

judul("SELAMAT DATANG")
nama_kasir = tanya("Masukkan nama kasir")
while not nama_kasir:
    print("Nama kasir tidak boleh kosong!")
    nama_kasir = tanya("Masukkan nama kasir")
    garis()
while True:
    tampilkan_menu()
    pilihan = tanya("Masukkan opsi pilihan")

    if pilihan == "1":
        transaksi_baru(nama_kasir)
    elif pilihan == "2":
        cari_transaksi()
    elif pilihan == "3":
        judul("TERIMA KASIH")
        break
    else:
        judul("OPSI TIDAK VALID")