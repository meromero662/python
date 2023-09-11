# Ta emot tre tal från användaren
tal1= float(input("ange första tal: "))
tal2= float(input("ange andra tal: "))
tal3= float(input("ange tredje tal: "))



# Använd if-satser för att identifiera det största talet
if tal1 >= tal2 and tal1 >= tal3 :
    storsta_tal = tal1
elif  tal2 >= tal1 and tal2 >= tal3 :
    storsta_tal = tal2
else:
    storsta_tal = tal3
# Presentera det största talet för användaren

print("storsta tal är" , storsta_tal)