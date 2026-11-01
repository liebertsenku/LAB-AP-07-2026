import re

print("=== Pembersihan Data Nomor Telepon ===")
jumlah_data = int(input("Masukkan jumlah data: "))

daftar_telepon = []
jumlah_valid = 0

for i in range(1, jumlah_data + 1):
    nomor_input = input(f"Nomor ke-{i}: ")
    nomor_bersih = re.sub(r'[ -]', '', nomor_input)
    pola_validasi = r'^\d{10,13}$'
    if re.match(pola_validasi, nomor_bersih):
        status = "Valid"
        jumlah_valid += 1
    else:
        status = "Tidak valid"
        
    daftar_telepon.append({
        "sebelum": nomor_input,
        "sesudah": nomor_bersih,
        "status": status
    })

print("\n--- Hasil Pembersihan ---")
for index, data in enumerate(daftar_telepon, 1):
    print(f"Data {index}:")
    print(f"Sebelum: {data['sebelum']}")
    print(f"Sesudah: {data['sesudah']}")
    print(f"Status : {data['status']}")
    print()

print(f"Jumlah nomor valid: {jumlah_valid}")