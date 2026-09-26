print('---setup denah bioskop nontonyuk---')

while True:
    try:
        baris = int(input('masukan jumlah baris: '))
        if baris <= 0:
            print('jumlah baris harus lebih dari 0')
            continue
        break
    except ValueError:
        print('input baris harus berupa angka')

while True:
    try:
        kursi = int(input('masukan jumlah kursi per baris: '))
        if kursi <= 0:  
            print('jumlah kursi harus lebih dari 0')
            continue
        break
    except ValueError:
        print('input kursi harus berupa angka')

print('---daftar kursi tersedia--')

for baris in range (1, baris + 1):
    for kursi in range (1, kursi + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue
        print('baris', baris, 'kursi', kursi)