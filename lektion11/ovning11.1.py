import json

# Din lista med random data
random_stuff = [1337, 13.37, '˚A˚ah Y¨a¨a!']

# Omvandla listan till en JSON-formaterad strängrepresentation
json_representation = json.dumps(random_stuff, ensure_ascii=False)

# Skriv ut JSON-objektet på skärmen
print(json_representation)

