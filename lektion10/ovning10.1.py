# Standardmeddelande
message = "Västerås"

while True:
    # Skapa vägskylten med aktuellt meddelande
    sign = f"""
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
| # --------------------------- # |
| ### | Welcome to {message} | # ### |
| ### --------------------------- ### ### |
| | | | | | # |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
| C | Change sign message
| E | Exit program
| - - - - - - - - - - - - - - - - - - - - - - - -
| >
"""

    # Visa vägskylten
    print(sign)

    # Låt användaren välja en option
    user_choice = input("Välj en option (C för att ändra, E för att avsluta): ").upper()

    # Om användaren väljer "C", låt dem ändra meddelandet
    if user_choice == "C":
        new_message = input("Skriv in det nya meddelandet: ")
        message = new_message
        print(f"Meddelandet ändrat till: {message}")
    # Om användaren väljer "E", avsluta programmet
    elif user_choice == "E":
        break
    # Om användaren gör ett ogiltigt val, visa felmeddelande
    else:
        print("Ogiltigt val. Försök igen.")
