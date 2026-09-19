#tugas 2

jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (Ya/Tidak): ").capitalize()

if jarak < 5 and jarak > 0:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
elif jarak > 20:
    tarif = 35000


layanan_expres = 15000 if express == "Ya" else 0
total_biaya = tarif + layanan_expres
print("Total tarif pengiriman: Rp", total_biaya)