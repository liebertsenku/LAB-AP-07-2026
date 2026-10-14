def cek_kata (teks, kata):
    indeks = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    if kata_kecil == "":
        return indeks
    for i in range(len(teks_kecil)):
        if teks_kecil[i:i + len(kata_kecil)] == kata_kecil:
            indeks.append(i)
    return indeks

def cek_batas_kata(teks, i, panjang):
    # Memeriksa batas sebelum kata
    if i > 0:
        sebelum = teks[i - 1].lower() 
        if sebelum in "abcdefghijklmnopqrstuvwxyz":
            return False

    # Memeriksa batas sesudah kata
    akhir = i + panjang
    if akhir < len(teks):
        sesudah = teks[akhir].lower()
        if sesudah in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True


def sensor_kata(teks, kata, simbol):
    indeks_kata = cek_kata(teks, kata)
    teks_tersensor = ""
    indeks_awal = []
    jumlah = 0
    posisi = 0

    for i in indeks_kata:
        if i < posisi:
            continue
        if cek_batas_kata(teks, i, len(kata)):
            teks_tersensor += teks[posisi:i]
            for j in range(len(kata)):
                teks_tersensor += simbol
            indeks_awal.append(i)
            jumlah += 1
            posisi = i + len(kata)

    # Menambahkan sisa teks setelah kata terakhir
    teks_tersensor += teks[posisi:]

    return (teks_tersensor, jumlah, indeks_awal)


# --- Program utama ---
teks = input("Masukkan Teks: ")

if teks == "":
    print("Teks tidak boleh kosong.")
else:
    kata = input("Masukkan kata target: ")

    if kata == "":
        print("Kata target tidak boleh kosong.")
    else:
        simbol = input("Masukkan simbol: ")

        if simbol == "":
            print("Simbol tidak boleh kosong.")
        else:
            hasil = sensor_kata(teks, kata, simbol)

            print("Hasil Teks:", hasil[0])
            print("Jumlah:", hasil[1], "| Indeks:", hasil[2])