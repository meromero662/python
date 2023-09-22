def get_even(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers

import random

numbers = []
for x in range(10):
    numbers.append(random.randint(0, 9))

even = get_even(numbers)
print('even:', even)
print('numbers:', numbers)
