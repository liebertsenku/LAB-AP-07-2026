ALFABET = "abcdefghijklmnopqrstuvwxyz"


def _kecil(teks):
    
    hasil = ""
    for ch in teks:
        k = ch.lower()
        hasil += k if len(k) == 1 else ch
    return hasil


def _huruf(ch):
    k = ch.lower()
    return len(k) == 1 and k in ALFABET


def cek_kata(teks, kata):

    daftar = []
    if kata == "":
        return daftar
    teks_kecil = _kecil(teks)
    kata_kecil = _kecil(kata)
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        daftar.append(idx)
        start = idx + 1
    return daftar


def cek_batas_kata(teks, i, panjang):

    if i > 0 and _huruf(teks[i - 1]):
        return False
    akhir = i + panjang
    if akhir < len(teks) and _huruf(teks[akhir]):
        return False
    return True


def sensor_kata(teks, kata, simbol):
   
    panjang = len(kata)
    pengganti = ""
    for _ in range(panjang):       
        pengganti += simbol
    hasil = ""
    posisi = 0          
    indeks_sensor = []

    for i in cek_kata(teks, kata):
        if i < posisi:  # lewati kemunculan yang tumpang tindih
            continue
        if cek_batas_kata(teks, i, panjang):
            hasil += teks[posisi:i] + pengganti
            posisi = i + panjang
            indeks_sensor.append(i)

    hasil += teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)


if __name__ == "__main__":
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ").strip()
    simbol = input("Masukkan simbol: ")
    if simbol == "":
        simbol = "*"
    simbol = simbol[0]  # satu karakter agar panjang hasil sama dengan kata

    hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", hasil)
    print("Jumlah:", jumlah, "| Indeks:", indeks)