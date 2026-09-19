jarak = int(input("Masukkan jarak pengiriman (km) :"))
express = input("Layanan express(ya/tidak) :").upper()

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

biaya_tambahan = 15000 if express == "YA" else 0
total = tarif + biaya_tambahan
print("Total tarif pengiriman: Rp", total)