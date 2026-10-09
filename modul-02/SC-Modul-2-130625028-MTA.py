# Program Mencari Faktor Bilangan
print("Program Mencari Faktor Bilangan")
print("Nama : Muhammad Taufik Anwar")
print("NIM : 1306625028")
print()

# Perulangan untuk meminta input bilangan dari pengguna
while True:
    # Input bilangan dari pengguna
    n = int(input("Masukkan bilangan(0 untuk keluar): "))

    #Jika bilangan adalah 0, keluar dari perulangan
    if n == 0:
        print("Terima kasih telah menggunakan program ini.")
        break

    # List untuk menyimpan faktor- faktor bilangan
    faktor = []

    # Mencari faktor bilangan
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)

    # Menampilkan faktor- faktor bilangan
    print(f"Faktor dari {n} adalah: {faktor}")
    print()