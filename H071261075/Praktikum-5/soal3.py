ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
   
    if ch.lower() not in ALFABET:
        return ch

    huruf_kecil = ch.lower()

    indeks = ALFABET.find(huruf_kecil)

    indeks_baru = (indeks + k) % 26

    hasil = ALFABET[indeks_baru]

    if ch.isupper():
        return hasil.upper()

    return hasil.lower()


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    kata_kunci = kata_kunci.lower()

    for k in range(26):
        pesan_asli = mesin_dekripsi(sandi, k)

        if pesan_asli.lower().find(kata_kunci) != -1:
            hasil.append((k, pesan_asli))

    return hasil

sandi = input("Masukkan pesan tersandi: ")
kata_kunci = input("Masukkan kata kunci target: ")

print("Hasil retas:", retas_sandi(sandi, kata_kunci))
