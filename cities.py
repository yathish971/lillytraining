# "New York", "Chicago", "Denver", "Las Vegas", "Los Angeles"

# list() constructor to make a List
List_cities=list(["New York", "Chicago", "Denver", "Las Vegas", "Los Angeles"])

# Print the length of the city list
print("The Number of Cities present in the List is: ",len(List_cities))

# Print the type of the city list
print(type(List_cities))

# Check if "Denver" is in the city list
print("Checking if 'Denver' is in the City list ",List_cities.count("Denver"))

# Replace the second and third city in the list with "Houston" and "Seattle"
print("Before Replacement :",List_cities)
List_cities[1]="Houston"
List_cities[2]="Seattle"
print("After Repalcement:",List_cities)

