def bersihkan_teks(teks):
   alfabet = "abcdefghijklmnopqrstuvwxyz"
   hasil = ''
   for karakter in teks.lower():
        if karakter in alfabet:
            hasil+= karakter
   return hasil

def cek_palindrome(teks):
    terbalik = ''.join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for indeks_beda in range(len(teks)):
        if teks[indeks_beda] != terbalik[indeks_beda]:
            return (False, indeks_beda)
    return(True, -1)

def inti_palindrome(teks):
    terbaik = ''
    indeks_awal = 0
    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            kandidat = teks[i:j]
            simetris, _ = cek_palindrome(kandidat)
            if simetris and len(kandidat) > len(terbaik):
                terbaik = kandidat
                indeks_awal = i
    return('teks:', terbaik, 'panjang:', len(terbaik),'indeks:', indeks_awal)


masukan = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(masukan)

print("Teks bersih:", bersih)
print('output terharap:', inti_palindrome(bersih))