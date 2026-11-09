class Pemain:
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
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<10} | {skor:<10.2f} | {status:<15} |")


def input_angka(pesan, tipe=int):
    while True:
        try:
            angka = tipe(input(pesan))
            if angka < 0:
                print("Nilai tidak boleh negatif. Coba lagi.")
            else:
                return angka
        except:
            print("Input harus berupa angka. Coba lagi.")


def main():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    jumlah = input_angka("\nMasukkan jumlah pemain: ", int)
    while jumlah < 1:
        print("Jumlah pemain minimal 1.")
        jumlah = input_angka("Masukkan jumlah pemain: ", int)

    daftar_pemain = []
    for i in range(1, jumlah + 1):
        print(f"\n-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = input_angka("Nilai Kill: ")
        nilai_assist = input_angka("Nilai Assist: ")
        nilai_objective = input_angka("Nilai Objective: ")
        pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        daftar_pemain.append(pemain)

    garis = "=" * 78
    print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
    print(garis)
    print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
    print(garis)
    for nomor, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(nomor)
    print(garis)


if __name__ == "__main__":
    main()
