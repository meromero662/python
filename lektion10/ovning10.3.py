import csv

# Läs in data från CSV-filen och skapa en lista med personer
data = []
with open('database.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Hoppa över header-rad
    for row in reader:
        data.append(row)

while True:
    print("\n.: PEOPLES DATABASE :.")
    print("----------------------")
    print("1 - Get person by ID")
    print("2 - List people by FORENAME")
    print("3 - List people by SURNAME")
    print("4 - Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_id = input("Enter ID: ")
        for person in data:
            if person[0] == search_id:
                print("Person found:")
                print(f"ID: {person[0]}")
                print(f"FORENAME: {person[1]}")
                print(f"SURNAME: {person[2]}")
                print(f"GENDER: {person[3]}")
                print(f"YEAR: {person[4]}")
                break
        else:
            print("Person not found.")

    elif choice == "2":
        search_name = input("Enter FORENAME: ")
        matching_people = []
        for person in data:
            if search_name.lower() in person[1].lower():
                matching_people.append(person)

        if matching_people:
            print("Matching people:")
            for person in matching_people:
                print(f"ID: {person[0]}, FORENAME: {person[1]}, SURNAME: {person[2]}")
        else:
            print("No matching people found.")

    elif choice == "3":
        search_name = input("Enter SURNAME: ")
        matching_people = []
        for person in data:
            if search_name.lower() in person[2].lower():
                matching_people.append(person)

        if matching_people:
            print("Matching people:")
            for person in matching_people:
                print(f"ID: {person[0]}, FORENAME: {person[1]}, SURNAME: {person[2]}")
        else:
            print("No matching people found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")
