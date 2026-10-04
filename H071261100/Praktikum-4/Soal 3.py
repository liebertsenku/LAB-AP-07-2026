def hitung_mundur(angka):
    print(angka)
    if angka == 0:
        print("Luncurkan!")
        return
    hitung_mundur(angka - 1)

while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    except:
        print("Input harus berupa angka bulat")
        continue

    if angka_awal >= 0:
        break

    print("Input tidak valid, angka tidak boleh negatif")

hitung_mundur(angka_awal)