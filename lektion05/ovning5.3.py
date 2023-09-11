# Variabler för att hålla reda på information om de inmatade heltalen
antal_tal = 0
summa = 0

print(".: MATHLETE v2 .0 :.")
print("-------------------")

while True:
    try:
        # Användaren matar in ett tal eller 'exit'
        inmatning = input("> ")

        # Avsluta programmet om användaren skriver 'exit'
        if inmatning == 'exit':
            break

        # Försök att konvertera inmatningen till ett heltal
        tal = int(inmatning)

        # Uppdatera informationen om de inmatade heltalen
        antal_tal += 1
        summa += tal

    except ValueError:
        # Felhantering om inmatningen inte är ett giltigt heltal
        print("FEL : Ogiltigt nummer")

# Skriv ut resultatet när användaren avslutar
if antal_tal > 0:
    medelvarde = summa / antal_tal
    print("-------------------")
    print("Kardinalitet : {}".format(antal_tal))
    print("Summa : {}".format(summa))
    print("Medelvärde : {:.1f}".format(medelvarde))
else:
    print("Inga giltiga heltal matades in.")
