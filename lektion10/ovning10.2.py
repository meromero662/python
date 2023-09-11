# Öppna och läs filen
with open("numbers.csv", "r") as file:
    data = file.read()

# Skapa en lista för att räkna förekomsten av varje heltal
number_count = [0] * 10

# Räkna förekomsten av varje heltal
for char in data:
    if char.isdigit():
        digit = int(char)
        number_count[digit] += 1

# Skriv ut resultatet
print("- NUMANALYZER -")
print("---------------")
for digit in range(10):
    print(f"| {digit} | {number_count[digit]}")
print("---------------")
