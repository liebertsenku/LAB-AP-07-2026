def cek_kata(teks, kata):
    indeks = []
    start = 0

    while True:
        posisi = teks.lower().find(kata.lower(), start)

        if posisi == -1:
            break

        indeks.append(posisi)
        start = posisi + 1

    return indeks


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0 and teks[i - 1].lower() in alfabet:
        return False

    akhir = i + panjang

    if akhir < len(teks) and teks[akhir].lower() in alfabet:
        return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks = cek_kata(teks, kata)
    indeks_valid = []

    for i in indeks:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)

    hasil = ""
    posisi = 0

    for i in indeks_valid:
        hasil += teks[posisi:i]
        hasil += simbol * len(kata)
        posisi = i + len(kata)

    hasil += teks[posisi:]

    return hasil, len(indeks_valid), indeks_valid


while True:
    try:
        teks = input("Masukkan teks: ")
        # alfabet = "abcdefghijklmnopqrstuvwxyz"

        if teks.strip() == "":
            print("Error: Teks tidak boleh kosong.\n")
            continue
        # if not any(huruf.lower() in alfabet for huruf in teks):
        #     print("Error: Teks harus mengandung huruf.")
        #     continue

        kata = input("Kata yang disensor: ")

        if kata.strip() == "":
            print("Error: Kata target tidak boleh kosong.\n")
            continue

        simbol = input("Simbol sensor: ")

        if len(simbol) != 1:
            print("Error: Simbol sensor harus tepat satu karakter.\n")
            continue

        hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

        if jumlah == 0:
            print("Peringatan: Kata utuh tidak ditemukan.")
        else:
            print("Teks tersensor:", hasil)
            print("Jumlah tersensor:", jumlah)
            print("Indeks awal:", indeks)

        break

    except ValueError as e:
        print("Error:", e)
        print("Silakan masukkan data kembali.\n")