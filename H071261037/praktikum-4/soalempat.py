print('=== konversi suhu ===')
def konversi_suhu(suhu, asal, tujuan):
    if asal == 'c':
        celcius = suhu
    elif asal == 'f':
        celcius = (suhu - 32) * 5/9
    elif asal == 'k':
        celcius = suhu - 273.15
    else:
        raise ValueError('skala suhu tidak dikenali')

    if tujuan == 'c':
        return celcius
    elif tujuan == 'f':
        return celcius * 9 / 5 + 32
    elif tujuan == 'k':
        return celcius + 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali.")

while True:
    suhu = input('masukan suhu(ketik selesai untuk keluaar):')
    if suhu == 'selesai':
        break
    try:
        suhu = float(suhu)
        asal = input('skala asal (C/F/K):').lower()
        tujuan = input('skala tujuan (C/F/K):').lower()
        hasil = konversi_suhu(suhu, asal, tujuan)
        print('hasil:', suhu, asal.upper(), hasil, tujuan.upper())
    except ValueError:
        print('invalid')