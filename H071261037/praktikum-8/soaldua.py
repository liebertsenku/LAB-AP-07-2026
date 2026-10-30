import re

def cek_username(username):
    return re.match( r'^[a-zA-Z]\w{5,12}$', username)

username_valid = []       
print('===== registrasi username =====')
print('ketik SELESAI untuk mengakhiri')
print()

while True:
    username = input('masukkan username: ').lower()
    if username == 'selesai':
        break
    elif cek_username(username):
        print('username tersedia')
        username_valid.append(username)
    else:
        print('username tidak valid')
print()

print('======= Rekapitulasi =======')
print('username valid:')
for nomor, name in enumerate(username_valid, start=1):
    print(f'{nomor}.  {name}')
print()

print(f'jumlah username valid: {len(username_valid)}')




