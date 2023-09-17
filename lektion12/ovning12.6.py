# En enkel lista för att lagra anteckningar som tupler (titel, text)
notes = []

# Räknare för att hålla koll på index
index_counter = 1

# Huvudprogram
while True:
    print(".: ALWAYSNOTE :.")
    print("-- gold edition --")
    print("******************")

    print("\nMenu:")
    print("1. List notes")
    print("2. Add note")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        if not notes:
            print("Inga anteckningar tillgängliga.")
        else:
            print("Dina anteckningar:")
            for title, text in notes:
                print(f"{index_counter}. {title}")
                index_counter += 1
    elif choice == "2":
        title = input("Ange titel för den nya anteckningen: ")
        text = input("Skriv in anteckningens innehåll: ")
        notes.append((title, text))
        print("Anteckningen har lagts till.")
    elif choice == "3":
        break
    else:
        print("Ogiltigt kommando. Försök igen.")
