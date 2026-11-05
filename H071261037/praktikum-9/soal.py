class pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return 'unggul'
        else:
            return 'perlu evaluasi'

    def tampilkan_data(self, nomor):
        print(f"| {nomor:<3} | {self.nama:<15} | {self.id_pemain:<12} | {self.role:<12} | {self.hitung_skor_akhir():<10} | {self.status_performa():<15} |")

daftar_pemain = []
print('=== SISTEM PENILAIAN PERFORMA PEMAIN ===')
print()
while True:
    try:
        jumlah = int(input('masukkan jumlah pemain: '))
        break
    except ValueError:
        print('input harus berupa angka')
        continue
print()
for i in range(jumlah):
    print(f'--- data pemain ke-{i+1} ---')
    nama = input('nama: ')
    id_pemain = input('id pemain: ')
    role = input('role: ')  
    nilai_kill = int(input('nilai kill: ')) 
    nilai_assist = int(input('nilai assist: '))
    nilai_objective = int(input('nilai objective: '))
    print()
    daftar_pemain.append(pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective))

print('=== REKAPITULASI PERFORMA PEMAIN ===')
print('=' * 86)
print(f"| {'no':<3} | {'nama':<15} | {'id_pemain':<12} | {'role':<12} | {'skor_akhir':<10} | {'status':<15} |")
print('=' * 86)
for nomor, pemainn in enumerate(daftar_pemain, start = 1):
    pemainn.tampilkan_data(nomor)
print('=' * 85)