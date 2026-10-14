def konversi_suhu(suhu, skala_asal, skala_tujuan):
    if skala_asal not in ("C", "F", "K") or skala_tujuan not in ("C", "F", "K"):
        raise ("Skala suhu tidak dikenali.")

    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:  
        celsius = suhu - 273.15
    
    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:  
        hasil = celsius + 273.15

    return round(hasil, 2)

print("=== Konversi Suhu ===")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if masukan.strip().lower() == "selesai":
        break

    try:
        suhu = float(masukan)
    except :
        print("Error: Suhu harus berupa angka.")
        continue

    skala_asal = input("Skala asal (C/F/K): ").strip().upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except:
        print("Error: Skala suhu tidak dikenali.")