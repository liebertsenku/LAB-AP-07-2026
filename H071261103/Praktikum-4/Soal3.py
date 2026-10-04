def hitung_mundur(angka):
    print(angka)

    if angka == 0:
        print("Luncurkan!")
    elif angka <0:
        print("Angka tidak boleh kurang dari 0")
    else:
        hitung_mundur(angka - 1)


while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))

        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
        
    except:
        print("Input harus berupa angka")
    else:
        hitung_mundur(angka_awal)
        break