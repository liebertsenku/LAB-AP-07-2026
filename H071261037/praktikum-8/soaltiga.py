import re

def bersihkan_nomor(nomor):
    pattern = r'[\s-]'
    hasil = re.sub(pattern, '', nomor)
    if hasil:
        nomor_bersih.append(hasil)
        nomor_kotor.append(nomor)
        

def cek_nomor(nomor):
    pattern = r'^\d{10,13}$'
    for nomor in nomor_bersih:
        hasil = re.match(pattern, nomor)
        if hasil:
            nomor_valid.append(nomor)
            
nomor_bersih = []
nomor_kotor = []
nomor_valid = []

print('====== PEMBERSIHAN DATA NOMOR TELEPON =======')
try:
        jumlah = int(input('masukan jumlah data: '))
except:
        print('jumlah data harus berupa angka')
print()

for i in range(jumlah):
    nomor = input(f'nomor ke-{i+1}: ')
    bersihkan_nomor(nomor)
cek_nomor(nomor)
print()

print('======== hasil pembersihan ========')
print()

for i in range(jumlah):
    if nomor_bersih[i] in nomor_valid:
        status = 'valid'
    else:
        status = 'tidak valid'
    print(f'data {i + 1}:')
    print(f'sebelum: {nomor_kotor[i]}')
    print(f'sesudah: {nomor_bersih[i]}')
    print(f'status: {status}')
print()

print(f'jumlah nomor valid: {len(nomor_valid)}')
