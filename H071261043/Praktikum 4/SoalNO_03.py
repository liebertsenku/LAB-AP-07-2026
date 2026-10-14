def minta_angka():
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
    except :
        print("Input tidak valid, angka tidak boleh negatif atau desimal.")
        return minta_angka()
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif atau desimal.")
        return minta_angka()
    return angka

def hitung_mundur(n):
    print(n)
    if n == 0:
        return
    hitung_mundur(n - 1)

angka_awal = minta_angka()
hitung_mundur(angka_awal)
print("Luncurkan!")