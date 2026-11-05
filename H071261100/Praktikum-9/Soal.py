class Pemain:

    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective


    # Method menghitung dan mengembalikan skor akhir
    def hitung_skor_akhir(self):
        skor_akhir = (
            (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        )
        return skor_akhir


    # Method menentukan status performa
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60 and self.hitung_skor_akhir() <= 100:
            return "Unggul"
        else:
            return "Perlu dievaluasi"


    # Method menampilkan data pemain
    def tampilkan_data(self):
        print(f"Nama            : {self.nama}")
        print(f"ID Pemain       : {self.id_pemain}")
        print(f"Role            : {self.role}")
        print(f"Nilai Kill      : {self.nilai_kill}")
        print(f"Nilai Assist    : {self.nilai_assist}")
        print(f"Nilai Objective : {self.nilai_objective}")
        print(f"Skor Akhir      : {self.hitung_skor_akhir(), 2}")
        print(f"Status          : {self.status_performa()}")


# Validasi jumlah pemain
def input_jumlah_pemain():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pemain: "))
            if jumlah > 0:
                return jumlah
            else:
                print("Jumlah pemain harus lebih dari 0")
        except ValueError:
            print("Input harus berupa bilangan bulat")


# Validasi teks
def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        else:
            print("Input tidak boleh kosong")


# Validasi nilai
def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus berada antara 0 sampai 100")
        except ValueError:
            print("Input harus berupa angka")


# PROGRAM UTAMA
print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")

daftar_pemain = []
daftar_id = []

jumlah = input_jumlah_pemain()


# Input data beberapa pemain
for i in range(jumlah):

    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input_teks("Nama: ")

    # Validasi ID agar tidak duplikat
    while True:
        id_pemain = input_teks("ID Pemain: ")
        if id_pemain not in daftar_id:
            daftar_id.append(id_pemain)
            break
        else:
            print("ID sudah digunakan. Masukkan ID lain.")

    role = input_teks("Role: ")

    nilai_kill = input_nilai("Nilai Kill: ")
    nilai_assist = input_nilai("Nilai Assist: ")
    nilai_objective = input_nilai("Nilai Objective: ")

    pemain = Pemain(
        nama,
        id_pemain,
        role,
        nilai_kill,
        nilai_assist,
        nilai_objective
    )

    daftar_pemain.append(pemain)


# Menampilkan tabel rekapitulasi
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")

garis = "=" * 78
print(garis)

print(
    f"| {'No':<2} | {'Nama':<9} | {'ID Pemain':<10} | "
    f"{'Role':<9} | {'Skor Akhir':<10} | {'Status':<15} |"
)

print(garis)

for i, pemain in enumerate(daftar_pemain, start=1):

    print(
        f"| {i:<2} | "
        f"{pemain.nama:<9} | "
        f"{pemain.id_pemain:<10} | "
        f"{pemain.role:<9} | "
        f"{round(pemain.hitung_skor_akhir(),2):<12} | "
        f"{pemain.status_performa():<15} |"
    )

print(garis)
