#soal empat
tujuan = input('masukan tujuan (pantai, kota, pengunungan) :')
waktu = input('masukan waktu(pagi/malam) :')
pengujung = input('masukan pengujung (dewasa/anak) :')

match tujuan:
 case 'pantai':
        if waktu  == 'pagi':    
            print('paket rekomendasi : paket A')
        elif waktu == 'malam' and pengujung == 'dewasa':
            print('paket rekomendasi : paket C')
        else:
            print('tidak ada paket yang cocok')
 case 'pengunungan':
        if waktu == 'pagi' and pengujung == 'dewasa':
            print('paket rekomendasi : paket b')
        elif waktu == 'malam' and pengujung == 'dewasa':
            print('paket rekomendasi : paket c')
        else:
            print('tidak ada paket yang cocok')
 case 'kota':
        if waktu == 'malam' :
            print('paket rekomendasi : paket c')
        else:
            print('tidak ada paket yang cocok')