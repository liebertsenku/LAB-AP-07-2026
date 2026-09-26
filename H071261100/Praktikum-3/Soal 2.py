print("---Setup Denai Bioskop NontonYuk---")

while True:
    try:
        N = int(input("Masukkan jumlah baris: "))
        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

while True:
    try:
        M = int(input("Masukkan jumlah kursi perbaris: "))
        if M <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        
    except ValueError:
        print("Input kursi harus berupa angka!")

print("---Daftar Kursi Tersedia---")
for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        if baris == 1 and kursi % 2 == 0:
            continue
        if kursi == 13: 
            continue
        print(f"Baris {baris} - Kursi {kursi}")