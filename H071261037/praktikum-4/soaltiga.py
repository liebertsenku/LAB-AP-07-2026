def htng_mndr(n):
    if n == 0:
        print(0)
        print('luncurkan')
        
    else:
        print(n)
        htng_mndr(n - 1)

while True:
    try:
        angka = int(input('masukkan angka awal hitung mundur:'))
    except ValueError:
        print('input harus berupa angka.')
        continue

    if angka <= 0:
        print('input tidak valid, angka tidak boleh negatif')
        continue
    else:
        htng_mndr(angka)
        break