print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        N = int(input("Masukkan jumlah baris: "))
    except ValueError:
        print("Input baris harus berupa angka!")
        print()
        continue

    if N <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue

    break

while True:
    try:
        M = int(input("Masukkan jumlah kursi: "))
    except ValueError:
        print("Input baris harus berupa angka!")
        print()
        continue
    if M <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue
    
    break

print()
print("--- Daftar Kursi Tersedia ---")

for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
       
        if baris == 1 and kursi % 2 == 0:
            continue

        if kursi == 13:
            continue

        print(f"Baris {baris} - Kursi {kursi}")

