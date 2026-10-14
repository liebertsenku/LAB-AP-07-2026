ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    huruf = ch.lower()
    posisi = ALFABET.find(huruf)
    # Jika bukan huruf alfabet, karakter tidak diubah
    if posisi == -1:
        return ch
    # Geser huruf sesuai kunci
    posisi_baru = (posisi + k) % len(ALFABET)
    hasil = ALFABET[posisi_baru]
    # Pertahankan huruf kapital
    if ch.isupper():
        hasil = hasil.upper()
    return hasil

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    # Dekripsi menggunakan arah pergeseran sebaliknya
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)
        # Cari kata kunci tanpa membedakan huruf kapital
        kata_ditemukan = (kata_kunci.casefold() in pesan_asli.casefold())
        if kata_ditemukan:
            hasil.append((kunci, pesan_asli))
    return hasil

# --- Program utama ---
def main():
    while True:
        sandi = input("Masukkan pesan tersita: ")
        if sandi.strip():
            break
        print("Pesan tidak boleh kosong. Silakan coba lagi")

    while True:
        kata_kunci = input("Masukkan kata kunci target: ")

        if kata_kunci.strip():
            break
        print("Kata kunci tidak boleh kosong. Silakan coba lagi.")

    hasil = retas_sandi(sandi, kata_kunci)

    if hasil:
        print("Output Deskripsi:")
        for kunci, pesan in hasil:
            print(f"{kunci}, '{pesan}'")
    else:
        print("Tidak ditemukan hasil yang cocok.")

if __name__ == "__main__":
    main()