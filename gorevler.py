gorevler = []

while True:

    print("\n--- GÖREV TAKİP SİSTEMİ ---")
    print("1 - Görev ekle")
    print("2 - Görevleri göster")
    print("3 - Görev sil")
    print("4 - Görevi tamamla")
    print("5 - Çıkış")

    secim = input("Seçimin: ")

    if secim == "1":

        gorev = input("Görevini yaz: ")

        gorevler.append({
            "ad": gorev,
            "tamamlandi": False
        })

        print("Görev eklendi!")

    elif secim == "2":

        for i, gorev in enumerate(gorevler):
            durum = "Tamamlandı" if gorev["tamamlandi"] else "Bekliyor"

            print(i + 1, "-", gorev["ad"], "-", durum)

    elif secim == "3":

        for i, gorev in enumerate(gorevler):
            print(i + 1, "-", gorev["ad"])

        try:
            sil = int(input("Silinecek görev numarası: "))

            if 1 <= sil <= len(gorevler):
                gorevler.pop(sil - 1)
                print("Görev silindi!")
            else:
                print("Geçersiz görev numarası!")

        except ValueError:
            print("Lütfen sayı gir!")

    elif secim == "4":

        for i, gorev in enumerate(gorevler):
            print(i + 1, "-", gorev["ad"])

        try:
            numara = int(input("Tamamlanan görev numarası: "))

            if 1 <= numara <= len(gorevler):
                gorevler[numara - 1]["tamamlandi"] = True
                print("Görev tamamlandı!")
            else:
                print("Geçersiz görev numarası!")

        except ValueError:
            print("Lütfen sayı gir!")

    elif secim == "5":
        break

    else:
        print("Geçersiz seçim!")
    