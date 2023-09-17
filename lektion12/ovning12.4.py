artiklar = {}

while True:
    titel = input("Ange titel på artikeln (eller 'sluta' för att avsluta): ")

    if titel.lower() == 'sluta':
        break

    text = input("Ange text för artikeln: ")
    artiklar[titel] = text


print("Artiklar:")
for titel, text in artiklar.items():
    print(f"Titel: {titel}")
    print(f"Text: {text}")
    print("-----")
