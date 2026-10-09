def adalah_huruf(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

def cek_kata(teks, kata):
    hasil = []
    if kata == '':
        return hasil
    teks_kecil= teks.lower()
    kata_kecil= kata.lower()

    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1
    return hasil

def cek_batas_kata(teks, i, panjang):
    if i == 0:
        kiri_aman = True
    else:   
        kiri_aman = not adalah_huruf(teks[i - 1])
    akhir = i + panjang
    if akhir == len(teks):
        kanan_aman = True
    else:
        kanan_aman = not adalah_huruf(teks[akhir])

    return kiri_aman and kanan_aman


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    indeks_valid = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            indeks_valid.append(i)

    hasil = ""
    posisi = 0                          
    for i in indeks_valid:
        hasil = hasil + teks[posisi:i]  
        for _ in range(panjang):        
            hasil = hasil + simbol
        posisi = i + panjang            
    hasil = hasil + teks[posisi:]       

    return (hasil, len(indeks_valid), indeks_valid)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

teks_tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", teks_tersensor)
print("Jumlah:", jumlah, "| Indeks:", indeks)