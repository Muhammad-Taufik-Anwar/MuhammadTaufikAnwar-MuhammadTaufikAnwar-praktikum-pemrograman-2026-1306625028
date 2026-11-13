import random

# Data nama buah
databuah = [
    'anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei', 'abiu',
    'alpukat', 'anjeng', 'bacang', 'baguk', 'belimbing',
    'bengkuang', 'benda', 'binjai', 'bisbul', 'blueberry',
    'burahol', 'blewah', 'bit', 'cempedak', 'ceplukan', 'cermai',
    'ceri', 'cokelat', 'delima', 'duku', 'durian', 'duwet', 'enau',
    'enamenam', 'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang',
    'jambuair', 'jambubatu', 'jambubol', 'jambumawar',
    'jambumede', 'jengkol', 'jeruk', 'jerukbali', 'jerukkeprok',
    'jerukkingkit', 'jeruknipis', 'jerukpurut', 'kapulasan',
    'kawista', 'kecapi', 'kedondong', 'kelapa', 'kelengkeng',
    'kelubi', 'ketela', 'kemang', 'kepel', 'kersen', 'kesemek',
    'kokosan', 'kiwi', 'koldi', 'kurma', 'kelawi', 'kenitu', 'lai',
    'langsat', 'lemon', 'leci', 'lobak', 'maja', 'malaka',
    'mangga', 'manggis', 'markisa', 'melon', 'mengkudu',
    'menteng', 'matoa', 'mentimun', 'namnam', 'nanas', 'nangka',
    'naga', 'nona', 'pepaya', 'persik', 'pir', 'pisang', 'pete',
    'rambai', 'rambusa', 'rambutan', 'rukem', 'sawo', 'semangka',
    'sirsak', 'siwalan', 'srikaya', 'stroberi', 'sukun', 'terap',
    'terong', 'tomat', 'timunsuri', 'ubi', 'waluh', 'wuni',
    'zaitun'
]

# Tampilan awal
print("================================")
print("      PERMAINAN TEBAK BUAH")
print("================================")
print("Oleh : Muhammad Taufik Anwar")
print("NIM  : 1306625028")

# Perulangan permainan
main_lagi = "y"

while main_lagi == "y":

    # Komputer memilih buah secara acak
    buah = random.choice(databuah)

    # Menghitung jumlah huruf dan kesempatan
    jumlah_huruf = len(buah)
    kesempatan = jumlah_huruf

    # Menyiapkan tampilan tebakan
    tampilan = ["-"] * jumlah_huruf

    print("\nKomputer sedang memikirkan nama buah.")
    print("Buah tersebut terdiri dari", jumlah_huruf, "huruf.")
    print("Nama buah:", " ".join(tampilan))

    # Proses menebak huruf
    while kesempatan > 0 and "-" in tampilan:

        print("\nAnda memiliki", kesempatan,
              "kesempatan untuk menebak.")
        huruf = input("Tebakan Anda: ").lower()

        # Memeriksa apakah huruf terdapat dalam nama buah
        if huruf in buah:

            print("Benar! Huruf", huruf,
                  "ada dalam nama buah tersebut.")

            # Menampilkan huruf sesuai posisinya
            for i in range(jumlah_huruf):
                if buah[i] == huruf:
                    tampilan[i] = huruf

        else:

            print("Sayang sekali! Huruf", huruf,
                  "tidak ada dalam nama buah tersebut.")

            # Mengurangi kesempatan
            kesempatan = kesempatan - 1

        # Menampilkan kondisi tebakan terbaru
        print("\nNama buah:", " ".join(tampilan))

    # Memeriksa hasil permainan
    if "-" not in tampilan:

        print("\nSELAMAT! Anda berhasil menebak nama buah.")

    else:

        print("\nANDA KALAH!")
        print("Nama buah tersebut adalah:", buah)

    # Menanyakan pilihan bermain kembali
    main_lagi = input("\nMau main lagi (y/t)? ").lower()

    while main_lagi != "y" and main_lagi != "t":
        print("Masukkan pilihan y atau t.")
        main_lagi = input("Mau main lagi (y/t)? ").lower()

# Program selesai
print("\n================================")
print("          PERMAINAN SELESAI")
print("================================")