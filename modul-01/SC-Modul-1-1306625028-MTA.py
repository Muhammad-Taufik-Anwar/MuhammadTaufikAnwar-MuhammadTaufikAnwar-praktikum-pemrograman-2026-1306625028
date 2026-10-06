# Program Konversi Suhu
nama = "Muhammad Taufik Anwar"
NIM = "1306625028"

suhu_awal = 0
suhu_akhi = 100
selang = 10

# Menampilkan Header Program
print(f"Program Konversi Suhu")
print(f"Nama : {nama}")
print(f"NIM : {NIM}")
print()
print(f"- Suhu awal : {suhu_awal}")
print(f"- Suhu akhir : {suhu_akhi}")
print(f"- Selang : {selang}")
print()

# Menampilkan Header Tabel Dengan Garis Penutup Atas
print("TABEL KONVERSI SUHU")
print("+-----+--------------+-----------------+-------------+")
print(f"| {'No.':<3} | {'Celcius (°C)':<12} | {'Fahrenheit (°F)':<15} | {'Reamur (°R)':<11} |")
print("+-----+--------------+-----------------+-------------+")

# Proses Perulangan Data Untuk Menghitung Dan Menampilkan Data
no = 1
celcius = suhu_awal
while celcius <= suhu_akhi:
    fahrenheit = (celcius * 9/5) + 32
    reamur = celcius * 4/5

    print(f"| {no:<3} | {celcius:<12} | {fahrenheit:<15.2f} | {reamur:<11.2f} |")
    print("+-----+--------------+-----------------+-------------+")

    celcius += selang
    no += 1

    # Menampilkan Garis Penutup Paling Bawah Tabel
print("+-----+--------------+-----------------+-------------+")