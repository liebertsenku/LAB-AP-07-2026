import re

def cek_nim(nim):
    pattern = r'^H071\d{6}$'
    hasil = re.match(pattern, nim)
    if hasil:
        print ('NIM: valid')
        return True
    else:
        print('format NIM tidak valid')
        return False

def cek_email(email):
    pattern = r'^\w+@[a-zA-Z]+\.[a-zA-Z]+$'
    hasil = re.match(pattern, email)
    if hasil:
        print('email: valid')
        return True
    else:
        print('email: tidak valid')
        return False

def cek_nomor(nomor):
    pattern = r'^\d{10,13}$'
    hasil = re.match(pattern, nomor)
    if hasil:
        print('nomor telfon: valid')
        return True
    else: 
        print('nomor telfon: tidak valid')
        return False

print('=== validasi data mahasiswa ===')
nim = input('masukan nim: ')
email = input('masukkan email: ')
nomor = input('masukan no. telp: ')
print()

print('=== hasil validasi ===')
nim_valid = cek_nim(nim)
email_valid = cek_email(email)
nomor_valid = cek_nomor(nomor)
print()

if nim_valid and email_valid and nomor_valid:
    print('data mahasiswa berhasil diverifikasi')

