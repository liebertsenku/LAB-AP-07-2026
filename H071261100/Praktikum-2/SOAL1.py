cabai = int(input("Masukkan presentase cabai: "))

if cabai < 0:
    print("Tidak valid")
elif cabai <= 10:
    print("Level aman")
elif cabai <= 40:
    print("Level sedang")
elif cabai <= 70:
    print("Level pedas")
else:
    print("Level ekstrem")