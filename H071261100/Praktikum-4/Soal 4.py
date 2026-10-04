def konversi_suhu(suhu, asal, tujuan):

    asal = asal.upper().strip()
    tujuan = tujuan.upper().strip()

    skala_valid = ("C", "F", "K")

    # Validasi skala asal
    if asal not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Validasi skala tujuan
    if tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Suhu asal menjadi Celsius
    if asal == "C":
        celsius = suhu

    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9

    else:  # Kelvin
        celsius = suhu - 273.15

    # Celsius ke skala tujuan
    if tujuan == "C":
        hasil = celsius

    elif tujuan == "F":
        hasil = (celsius * 9 / 5) + 32

    else:  # Kelvin
        hasil = celsius + 273.15

    return hasil


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)

    except ValueError:
        print("Suhu harus berupa angka!")
        continue

    skala_valid = ("C", "F", "K")

#Input skala asal
    while True:
        asal = input("Skala asal (C/F/K): ").upper().strip()

        if asal in skala_valid:
            break
        else:
            print("Skala asal tidak dikenali. Masukkan C, F, atau K.")

    # Input skala tujuan
    while True:
        tujuan = input("Skala tujuan (C/F/K): ").upper().strip()

        if tujuan in skala_valid:
            break
        else:
            print("Skala tujuan tidak dikenali. Masukkan C, F, atau K.")

    hasil = konversi_suhu(suhu, asal, tujuan)

    print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")