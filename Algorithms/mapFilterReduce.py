numbers = [1, 2, 3, 4, 5]

# Using map() to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert the iterator to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]

##############

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to calculate the product
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)

##############

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() to filter out even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the iterator to a list
even_numbers_list = list(even_numbers)

print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]
