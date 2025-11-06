import random

numbers = []

for i in range(5):
    numbers.append(random.randint(-100,100))

s = 0

for number in numbers:
    s += number

print(numbers)

biggest = numbers[0]

smallest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number

print(smallest, biggest)