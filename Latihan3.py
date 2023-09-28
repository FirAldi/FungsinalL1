# Fungsi untuk menghitung nilai akhir mahasiswa
def hitung_nilai_akhir(nilai_uts, nilai_uas):
    return 0.4 * nilai_uts + 0.6 * nilai_uas

# Fungsi untuk menampilkan nilai akhir semua mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"{nama}: Nilai Akhir: {nilai_akhir:.2f}")

def main():
    # Data mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
    data_mahasiswa = {
        "Hana": (80, 90),
        "Budi": (75, 85),
        "Citra": (90, 95),
    }

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = {}
    for nama, (nilai_uts, nilai_uas) in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai_uts, nilai_uas)
        data_nilai_akhir[nama] = nilai_akhir

    # Menampilkan nilai akhir semua mahasiswa
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
