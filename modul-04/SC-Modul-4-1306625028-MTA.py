# Program Grading

print("Program Grading")
print("Nama : Muhammad Taufik Anwar")
print("NIM  : 1306625028")

import pandas as pd

data = pd.read_excel("DataNilai.xlsx")

# Merapikan nama kolom
data.columns = (
    data.columns.astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip())

# Membaca data mahasiswa
nama = data["Mahasiswa"].tolist()
nilai_lain = data["Nilai Lain2"].tolist()
uts = data["Nilai UTS"].tolist()
uas = data["Nilai UAS"].tolist()

# Inisialisasi counting grade
grade_A = 0
grade_Amin = 0
grade_Bplus = 0
grade_B = 0
grade_Bmin = 0
grade_Cplus = 0
grade_C = 0
tidak_lulus = 0

# Menampilkan tabel
print("-" * 51)
print(f"| {'No':^3} | {'Nama Mahasiswa':^20} | {'Nilai Akhir':^10} | {'Grade':^4} |")
print("-" * 51)

i = 0

while i < len(nama):
    # Menghitung nilai akhir
    NA = 0.30 * nilai_lain[i] + 0.35 * uts[i] + 0.35 * uas[i]

    # Menentukan grade
    if NA >= 86:
        grade = "A"
        grade_A += 1
    elif NA >= 81:
        grade = "A-"
        grade_Amin += 1
    elif NA >= 76:
        grade = "B+"
        grade_Bplus += 1
    elif NA >= 71:
        grade = "B"
        grade_B += 1
    elif NA >= 66:
        grade = "B-"
        grade_Bmin += 1
    elif NA >= 61:
        grade = "C+"
        grade_Cplus += 1
    elif NA >= 56:
        grade = "C"
        grade_C += 1
    else:
        grade = "TL"
        tidak_lulus += 1

    # Menampilkan data mahasiswa
    print(f"| {i+1:<3} | {nama[i]:<20} | {NA:>11.2f} | {grade:^5} |")

    i += 1

print("----------------------------------------------------")

# Rekapitulasi
print("Rekapitulasi :")
print(f"Grade A      = {grade_A}")
print(f"Grade A-     = {grade_Amin}")
print(f"Grade B+     = {grade_Bplus}")
print(f"Grade B      = {grade_B}")
print(f"Grade B-     = {grade_Bmin}")
print(f"Grade C+     = {grade_Cplus}")
print(f"Grade C      = {grade_C}")
print(f"Tidak Lulus  = {tidak_lulus}")

print(f"\nTotal Mahasiswa = {len(nama)}")