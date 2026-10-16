gorevler = []

while True:
    print("\n--- GÖREV TAKİP SİSTEMİ ---")
    print("1 - Görev ekle")
    print("2 - Görevleri göster")
    print("3 - Çıkış")

    secim = input("Seçimin: ")

    if secim == "1":
        gorev = input("Görevini yaz: ")
        gorevler.append(gorev)
        print("Görev eklendi!")

    elif secim == "2":
        for gorev in gorevler:
            print(gorev)

    elif secim == "3":
        break

    else:
        print("Geçersiz seçim!")