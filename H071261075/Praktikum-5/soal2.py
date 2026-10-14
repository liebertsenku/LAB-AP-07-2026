ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    hasil = []

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    start = 0

    while True:
        indeks = teks_kecil.find(kata_kecil, start)

        if indeks == -1:
            break

        hasil.append(indeks)
        start = indeks + 1

    return hasil

def cek_batas_kata(teks, i, panjang):
    # Mengecek karakter sebelum kata
    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in ALFABET:
            return False

    # Mengecek karakter setelah kata
    posisi_akhir = i + panjang

    if posisi_akhir < len(teks):
        sesudah = teks[posisi_akhir].lower()

        if sesudah in ALFABET:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_kemunculan = cek_kata(teks, kata)

    hasil = ""
    jumlah_tersensor = 0
    list_indeks_awal = []

    posisi = 0
    panjang_kata = len(kata)

    for i in indeks_kemunculan:

        if i < posisi:
            continue

        if cek_batas_kata(teks, i, panjang_kata):
            hasil += teks[posisi:i]
            hasil += simbol * panjang_kata

            posisi = i + panjang_kata

            jumlah_tersensor += 1
            list_indeks_awal.append(i)

    hasil += teks[posisi:]

    return (hasil, jumlah_tersensor, list_indeks_awal)


# Program utama
teks = input("Masukkan teks: ")
kata = input("Masukkan kata yang ingin disensor: ")
simbol = input("Masukkan simbol sensor: ")

hasil = sensor_kata(teks, kata, simbol)

print("Teks tersensor:", hasil[0])
print("Jumlah tersensor:", hasil[1])
print("Indeks awal:", hasil[2])