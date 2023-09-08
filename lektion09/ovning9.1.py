summa = 0
for i in range(1000001):
    summa += i
print("Summan av alla heltal mellan 0 och 1000000 är:", summa)


summa_udda = 0
for i in range(1, 501, 2):
    summa_udda += i
print("Summan av alla udda heltal mellan 0 och 500 är:", summa_udda)
