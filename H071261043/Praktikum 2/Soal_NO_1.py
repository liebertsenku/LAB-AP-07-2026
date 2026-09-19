print ("SOAL 1")
print ("KLASIFIKASI TINGKAT KEPEDASAN MAKANAN RESTORAN")

persentase_kepedasan = int(input("Masukkan persentase kepedasan : "))
if persentase_kepedasan < 0 or persentase_kepedasan > 100:
    print ("Tidak Valid")
elif persentase_kepedasan <= 10:
    print ("Aman")
elif persentase_kepedasan <= 40:
    print ("Sedang")
elif persentase_kepedasan <= 70:
    print ("Pedas")
elif persentase_kepedasan > 70:
    print ("Ekstrem")
else:
    print ("Tidak Valid")
print ()