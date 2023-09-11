import random

dice = random.randint(1, 6)
print(f'Du slog en {dice}:')
print('---------')
if dice == 1:
    print('|     |')
    print('|  X  |')
    print('|     |')
elif dice == 2:
    print('| X   |')
    print('|     |')
    print('|   X |')
elif dice == 3:
    print('| X   |')
    print('|  X  |')
    print('|   X |')
elif dice == 4:
    print('| X X |')
    print('|     |')
    print('| X X |')
elif dice == 5:
    print('| X X |')
    print('|  X  |')
    print('| X X |')
else:
    print('| X X |')
    print('| X X |')
    print('| X X |')
print('---------')



