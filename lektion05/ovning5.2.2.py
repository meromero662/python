try:
    a = float(input("Ange värde för a: "))
    b = float(input("Ange värde för b: "))

    if b == 0 :
        raise ZeroDivisionError ("Division med 0 är inte tillåtet")

    result = a / b
    print(f"{a} / {b} = {result}")
except ValueError:
    print("Fel , Ogiltigt nummer!")
except ZeroDivisionError:
    print("Fel,omojligt att devidera med 0")
