
# ======================== Seznamy =========================

ukoly = []

# ======================== Funkce ==========================

def hlavni_menu():
    print("")
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    volba = input("Vyberte možnost (1 - 4): ")
    if volba == "1" or volba == "2" or volba == "3" or volba == "4":
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("PROBÍHÁ UKONČENÍ PROGRAMU")
            return False
    else:
        print("Zadali jste špatnou volbu ! Zadej správnou volbu 1 až 4")
    return True

def pridat_ukol():
    print("")
    nazev = input("Zadejte název úkolu: ")
    if nazev.strip() == "":
        print("Zadali jste prázdný vstup !!! Žádný úkol ani popis nepřidán. Zkuste to znovu a lépe !")
        pridat_ukol()
    else:
        popis = input("Zadejte popis úkolu: ")
        if popis.strip() == "":
            print("Zadali jste prázdný vstup !!! Žádný úkol ani popis nepřidán. Zkuste to znovu a lépe !")
            pridat_ukol()
        else:
            ukol_s_popisem = nazev + " - " + popis
            ukoly.append(ukol_s_popisem)
            print("Do seznamu přidán úkol:", ukol_s_popisem)
            return 

def zobrazit_ukoly():
    print("")
    print("Seznam úkolů: ")
    for i, ukol in enumerate(ukoly):
        poradi = i + 1
        print(f"{poradi}. {ukol}")
    #return

def odstranit_ukol():
    print("")
    pocet_ukolu = len(ukoly)
    zobrazit_ukoly()
    cislo = input("Zadejte číslo úkolu, který chcete odstranit: ")
    try:
        cislo_int = int(cislo)
        cislo_int = cislo_int - 1
    except ValueError:
        print("Zadaný vstup není číslo !!! Žádný úkol ani popis nebyl odstraněn.")
        return
    if cislo_int < 0 or cislo_int > pocet_ukolu - 1:
        print("Zadal jste číslo neexistujícího úkolu !!! Žádný úkol ani popis nebyl odstraněn.")
    else:
        odstraneny_ukol = ukoly.pop(cislo_int)
        print("Úkol číslo:", cislo_int + 1,"s názvem:", odstraneny_ukol, "byl odstraněn !")
        return

# ==================== HLAVNÍ PROGRAM ========================

while True:
    if not hlavni_menu():
        print("PROGRAM UKONČEN")
        break
