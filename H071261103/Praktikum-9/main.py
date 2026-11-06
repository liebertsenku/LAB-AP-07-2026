class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (self.nilai_kill * 0.3) + (self.nilai_assist * 0.3) + (self.nilai_objective * 0.4)

    def status_performa(self):
        if 60 <= self.hitung_skor_akhir() <= 100:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<3} | {self.nama:<12} | {self.id:<12} | {self.role:<10} | {skor:<10.2f} | {status:<15} |")


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

while True:
    try:
        jumlahPemain = int(input("Masukkan Jumlah Pemain: "))

        if jumlahPemain > 0:
            break
        else:
            print("Jumlah pemain harus lebih dari 0!")

    except ValueError:
        print("Harus berupa angka!")

dataPemain = []

while jumlahPemain > 0:
    print(f"\n-- Data Pemain ke-{len(dataPemain) + 1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")

    while True:
        try:
            nilai_kill = int(input("Nilai Kill: "))
            nilai_assist = int(input("Nilai Assist: "))
            nilai_objective = int(input("Nilai Objective: "))

            if nilai_kill < 0 or nilai_assist < 0 or nilai_objective < 0:
                print("Nilai tidak boleh negatif!")
                continue
            break

        except ValueError:
            print("Harus berupa angka!")

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    dataPemain.append(pemain)

    jumlahPemain -= 1


print("\n=== REKAPITULASI PERFORMA PEMAIN ===")

print("=" * 81)
print(f"| {'No':<3} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
print("=" * 81)

for no, pemain in enumerate(dataPemain, start=1):
    pemain.tampilkan_data(no)

print("=" * 81)