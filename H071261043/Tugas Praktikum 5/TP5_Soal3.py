ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    
    kecil = ch.lower()
    pos = ALFABET.find(kecil) if len(ch) == 1 else -1
    if pos == -1:                      
        return ch
    baru = ALFABET[(pos + k) % 26]
    if ch == kecil:
        return baru.lower()
    return baru.upper()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)    


def retas_sandi(sandi, kata_kunci):
    
    kandidat = []
    kata_kunci = kata_kunci.strip()
    if kata_kunci == "":           
        return kandidat
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) !=-1 :
            kandidat.append((k, pesan))
    return kandidat


if __name__ == "__main__":
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kunci = input("Masukkan kata kunci target: ")
    print()
    print("Output Deskripsi:", retas_sandi(sandi, kunci))
