person = {
    "förnamn": "Johan",
    "efternamn": "Svensson",
    "ålder": 25,
    "husdjur": [
        {
            "namn": "Morris",
            "ålder": 3,
            "typ": "hund"
        },
        {
            "namn": "Lisa",
            "ålder": 2,
            "typ": "katt"
        }
    ]
}

forename = person['förnamn']
surename = person['efternamn']
age = person['ålder']

print(forename ,surename , 'är' , age , 'år gammal och har 2 husdjur')

#skapa en for loop som visar: en 3 år gammal hund som heter Morris
for pet in person['husdjur']:
    print("* En " , pet['ålder'] , "år gammal ", pet['typ'] , "som heter" , pet['namn'])

