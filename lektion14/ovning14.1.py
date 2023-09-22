def km_to_miles(dist):
    miles = dist * 0.621371
    return miles

def miles_to_km(dist):
    km = dist / 0.621371
    return km

# Huvudprogrammet
while True:
    try:
        input_str = input("Ange distans (t.ex. 15 km eller 500 miles): ")
        if "km" in input_str:
            distance = float(input_str.replace("km", "").strip())
            result = km_to_miles(distance)
            print(f"{distance} km motsvarar {result} miles.")
        elif "miles" in input_str:
            distance = float(input_str.replace("miles", "").strip())
            result = miles_to_km(distance)
            print(f"{distance} miles motsvarar {result} km.")
        else:
            print("Ogiltig inmatning. Var vänlig ange distans med enheten 'km' eller 'miles'.")
    except ValueError:
        print("Ogiltig inmatning. Var vänlig ange en giltig siffra följt av enheten 'km' eller 'miles'.")
    except KeyboardInterrupt:
        print("\nAvslutar programmet.")
        break

