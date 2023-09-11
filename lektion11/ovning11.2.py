import json

# Din lista
char_list = [" abc ", "åäö", "123"]

# Skriv listan till en JSON-fil
with open("char_list.json", "w") as json_f:
    json.dump(char_list, json_f)

# Läs listan från JSON-filen och ta bort eventuella extra mellanslag
with open("char_list.json", "r") as json_f:
    char_list_from_file = json.load(json_f)

for char in char_list_from_file:
    print(char.strip())
