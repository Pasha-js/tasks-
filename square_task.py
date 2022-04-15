numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_sum = sum(numbers)

for num in numbers:
    square = (numbers_sum - num) % 2
    if square == 0:
        print(num)