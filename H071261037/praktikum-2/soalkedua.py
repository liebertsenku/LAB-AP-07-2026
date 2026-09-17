#soal kedua
jarak = int(input("masukan jarak pengiriman (km) : "))
layanan_express = input("Layanan Express (yes/no) : ").lower()

if jarak < 5:
     tarif = 10000 
elif jarak >= 5 and jarak <=20:
     tarif = 20000
elif jarak >20:
     tarif = 35000
else:
     print('invalid')

biaya_tambahan = 15000 if layanan_express =='yes' else 0
total_tarif = biaya_tambahan + tarif
print('Total tarif pengiriman' ,total_tarif)