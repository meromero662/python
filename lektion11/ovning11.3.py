# Skapar en tom lista för att lagra heltal
saved_numbers = []

print(".: intMEMORIZER :.")
print("******************")

while True:
    try:
        user_input = int(input("Mata in ett heltal (0 för att avsluta): "))
        if user_input == 0:
            break
        elif user_input not in saved_numbers:
            saved_numbers.append(user_input)
    except ValueError:
        print("Ogiltigt heltal. Försök igen.")

# Spara de unika heltalen till en fil
with open("saved_numbers.txt", "w") as file:
    for number in saved_numbers:
        file.write(str(number) + "\n")

print("------------------")
print("Memoriserade heltal:")
for number in saved_numbers:
    print(f"* {number}")

print("------------------")
print(f"SUMMA : {sum(saved_numbers)}")
print("------------------")
print(f"{len(saved_numbers)} st gånger scriptet kördes")
print("------------------")
