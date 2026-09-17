#soal ketiga
nilai_tes = int(input('masukan nilai tes : '))

if nilai_tes >=80 and nilai_tes <=100 :
     print('lolos ke tahap wawancara')
elif nilai_tes >=65 :
    pengalaman_kerja =int(input('masukan pengalaman kerja(tahun) : '))
    if pengalaman_kerja >=2 :
     print('lolos bersyarat')
    else:
     print('tidak lolos')
else:
     print('tidak lolos')