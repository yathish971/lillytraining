numbers = (10, 20, 30, 40, 50)

# 1. Print a tuple
print(numbers)
# Output: Tuple of numbers: (10, 20, 30, 40, 50)

# 2. Indexing elements in the tuple
print("First Number: ",numbers[0])
print("Last Number: ",numbers[-1])

# Output: First number: 10


# Output: Last number: 50

# 3. Slicing the tuple

# Output: Sliced numbers: (20, 30, 40)
print(numbers[1:4])

# Output: Sliced numbers: (30, 40, 50)
print(numbers[2::])

# Output: Sliced numbers: (10, 20, 30)
print(numbers[0:3])