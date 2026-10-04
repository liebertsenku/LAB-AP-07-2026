def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    if skala_asal not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_asal == skala_tujuan:
        return suhu

    if skala_asal == "C":
        if skala_tujuan == "F":
            return (suhu * 9 / 5) + 32
        elif skala_tujuan == "K":
            return suhu + 273.15

    elif skala_asal == "F":
        if skala_tujuan == "C":
            return (suhu - 32) * 5 / 9
        elif skala_tujuan == "K":
            return (suhu - 32) * 5 / 9 + 273.15

    elif skala_asal == "K":
        if skala_tujuan == "C":
            return suhu - 273.15
        elif skala_tujuan == "F":
            return (suhu - 273.15) * 9 / 5 + 32


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)

        skala_asal = input("Skala asal (C/F/K): ")
        skala_tujuan = input("Skala tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil:.1f} {skala_tujuan.upper()}")

    except ValueError as e:
        print(f"Error: {e}")