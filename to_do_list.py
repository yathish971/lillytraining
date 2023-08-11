# Creating a to-do list
todo_list = ["Go for a morning walk", "Finish a work project", "Have lunch with a friend",
             "Buy groceries", "Read a book", "Exercise", "Cook dinner"]

# Accessing the first task
# Output: "Go for a morning walk"
print(todo_list[0])
# Accessing the third task
# Output: "Have lunch with a friend"
print(todo_list[2])
# Slicing from index 1 to 4 (excluding 4)
# Output: ["Finish a work project", "Have lunch with a friend", "Buy groceries"]
print(todo_list[1:4])
# Slicing from the beginning to index 3 (excluding 3)
# Output: ["Go for a morning walk", "Finish a work project", "Have lunch with a friend"]
print(todo_list[0:3])
# Slicing from index 4 to the end
# Output: ["Read a book", "Exercise", "Cook dinner"]
print(todo_list[4:])
# Last item

# Output: "Cook dinner"
print(todo_list[-1])
# Slicing from the second-to-last task to the end
# Output: ["Exercise", "Cook dinner"]
print(todo_list[(len(todo_list)-2):])
#Reverse the list
# Output: ['Cook dinner', 'Exercise', 'Read a book', 'Buy groceries', 'Have lunch with a friend', 'Finish a work project', 'Go for a morning walk']
(todo_list.reverse())
# Display the to do list
print(todo_list)
