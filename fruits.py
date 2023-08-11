fruits = ["apple", "banana", "orange"]

# 1. Append a new fruit to the list using the `append` method
fruits.append("grape")
# Output: List after appending 'grape': ['apple', 'banana', 'orange', 'grape']
print(fruits)
# 2. Extend the list by adding elements from another list using the `extend` method
additional=["guava","watermelon","kiwi"]
fruits.extend(additional)
# Output: List after extending with more fruits: ['apple', 'banana', 'orange', 'grape', 'watermelon', 'kiwi']
print(fruits)
# 3. Insert a new fruit at a specific index using the `insert` method
fruits.insert(1,"mango")
# Output: List after inserting 'pear' at index 2: ['apple', 'banana', 'pear', 'orange', 'grape', 'watermelon', 'kiwi']
print(fruits)
# 4. Remove a specific fruit from the list using the `remove` method
fruits.remove("banana")
# Output: List after removing 'banana': ['apple', 'pear', 'orange', 'grape', 'watermelon', 'kiwi']
print(fruits)