# SOAL 2: Sensor Kata

ALFABET = "abcdefghijklmnopqrstuvwxyz"


def adalah_huruf(ch):
    return ch in ALFABET or ch in ALFABET.upper()


def cek_kata(teks, kata):
    hasil = []
    if kata == "":
        return hasil

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    i = teks_kecil.find(kata_kecil, 0)
    while i != -1:
        hasil.append(i)
        i = teks_kecil.find(kata_kecil, i + 1)
    return hasil


def cek_batas_kata(teks, i, panjang):
    akhir = i + panjang
    kiri_aman = (i == 0) or not adalah_huruf(teks[i - 1])
    kanan_aman = (akhir == len(teks)) or not adalah_huruf(teks[akhir])
    return kiri_aman and kanan_aman


def sensor_kata(teks, kata, simbol):
    if simbol == "":
        simbol = "*"

    hasil = ""
    indeks = []
    terakhir = 0  # teks asli sudah disalin sampai posisi ini

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, len(kata)):
            hasil += teks[terakhir:i] + simbol[0] * len(kata)
            terakhir = i + len(kata)
            indeks.append(i)

    hasil += teks[terakhir:]
    return (hasil, len(indeks), indeks)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ").strip()
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)
