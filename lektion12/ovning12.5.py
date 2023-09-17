# Skapa en lista med anteckningar som representeras som tupler
anteckningar = []

# Användarinteraktion
while True:
    print("Välkommen till anteckningshanteraren!")
    print("1. Lägg till en anteckning")
    print("2. Ta bort en anteckning")
    print("3. Visa alla anteckningar")
    print("4. Avsluta")
    val = input("Välj ett alternativ: ")

    if val == "1":
        titel = input("Ange titeln på anteckningen: ")
        text = input("Ange texten på anteckningen: ")
        anteckningar.append((titel, text))
        print("Anteckningen har lagts till.")
    elif val == "2":
        titel = input("Ange titeln på anteckningen du vill ta bort: ")
        hittad = False
        for anteckning in anteckningar:
            if anteckning[0] == titel:
                anteckningar.remove(anteckning)
                hittad = True
                print("Anteckningen har tagits bort.")
                break
        if not hittad:
            print("Kunde inte hitta anteckningen med den angivna titeln.")
    elif val == "3":
        print("-----")
        for titel, text in anteckningar:
            print(f"Titel: {titel}")
            print(f"Text: {text}")
            print("-----")
    elif val == "4":
        print("Hej då!")
        break
    else:
        print("Ogiltigt val. Försök igen.")
