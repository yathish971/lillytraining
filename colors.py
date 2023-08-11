# "red", "green", "blue", "yellow", "orange", "black", "white"

# Creating the colors list using the list() constructor
colors=list(["red", "green", "blue", "yellow", "orange", "black", "white"])
# Print the length of the colors list
print(len(colors))

# Print the type of the colors list
print(type(colors))

# Check if "yellow" is in the colors list
if colors.count("yellow")>0:
    print("present")
else:
    print("Not Present")

# Replace the second and third colors in the list with "purple" and "pink"

colors[1]="purple"
colors[2]="pink"

print(colors)