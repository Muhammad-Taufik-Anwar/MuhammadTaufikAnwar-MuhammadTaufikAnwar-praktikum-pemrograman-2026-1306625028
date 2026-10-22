import math

def main():
    while True:
        print("Program sinus-cosinus")
        print("Nama : Muhammad Taufik Anwar")
        print("NIM : 1306625028")

        sudut_deg = float(input("Besar sudut (derajat) : "))
        x_rad = math.radians(sudut_deg)

        tv_sin = math.sin(x_rad)
        tv_cos = math.cos(x_rad)

        print(f"\nTrue value sin({sudut_deg:.0f}) = {tv_sin:.6f}")
        print(f"True value cos({sudut_deg:.0f}) = {tv_cos:.6f}")
        print("-" * 75)

        print(f"{'Jumlah suku':^12} | " f"{'AV sinus':^12} | " f"{'Er sinus':^10} | " f"{'AV cosinus':^12} | " f"{'Er cosinus':^10}" )
        print("-" * 75)

        suku = 1
        av_sin = 0.0
        av_cos = 0.0
        batas_maks = 1000

        while suku <= batas_maks:
            term_sin = ((-1) ** (suku - 1) * x_rad ** (2 * suku - 1) / math.factorial(2 * suku - 1) )

            term_cos = ( (-1) ** (suku - 1) * x_rad ** (2 * suku - 2) / math.factorial(2 * suku - 2) )

            av_sin += term_sin
            av_cos += term_cos

            # Galat sinus
            if tv_sin != 0:
                er_sin = abs((av_sin - tv_sin) / tv_sin) * 100
            else:
                er_sin = 0.0 if av_sin == 0 else float("inf")

            # Galat cosinus
            if tv_cos != 0:
                er_cos = abs((av_cos - tv_cos) / tv_cos) * 100
            else:
                er_cos = 0.0 if av_cos == 0 else float("inf")

            print(f"{suku:^12} | " f"{av_sin:^12.6f} | " f"{er_sin:^9.2f}% | " f"{av_cos:^12.6f} | "f"{er_cos:^9.2f}%")

            if er_sin < 5 and er_cos < 5:
                break

            suku += 1

        if suku > batas_maks:
            print("Batas maksimum iterasi tercapai.")

        print("-" * 75)

        ulang = input("Mau menghitung lagi (y/t)? ").strip().lower()

        if ulang != "y":
            break

        print("\n" + "-" * 75 + "\n")

if __name__ == "__main__":
    main()