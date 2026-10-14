def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    # Iterasi per karakter & pengecekan manual ke string alfabet
    for char in teks:
        char_lower = char.lower()
        if char_lower in alfabet:
            teks_bersih += char_lower
    return teks_bersih


def cek_palinrome(teks):
    # Memeriksa palinrome menggunakan reversed() dan join()
    if teks == "":
        return False, -1
    teks_dibalik = "".join(reversed(teks))
    if teks == teks_dibalik:
        return True, -1
    # Mencari indeks pertama yang berbeda jika tidak simetris
    for i in range(len(teks)):
        if teks[i] != teks_dibalik[i]:
            return False, i


def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)

    max_len = 0
    hasil_teks = ""
    indeks_awal = 0

    n = len(teks_bersih)

    # Nested loop dan slicing untuk mencari palindrom terpanjang
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_bersih[i:j]
            cek = cek_palinrome(sub)

            if cek [0]:
                panjang_sub = len(sub)
                # Jika panjang, simpan
                if panjang_sub > max_len:
                    max_len = panjang_sub
                    hasil_teks = sub
                    indeks_awal = i

    return {"teks": hasil_teks, "panjang": max_len, "indeks_awal": indeks_awal}


# --- Program Utama / Pengujian ---
input_user = input("Masukkan teks: ")
teks_bersih = bersihkan_teks(input_user)

if teks_bersih == "":
    print("Input tidak mengandung huruf alfabet")
else:
    hasil = inti_palinrome(teks_bersih)
    print(f"Teks Bersih: {teks_bersih}")
    print(f"Output Terharap: {hasil}")