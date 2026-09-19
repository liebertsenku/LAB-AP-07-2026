#tugas 3


nilai = int(input("Masukkan nilai tes: "))

if nilai <= 0:
    print("Tidak lolos")
elif nilai >= 80 and nilai < 100:
    print("Lolos wawancara")
elif nilai >= 65 and nilai < 80:     
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))
    if pengalaman >= 2:
        print("Lolos bersyarat")
    else:
        print("Tidak lolos")
else:
    print("Tidak lolos")
