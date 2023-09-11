# Låt användaren mata in en mening
input_sentence = input("Ange en mening: ")

# Ta bort blanksteg och skiljetecken och gör allt till små bokstäver
clean_sentence = ''.join(filter(str.isalnum, input_sentence)).lower()

# Jämför om den rena meningen är samma som dess omvända version
if clean_sentence == clean_sentence[::-1]:
    print(f"'{input_sentence}' är ett palindrom")
else:
    print(f"'{input_sentence}' är inte ett palindrom")
