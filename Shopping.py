# Creating a shopping list
shopping_list = ["apples", "bananas", "milk", "bread", "eggs", "cheese", "chicken"]


# Accessing the first item
# Output: "apples"
print(shopping_list[0])
# Accessing the third item
# Output: "milk"
print(shopping_list[2])
# Slicing from index 1 to 4 (excluding 4)
# Output: ["bananas", "milk", "bread"]
print(shopping_list[1:4])
# Slicing from the beginning to index 3 (excluding 3)
# Output: ["apples", "bananas", "milk"]
print(shopping_list[0:3])
# Slicing from index 4 to the end
print(shopping_list[4::])
# Output: ["eggs", "cheese", "chicken"]

# Last item
print(shopping_list[-1])
# Output: "chicken"
# Slicing from the second-to-last item to the end
print(shopping_list[(len(shopping_list)-2)::])
# Output: ["cheese", "chicken"]