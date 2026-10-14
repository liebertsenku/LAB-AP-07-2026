ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() not in ALFABET:
        return ch

    indeks = ALFABET.find(ch.lower())
    indeks_baru = (indeks + k) % 26
    hasil = ALFABET[indeks_baru]

    if ch.isupper():
        return hasil.upper()

    return hasil


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    kemungkinan = []

    for kunci in range(26):
        pesan = mesin_dekripsi(sandi, kunci)

        if pesan.lower().find(kata_kunci.lower()) != -1:
            kemungkinan.append((kunci, pesan))

    return kemungkinan


while True:
    try:
        pesan = input("Masukkan pesan tersita: ")
        kata_kunci = input("Masukkan kata kunci target: ")

        if pesan.strip() == "":
            raise ValueError("Pesan tidak boleh kosong.")

        if kata_kunci.strip() == "":
            raise ValueError("Kata kunci tidak boleh kosong.")

        hasil = retas_sandi(pesan, kata_kunci)

        if len(hasil) == 0:
            print("Peringatan: Tidak ditemukan pesan yang cocok.")
        else:
            print("Output dekripsi:", hasil)

        break

    except ValueError as e:
        print("Error:", e)
        print("Silakan masukkan data kembali.\n")