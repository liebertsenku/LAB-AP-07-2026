# database = []
# def hitung_nilai(*nilai):
#     if not nilai 
#     terendah = (min(nilai))
#     tertinggi = (max(nilai))
#     rata_ratanya = sum(nilai) / len(nilai)
#     return rata_ratanya, terendah, tertinggi

# while True:
#     try:
#         masukkan_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
#         if masukkan_nilai == "":
#             break
#         nilai = masukkan_nilai   
#         database.append(nilai)
#     except:
#         print("Tidak ada data")

# hasil = hitung_nilai(*database) 

# if database None:
#     print("Nilai tidak ada")
# else:
#     rata_rata, terendah, tertinggi = hasil 
#     print(f"Rata-rata kelas: {int(rata_rata)}")
#     print(f"Nilai tertinggi: {int(terendah)}")
#     print(f"Nilai terendah: {int(tertinggi)}")

database = []

def hitung_nilai(*nilai):
    if not nilai:
        return None  
    terendah = min(nilai)
    tertinggi = max(nilai)
    rata_ratanya = sum(nilai) / len(nilai)
    return rata_ratanya, terendah, tertinggi

while True:
    try:
        masukkan_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if masukkan_nilai == "":
            break
        nilai = int(masukkan_nilai)
        database.append(nilai)
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")

hasil = hitung_nilai(*database)

if hasil is None:
    print("Nilai tidak ada")
else:
    rata_rata, terendah, tertinggi = hasil
    print(f"Rata-rata kelas: {int(rata_rata)}")
    print(f"Nilai tertinggi: {int(tertinggi)}")
    print(f"Nilai terendah: {int(terendah)}")



