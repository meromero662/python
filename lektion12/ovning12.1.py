rubriker = {"kom ihåg" : "Något",
            "Ta bilen till verkstad": "Something",
}
for rub_ik in rubriker:
    print(rub_ik)

anvandare_rubrik = input("Ange rubrik: ")

if anvandare_rubrik == "kom ihåg":
    print(rubriker['kom ihåg'])
elif anvandare_rubrik == "Ta bilen till verkstad":
    print(rubriker['Ta bilen till verkstad'])
else:
    print(f"Fel")

