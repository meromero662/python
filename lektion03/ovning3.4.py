land = str.lower(input("vilket land? "))
if land == "danmark" or land == "finland" or land =="island" or land =="norge" or land =="sverige" :
    print(land , "tillhör norden.")
elif land ==  "england" or land =="nordirland" or land =="skottland" or land =="wales" :
    print(land , "tillhör storbritanien.")
else:
    print("ops,du valde fel land!")