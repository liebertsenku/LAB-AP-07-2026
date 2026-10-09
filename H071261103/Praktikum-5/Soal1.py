
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for huruf in teks.lower():
        if huruf in alfabet:
            hasil += huruf

    return hasil

def cek_palinrome(teks):
    balik = "".join(reversed(teks))

    if teks == balik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != balik[i]:
            return False, i

    return False, -1

def inti_palinrome(teks):
    teks = bersihkan_teks(teks)

    if teks == "":
        raise ValueError("Teks harus mengandung minimal satu huruf alfabet.")

    terbaik = ""
    indeks = -1

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            substring = teks[i:j]

            if cek_palinrome(substring)[0]:
                if len(substring) > len(terbaik):
                    terbaik = substring
                    indeks = i
    
    return {
        "teks": terbaik,
        "panjang": len(terbaik),
        "indeks_awal": indeks
    }
    
while True:
    try:
        teks = input("Masukkan teks: ")

        if teks.strip() == "":
            raise ValueError("Input tidak boleh kosong.")

        hasil = inti_palinrome(teks)
        hasil2 =bersihkan_teks(teks)
        print ("Teks Bersih" + hasil2)
        print("Hasil:", hasil)
        break

    except ValueError as e:
        print("Error:", e)