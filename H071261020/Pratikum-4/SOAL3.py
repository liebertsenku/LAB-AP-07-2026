def hitung_mundur(angka):
    print(angka)

    if angka == 0:
        print("Luncurkan!")
        return

    hitung_mundur(angka - 1)


while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
    except ValueError:
        print("Inputnya harus angka.")
        continue

    if angka_awal < 0:
        print("angkanya tidak boleh negatif.")
        continue

    break

hitung_mundur(angka_awal)