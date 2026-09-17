presentase_cabai = int(input("masukan presentase cabai : "))

if presentase_cabai >=0 and presentase_cabai <=10:
     print('level aman')

elif presentase_cabai >=11 and presentase_cabai <=40:
     print('level sedang')

elif presentase_cabai >=41 and presentase_cabai <=70:
     print('level pedas')

elif presentase_cabai >70:
     print('level ekstrem')

else:
     print('input tidak valid')
