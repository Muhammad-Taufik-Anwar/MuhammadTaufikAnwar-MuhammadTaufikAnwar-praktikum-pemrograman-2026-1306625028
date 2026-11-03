# Program Sorting

Nilai = [85, 13, 99, 34, 71, 15, 82, 24, 64, 61,
         67, 99, 50, 68, 25, 37, 32, 27, 14, 91,
         79, 15, 47, 48, 74, 88, 64, 53, 77, 50,
         24, 91, 87, 55, 60, 75, 91, 22, 47, 64,
         81, 88, 26, 48, 69, 59, 84, 77, 28, 36,
         59, 74, 89, 73, 91, 64, 55, 88, 90, 48,
         73, 97, 98, 40, 93, 50, 78, 60, 44, 77,
         82, 51, 53, 65, 98, 59, 94, 91, 52, 44,
         65, 85, 72, 92, 49, 67, 58, 48, 62, 54,
         89, 67, 58, 48, 85, 45, 77, 76, 81, 77]

print("Program Sorting")
print("Nama : Muhammad Taufik Anwar")
print("NIM : 1306625028")
print()

print("Data nilai awal :")
# Menampilkan Nilai dipisah koma menggunakan join string
print(", ".join(map(str, Nilai)))

# Membuat salinan list Nilai agar data asli tidak termodifikasi langsung
data = list(Nilai)
n = len(data)
ditukar = True

# Proses Bubble Sort
while ditukar:
    ditukar = False
    i = 0
    while i < n - 1:
        # Bandingkan data ke-i dengan data sebelahnya (i+1)
        if data[i] > data[i + 1]:
            # Tukar posisi data jika data kiri lebih besar dari data kanan
            data[i], data[i + 1] = data[i + 1], data[i]
            ditukar = True
        i += 1

print()
print("Data nilai terurut :")
k = 0
while k < n:
    # Mengambil potongan data (slicing) sebanyak 10 elemen, lalu cetak per baris
    baris_data = data[k:k + 10]
    print(", ".join(map(str, baris_data)))
    k += 10

print("selesai")