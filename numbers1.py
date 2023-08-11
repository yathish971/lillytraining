numbers = [1, 2, 3]

# 1. Append a new number to the list using the `append` method
numbers.append(4)
# Output: List after appending 4: [1, 2, 3, 4]
print(numbers)
# 2. Extend the list by adding elements from another list using the `extend` method
numbers2=[5,6]
numbers.extend(numbers2)
# Output: List after extending with more numbers: [1, 2, 3, 4, 5, 6]
print(numbers)
# 3. Insert a new number at a specific index using the `insert` method
numbers.insert(2,10)
# Output: List after inserting 10 at index 2: [1, 2, 10, 3, 4, 5, 6]
print(numbers)
# 4. Remove a specific number from the list using the `remove` method
numbers.remove(3)
# Output: List after removing 3: [1, 2, 10, 4, 5, 6]
print(numbers)