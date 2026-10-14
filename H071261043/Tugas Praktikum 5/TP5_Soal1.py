ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for a in teks:
        kecil = a.lower()
        if len(kecil) == 1 and kecil in ALFABET:
            hasil += kecil
    return hasil


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    bersih = bersihkan_teks(teks)
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}

    for i in range(len(bersih)):
        for j in range(i + 1, len(bersih) + 1):
            sub = bersih[i:j]
            simetris, _ = cek_palinrome(sub)
            if simetris and len(sub) > terbaik["panjang"]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terbaik


if __name__ == "__main__":
    teks = input("Masukkan teks prasasti: ")
    print()
    print("Teks Bersih:", bersihkan_teks(teks))
    print("Output Terharap:", inti_palinrome(teks))
