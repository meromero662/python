try:
    tal = int(input("Skriv in ett heltal: ")) # Läs inmatning och konvertera till heltal
    resultat = tal * 2 # Beräkna det dubbla värdet
    print("RESULTAT:", resultat) # Skriv ut resultatet
except ValueError:
    print("FEL:", input(), "kan inte översättas till ett heltal") # Felmeddelande om inmatningen inte är ett heltal
