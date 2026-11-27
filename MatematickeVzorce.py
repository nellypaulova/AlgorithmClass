import math



#prevod z EUR na CZK

while True:
    try:
        print ("Vyberte z moznosti co chcete spocitat.")
        print("1 - Trojuhelnik")
        print("2 -  Kruh")
        print("3 - Krychle")
        print("4 - Koule")
        print("5 - Aritmeticky prumer")
        print("6 - z °C na °F")
        print("7 - Prevod casu")
        print("8 - Prevod vzdalenosti")
        print("9 - Prevod měn")

        volba = input("Vyber 1 - 9: ")

        try:

            if volba == "1":
                print("Co znas o trojuhelniku?")
                print("A - vsechny tri strany")
                print("B - dve odvesny pravouhleho trojuhelniku")
                print("C - dve strany a uhel mezi nimi")
                print("D - zakladnu a vysku")

                volba1 = input("Vyber A - D: ")

                if volba1 == "A":
                    zakladna = int(input("Zadej zakladnu trojuhelniku: "))
                    vyska = int(input("Zadej vysku trojuhelniku: "))
                    prepona = int(input("Zadej preponu trojuhelniku: "))

                    if zakladna + vyska <= prepona or zakladna + prepona <= vyska or vyska + prepona <= zakladna:
                        print("Z těchto stran trojúhelník nejde sestrojit.")

                    else:

                        obsah = zakladna * vyska /2
                        obvod = zakladna + vyska + prepona

                        print(f"Obsah: {obsah:.1f}cm")
                        print(f"Obvod: {obvod:.1f}cm")

                elif volba1 == "B":
                    a = float(input("Odvesna a: (cm)"))
                    b = float(input("Odvesna b: (cm)"))
                    c = (a ** 2 + b ** 2) ** (0.5)

                    print(f"Odvesna c: {c:.1f}cm")
                    print(f"Obvod a: {a + b + c:.1f}cm")
                    print(f"Obsah b: {a * b / 2:.1f}cm")

                elif volba1 == "C":
                    a = float(input("Strana a: "))
                    b = float(input("Strana b: "))
                    uhel = float(input("Úhel mezi nimi (ve stupních): "))
                    c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(uhel))) ** 0.5
                    obsah = a * b * math.sin(math.radians(uhel)) / 2

                    print(f"Třetí strana c: {c:.1f}cm")
                    print(f"Obvod: {a + b + c:.1f}cm")
                    print(f"Obsah: {obsah:.1f}cm")

                elif volba1 == "D":
                    zakladna = float(input("Základna: "))
                    vyska = float(input("Výška: "))
                    print(f"Obsah: {zakladna * vyska / 2:.1f}cm\u00b2")

                else:
                    print("Neplatna volba.")

        except ValueError:(
            print("Zadej prosim jen cisla."))

        if volba == "2":
            r = float(input("Polomer (cm): "))

            obvod = 2 * math.pi * r
            obsah = math.pi * r ** 2

            print(f"Obvod: {obvod:.1f}cm")
            print(f"Obsah: {obsah:.1f}cm\u00b2")

        if volba == "3":
            a = float(input("Delka hrany a(cm): "))

            povrch = 6 * a ** 2
            objem = a ** 3
            soucet_hran = 12 * a

            print(f"Povrch: {povrch:.1f}cm\u00b2")
            print(f"Objem: {objem:.1f}cm\u00b3")
            print(f"Soucet vsech hran: {soucet_hran:.1f}cm")

        if volba == "4":
            r = float(input("Zadejte polomer koule (cm): "))
            povrch = 4 * math.pi * r ** 2
            objem = 4 / 3 * math.pi * r ** 3

            print(f"Povrch: {povrch:.1f}cm")
            print(f"Objem: {objem:.1f}cm")

        if volba == "5":
            text = input("Zadej cisla oddelena mezerou: ")
            cisla = [float(x) for x in text.split()]

            prumer = sum(cisla) / len(cisla)
            print(f"Prumer: {prumer:.1f}")

        if volba == "6":
            print("Vyberte prevod z '°C na °F' nebo z '°F na °C'")
            print("A - z '°C na °F': ")
            print("B - z '°F na °C': ")

            volba2 = input("Vyber A - B: ")

            if volba2 == "A":
                celsius = float(input("Zadejte teplotu v °C: "))
                fahrenheit = (celsius * 9 / 5) + 32

                print(f"{celsius:.1f}\u00b0C je {fahrenheit:.1f}\u00b0F")

            if volba2 == "B":
                fahrenheit = float(input("Teplota v °F"))
                celsius = (fahrenheit - 32) * 5 / 9

                print(f"{fahrenheit:.1f}\u00b0F je {celsius:.1f}\u00b0C")

        if volba == "7":
            jednotky = {
                "1": ("roky", 365 * 24 * 60 * 60),
                "2": ("mesice", 365 / 12 * 24 * 60 * 60),
                "3": ("tydny", 7 * 24 * 60 * 60),
                "4": ("dny", 24 * 60 * 60),
                "5": ("hodiny", 60 * 60),
                "6": ("minuty", 60),
                "7": ("vteriny", 1),
            }
            for klic, (nazev, nasobek) in jednotky.items():
                print(klic, "-", nazev)

            z_volba = input("Z ceho prevadis? ")
            do_volba = input("Na co prevadis? ")

            if z_volba in jednotky and do_volba in jednotky:
                hodnota = float(input("Zadej hodnotu: "))

                z_nazev, z_nasobek = jednotky[z_volba]
                do_nazev, do_nasobek = jednotky[do_volba]

                vteriny = hodnota * z_nasobek
                vysledek = vteriny / do_nasobek

                print(f"{hodnota} {z_nazev} je {vysledek:.2f} {do_nazev}")
            else:
                print("Neplatna volba.")


        if volba == "8": #prevod km na m, cm, miles, stopy, palce
            jednotky = {
                "1": ("km", 1000),
                "2": ("m", 1),
                "3": ("cm", 0.01),
                "4": ("miles", 1609.344),
                "5": ("feet", 0.3048),
                "6": ("inches", 0.0254),
            }

            for klic, (nazev, nasobek) in jednotky.items():
                print(klic, "-", nazev)

            z_volba = input("Z ceho prevadis? ")
            do_volba = input("Na co prevadis? ")

            if z_volba in jednotky and do_volba in jednotky:
                hodnota = float(input("Zadej hodnotu: "))

                z_nazev, z_nasobek = jednotky[z_volba]
                do_nazev, do_nasobek = jednotky[do_volba]

                metry = hodnota * z_nasobek
                vysledek = metry / do_nasobek

                print(f"{hodnota} {z_nazev} je {vysledek:.2f} {do_nazev}")
            else:
                print("Neplatna volba.")


        if volba == "9": #prevod z EUR na CZK
            kurz = 24.3  # kolik CZK je 1 EUR (zkontroluj aktuální kurz)

            print("1 - EUR na CZK")
            print("2 - CZK na EUR")

            volba = input("Vyber: ")

            if volba == "1":
                eur = float(input("Zadej castku v EUR: "))
                print(f"{eur:.2f} EUR je {eur * kurz:.2f} CZK")

            elif volba == "2":
                czk = float(input("Zadej castku v CZK: "))
                print(f"{czk:.2f} CZK je {czk / kurz:.2f} EUR")

            else:
                print("Neplatna volba.")

    finally:
        print("Thank you for using this calculator.")

    answer = input("Do you wish to calculate again? (yes/no): ")
    if answer != "yes":
        break