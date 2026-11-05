import re

class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60 and self.hitung_skor_akhir() <=100:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        print(f"{nomor:<5} {self.nama:<15} {self.id_pemain:<12} {self.role:<12} {self.hitung_skor_akhir():<12.2f} {self.status_performa():<18}")


daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

while True:
    try:
        jumlah_pemain = int(input("Masukkan jumlah pemain: "))
        if jumlah_pemain > 0:
            break
        else:
            print("Jumlah pemain harus lebih dari 0!")
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")


for i in range(jumlah_pemain):

    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input("Masukkan nama: ")
    id_pemain = input("Masukkan ID pemain: ")
    role = input("Masukkan role pemain: ").capitalize()

    while True:
        try:
            nilai_kill = int(input("Masukkan nilai kill: "))
            nilai_assist = int(input("Masukkan nilai assist: "))
            nilai_objective = int(input("Masukkan nilai objective: "))
            break
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print(f"{'No.':<5} {'Nama':<15} {'ID Pemain':<12} {'Role':<12} {'Skor Akhir':<12} {'Status':<18}")

print("-" * 78)
for i in range(len(daftar_pemain)):
    daftar_pemain[i].tampilkan_data(i + 1)
print("-" * 78)
