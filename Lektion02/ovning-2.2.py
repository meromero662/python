# Prislista
prislista = {
    "Vanlig korv": 20.95,  # per förpackning (8 korvar)
    "Vegansk korv": 34.95,  # per förpackning (4 korvar)
    "Dryck": 13.95  # per flaska (per elev)
}

# Antal önskade korvar och drycker från eleverna
antal_vanliga_korvar_2 = int(input("Hur många elever vill ha 2 vanliga korvar? "))
antal_vanliga_korvar_3 = int(input("Hur många elever vill ha 3 vanliga korvar? "))
antal_veganska_korvar_2 = int(input("Hur många elever vill ha 2 veganska korvar? "))
antal_veganska_korvar_3 = int(input("Hur många elever vill ha 3 veganska korvar? "))
antal_drycker = int(input("Hur många elever vill ha dryck? "))

# Beräkna antal förpackningar och total kostnad
antal_forpackningar_vanliga_korvar = (antal_vanliga_korvar_2 + antal_vanliga_korvar_3) // 4 + (antal_vanliga_korvar_2 + antal_vanliga_korvar_3) % 4
antal_forpackningar_veganska_korvar = (antal_veganska_korvar_2 + antal_veganska_korvar_3) // 4 + (antal_veganska_korvar_2 + antal_veganska_korvar_3) % 4
total_kostnad = (antal_forpackningar_vanliga_korvar * prislista["Vanlig korv"] +
                antal_forpackningar_veganska_korvar * prislista["Vegansk korv"] +
                antal_drycker * prislista["Dryck"])

# Skriv ut inköpslistan och total kostnad
print("\n- INKÖPSLISTA -")
print(f"| Vanlig korv : {antal_forpackningar_vanliga_korvar} förpackningar")
print(f"| Vegansk korv : {antal_forpackningar_veganska_korvar} förpackningar")
print(f"| Dryck : {antal_drycker} flaskor")
print("----------------------")
print(f"| {total_kostnad} SEK")
print("----------------------")

