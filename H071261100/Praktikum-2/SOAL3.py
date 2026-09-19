nilai = int(input("Masukkan nilai tes: "))


if nilai >= 80:
    print("Lolos ke tahap wawancara")
elif nilai >= 65:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): ")) 
    if pengalaman >=2:
        print("Lolos bersyarat")
    else:
        print("Tidak lolos")
else:
    print("Tidak lolos")