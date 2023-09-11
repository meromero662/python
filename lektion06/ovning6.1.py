# Användarinmatning
text = input("Ange en text: ")
bokstav = input("Ange bokstav: ")

# Konvertera både texten och bokstaven till gemener (lowercase) för att undvika skiftlägeskänslighet
text = text.lower()
bokstav = bokstav.lower()

# Variabel för att räkna antalet förekomster av bokstaven
forekomst = 0

# Index för att iterera genom texten
index = 0

# Loop för att räkna förekomsten av bokstaven
while index < len(text):
    if text[index] == bokstav:
        forekomst += 1  # Om bokstaven matchar, öka räknaren
    index += 1  # Gå vidare till nästa bokstav i texten

# Skriv ut resultatet
print(f"Bokstaven {bokstav} förekommer {forekomst} gånger i texten.")

