age = input('Ange din ålder: ')
age = int(age)

if age < 15:
    print('Du måste åka med målsman!')
elif age < 18:
    print('Du behöver mälsmans tillstånd!')
else:
    print('Du får åka!')  
