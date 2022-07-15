import sys
from io import StringIO

test_input_1 = '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'
test_input_2 = '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'

sys.stdin = StringIO(test_input_1)

numbers_count = {}
numbers = [float(x) for x in input().split(' ')]
# numbers = tuple(map(float, input().split(' ')))
for number in numbers:
    if number not in numbers_count:
        numbers_count[number] = 0
    numbers_count[number] += 1

for number, count in numbers_count.items():
    print(f'{number} - {count} times')

# example for sorting with tuples:
sorted_numbers_by_counter = sorted((value, key) for key, value in numbers_count.items())
print(sorted_numbers_by_counter)