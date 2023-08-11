# Friends of two individuals
friend1 = {"Alice", "Bob", "Charlie", "David"}
friend2 = {"Charlie", "David", "Eve", "Frank"}

# Find common friends using intersection
print(friend1.intersection(friend2))

# Add a new friend to friend1
friend1.add("yathish")

# Remove a friend from friend2
friend2.remove("Eve")

# Print the updated friend sets
print(friend1,friend2)