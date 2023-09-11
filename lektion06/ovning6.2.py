consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

input_text = input("Svenska < ")
result = ""

for char in input_text:
    if char in consonants:
        result += char + 'o' + char
    else:
        result += char

print("Rövarspråk > " + result)
