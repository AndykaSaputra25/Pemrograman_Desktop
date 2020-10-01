def bangunDatar():
    print('''Bangun Datar (Luas dan keliling [cm])
        1. Segitiga
        2. Persegi
        3. Persegi Panjang
        4. Jajar Genjang
        5. Belah Ketupat
        6. Layang-Layang
        7. Trapesium
        8. Lingkaran
    ''')
    pilih = int(input("Cari bangun apa? "))
#___Segitiga___#
    if pilih == 1:
        print("\n\tSegitiga")
        a = int(input("Alas: "))
        b = int(input("Sisi b: "))
        c = int(input("Sisi c: "))
        t = int(input("Tinggi: "))
        L = 1/2 * a * t
        K = a+b+c
        print("\nLuas segitiga = ", L, "cm^2")
        print("Keliling segitiga = ", K, "cm")
#___Persegi___#
    elif pilih == 2:
        print("\n\tPersegi")
        s = int(input("Sisi: "))
        L, K = s**2, 4*s
        print("\nLuas persegi = ", L, "cm^2")
        print("Keliling persegi = ", K, "cm")
#___Persegi Panjang___#
    elif pilih == 3:
        print("\n\tPersegi Panjang")
        p = int(input("Panjang: "))
        l = int(input("Lebar: "))
        print("\nLuas segitiga = ", p*l, "cm^2")
        print("Keliling segitiga = ", 2*(p+l), "cm")
#___Jajar Genjang___#
    elif pilih == 4:
        print("\n\tJajar Genjang")
        a = int(input("Alas: "))
        b = int(input("Miring: "))
        t = int(input("Tinggi: "))
        print("\nLuas segitiga = ", a*t, "cm^2")
        print("Keliling segitiga = ", 2*(a+b), "cm")
#___Belah Ketupat___#
    elif pilih == 5:
        print("\n\tBelah Ketupat")
        s = int(input("Sisi: "))
        d1 = int(input("Diagonal1: "))
        d2 = int(input("Diagonal2: "))
        print("\nLuas segitiga = ", 1/2 * d1 * d2, "cm^2")
        print("Keliling segitiga = ", s*4, "cm")
#___Layang-Layang___#
    elif pilih == 6:
        print("\n\tLayang-Layang")
        a = int(input("Sisi a/b: "))
        b = int(input("Sisi c/d: "))
        d1 = int(input("Diagonal1: "))
        d2 = int(input("Diagonal2: "))
        print("\nLuas segitiga = ", 1/2 * d1 * d2, "cm^2")
        print("Keliling segitiga = ", 2*(a+b), "cm")
#___Trapesium___#
    elif pilih == 7:
        print("\n\tTrapesium")
        a = int(input("Alas(a): "))
        b = int(input("Atas(b): "))
        c = int(input("Kanan(c): "))
        d = int(input("Kiri(d): "))
        t = int(input("Tinggi(t): "))
        print("\nLuas segitiga = ", ((a+b)*t) / 2, "cm^2")
        print("Keliling segitiga = ", a+b+c+d, "cm")
#___Lingkaran___#
    elif pilih == 8:
        print("\n\tLingkaran")
        r = int(input("Jari-Jari: "))
        print("\nLuas segitiga = ", 22/7 * r * r , "cm^2")
        print("Keliling segitiga = ", 22/7 * 2 * r, "cm")
bangunDatar()