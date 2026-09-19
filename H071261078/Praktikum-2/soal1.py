# bismillah alia bisa

#tugas 1

angka = int(input("Masukkan persentase cabai :"))

if angka >= 0 and angka <= 10:
    print("Level Aman")
elif angka >= 11 and angka <= 40:
    print("Level Sedang")
elif angka >= 41 and angka <= 70:
    print("Level Pedas")
elif angka >= 70 and angka <= 100:
    print("Level Ekstream")
else:
    print("invalid")