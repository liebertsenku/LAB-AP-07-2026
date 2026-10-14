ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""

    for ch in teks:
        ch = ch.lower()

        if ch in ALFABET:
            hasil += ch

    return hasil


def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))

    if teks == teks_balik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)


def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)

    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            substring = teks_bersih[i:j]

            hasil = cek_palinrome(substring)

            if hasil[0]:
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }

teks = input("Masukkan teks prasasti: ")

print("Teks bersih:", bersihkan_teks(teks))
print(inti_palinrome(teks))