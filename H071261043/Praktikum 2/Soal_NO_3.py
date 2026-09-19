print("SOAL 3")
print("Menentukan Kriteria Kelulusan Wawancara")

nilai_tes = int(input("Masukkan nilai tes wawancara (0-100) : "))

if nilai_tes < 0 or nilai_tes > 100:
    print("Maaf nilai tidak valid, masukkan nilai yang valid")
elif nilai_tes < 65:
    print("Maaf anda tidak lolos")
else:
    
    
    if nilai_tes >= 80:
        print("Lolos ke tahap wawancara")
    elif nilai_tes >= 65:
        pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun) : "))  
        if pengalaman_kerja <2 :
            print("Tidak Lulus")
        else:
            print ("Lulus Bersyarat")
    else:
        print("Maaf anda tidak lolos")