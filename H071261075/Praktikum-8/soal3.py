
import re

def validasi_nomor(nomor):
    hasil = re.search(r'^\d{10,13}$', nomor)
    return hasil

print("=== Pembersihan Data Nomor Telepon ===")

while True:
    try:
        jumlah = int(input("Masukkan jumlah nomor telepon: "))
        if jumlah > 0:
            break
        else:
            print("Jumlah harus lebih dari 0!")
    except ValueError:
        print("Masukkan jumlah dalam bentuk angka!")

data_awal = []
data_bersih = []
nomor_valid = set()

i = 0
while i < jumlah:
    nomor = input(f"Masukkan nomor ke-{i + 1}: ")
    data_awal.append(nomor)

    hasil = re.sub(r'\s|-', '', nomor)
    data_bersih.append(hasil)

    if validasi_nomor(hasil):
        nomor_valid.add(hasil)
        print("Nomor telepon valid.")
    else:
        print("Nomor telepon tidak valid!")

    i += 1

print("\n=== Hasil Pembersihan ===")

i = 0

while i < jumlah:
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {data_awal[i]}")
    print(f"Sesudah : {data_bersih[i]}")

    if validasi_nomor(hasil):
        nomor_valid.add(hasil)
        status = "Valid"
    else:
        status = "Tidak valid"

        print("Status  :", status)

    i += 1

print(f"\nJumlah nomor valid: {len(nomor_valid)}")
print(nomor_valid)
